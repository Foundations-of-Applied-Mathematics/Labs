\lab{Modelling the spread of an epidemic: SIR models}{Modelling the spread of an epidemic: SIR models}
\label{lab:SIRModels}

% Many industry grade ode solvers are similar to the RK4 method already described. A common, reliable method that is a good choice for initially studying most problems is the Dormand-Prince method. This method is implemented in Python's \li{scipy.integrate} module as \li{dopri5}, and in MatLab as \li{ode45}. A similar method is the Runge-Kutta-Fehlberg method (RKF45).
%
% The Dormand-Prince method is a Runge-Kutta method that computes a fourth order accurate solution, followed by a fifth order accurate solution. These solutions are used to estimate the error in the fourth order solution. In turn, the estimated error is used to help determine the size of each step $h_i = t_i-t_{i-1}$ used by the method, instead of used a fixed stepsize $h = (b-a)/n$.
%
% We will demonstrate how to solve the initial value problem
% \begin{align*}
% y'(t) &= 6+2t-y, \\
% y(0) &= 2,
% \end{align*}
% using \li{dopri5}. We start with importing several useful modules and defining the ode.
% The \li{ode} class is imported from the \li{scipy.integrate} module.
% This class functions as an interface to several numerical ode methods, one of which is \li{dopri5}.
% These other methods can be useful in certain situations; however, \li{dopri5} is a good solver to try on new problems.
%
%
%
% We create an instance of the \li{ode} class and initialize it using the \li{set_integrator} and \li{set_initial_value} methods.
% Useful parameters are \li{atol} and \li{rtol}, which set the maximum allowed absolute and relative tolerances for the solution.
% Other parameters and methods are explained in the documentation for \li{scipy}.
% Here the method solves for $y(1.6)$:
%
% \begin{lstlisting}
% from scipy.integrate import ode
% import numpy as np
% import matplotlib.pyplot as plt
%
% a, ya, b = 0., 2., 1.6
% def ode_f(t,y): return np.array([-1.*y+6.+2.*t])
%
% ode_object = ode(ode_f)
% ode_object.set_integrator('dopri5',atol=1e-5)
% ode_object.set_initial_value(ya,a)
% print ode_object.integrate(b)
% \end{lstlisting}
%
% Alternatively, let us solve for $y$ on a evenly spaced mesh, and then plot the results.
% %# The output of this function must have the shape (dim,), where dim
% %# is the dimension of the system.
% \begin{lstlisting}
% ode_object = ode(ode_f).set_integrator('dopri5',atol=1e-5)
% ode_object.set_initial_value(ya,a)
%
% dim, t = 1, np.linspace(a,b,51)
% Y = np.zeros((len(t),dim))
% Y[0,:] = ya
% for j in range(1,len(t)): Y[j,:] = ode_object.integrate(t[j])
%
% plt.plot(t,Y[:,0],'-k')
% plt.show()
% \end{lstlisting}
%
% \begin{figure}[ht]
% \centering
% \includegraphics[width=\textwidth]{Example1.pdf}
% \caption{The solution of $y'(t) = 6+2t-y$, $y(0) = 2$, on the interval $[0,1.6]$, using the solver \li{dopri5} from \li{scipy.integrate}.}
% \label{sir:example1}
% \end{figure}
%
%
% \begin{problem}
% Using \li{dopri5}, solve the IVP
% \begin{align*}
% 5y''' + y'+2y &= 0, \,\, 0 \leq x \leq 16,\\
% y(0) &=0,\\
% y'(0) &= 1,\\
% y''(0) &= -2.
% \end{align*}
% \end{problem}
%
% Another good ode solver to try is \li{odeint}, also in \li{scipy.integrate}. \li{odeint} is a Python wrapping for the function \li{lsoda} from the Fortran library \li{odepack}. One of the nice features of \li{lsoda} is that it automatically switches between stiff and nonstiff solvers depending on the behavior of the problem.
%
%
% \section*{The SIR Model}
The SIR model describes the spread of an epidemic through a large population.
It does this by describing the movement of the population through three phases of the disease: those individuals who are \emph{susceptible}, those who are \emph{infectious}, and those who have been \emph{removed} from the disease.
Those individuals in the removed class have either died, or have recovered from the disease and are now immune to it.
If the outbreak occurs over a short period of time, we may reasonably assume that the total population is fixed, so that $S'(t) + I'(t) + R'(t) = 0$.
We may also assume that $S(t) + I(t) + R(t) = 1$, so that $S(t)$ represents the \textit{fraction} of the population that is susceptible, etc.

Individuals may move from one class to another as described by the flow
\[S \to I \to R.\]
Let us consider the transition rate between $S$ and $I $.
Let $\beta$ represent the average number of contacts made per day that could spread the disease.
The proportion of these contacts that are with a susceptible individual is $S(t)$.
Thus, one infectious individual will on average infect $\beta S(t)$ others per day.
Let $N$ represent the total population size.
Then we obtain the differential equation
\[\frac{d}{dt}(S(t) N) = -\beta S(t) (I(t) N)\]

 Now consider the transition rate between $I$ and $R$.
We assume that there is a fixed proportion $\gamma$ of the infectious group who will recover on a given day, so that
\[\frac{d}{dt}R(t) = -\gamma I(t).\]
Note that $\gamma$ is the reciprocal of the average length of time spent in the infectious phase.

Since the derivatives sum to $0$, we have $I'(t) = - S'(t) - R'(t)$, so the  differential equations are given by
\begin{align*}
\frac{dS}{dt} &=-\beta IS ,\\
\frac{dI}{dt} &= \beta I S-\gamma I,\\
\frac{dR}{dt} &=\gamma I.
\end{align*}


\begin{figure}[ht]
\centering
\includegraphics[width=\textwidth]{SIR1.pdf}
\caption{Solution to Problem (\ref{prob_sir1})}
\label{sir1}
\end{figure}


\begin{problem}
Solve the IVP
\begin{align*}
\frac{dS}{dt} &=-\frac{1}{2} IS ,\\
\frac{dI}{dt} &= \frac{1}{2} I S-\frac{1}{4} I, \\
\frac{dR}{dt} &=\frac{1}{4} I,\\
S(0) &= 1-6.25\cdot10^{-7},\\
I(0) &= 6.25\cdot10^{-7},\\
R(0) &=0,
\end{align*}
on the interval $[0,100]$, and plot your results.  See Figure \ref{sir1}. \label{prob_sir1}
\end{problem}



\begin{problem}
Suppose that, in a city of approximately three million, five have recently entered the city carrying a certain disease.
(Suppose they have just entered the infectious state.)

Each of those individuals has a contact each day that could spread the disease, and an average of three days is spent in the infectious state.
Find the solution of the corresponding SIR equations for the next fifty days and plot your results.


At the peak of the infection, how many in the city will still be able to work (Assume for simplicity that those who are in the infectious state either cannot go to work or are unproductive, etc.)
Print your result.

\end{problem}


\begin{problem}
Suppose that, in a city of approximately three million, five have recently entered the city carrying a certain disease.
(Suppose they have just entered the infectious state.)

Each of those individuals will make three contacts every ten days that could spread the disease, and an average of four days is spent in the infectious state.
Find the solution of the corresponding SIR equations and plot your results. See Figure \ref{sir:exercise3}.
\label{prob_sir3}
\end{problem}


\begin{figure}[ht]
\centering
\includegraphics[width=\textwidth]{exercise3.pdf}
\caption{Solution to Problem (\ref{prob_sir3}).}
\label{sir:exercise3}
\end{figure}



\section*{Variations on the SIR Model}

SIS Models describe diseases where individuals who have recovered from the disease do not gain
any lasting immunity.
There are only two compartments in this model: those who are \emph{susceptible}, and those who are \emph{infectious}.

The basic equations are given by
\begin{align*}
\frac{dS}{dt} &=-\beta I S + \gamma I ,\\
\frac{dI}{dt} &= \beta I S-\gamma I
\end{align*}

If we add to our basic SIR model to account for the death rate and an equal birth rate, the equations become
\begin{align*}
\frac{dS}{dt} &=\mu(1 -S) - \beta I S,\\
\frac{dI}{dt} &= \beta I S - (\gamma + \mu)I, \\
\frac{dR}{dt} &= \gamma I - \mu R
\end{align*}
where $\mu$ represents the death rate and equal birth rate, noting that any new person born is born into the susceptible population.

SIRS models take the previous model and allow the transfer of individuals from the recovered/removed class to rejoin the susceptible class.
\begin{align*}
\frac{dS}{dt} &= fR + \mu(1 -S) - \beta I S,\\
\frac{dI}{dt} &= \beta I S - (\gamma + \mu)I, \\
\frac{dR}{dt} &= -fR + \gamma I - \mu R.
\end{align*}

\begin{problem}
In the world there are 7 billion people.
Influenza, or the flu, is one of those viruses that everyone can be susceptible to, even after recovering from their last sickness.
The flu virus is able to change in order to evade our immune system and we become susceptible once more (although technically it is now a different strain).
Suppose the virus originates with 1000 people in Texas after Hurricane Harvey flooded Houston and stagnant water allowed the virus to proliferate.
According to WebMD (trustworthy source, right?), once you get the virus you are contagious up to a week, and kids up to 2 weeks.
For this lab, suppose you are contagious for 10 days before recovering.
Also suppose that on average someone makes one contact every two days that could spread the flu.
Since we can catch a new strain of the flu, suppose that a recovered individual becomes susceptible again with probability $f=1/50$.
The flu is also known to be deadly, killing hundreds of thousands every year on top of the normal death rate.
To assure a steady population, let the birth rate balance out the death rate, and in particular let $\mu=.0001$.

Using the SIRS model above, plot the proportion of population that is Susceptible, Infected, and Recovered over a year span (365 days).
\end{problem}

\subsection*{Boundary Value Problem}

The next exercise uses a variation of the SIR model called an SEIR model to describe the spread of measles (see \footnote{Numerical Solution of Boundary Value Problems for Ordinary Differential Equations, by Aescher, Mattheij, and Russell}).
This new model adds another compartment, called the \emph{exposed} or \emph{latency} phase.
It assumes that the rate at which measles is contracted depends on the season, i.e. the rate is periodic.
That allows us to formulate the yearly occurrence rate for measles as a boundary value problem.
The boundary value problem looks like
\begin{align}\label{SEIR_BVP}
\left[\begin{array}{c}S \\ E \\ I\end{array}\right]' &= \left[\begin{array}{c}\mu - \beta(t) S I \\\beta(t) SI - E/\lambda \\E/\lambda - I/\eta\end{array}\right],\\
S(0) &= S(1),\\
E(0) &= E(1),\\
I(0) &= I(1)
\end{align}

Parameters $\mu$ and $\lambda$ represent the birth rate of the population and the latency period of measles, respectively.
$\eta$ represents the infectious period before an individual moves from the infectious class to the recovered class.
After recovery an individual remains immune, which is why $R(t)$ is not included in the system.
The set up of this problem is not normal since we are excluding $R(t)$, but it results in a nice graph.

To solve this problem we will use a full-featured BVP solver that is available in \li{scipy}.
The code below demonstrates how to use \li{solve_bvp} to solve the BVP
\begin{align}\label{simple_bvp}
	\epsilon y'' + yy' - y &= 0, \quad y(-1) = 1, \quad y(1) = -1/3, \epsilon=.1
\end{align}
Look at figure \ref{bvp_ex} for the solution.

\begin{figure}
\centering
\includegraphics[width=\textwidth]{bvp_example.pdf}
\caption{Solution to \eqref{simple_bvp}}
\label{bvp_ex}
\end{figure}

\begin{lstlisting}
import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

epsilon, lbc, rbc = .1, 1, - 1/3

# The ode function takes the independent variable first
# It has return shape (n,)
def ode(x , y):
    return np.array([y[1] , (1/epsilon) * (y[0] - y[0] * y[1])])

# The BVP solver expects you to pass it the boundary
# conditions as a callable function that computes the difference
# between a guess at the boundary conditions
# and the desired boundary conditions.
# When we use the BVP solver, we will tell it how many constraints
# there should be on each side of the domain so that it knows
# how many entries to expect in the tuples BCa and BCb.
# In this case, we have one boundary condition on either side.
# These constraints are expected to evaluate to 0 when the
# boundary condition is satisfied.

# The return shape of bcs() is (n,)
def bcs(ya, yb):
    BCa = np.array([ya[0] - lbc])   # 1 Boundary condition on the left
    BCb = np.array([yb[0] - rbc])   # 1 Boundary condition on the right
    # The return values will be 0s when the boundary conditions are met exactly
    return np.hstack([BCa, BCb])

# The independent variable has size (m,) and goes from a to b with some step size
X = np.linspace(-1, 1, 200)
# The y input must have shape (n,m) and includes our initial guess for the boundaries
y = np.array([-1/3, -4/3]).reshape((-1,1))*np.ones((2, len(X)))

# There are multiple returns from solve_bvp(). We are interested in the y values which can be found in the sol field.
solution = solve_bvp(ode, bcs, X, y)
# We are interested in only y, not y', which is found in the first row of sol.
y_plot = solution.sol(X)[0]

plt.plot(X, y_plot)
plt.show()
\end{lstlisting}

\begin{problem}
Consider \eqref{SEIR_BVP}
Let the periodic function for our measles case be $\beta(t) = \beta_0(1 + \beta_1 \cos{2\pi t})$.
Use parameters $\beta_1 = 1,$ $\beta_0 = 1575,$ $\eta = 0.01,$ $\lambda = .0279,$ and $\mu = .02.$
Note: in this case, time is measured in years, so run the solution over the interval $\left[0, 1\right]$ to show a one-year cycle.
The boundary conditions are really just saying that the year will begin and end in the same state.

\li{solve_bvp} requires \emph{separated boundary conditions}.
In other words, each equation in the set of boundary conditions can only include values at one end of the interval.
To deal with this, let $C = [C_1, C_2, C_3]$, and add the equation
\[C' = 0\]
to the system of ODEs given above (for a total of 6 equations).
Then the boundary conditions can be separated using the following trick:
\begin{align*}
	\begin{pmatrix}C_1(0) \\C_2(0) \\ C_3(0) \end{pmatrix} &= \begin{pmatrix}S(0) \\E(0) \\ I(0) \end{pmatrix}, \quad 	\begin{pmatrix}C_1(1) \\C_2(1) \\ C_3(1) \end{pmatrix} = \begin{pmatrix}S(1) \\E(1) \\ I(1) \end{pmatrix}.
\end{align*}
Now $C_1,C_2,C_3$ become the 4th, 5th, and 6th rows of your solution matrix, so the 3 boundary conditions for the left are obtained by subtracting the last three entries of $y(0)$ from the first three entries, giving you $ya[0:3]-ya[3:]$. Similarly, your right boundary conditions will look like $yb[0:3]-yb[3:]$.

%This translates to 3 boundary conditions for the left and 3 for the right.  Now $C_1,C_2,C_3$ become the 4th, 5th, and 6th rows of your solution matrix.  
%The formulae you will want to use for the boundary conditions can be formed by subtracting one side of these equations from the other. That is, subtract the last 3 entries of $y(a)$ from the %first 3 entries for the left boundary conditions, and similarly for the right.
When you code your boundary conditions, note that \li{solve_bvp} changes the initial conditions to force all the entries in the return of \li{bcs()} to be zero.
You can use the initial conditions from Fig.~\ref{fig:sir4} as your initial guess (which will be an array of 6 elements). Remember that the initial infected proportion is small, not 0.

\label{prob:sir_measles}
\end{problem} 

\begin{figure}[ht]
\centering
\includegraphics[width=\textwidth]{measles.pdf}
\caption{Solution to Problem (\ref{prob:sir_measles})}
\label{fig:sir4}
\end{figure}