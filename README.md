## About

_Foundations of Applied Mathematics_ is a series of four textbooks developed for Brigham Young University’s Applied and Computational Mathematics degree program for beginning graduate and advanced undergraduate students.
These are as follows:
- [_Volume 1: Mathematical Analysis._](http://bookstore.siam.org/ot152/)
- _Volume 2: Algorithms, Approximation, and Optimization._
- _Volume 3: Modeling with Uncertainty and Data._
- _Volume 4: Modeling with Dynamics and Control._

The textbooks are being published by [the Society for Industrial and Applied Mathematics](http://bookstore.siam.org).
[Volume 1](http://bookstore.siam.org/ot152/) is available now.
Volume 2 will be available in 2019, and the remaining volumes will be available soon thereafter.

This repository contains a collection of Python labs that go in tandem with the textbooks.
These expose students to applications and numerical computation and reinforce the theoretical ideas taught in the text.
The text and labs combine to make students technically proficient and to answer the age-old question, "When am I going to use this?"

The _Python Essentials_ labs introduce Python and its scientific computing tools.
The  _Data Science Essentials_ labs introduce common tools for gathering, cleaning, organizing, and presenting data in Python.
The _Volume 1_ and _Volume 2_ labs are also currently available; labs for the other volumes are forthcoming.

Visit [foundations-of-applied-mathematics.github.io/](http://foundations-of-applied-mathematics.github.io) or the [releases page](https://github.com/Foundations-of-Applied-Mathematics/Labs/releases) to download the lab manual PDFs directly.

## Build Instructions

If you would rather build the PDFs locally, [fork this repository and clone your fork](https://guides.github.com/activities/forking/).
Each volume can then be built separately using the LaTeX files listed below.
- Python Essentials: `PythonEssentials.tex`
- Data Science Essentials: `DataScienceEssentials.tex`
- Volume 1, Mathematical Analysis: `Volume1.tex`
- Volume 2, Algorithm Design and Optimization: `Volume2.tex`
- Volume 3, Modeling with Uncertainty and Data: `Volume3.tex`
- Volume 4, Modeling with Dynamics and Control: `Volume4.tex`

Compile the files using TeXShop or a similar program, or via the command line:
```bash
# Create docs/Volume1.pdf with latexmk (see Makefile).
$ make Volume1.pdf

# Equivalently, use latexmk directly.
$ latexmk -pdf -outdir=docs Volume1.tex
```
These commands create a PDF in the `docs/` folder called, for example, `docs/Volume1.pdf`.

## Contributing

To report bugs in the provided materials, typos or inaccuracies in the labs, or any other problems, [submit an issue on Github](https://github.com/Foundations-of-Applied-Mathematics/Labs/issues/new).
Please contact us at [acme@mathematics.byu.edu](mailto:acme@mathematics.byu.edu) if you have specific questions or feedback, or if you would like to be more involved with developing the labs.

## Authors

#### Managing Editors

Jeffrey Humpherys and Tyler J. Jarvis  
Department of Mathematics  
Brigham Young University  
Email: [acme@mathematics.byu.edu](mailto:acme@mathematics.byu.edu)  

#### Faculty Contributors

- E. Evans, Brigham Young University
- R. Evans, University of Chicago
- J. Grout, Drake University
- J. Whitehead, Brigham Young University

#### Editors

R. Jones, S. McQuarrie, M. Cook, A. Zaitzeff, A. Henriksen, R. Murray

#### Student Contributors

J. Adams, J. Bejarano, Z. Boyd, M. Brown, A. Carr, T. Christensen, M. Cook,
B. Ehlert, M. Fabiano, A. Frandsen, K. Finlinson, J. Fisher, R. Fuhriman,
S. Giddens, C. Gigena, C. Glover, M. Graham, F. Glines, M. Goodwin, R. Grout,
J. Hendricks, A. Henriksen, I. Henriksen, M. Hepner, C. Hettinger, S. Horst,
K. Jacobson, R. Jones, J. Leete, J. Lytle, R. McMurray, S. McQuarrie,
D. Miller, J. Morrise, M. Morrise, A. Morrow, R. Murray, J. Nelson,
E. Parkinson, M. Probst, M. Proudfoot, D. Reber, C. Robertson, M. Russell,
R. Sandberg, C. Sawyer, J. Stewart, S. Suggs, A. Tate, T. Thompson,
M. Victors, J. Webb, R. Webb, J. West, and A. Zaitzeff.

## License

This work is licensed under the Creative Commons Attribution 3.0 United States License.
To view a copy of this license please visit [http://creativecommons.org/licenses/by/3.0/us/](http://creativecommons.org/licenses/by/3.0/us/).

This project is funded in part by the National Science Foundation, grant no. TUES Phase II DUE-1323785.
