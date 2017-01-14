### About

This project contains the labs for the Foundations of Applied Mathematics curriculum and are being developed as part of BYU's Applied and Computational Mathematics degree program.
The labs go in tandem with the four textbooks that are currently being written and will start rolling out in 2017.

This work is licenced under the Creative Commons Attribution 3.0 United States License.
To view a copy of this license please visit http://creativecommons.org/licenses/by/3.0/us/ and see [cc-by-license.txt](https://github.com/Foundations-of-Applied-Mathematics/Lab-Development/blob/develop/cc-by-license.txt).

The owners of this work are  
Jeffrey Humpherys and Tyler J. Jarvis  
Department of Mathematics  
Brigham Young University  
Email: acme@math.byu.edu

This project is funded in part by the National Science Foundation, grant no. TUES Phase II DUE-1323785.

### Build Instructions

Visit the [releases page](https://github.com/Foundations-of-Applied-Mathematics/Lab-Development/releases) to download the latest version of the lab curriculum.

To gain access to the entire repository, fork this repository and clone it.
Each volume can then be built separately using the LaTex files listed below.
- Python Basics: `Introduction.tex`
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

### Data Files

The data sets used in these labs can be found at http://acme.byu.edu/data/.
They are organized by semester: Volume 1 first half as `Vol1A`, second half as `Vol1B`, and so on.

See the [Wiki page](https://github.com/Foundations-of-Applied-Mathematics/Lab-Development/wiki/File-Dependencies-Index) for an index of labs and data file dependencies.

<!-- ### Contributors

In alphabetical order by last name,

- J. Adams, Brigham Young University
- J. Bejarano, Brigham Young University
- Z. Boyd, Brigham Young University
- M. Brown, Brigham Young University
- T. Christensen, Brigham Young University
- K. Clay, Brigham Young University
- M. Cook, Brigham Young University
- R. Dorff, Brigham Young University
- B. Ehlert, Brigham Young University
- E. Evans, Brigham Young University
- R. Evans, Brigham Young University
- M. Fabiano, Brigham Young University
- A. Frandsen, Duke University
- K. Finlinson, Brigham Young University
- J. Fisher, Brigham Young University
- R. Fuhriman, Brigham Young University
- S. Giddens, Brigham Young University
- C. Gigena, Brigham Young University
- M. Graham, Brigham Young University
- F. Glines, Brigham Young University
- M. Goodwin, Brigham Young University
- J. Grout, Drake University
- R. Grout, Brigham Young University
- J. Hendricks, Brigham Young University
- A. Henriksen, Brigham Young University
- I. Henriksen, Brigham Young University
- C. Hettinger, Brigham Young University
- S. Horst, Brigham Young University
- J. Humpherys, Brigham Young University
- T. Jarvis, Brigham Young University
- J. Leete, Duke University
- J. Lytle, Brigham Young University
- R. McMurray, Brigham Young University
- [S. McQuarrie](https://github.com/shanemcq18), Brigham Young University
- J. Morrise, Brigham Young University
- M. Morrise, Brigham Young University
- A. Morrow, Brigham Young University
- R. Murray, Brigham Young University
- J. Nelson, Brigham Young University
- M. Proudfoot, Brigham Young University
- D. Reber, Brigham Young University
- C. Robertson, Brigham Young University
- R. Sandberg, Brigham Young University
- J. Stewart, Brigham Young University
- S. Suggs, Brigham Young University
- T. Thompson, Brigham Young University
- M. Victors, Brigham Young University
- J. Webb, Brigham Young University
- J. West, University of Michigan}
- J. Whitehead, Brigham Young University
- A. Zaitzeff, Brigham Young University -->
