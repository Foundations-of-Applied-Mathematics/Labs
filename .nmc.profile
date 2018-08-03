# A file to  be passed to the --profile option of install-tl-ubuntu.
# Restricts the number of packages to install so Travis is quicker.
selected_scheme scheme-minimal
#
# Environment variables
TEXDIR /usr/local/texlive/foam
TEXMFCONFIG ~/.texlivefoam/texmf-config
TEXMFHOME ~/texmf
TEXMFLOCAL /usr/local/texlive/texmf-local
TEXMFSYSCONFIG /usr/local/texlive/foam/texmf-config
TEXMFSYSVAR /usr/local/texlive/foam/texmf-var
TEXMFVAR ~/.texlivefoam/texmf-var
binary_x86_64-linux 1
#
# Desired Collections
collection-basic 1
collection-bibtexextra 1
collection-binextra 1
collection-fontsextra 1
collection-fontsrecommended 1
collection-latex 1
collection-latexextra 1
collection-latexrecommended 1
collection-mathscience 1

# Options
option_adjustrepo 1
option_doc 0
option_fmt 1
option_src 0
option_sys_bin /usr/local/bin
option_sys_info /usr/local/share/info
option_sys_man /usr/local/share/man
