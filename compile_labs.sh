#!/bin/bash
# Compile the main tex files and ensure that there are no errors.

MAX_TIME=60
FILES=(PythonEssentials DataScienceEssentials Volume1 Volume2 Volume3 Volume4 GettingStarted)
SUCCESS="true"
LOG="_compilelog.errlog"
SEP="===================="
OUTDIR="docs"
RED="\033[0;91m"        # Red text color
GREEN="\033[0;92m"      # Green text color
CYAN="\033[0;96m"       # Cyan text color
NC="\033[0m"            # No text color

set -e

# Ignore command line arguments.
if [ "$#" -ne 0 ]; then
    echo "usage: ./compile_labs.sh"
    exit 1
fi

# Check that latexmk is installed.
command -v latexmk &> /dev/null || { echo "'latexmk' not found!"; exit 1; }

# Create a directory to deposit the labs in.
if [ ! -e "${OUTDIR}" ]; then
    mkdir "${OUTDIR}"
fi

# Compile each tex file in one minute or less.
function ctimeout() { perl -e "alarm ${MAX_TIME}; exec @ARGV" "$@"; }
echo -e "${CYAN}Compiling labs with latexmk${NC}"
for FILE in ${FILES[@]}; do
    LOGFILE="${FILE}${LOG}"
    echo -n "          ${FILE}.tex..."
    if ctimeout latexmk -pdf -outdir="${OUTDIR}" "${FILE}.tex" &> "${LOGFILE}"; then
        echo -e "${GREEN}success!${NC}"
    else
        # Report and record a failure, then move on to the next file.
        echo -e "${RED}FAILURE${NC}"
        SUCCESS="false"
    fi
done

# If any of the compilations failed, print the end of each compile log.
if [ "$SUCCESS" == "false" ]; then
    echo -en "\n${RED}LAB COMPILATION FAILED${NC}"
    for FILE in ${FILES[@]}; do
        echo -e "\n\n${SEP} ${FILE} Compiler Log ${SEP}\n"
        LOGFILE="${FILE}${LOG}"
        tail "${LOGFILE}"
        rm "${LOGFILE}"
    done
    echo
    exit 1
else    # If successful, delete compile logs and check that PDF files exist.
    for FILE in ${FILES[@]}; do
        rm "${FILE}${LOG}"
        if [ ! -e "${OUTDIR}/${FILE}.pdf" ]; then
            echo -e "\nFAILURE: ${OUTDIR}/${FILE}.pdf does not exist\n"
            exit 1
        fi
    done
fi

echo -e "\n${GREEN}LABS SUCCESSFULLY COMPILED${NC}\n"
