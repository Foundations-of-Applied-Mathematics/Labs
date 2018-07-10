#!/bin/bash
# Compile the main tex files and ensure that there are no errors.

USAGE="usage: ./compile_labs.sh [LaTeX compiler, defaults to pdflatex]"
MAX_TIME=30
FILES=(PythonEssentials DataScienceEssentials Volume1 Volume2 Volume3 Volume4)
SUCCESS=true
LOG="_compilelog.errlog"
SEP="===================="
OUTDIR="docs"

set -e
echo

# Select a program to compile LaTeX files (deault pdflatex).
if [ "$#" -eq 0 ]; then
    COMPILER="pdflatex -halt-on-error"
else
    COMPILER=""
    for arg in "$@"
    do
        if [ ${#COMPILER} -ne 0 ]; then
            COMPILER+=" "
        fi
        COMPILER+=$arg
    done
fi

# Check that the compile command exists.
command -v $COMPILER > /dev/null 2>&1 || { echo "This script requires $COMPILER but it's not installed. Aborting."; exit 1; }

# Create a directory to deposit the labs in.
if [ ! -e "$OUTDIR" ]; then
    mkdir $OUTDIR
fi

# Compile each tex file twice in 30 seconds or less each time.
for FILE in ${FILES[@]}
do
    LOGFILE=$FILE$LOG
    echo -n "Compiling $FILE.tex..."
    for i in {1..2}
    do
        if ! perl -e "alarm $MAX_TIME; exec @ARGV" "eval $COMPILER $FILE.tex > $LOGFILE"; then
            # Report and record a failure, then move on to the next file.
            echo "FAILURE"
            SUCCESS=false
            continue 2
        fi
    done

    # Store the output in the target location.
    mv $FILE.pdf $OUTDIR
    echo "success"
done

bash ./.clean.sh

# If any of the compilations failed, print the end of each compile log.
if [ "$SUCCESS" = false ]; then
    echo -e "\nLAB COMPILATION FAILED"
    for FILE in ${FILES[@]}
    do
        echo -e "\n$SEP $FILE Compiler Log $SEP\n"
        LOGFILE=$FILE$LOG
        tail $LOGFILE
        rm $LOGFILE
    done
    exit 1
else    # If successful, delete compile logs and check that PDF files exist.
    for FILE in ${FILES[@]}
    do
        rm $FILE$LOG
        if [ ! -e $OUTDIR/$FILE.pdf ]; then
            echo -e "\nFAILURE: $FILE.pdf does not exist\n"
            exit 1
        fi
    done
fi

echo -e "\nLABS SUCCESSFULLY COMPILED\n"
