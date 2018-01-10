\lab{Newton and Quasi-Newton Methods}{Newton and Quasi-Newton Methods}

\objective{Newton's method is widely used due to its quick convergence properties. However, its formula includes computationally inefficient steps which can be avoided.
This lab explores variants on Newton's method which do not require the computationally costly calculation of the second derivative and demonstrates a common application of these methods.}

\section*{Introduction}
Newton's method is generally useful because of its fast convergence properties. 
However, Newton's method requires the explicit calculation of the second derivative (i.e., the Hessian matrix) at each step, which is computationally costly. 
Quasi-Newton methods modify Newton's method so that the Hessian does not have to be computed at each step, thus making computations faster.
This generally comes at the cost of slower convergence speed, but the increased computation speed can make these methods more effective in many cases.

\section*{Newton's Method}
At this point, we have discussed Newton's Method several times. In the n-dimensional version,
the next step is given by:

\begin{equation} \label{Eq:BasicNewton}
\mathbf{x}_{k+1} = \mathbf{x}_k - D^2f(\mathbf{x}_k)^{-1}Df(\mathbf{x}_k)^T
\end{equation}

\begin{problem}
Write a method that accepts the first and second derivatives $Df$ and $D^2f$ of objective function,  a starting point $\textbf{x}_0$, a maximum number of iterations \li{maxiter}, and a stopping tolerance \li{tol}.
Implement an n-dimensional Newton's method iteration and return a list containing: the minimizing x value, the number of iterations performed, and if the method converged as a boolean.
Test this method on the Rosenbrock function:
\[
f(x,y) = 100(y-x^2)^2 + (1-x)^2
\]
using starting points $(-2,2)$ and $(10,-10)$, maximum iterations $1000$, and tolerance $10^{-2}$.
Your results can be tested with the following:
\begin{lstlisting}
>>> import scipy.optimize as opt
>>> f = opt.rosen
>>> df = opt.rosen_der
>>> d2f = opt.rosen_hess
>>> minx = opt.fmin_bfgs(f=f,x0=np.array([-2,2]),fprime=df,maxiter=1000,avextol=10**-2)
\end{lstlisting}
\end{problem}

Newton's method is an extremely fast way to find optimizers, however, it requires an inputed second derivative.
If this derivative is not available, or too difficult to compute, we can use Quasi-Newton methods to find a minimum without drastically reducing the rate of convergence and improving the computational efficiency.

\begin{info}
Remember, Newton's method has quadratic convergence if:
\begin{enumerate}
\item $f: \mathbb{R} \rightarrow \mathbb{R}$ is $C^2$ in an open neighborhood $ I = (x_* - r, x_* + r)$ with $r \geq |x_* - x_0|$
\item $Df(x_k) \neq 0$ for $x_k$ in the iteration
\item $x_0$ is sufficiently close to $\alpha$ that the Taylor series approximation is accurate enough to ignore higher order terms. Additional conditions of closeness can be found in Volume 2 text.
\end{enumerate}
\end{info}

\section*{Broyden's Method}
Broyden's Method is a multidimensional version of the one dimensional secant method discussed previously.
Just as the secant method approximates the second derivative of a function by using the first derivatives at nearby points, Broyden's Method uses the Jacobian to update an approximated Hessian matrix.

To get an overview of how this method works, consider the quadratic Taylor series approximation used to construct Newton's method for a function:

\begin{equation}
g_k(\mathbf{x}) = f(\mathbf{x}_k) + Df(\mathbf{x}_k)(\mathbf{x} - \mathbf{x}_k) + \frac{1}{2}(\mathbf{x} - \mathbf{x}_k)^TA_K(\mathbf{x} - \mathbf{x}_k)
\end{equation}

\noindent By assuming that the Jacobian is the same at $\mathbf{x}$ and $\mathbf{x}_k$ this equation can be rearranged to

\begin{equation} \label{Eq:BroydenRestraint}
Df(\mathbf{x}_{k+1})-Df(\mathbf{x}_k)=(\mathbf{x}_{k+1}-\mathbf{x}_k)^TA_{k+1}.
\end{equation}
(See Volume 2, 9.4 for additional details)

Though there are many possible matrices,$A_{k+1}$, that can satisfy this equation, if an estimate of the Hessian $A_k$ at the point $\mathbf{x}_k$ is given, the best rank one approximation of $A_{k+1}$ (meaning that $A_{k+1} -  A_{k}$ is rank one) can be found to minimize $\|A_{k+1}-A_k\|$.
If $\mathbf{y}_k = Df(\mathbf{x}_{k+1})^T-Df(\mathbf{x}_k)^T$ and $\mathbf{s}_k=\mathbf{x}_{k+1}-\mathbf{x}_k$,  then $\mathbf{y}_k = A_{k+1}^T\mathbf{s}_k$.
With this notation, $\|A_{k+1}-A_k\|$ can be shown to be uniquely minimized by the following:

\begin{equation} \label{Eq:BroydenHessian}
A_{k+1} = A_k + \frac{\mathbf{y}_k-A_k\mathbf{s}_k}{\|\mathbf{s}_k\|^2}\mathbf{s}_k^T.
\end{equation}

This Hessian approximation can then be used in Newton's method as a replacement for the real Hessian as follows:
\begin{equation} \label{Eq:BroydenSolve}
\mathbf{x}_{k+1} = \mathbf{x}_k-A_{k}^{-1}Df(\mathbf{x}_k)^T
\end{equation}

Though this method no longer requires the Hessian $Df^2(x)$, it contains the calculation of $A_k^{-1}Df(\mathbf{x}_K)$ which is $O(n^3)$.
This computational cost can be remedied by adding a low rank update to the previously calculated $A_k^{-1}$.
This update process uses the Sherman-Morrison-Woodbury identity and is written as:
\[
A_{k+1}^{-1} = A_{k}^{-1} + \frac{\mathbf{s}_k - A_{k}^{-1}\mathbf{y}_k}{\mathbf{s}_k^T A_{k}^{-1}\mathbf{y}_k} (\mathbf{s}_k^T A_{k}^{-1})
\]

Though this method no longer requires the Hessian $Df^2(x)$ and is fairly quick computationally, it is not used commercially because it cannot always guarantee that the approximated Hessian $A_k$ is positive definite and that the method will converge.
This issue is remedied in a Quasi-Newton method called BFGS.

\subsection*{BFGS}
Descent methods require a decreasing sequence of approximations in the function, i.e. $(f(\mathbf{x}_k))_{k=0}^{\infty}$ where  $f(\mathbf{x}_{k})<f(\mathbf{x}_{k-1})$.
However, if the Hessian $Df^2(\mathbf{x}_k)$ (from Newton's method or the approximated Hessian $A_k$ from Broyden's method) is not positive definite, it is not guaranteed that $f(\mathbf{x}_{k})<f(\mathbf{x}_{k-1})$.
Broyden's method is particularly susceptible to this behavior because even with $D^2f(\mathbf{x}_k)>0$, the approximated Hessian $A_k$ can be negative.

The Broyden-Fletcher-Goldfarb-Shanno (BFGS) method is an adjustment to Broyden's method that maintains a positive-definite Hessian approximation.
It accomplishes this by creating a rank-two approximation instead of the rank-one approximation of Broyden's method using the formula: 

\begin{equation} \label{Eq:BFGSHessian}
A_{k+1} = A_k + \frac{\mathbf{y}_k\mathbf{y}_k^T}{\mathbf{y}_k^T\mathbf{s}_k}-\frac{A_k\mathbf{s}_k\mathbf{s}_k^TA_k}{\mathbf{s}_k^TA_k\mathbf{s}_k}
\end{equation}
 
\noindent with $\mathbf{y}_k = Df(\mathbf{x}_{k+1})^T-Df(\mathbf{x}_k)^T$ and $\mathbf{s}_k=\mathbf{x}_{k+1}-\mathbf{x}_k$ as before in \ref{Eq:BroydenSolve}.

This new approximation can also be altered by the Sherman-Morrison-Woodbury identity to increase computational speed. It is then written as:
\begin{equation} \label{Eq:BFGSHessianInv}
A_{k+1}^{-1} = A_k^{-1} + \frac{(\mathbf{s}_k^T\mathbf{y}_k + \mathbf{y}_k^TA_k^{-1}\mathbf{y}_k)\mathbf{s}_k\mathbf{s}_k^T}{(\mathbf{s}_k^T\mathbf{y}_k)^2} - \frac{A_k^{-1}\mathbf{y}_k\mathbf{s}_k^T + \mathbf{s}_k\mathbf{y}_k^TA_k^{-1}}{\mathbf{s}_k^T\mathbf{y}_k}
\end{equation}

\begin{problem}
Write a method that accepts a callable first derivative $Df$ of objective function, a starting Hessian guess $A_0$, a starting point $\textbf{x}_0$, a maximum number of iterations \li{maxiter}, and a stopping tolerance \li{tol}.
This method should implement the BFGS method using Equations \ref{Eq:BroydenSolve} and \ref{Eq:BFGSHessianInv} and return a list containing: the minimizing x value, the number of iterations performed, and if the method converged as a boolean.
Test this method on the following function:
\[
f(x,y) = e^{x-1}+e^{1-y}+(x-y)^2
\]
using starting point $(2,3)$, maximum iterations $1000$, and tolerance $10^{-2}$.
Your results can be tested with the following:
\begin{lstlisting}
>>> import scipy.optimize as opt
>>> f = lambda x : np.exp(x[0]-1) + np.exp(1 - x[1]) + (x[0] - x[1])**2
>>> df = lambda x : np.array([np.exp(x[0]-1) + 2*(x[0]-x[1]), -1*np.exp(1-x[1]) - 2*(x[0]-x[1])])
>>> minx = opt.fmin_bfgs(f=f,fprime=df,x0=[2,3],gtol=10**-2,maxiter=1000)
\end{lstlisting}
%Experiment with different starting points. Is BFGS faster than Broyden's method? Are there cases (i.e., different starting points or varying number of iterations) where one implementation is better than the other?
\end{problem}

\section*{Comparing Newton and Quasi-Newton Methods}

Each of the presented optimization algorithms can be efficient in different situations.
If the Jacobian and Hessian of a function are readily available and the Hessian is easily inverted, Newton's Method is usually the best option. 
If the Hessian is not available or difficult to compute, then using BFGS is most likely the best option.
Broyden's method is almost never better than BFGS but is useful for foundational understanding.

\begin{problem}
Compare the performance of your Newton's method and BFGS with the commercial versions in \li{scipy.optimize} on the following functions:
\begin{align*}
f(x,y) = 0.26(x^2+y^2) - 0.48xy
\end{align*}
\begin{align*}
f(x,y) = sin(x+y) + (x-y)^2 - 1.5x + 2.5y + 1
\end{align*}
Start at $(3,3)$, time how long each algorithm takes to run, and output the number of iterations that each took to complete.
\end{problem}

\section*{The Gauss-Newton Method}
\subsection*{Non-linear Least Squares Problems}
Least Squares problems aim to fit a line (or model parameters) to a given set of data points. 
These problems arise in many scientific fields, including economics, physics, and statistics and represent unconstrained optimization problems that minimize an objective function of the form
$$
f(\mathbf{x}) = \frac{1}{2}\displaystyle\sum_{j=1}^m r_j^2(\mathbf{x}),
$$
where each $r_i : \mathbb{R}^n \rightarrow \mathbb{R}$ is smooth and $m \geq n$.
This case of least squares problems can be solved with a line search method.

Specifically, with data points $(t_1, y_1), (t_2, y_2), \ldots, (t_m, y_m)$, where $t_i,y_i \in \mathbb{R}$ for $i = 1, \ldots, m$. 
Let $\phi(\mathbf{x}, \mathbf{t)}$ be a possible model for this data set, where $\mathbf{x}$ is a vector of parameters of the model, and $\mathbf{t} \in \mathbb{R}^n$. 
We can measure the error at the $i$-th data point (called the residual) by the value $$r_i(\mathbf{x}) := \phi(x_i, t_i) - y_i,$$ and by summing the squares of these errors, we obtain our non-linear least squares objective function:
$$
f(\mathbf{x}) = \frac{1}{2} \displaystyle \sum_{j=1}^m  r_j^2(\mathbf{x}).
$$

The Jacobian and Hessian of this function can then be expressed as,
\begin{align*}
Df(\mathbf{x}) &= J(\mathbf{x})^T r(\mathbf{x}), \\
D^2 f(\mathbf{x}) &= J(\mathbf{x})^TJ(\mathbf{x}) + \displaystyle \sum_{j=1}^m r_j(\mathbf{x}) D^2r_j(\mathbf{x}).
\end{align*}

\noindent with, 
%\begin{align*}
$\mathbf{r}(\mathbf{x}) = [r_1(\mathbf{x}), r_2(\mathbf{x}), \ldots, r_m(\mathbf{x})]^T$, and,
$J(\mathbf{x}) = [D r_1(\mathbf{x})^T, D r_2(\mathbf{x})^T, \hdots, D r_m(\mathbf{x})]^T$.
%\end{align*}


The second term in the formula for $D^2 f$ involves second derivatives and can be problematic to compute. 
In practice, the second term in the formula for $D^2 f$ is small, either because the residuals themselves are small, or because they are nearly affine in a neighborhood of the solution.
The simplest method for solving the nonlinear least squares problem, known as the \emph{Gauss-Newton Method}, exploits this observation, simply ignoring the second term and making the approximation
$$
D^2 f(\mathbf{x}) \approx J(\mathbf{x})^TJ(\mathbf{x}).
$$
The method then proceeds in a manner similar to Newton's Method.
Thus, at each iteration, we find $\mathbf{x}_{k+1}$ as follows:
\begin{equation} \label{Eq:GaussNewtonUpdate}
\mathbf{x}_{k+1} = \mathbf{x}_k-(J(\mathbf{x}_k)^TJ(\mathbf{x}_k))^{-1}J( \mathbf{x}_k)^T \mathbf{r}( \mathbf{x}_k).
\end{equation}

\noindent An example of this kind of nonlinear least squares problem follows below.

Suppose we have data points generated from a sine function and slightly perturbed by gaussian noise. 
In Python this data can be generated as follows:

\begin{lstlisting}
>>> t = np.arange(10)
>>> y = 3*np.sin(0.5*t)+ 0.5*np.random.randn(10)
\end{lstlisting}

Python functions for the proposed model, the residual vector, and the Jacobian can then be written as follows:

\begin{lstlisting}
>>> def model(x, t):
>>>     return x[0]*np.sin(x[1]*t)
>>> def residual(x):
>>>     return model(x, t) - y
>>> def jac(x):
>>>     ans = np.empty((10,2))
>>>     ans[:,0] = np.sin(x[1]*t)
>>>     ans[:,1] = x[0]*t*np.cos(x[1]*t)
>>>     return ans
\end{lstlisting}

By inspecting the data, an initial guess for the parameters could be $x_0 = (2.5, 0.6)$.
A function implementing Gauss Newton can then be used to find the least squares solution.

\begin{lstlisting}
>>> x0 = np.array([2.5,.6])
>>> x,niters,conv = gaussNewton(jac, residual, x0, maxiter=10, tol=10**-3)
\end{lstlisting}

A plot can then compare the fitted model with the data and the original sine curve from which the data were generated.

\begin{lstlisting}
dom = np.linspace(0,10,100)
plt.plot(t, y, '*')
plt.plot(dom, 3*np.sin(.5*dom), '--')
plt.plot(dom, x[0]*np.sin(x[1]*dom))
plt.show()
\end{lstlisting}


\begin{problem}
Write a method that accepts a function for the proposed model $\phi(\mathbf{x})$, the model derivative $D\phi(\mathbf{x})$, a function that returns the residual vector $r(\mathbf{x})$, a callable function that returns the Jacobian of the residual $Dr(\mathbf{x}) = J(\mathbf{x})$, a starting point $\mathbf{x}_0$, a max number of iterations \li{maxiter}, and a stopping tolerance \li{tol}.
This method should implement the Gauss-Newton Method and return a list containing: the minimizing x value, the number of iterations performed, and if the method converged as a boolean.

Test your function by using the Jacobian function, residual function, and starting point given in the example above.
You can test your results with the following function:
\begin{lstlisting}
>>> import scipy.optimize as opt
>>> r = lambda x:
>>> J = lambda x:
>>> minx = opt.leastsq(fun=r, x0=, Dfun=J,xtol=,maxfev=maxiter)
\end{lstlisting} 
\end{problem}

\subsection*{Application of Non-linear Least Squares}
Non-linear least squares problems can be used to analyze trends in data or to predict future events and are ubiquitous in many academic fields as well as in industrial applications and machine learning.

\begin{problem}
We have census data giving the population of the United States every ten years since 1790.
The data is contained in a group of the first 8 decades and the first 16 decades of records in \li{pop_sample1.npy} and \li{pop_sample2.npy}.
The top row of these is the decade number and the second row is the population samples.
These can be loaded as follows:
\begin{lstlisting}
>>> import numpy as np
>>> pop_sample1 = np.load('pop_sample1.npy')
>>> print(pop_sample1)
<<[[  0.      1.      2.      3.      4.      5.      6.      7.   ]>>
<<[  3.929   5.308   7.24    9.638  12.866  17.069  23.192  31.443]]>>
\end{lstlisting}
Consider just the first 8 decades of population data. 
By plotting the data and hypothesizing about the behavior of populations, it is reasonable to hypothesize an exponential model for the population.
That is,
$$
\phi(x_1,x_2,x_3,t) = x_1\exp(x_2(t+x_3)).
$$
Use initial guess $(150, .4, 2.5)$ for the parameters $(x_1, x_2, x_3)$ and your Gauss Newton function (or the \li{opt.leastsq} function) to fit the model.
Plot the data against the fitted curve, to see how close it approximates population behavior.

Do the same for the 16 data points.
The plot of the 16 data points shows that the model is no longer a good fit.
This suggests that population growth is not exactly exponential but instead a logistic model.
These types of models are treated in the gradient descent lab.
\end{problem}
















%%Old Broyden's
\begin{comment}
If we have the point $\mathbf{x}_k$ and the Hessian $D^2f(\mathbf{x}_k)$ at that point, we can use the following equation to select our guess for the zero of the function:

\begin{equation} \label{Eq:BroydenSolve}
\mathbf{x}_{k+1} = \mathbf{x}_k-D^2f(\mathbf{x}_k)^{-1}Df(\mathbf{x}_k)^T.
\end{equation}
This is precisely Newton's method. However, since calculating the Hessian at each step is costly, we instead estimate the Hessian (just as we used a secant line to approximate the derivative in the one-dimensional case).

The idea is to construct the best rank-one approximation of the Hessian at each iteration. This approximation, denoted $A_{k+1}$, must satisfy

In multiple dimensions, this equation will be underdetermined (i.e., many $A_{k+1}$'s will satisfy the equation). Suppose that we have a previous estimate of the Hessian $A_k$ at the point $\mathbf{x}_k$ (note that for the first iteration, we plug in the starting point to the Hessian as our first approximation). We can then find the best approximation of $A_{k+1}$ that minimizes $\|A_{k+1}-A_k\|$. If we define $\mathbf{y}_k = Df(\mathbf{x}_{k+1})^T-Df(\mathbf{x}_k)^T$ and $\mathbf{s}_k=\mathbf{x}_{k+1}-\mathbf{x}_k$, this requirement is uniquely fulfilled by the following:
\begin{equation} \label{Eq:BroydenHessian}
A_{k+1} = A_k + \frac{\mathbf{y}_k-A_k\mathbf{s}_k}{\|\mathbf{s}_k\|^2}\mathbf{s}_k^T.
\end{equation}

After we have obtained the approximation of the Hessian (Equation \ref{Eq:BroydenHessian}), we can apply Equation \ref{Eq:BroydenSolve} to find $\mathbf{x}_{k+1}$. We can then repeat this process until we have (presumably) converged to a zero of the function.

\begin{problem}
Write a method that accepts a callable function $f$, it's first derivative $Df$, a starting Hessian guess $A_0$, a starting point $\textbf{x}_0$, a maximum number of iterations \li{maxiter}, and a stopping tolerance \li{tol}.
This method should implement Broyden's method and return a list containing: the minimizing x value, the number of iterations performed, and if the method converged as a boolean.
Test this method on the following function:
\[
f(x,y) = e^{x-1}+e^{1-y}+(x-y)^2
\]
using starting points $(2,3)$ and $(3,2)$, maximum iterations $1000$, and tolerance $10^{-2}$.
Your results can be tested with the following:
\begin{lstlisting}
>>> import scipy.optimize as opt
>>> f = lambda x: np.array([])
>>> df = lambda x: np.array([np.exp(x[0] - 1) + 2*(x[0] - x[1]), np.exp(1-x
    ...: [1]) - 2*(x[0]-x[1])])
>>> A0 = np.array([])
>>> minx = opt.broyden1(F=df, xin=[2,3], x_tol=10**2, maxiter=1000)
\end{lstlisting}
\end{problem}

\begin{info}
We can often make Broyden's method faster using the Sherman-Morrison-Woodbury Formula.
This formula allows us to efficiently calculate the inverse of a matrix when we add
a low rank update to that matrix. After manipulation of the Sherman-Morrison-Woodbury
Formula, we obtain the following:
\[
A_{k+1}^{-1} = A_{k}^{-1} + \frac{\mathbf{s}_k - A_{k}^{-1}\mathbf{y}_k}{\mathbf{s}_k^T A_{k}^{-1}\mathbf{y}_k} (\mathbf{s}_k^T A_{k}^{-1})
\]
Thus, we can calculate the inverse of the Hessian in the first step of our algorithm
and then calculate an update to the inverse at each step using the above formula.
\end{info}

%%% OLD GAUSS NEWTON
The individual functions $r_i$ that measure the error between the model and the data point are known as \emph{residuals},
and we can aggregate these functions into a \emph{residual vector}
$$
\mathbf{r}(\mathbf{x}) := (r_1(\mathbf{x}), r_2(\mathbf{x}), \ldots, r_m(\mathbf{x}))^T.
$$
The Jacobian of $\mathbf{r}(\mathbf{x})$ can be expressed in terms of the gradients of each $r_i$ as follows:
$$
J(\mathbf{x}) = \begin{bmatrix} \nabla r_1(\mathbf{x})^T \\ \nabla r_2(\mathbf{x})^T \\ \vdots \\ \nabla r_m(\mathbf{x})^T \end{bmatrix}
$$
You can further verify that
\begin{align*}
\nabla f(\mathbf{x}) &= J(\mathbf{x})^T r(\mathbf{x}), \\
\nabla^2 f(\mathbf{x}) &= J(\mathbf{x})^TJ(\mathbf{x}) + \displaystyle \sum_{j=1}^m r_j(\mathbf{x}) \nabla^2r_j(\mathbf{x}).
\end{align*}

In particular, at the $k$-th iteration, we choose a search direction $p_k$ that solves the linear system
$$
J_k^TJ_kp_k = -J_k^Tr_k.
$$

For convenience, we summarize these steps in Algorithm \ref{alg:guassnewton}.

\begin{algorithm}
\begin{algorithmic}[1]
\Procedure{Gauss-Newton}{}
    \State \textrm{Choose initial parameter vector } $x_0$
    \State $k \gets 0$
    \While{$J_k^Tr_k \neq 0$}
        \State \textrm{solve } $J_k^TJ_kp_k = -J_k^Tr_k$
        \State \textrm{choose step size } $\alpha_k$ \textrm{ satisfying Wolfe Conditions.}
        \State $x_{k+1} \gets x_k + \alpha_kp_k$
        \State $k \gets k+1$
    \EndWhile
\EndProcedure
\end{algorithmic}
\caption{Gauss-Newton Method}
\label{alg:guassnewton}
\end{algorithm}

Now we write Python functions for our model, the residual vector, the Jacobian, the objective function,
and the gradient. The calculations for all of these are straight forward.
\begin{lstlisting}
>>> def model(x, t):
>>>     return x[0]*np.sin(x[1]*t)
>>> def residual(x):
>>>     return model(x, t) - y
>>> def jac(x):
>>>     ans = np.empty((10,2))
>>>     ans[:,0] = np.sin(x[1]*t)
>>>     ans[:,1] = x[0]*t*np.cos(x[1]*t)
>>>     return ans
>>> def objective(x):
>>>     return .5*(residual(x)**2).sum()
>>> def grad(x):
>>>     return jac(x).T.dot(residual(x))
\end{lstlisting}
By inspecting our data, we might make an initial guess for the parameters $x_0 = (2.5, 0.6)$.
We are now ready to use our \li{gaussNewton} function to find the least squares solution.
\begin{lstlisting}
>>> x0 = np.array([2.5,.6])
>>> x = gaussNewton(jac, residual, x0, niter=10)
\end{lstlisting}
We can plot everything together to compare our fitted model with the data and the original sine
curve from which the data were generated.
\begin{lstlisting}
dom = np.linspace(0,10,100)
plt.plot(t, y, '*')
plt.plot(dom, 3*np.sin(.5*dom), '--')
plt.plot(dom, x[0]*np.sin(x[1]*dom))
plt.show()
\end{lstlisting}


The module \li{scipy.optimize} also has a method to solve non-linear least squares problem, and it
is quite convenient. The function is called \li{leastsq}, and in its most basic use, you only need
to pass in the residual function and starting point as arguments. In the example above, we simply
need to execute the following code:
\begin{lstlisting}
>>> from scipy.optimize import leastsq
>>> x2 = leastsq(residual, x0)[0]
\end{lstlisting}
This should give us the same answer, but much faster.

Thus, your new model is
$$
\phi(x_1,x_2,x_3,t) = \frac{x_1}{1+\exp(-x_2(t+x_3))}.
$$
By inspection, find a reasonable
initial guess for the parameters $(x_1, x_2, x_3)$ (i.e. $(150, .4, -15)$).
Again, write Python functions for the model and the corresponding residual vector,
and fit the model. Plot the data against the fitted curve. It should be a good fit.



\end{comment}
