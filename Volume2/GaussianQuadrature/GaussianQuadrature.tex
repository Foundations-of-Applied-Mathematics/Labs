\lab{Gaussian Quadrature}{Gaussian Quadrature}
\label{Lab:GaussQuad}

\objective{
Learn the basics of Gaussian quadrature and its application to numerical integration.
Build a class to perform numerical integration using Legendre and Chebyshev polynomials.
Compare the accuracy and speed of both types of Gaussian quadrature with the built-in Scipy package.
Perform multivariate Gaussian quadrature.
}

% TODO:
% - Most of the lab is essentially magic right now. Needs explanation related to the theory of orthogonal polynomials. This item is possibly complete, not sure exactly what was wanted.

\section*{Quadrature Basics}

It can be shown that for any class of orthogonal polynomials $p\in \mathbb{R}[x;2n+1]$ with corresponding weight function $w(x)$, there exists a set of weights and points $\{ w_i, x_i \}_{i=0}^n$ such that
\[
\int_a^b p(x) w(x) dx = \sum_{i=0}^n p(x_i)w_i.
\]
Since this relationship is exact, a good approximation for the integral
\[
\int_a^b f(x) w(x) dx
\]
can be expected as long as the function $f(x)$ can be reasonably interpolated by a polynomial at the points $x_i$ for $i=0,1,\dots,n$.
In fact, it can be shown that if $f(x)$ is $2n+1$ times differentiable, the error of the approximation will decrease as $n$ increases.

Gaussian quadrature can be performed using any basis of orthonormal polynomials.
In this lab, two sets of orthogonal polynomials, the Legendre polynomials and the Chebyshev polynomials, will be used.
These polynomials have weight functions $w(x)=1$ and $w(x)=\frac{1}{\sqrt{1-x^2}}$, respectively.
Both of these weight functions are defined on the open interval $(-1,1)$.
\begin{problem}
Define a class to perform Gaussian quadrature.
The constructor should accept a variable $n$ denoting the number of points and weights to use (this will be explained later in the lab) and a variable \li{ptype} which defaults to \li{'legendre'}, 
\li{ptype} should be stored as a class attribute.
If \li{ptype} is not equal to \li{'legendre'} or \li{'chebyshev'}, raise a value error.
The rest of the class methods will be written throughout the remainder of this lab.
\end{problem}


\section*{Calculating Weights and Points} % ===================================

The first step of Gaussian quadrature is finding the weights and points that will be used.
There are several important algorithms that will find the weights and points of quadrature.
One based on a recurrence relationship inherent in all orthogonal polynomials will be considered in this lab.

\subsection*{The Golub-Welsch Algorithm} % ------------------------------------

All sets of orthogonal polynomials $\{u_k\}_{i=0}^{n}$ satisfy the three term recurrence relation
\[
u_{k+1} = (x-\alpha_k)u_k - \beta_ku_{k-1}
\]
where $u_{0} = 1$ and $u_1 = x-\alpha_1$.
The coefficients $\{\alpha_k, \beta_k\}$ have been calculated for several classes of orthogonal polynomials; there also exist algorithms for finding the coefficients for arbitrary classes of orthogonal polynomials.
%and may be determined for an arbitrary class using the procedure found in ``Calculation of Gauss Quadrature Rules'' by Golub and Welsch.
The coefficients of the Legendre polynomials are given by
\[
\alpha_k=0 \text{ and } \beta_k=\frac{k^2}{4k^2-1}
\]
while the coefficients of the Chebyshev polynomials are
\[
\alpha_k=0 \text{ and } \beta_k=\begin{cases} \frac{1}{2} &\mbox{ if } k = 1\\ \frac{1}{4} &\text{otherwise} \\ \end{cases}.
\]

The Golub-Welsch algorithm builds a tri-diagonal matrix from the recurrence relation coefficients and uses the eigenvalues and eigenvectors of the resulting matrix to find the weights and points of a quadrature.
The matrix is known as the Jacobi matrix and is defined as

\[
J = \begin{bmatrix}
\alpha_1 & \sqrt{\beta_1} & 0 & \dots & 0 \\
\sqrt{\beta_1} & \alpha_2 & \sqrt{\beta_2} & \dots & 0 \\
0 & \sqrt{\beta_2} & \alpha_3 &  \dots & 0 \\
\vdots & & \ddots & & \vdots \\
%\vdots & & \ddots & & \vdots \\
0 & \dots & & & \sqrt{\beta_{n-1}} \\
0 & \dots & & \sqrt{\beta_{n-1}} & \alpha_n
\end{bmatrix}.
\]

The $n$ eigenvalues are the quadrature points $x_i$ and their corresponding weights are given by $w_i=\mu(\mathbb{R})v_{i,0}^2$ where $v_{i,0}$ is the first entry of the $i^{th}$ eigenvector and 
$\mu(\mathbb{R})$ is the measure of the weight function.
The measures of the weight functions of the Legendre and Chebyshev polynomials are $2$ and $\pi$, respectively.
%Finding eigenvalues and eigenvectorsfor a tridiagonal matrix is a well conditioned problem.
%Using a good eigenvalue solver gives the Golub-Welsch algorithm a complexity of $O(n^2)$.
A complete treatment of the Golub-Welsch algorithm, including the computation of the recurrence relation coefficients for arbitrary orthogonal polynomials, may be found 
at \url{http://gubner.ece.wisc.edu/gaussquad.pdf}.

\begin{problem} % Construct the Jacobi matrix.\
\label{prob:jacobi}
Add a function to your class that accepts two Numpy arrays, one containing the $\alpha_k$ coefficients, and the other containing the $\beta_k$ coefficients from the recurrence relation given above.
Your function should return the corresponding Jacobi matrix.
\end{problem}

\begin{problem} % Calculate points and weights.
Add another function to your class that accepts an integer $n$ representing the number of points to use for the quadrature.
Calculate $\alpha$ and $\beta$ as above, form the Jacobi matrix using the function written in Problem \ref{prob:jacobi}, then use the matrix to find the points $x_i$ and weights $w_i$ that 
correspond to the initialized polynomial class.
This function should return two Numpy arrays of length $n$, one for the points and the other for the weights.

Recall that $\alpha$, $\beta$ and $\mu(\mathbb{R})$ will change, depending on the polynomial class being used.
Test your function by checking your returned points and weights against the following values using the Legendre polynomials with $n=5$
\[
\centering % TODO: make this a little prettier.
\begin{array}{c|c|c|c|c|c}
    x_i
    & -\frac{1}{3}\sqrt{5 + 2\sqrt{\frac{10}{7}}}
    & -\frac{1}{3}\sqrt{5 - 2\sqrt{\frac{10}{7}}}
    & 0
    & \frac{1}{3}\sqrt{5 - 2\sqrt{\frac{10}{7}}}
    & \frac{1}{3}\sqrt{5 + 2\sqrt{\frac{10}{7}}}
    \\[1em] \hline
    w_i
    & \dfrac{322-13\sqrt{70}}{900}
    & \dfrac{322+13\sqrt{70}}{900}
    & \dfrac{128}{225}
    & \dfrac{322+13\sqrt{70}}{900}
    & \dfrac{322-13\sqrt{70}}{900}
\end{array}.
\]
Note that the order of the points and weights in the given table may differ.

Now modify the constructor of your class so that it calls this function and stores the resulting points and weights as class attributes.
\end{problem}


\section*{Integrating with Given Weights and Points} % ========================

Now that the points and weights have been obtained, they can be used to approximate the integrals of different functions.
For a given function $f(x)$ with points $x_i$ and weights $w_i$
\[
\int_{-1}^{1} f(x) w(x) dx \approx \sum_{i=1}^n f(x_i)w_i.
\]
There are two problems with the preceding formula.
First, the weight function is part of the integral being approximated, and second, the points obtained are only found on the interval $(-1,1)$ (in the case of the Legendre and Chebyshev polynomials).
The second problem will be discussed in the following section, the first problem, however, can be fixed by defining a new function $g(x)$ as follows
\[
g(x) = f(x) / w(x).
\]
Thus
\[
\sum_{i=1}^n g(x_i)w_i \approx \int_{-1}^{1} g(x) w(x) dx = \int_{-1}^{1} f(x) dx.
\]

The integral of $f(x)$ on $[-1,1]$ can thus be approximated with the inner product $\w\trp g(\x)$, where $g(\x) = [g(x_1),\dots,g(x_n)]\trp$ and $\w = [w_1,\dots,w_n]\trp$.

\begin{problem} % Integrate with given points and weights.
Add a function to your class that accepts a callable function \li{f}.
Return the approximation of the integral of the function \li{f} on the interval $[-1,1]$.

Remember that the weight function depends on the type of polynomial (the type should be stored as a class attribute).
%Call your function \li{basic}.
You can test your function by integrating various functions by hand on this interval and comparing that value to your function's output.
Small values of $n$ ($n<10$) should give fairly accurate results and as you increase $n$, your approximation should improve.
%Using these points and weights should yield the approximations \[\int_{-\pi}^\pi \sin(x)dx \approx 0\quad\text{and}\quad\int_{-\pi}^\pi \cos(x)dx \approx 0.000196.\]
\label{prob:basic}
\end{problem}

\begin{info}
One of the most desirable properties of Gaussian quadrature is that the weights and points only need to be computed once.
Once the points and weights have been computed for a given $n$, the integral of a function $f$ can be approximated by using only $n$ evaluations and a simple summation.
Since the points and weights are independant of the function $f$, we can approximate the integral of any function without recomputing these values.
\end{info}


\section*{Shifting the Interval of Integration} % =============================

As discussed before, the weight functions used in this lab are defined only on the interval $(-1,1)$ so all of the points are found on that interval as well.
To integrate a function on an arbitrary interval $[a,b]$, a change of variables needs to take place.
Let \[u = \frac{2x - b - a}{b - a}\] so that $u = -1$ when $x = a$ and $u = 1$ when $x=b$.
Then 
\[
x = \frac{b - a}{2}u + \frac{a + b}{2}\qquad \text{and}\qquad dx = \frac{b - a}{2}du,
\] 
so the transformed integral is given by
\[
\int_a^b f(x) dx = \frac{b-a}{2}\int_{-1}^1 f\left(\frac{b-a}{2}u + \frac{a+b}{2}\right)du.
\]

\begin{comment}
The general quadrature formula is then given by the following equation.
\[
\int_a^b f(x) dx \approx \frac{b - a}{2} \sum_i w_i f\left(\frac{(b-a)}{2}x_i + \frac{(a+b)}{2}\right)
\]
\end{comment}

By defining a new function $h(x)$ as
\[
h(x_i) = f\left(\frac{(b-a)}{2}x_i + \frac{(a+b)}{2}\right) / w(x_i),
\]
the final form of the approximated integral is obtained
\[
\int_{a}^{b} f(x) dx \approx \frac{b-a}{2} \sum_{i=1}^n h(x_i)w_i .
\]

\begin{problem} % Shift the integral.
Write the final method of your class.
This method should accept a function \li{f} to integrate, an integer $n$ denoting the number of points to use and numbers $a$ and $b$ denoting the bounds of integration.
The function should return the approximation of the integral.
Test this function in a similar manner to Problem \ref{prob:basic}
\end{problem}

\begin{comment} % Unnecessary.
As an example, let $f(x) = x^2$ on $[1,4]$.
We know that $\left.\int_1^4 x^2 dx = \frac{x^3}{3}\right|_1^4 = 21$.
Then setting
\begin{align*}
g(x) &= \frac{b - a}{2}f\left(\frac{b-a}{2}x + \frac{b+a}{2}\right) \\
& = \frac{3}{2}\left(\frac{3}{2}x + \frac{5}{2}\right)^2 \\
&= \frac{27}{8}x^2 + \frac{45}{8}x + \frac{75}{8},
\end{align*}
the interval-adjusted integral of $f(x)$ is given by
\begin{align*}
\int_a^b f(x)dx = \int_{-1}^1 g(x)dx = \left.\frac{9}{8} x^3 + \frac{45}{4} x^2 + \frac{75}{8} x\right|_{-1}^1 = 21.
\end{align*}
\end{comment}


\section*{Numerical Integration with SciPy} % =================================

There are many other techniques for finding the weights and points for a given weighting function.
SciPy's \li{integrate} module provides some general-purpose integration tools.
For example, \li{scipy.integrate.quad()} is a reasonably fast Gaussian quadrature implementation.
Also included in the \li{integrate} module are fixed-precision and fixed-order Gaussian quadrature methods.
\begin{lstlisting}
>>> from scipy.integrate import quad

>>> f = lambda x: np.cos(x) * np.sin(x)**2 # Function to integrate.
>>> g = lambda x: np.sin(x)**3 / 3         # Indefinite integral.

# quad returns an array, the first entry is the computed value.
>>> calc = quad(f, -2, 3)[0]
>>> exact = g(3) - g(-2)                   # Exact value of the integral.
>>> np.<<abs>>(exact - calc)                   # Error of the approximation.
0.0
\end{lstlisting}

% TODO: need to demonstrate this if it's to be included.
\begin{comment}
Another common hallmark of quadrature is that it can be used adaptively.
It is common in practice to refine the points of a quadrature estimate on an interval where a function is observed to be changing rapidly.
This allows for more accurate computation at a relatively low computational cost.
This is the approach used by the function \li{scipy.integrate.quad()}.
\end{comment}

The standard normal distribution is an important object of study in probability and statistics.
It is defined by the probability density function $p(x) = \frac{1}{\sqrt{2 \pi}} e^{-x^2/2}$ (for a distribution with mean $0$ and a variance $1$).
This is function cannot be integrated symbolically so numerical techniques must be used.

The probability that a normally distributed random variable $X$ will take on a value less than (or equal to) a given value $x$ is
\[
P(X \le x) = \int_{-\infty}^x \frac{1}{\sqrt{2 \pi}} e^{-t^2/2} dt.
\]
This function is essentially zero for values of $x$ that lie far from the mean, so this probability can be estimated by integrating from $-5$ to $x$ instead of from $-\infty$ to $x$.

\begin{problem} % Integrate the standard normal.
Write a function that uses the standard normal distribution to compare the error of Legendre quadrature, Chebyshev quadrature and \li{scipy.integrate.quad()}.
Using your quadrature class, estimate the integral of the probability density function of the normal distribution (\li{scipy.stats.norm.pdf()}) on the interval $[-5,1]$.
Do this for $n=[1,5,10,\dots,30]$ and use these values to plot the error of the Legendre and Chebyshev quadratures on the same plot with $n$ on the $x$-axis and error on the $y$-axis 
(using a log scale for the $y$-axis).
Finally, plot a horizontal line accross your plot showing the error of \li{scipy.integrate.quad()}.
The following code will give you an exact value to use in computing the error of your approximations:

\begin{lstlisting}
from scipy.stats import norm
normal = norm()                  # Make a standard normal random variable.
exact = normal.cdf(1)            # Integrate the pdf from -infinity to 1.
\end{lstlisting}
\end{problem}


\section*{Multivariate Quadrature}

The extension of Gaussian quadrature to higher dimensions is fairly straightforward.
The following discussion concerns Gaussian quadrature using Legendre polynomials but extending to other polynomials is similar.
In the two-dimensional case, both the weights and the points in the $x$-dimension and $y$-dimension are calculated separately using a Jacobi matrix as before.
Given a function $f(x,y)$ to integrate, the function $g(x,y)$ is defined as
\[
g(x,y) = \frac{(b_1 - a_1) (b_2 - a_2)}{4} f\left( \frac{b_1 - a_1}{2} x + \frac{a_1 + b_1}{2}, \frac{b_2 - a_2}{2}y + \frac{a_2 + b_2}{2}\right)
\]
where $[a_1,b_1]\times [a_2,b_2]$ is the domain of integration.
The final Gaussian quadrature approximation is given by
\[
\int_{a_2}^{b_2} \int_{a_1}^{b_1} f(x,y) dx dy \approx \sum_{i=1}^n \sum_{j=1}^n w_i w_j g(z_i,z_j).
\]
In the previous formula, it was assumed that the number of points and weights is the same in the $x$- and $y$- dimensions; in this case, the points $\{z_i\}_{i=1}^n$ and weights $\{w_i\}_{i=1}^n$ 
are the same in both dimensions and the Jacobi matrix need only be computed once.

\begin{problem}
Write a function that performs two-dimensional Gaussian quadrature using Legendre polynomials.
Your function should accept a callable multivariate function \li{f}, four integers that denote the domain of integration (given in the order $a_1, b_1, a_2$ then $b_2$) and an integer $n$ denoting the number 
of points to use in each dimension.
Note that we have assumed that we will be using the same number of points in both dimensions so the previous equation is valid.
You should be able to copy and paste many of the methods you have already written in the \li{quadrature} class with minimal changes.

The following gives a sample outline of what your code should do:
\begin{enumerate}
\item Define a lambda function $g(x,y):\mathbb{R}^2 \rightarrow \mathbb{R}$ using the formula given above.
\item Construct the $n\times n$ Jacobi matrix.
\item Use the eigenvalues and eigenvectors of the Jacobi matrix to calculate the weights and points (these will be the same in both dimensions).
\item Calculate the double summation.
\end{enumerate}

Check that your function is working by comparing its output to simple hand computations or by using Scipy's multivariate quadrature method 
\li{scipy.integrate.dblquad()}\footnote{Documentation found at \url{https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.dblquad.html}}.
\end{problem}

Generalizing to even higher dimensions is a similar process with the points and weights being computed separately for each dimension.
Although Gaussian quadrature can obtain reasonable approximations in lower dimensions, it quickly becomes untractable in higher dimensions.
The number of points and weights required to obtain a good approximation prohibits Gaussian quadrature from being a viable method in higher dimensions.

