\lab{K-Nearest Neighbors and Support Vector Machines}{K-Nearest Neighbors and Support Vector Machines}
\objective{Implement the k-Nearest Neighbor (KNN) and binary Support Vector Machine (SVM) classifiers.}

For numerical data, one of the most simple classification methods is the 
k-nearest neighbor (KNN) classifier, which labels a new sample according 
to the majority vote of the nearest $k$ training samples. 
As $k$ is the only parameter for the model, this choice determines the effectiveness of the classifier. 
Throughout this lab we will explore how different values of $k$ affect the accuracy of our classifier.

Suppose we have numerical data $\mathbf{x}_{1}, \cdots, \mathbf{x}_{N}$ and 
associated labels $y_{1}, \cdots, y_{N}$, along with a metric $d$ on our feature space. 
We define the $k$-neighborhood of a new sample $\mathbf{x}$ to be 
\begin{equation*}
n(\mathbf{x},k) = 
\setconstruct{\mathbf{x}_{i}}{d(\mathbf{x}_{i}, \mathbf{x}) < d(\mathbf{x}_{j}, 
\mathbf{x}) \text{ for all but fewer than } k \text{ samples } \mathbf{x}_{j}}
\end{equation*}
Thus the $k$-neighborhood of a new sample is the set of samples from our training set 
which are the $k$ closest samples according to our metric.

\begin{problem}
Write a function that computes the $k$-neighborhood of a sample 
$\mathbf{x}$ given $k$ and a training set. Assume the use of the Euclidean metric.
\end{problem}

We define the $k$-neighborhood votes of a new sample $\mathbf{x}$ to be 
\begin{equation*}
v(\mathbf{x},k) = \setconstruct{y_{i}}{\mathbf{x}_{i} \in n(\mathbf{x},k)}
\end{equation*}
The label assigned to $\mathbf{x}$ according to the standard KNN classifier is the mode of the $k$-neighborhood votes.

\begin{problem}
Write a function that labels a new sample $\mathbf{x}$ given $k$ and a training set. Assume the use of the Euclidean metric.
\end{problem}

\begin{problem}
Write a KNN class which accepts initial training data and training labels. 
It should have a method to classify new samples, given a value of $k$. 
Load the iris dataset from \li{sklearn.datasets}, and by separating the data into training and testing sets, 
implement your class. Test your classifier on the test data given different values of $k$. 
What are the misclassification rates?
\end{problem}

Different values of $k$ lead to different results. 
Essentially, our choice of $k$ determines how far-reaching we would like the influence of a sample to be. 
Larger $k$ means that a sample is influenced by points farther away from it. 
Smaller $k$ means that a sample is influenced only by the few points nearest it. 
In either case, extreme choices of $k$ (too small or too big) often yield poor results.

Another powerful classifier is the support vector machine (SVM). 
There are two main ideas in this classifier: maximum-margin hyperplanes and kernel functions. 
The first is simply the thought that the simplest binary classifier is a separating hyperplane, 
the best being the hyperplane that is ``farthest'' from the nearest two points of opposing classes, 
while perfectly partitioning the training data. 
There are very few interesting classification problems where this is possible in the standard feature space. 
However, if we can transform the feature space into a higher-dimensional space, 
then we might be able to find such a hyperplane. Unfortunately, working in this higher-dimensional space can be quite costly,
which is where the kernel functions come into play.

The second big idea is that instead of working directly in the higher-dimensional space, 
we can choose our transformation in such a way that we can use \emph{kernel} functions for any 
necessary computations whose domain is the product space of the original feature space with itself. 
There are many, sometimes exotic, kernel functions to choose from, though in practice only a few forms are used. 
We let $\phi(\mathbf{x})$ be the transformation of $\mathbf{x}$ into the higher-dimensional space, 
and we let this transformation be determined by some kernel function 
\begin{equation*}
k(\mathbf{x}_{i},\mathbf{x}_{j}) = \phi(\mathbf{x}_{i})^{T}\phi(\mathbf{x}_{j}).
\end{equation*}

We assume now that our labels are simply $\pm 1$, and we assume $\phi(\mathbf{x}) \in \mathbb{R}^{K}$. 
We consider the hyperplane defined by $f(\phi(\mathbf{x})) = \mathbf{w}^{T}\phi(\mathbf{x}) + b$, 
where $\mathbf{w} \in \mathbb{R}^{K}$ and $b \in \mathbb{R}$. 
We wish to find $\mathbf{w}$ and $b$ such that 
$f(\phi(\mathbf{x}_{i})) > 0$ if $y_{i} = 1$ and 
$f(\phi(\mathbf{x}_{i})) < 0$ if $y_{i} = -1$. 
Thus we need $\mathbf{w}$ and $b$ to satisfy $y_{i}\left( \mathbf{w}^{T}\phi(\mathbf{x}) + b\right) > 0$ 
for all $i = 1, \cdots, N$. Additionally, we would like the distance between the boundary 
$\mathbf{w}^{T}\phi(\mathbf{x}) + b = 0$ and the nearest points to be maximized. 
We can determine this distance geometrically to be 
\begin{equation*}
\frac{2}{\norm{\mathbf{w}}},
\end{equation*}
and is called the margin. Thus we would like to solve the following optimization problem:
\begin{align*}
\text{minimize } & \norm{\mathbf{w}} \\
\text{subject to } & y_{i}\left(\mathbf{w}^{T}\phi(\mathbf{x}) + b\right) > 0 \; \; \; \text{for } i = 1, \cdots, N.
\end{align*}

Considering the Lagrangian of this optimization problem, we have the dual formulation of this optimization problem as
\begin{align*}
\text{maximize } & \sum_{n=1}^{N} a_{n} - \frac{1}{2} \sum_{i=1}^{N}\sum_{j=1}^{N} a_{i}a_{j}y_{i}y_{j}\phi(\mathbf{x}_{i})^{T}\phi(\mathbf{x}_{j}) \\
\text{subject to } & a_{i} \geq 0 \; \; \; i = 1, \cdots, N \\
 & \sum_{i=1}^{N} a_{i}y_{i} = 0.
\end{align*}

This is simply a quadratic programming problem, where the objective function is 
$\mathbf{a}^{T}\mathbf{1} - \frac{1}{2} \mathbf{a}^{T}Q\mathbf{a}$, where 
\begin{equation*}
Q_{ij} = y_{i}y_{j}\phi(\mathbf{x}_{i})^{T}\phi(\mathbf{x}_{j})^{T} = y_{i}y_{j}k(\mathbf{x}_{i},\mathbf{x}_{j}).
\end{equation*}
Quadratic programming problems have nice solutions, so this will be easy to solve. 
The classifier function $f(\mathbf{x}) = \sum_{i=1}^{N} a_{i}y_{i}k(\mathbf{x},\mathbf{x}_{i})$ 
also has a nice closed-form solution.

Given a training set of size \li{n\_samples} and a kernel $k$, with data $X$ and target $Y$, 
we can use \li{cvxopt} to solve this quadratic programming problem:
\begin{lstlisting}
>>> import cvxopt
>>> import numpy as np
>>> K = np.zeros((n_samples,n_samples))
>>> for i in xrange(n_samples):
>>>     for j in xrange(n_samples):
>>>         K[i,j] = k(X[i,:], X[j,:])
>>> Q = cvxopt.matrix(np.outer(Y, Y) * K)
>>> q = cvxopt.matrix(np.ones(n_samples) * -1)
>>> A = cvxopt.matrix(Y, (1, n_samples))
>>> b = cvxopt.matrix(0.0)
>>> G = cvxopt.matrix(np.diag(np.ones(n_samples) * -1))
>>> h = cvxopt.matrix(np.zeros(n_samples))
>>> solution = cvxopt.solvers.qp(Q, q, G, h, A, b)
>>> a = np.ravel(solutions['x'])
\end{lstlisting}
From this value $a$, our kernel $k$, a training set $X$, and target $Y$, we have everything we need to build an SVM classifier. 
But what should our kernel $k$ be?
There are three common kernels used:
\begin{align*}
\text{Polynomial: } & k(\mathbf{x},\mathbf{y}) = (\mathbf{x}^{T}\mathbf{y} + a)^{d} \\
\text{Radial Basis Function: } & k(\mathbf{x},\mathbf{y}) = e^{-\gamma \norm{\mathbf{x} - \mathbf{y}}^{2}} \\
\text{Sigmoid: } & k(\mathbf{x},\mathbf{y}) = \tanh \left(\mathbf{x}^{T}\mathbf{y} + r \right)
\end{align*}

\begin{problem}
Write an SVM class. Upon initialization, it should accept a training data set and training target set.
It should have a method called \texttt{setKernel} which accepts one of the three kernel types, 
and defines a kernel function for the object. It should also have a method to train the classifier, 
and another method to predict the class of a new sample. 
It should predict $1$ if $f(\mathbf{x}) > 0$ and $-1$ if $f(\mathbf{x}) < 0$.
\end{problem}

A data set on breast cancer has been provided to you. 
This is from a breast cancer database from the University of Wisconsin Hospital, Madison, from Dr. W. H. Wolberg.
The attributes are (in order): clump thickness, uniformity of cell size, uniformity of cell shape, 
marginal adhesion, single epithelial cell size, bare nuclei, bland chromatin, 
normal nucleoli, and mitoses, all on a scale from $1$ to $10$. 
The targets are either $1$ or $-1$, signifying malignant or benign, respectively.

\begin{problem}
Load the data set. Separate it into a training set and a test set. 
Train SVMs on the data, trying each kernel with various parameter values. What are your misclassification rates?
\end{problem}
