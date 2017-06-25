# A file to  be passed to the --profile option of install-tl-ubuntu.
# Restricts the number of packages to install so Travis is quicker.
selected_scheme scheme-minimal
#
# Environment variables
TEXDIR /usr/local/texlive/20*
TEXMFCONFIG ~/.texlive20*/texmf-config
TEXMFHOME ~/texmf
TEXMFLOCAL /usr/local/texlive/texmf-local
TEXMFSYSCONFIG /usr/local/texlive/20*/texmf-config
TEXMFSYSVAR /usr/local/texlive/20*/texmf-var
TEXMFVAR ~/.texlive20*/texmf-var
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
#
# Ignored collections
collection-context 0
collection-fontutils 0
collection-formatsextra 0
collection-games 0
collection-genericextra 0
collection-genericrecommended 0
collection-htmlxml 0
collection-humanities 0
collection-langafrican 0
collection-langarabic 0
collection-langcjk 0
collection-langcyrillic 0
collection-langczechslovak 0
collection-langenglish 0
collection-langeuropean 0
collection-langfrench 0
collection-langgerman 0
collection-langgreek 0
collection-langindic 0
collection-langitalian 0
collection-langother 0
collection-langpolish 0
collection-langportuguese 0
collection-langspanish 0
collection-luatex 0
collection-mathextra 0
collection-metapost 0
collection-music 0
collection-omega 0
collection-pictures 0
collection-plainextra 0
collection-pstricks 0
collection-publishers 0
collection-texworks 0
collection-xetex 0
#
# Options
option_adjustrepo 1
option_doc 0
option_fmt 1
option_src 0
option_sys_bin /usr/local/bin
option_sys_info /usr/local/share/info
option_sys_man /usr/local/share/man
