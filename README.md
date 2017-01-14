## About

This project contains the labs for the Foundations of Applied Mathematics curriculum and are being developed as part of BYU's Applied and Computational Mathematics degree program.
The labs go in tandem with the four textbooks that are currently being written and will start rolling out in 2017.

This work is licenced under the Creative Commons Attribution 3.0 United States License.
To view a copy of this license please visit http://creativecommons.org/licenses/by/3.0/us/ and see [cc-by-license.txt](https://github.com/Foundations-of-Applied-Mathematics/Labs/blob/master/cc-by-license.txt).

The owners of this work are  
Jeffrey Humpherys and Tyler J. Jarvis  
Department of Mathematics  
Brigham Young University  
Email: acme@math.byu.edu

This project is funded in part by the National Science Foundation, grant no. TUES Phase II DUE-1323785.

## Build Instructions

Visit the [releases page](https://github.com/Foundations-of-Applied-Mathematics/Labs/releases) to download the latest version of the lab curriculum.

To gain access to the entire repository, fork this repository and clone it.
Each volume can then be built separately using the LaTex files listed below.
- Volume 1, Mathematical Analysis: `Vol1.tex`
- Volume 2, Algorithm Design and Optimization: `Vol2.tex`
- Volume 3, Modeling with Uncertainty and Data: `Vol3.tex`
- Volume 4, Modeling with Dynamics and Control: `Vol4.tex`

Compile the files using TeXShop or a similar program, or via the command line:
```bash
$ latexmk -pdf Vol1.tex
```
or
```bash
$ pdflatex Vol1.tex
```
(These commands create a PDF called, for example, `Vol1.pdf`.)

## Data Files

The data sets used in these labs can be found at http://acme.byu.edu/data/.
They are organized by semester: Volume 1 first half as `Vol1A`, second half as `Vol1B`, and so on.

See the [Wiki page](https://github.com/Foundations-of-Applied-Mathematics/Lab-Development/wiki/File-Dependencies-Index) for an index of labs and data file dependencies.

## Contributors

- E. Evans, Brigham Young University
- R. Evans, Brigham Young University
- J. Grout, Drake University
- J. Humpherys, Brigham Young University
- T. Jarvis, Brigham Young University
- J. West, University of Michigan
- J. Whitehead, Brigham Young University

The following students contributed to the labs while studying at Brigham Young University.
Graduate student contributors are marked in bold.

- **J. Adams**
- J. Bejarano
- Z. Boyd
- M. Brown
- T. Christensen
- M. Cook
- R. Dorff
- B. Ehlert
- M. Fabiano
- **A. Frandsen**
- K. Finlinson
- J. Fisher
- R. Fuhriman
- S. Giddens
- C. Gigena
- M. Graham
- F. Glines
- M. Goodwin
- R. Grout
- J. Hendricks
- A. Henriksen
- **I. Henriksen**
- **C. Hettinger**
- S. Horst
- K. Jacobson
- J. Leete
- **J. Lytle**
- R. McMurray
- **S. McQuarrie**
- J. Morrise
- M. Morrise
- A. Morrow
- R. Murray
- J. Nelson
- M. Proudfoot
- D. Reber
- C. Robertson
- R. Sandberg
- J. Stewart
- S. Suggs
- T. Thompson
- M. Victors
- **J. Webb**
- **R. Webb**
- A. Zaitzeff
