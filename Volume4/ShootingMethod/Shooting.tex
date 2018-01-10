\lab{The Shooting Method for Boundary Value Problems}{The Shooting Method for Boundary Value Problems}
\label{lab:Shooting}

Consider a boundary value problem of the form
\begin{align}
	\label{shooting_bvp}
	\begin{split}
y'' &= f(x,y,y'), \quad a \leq x \leq b, \\
y(a) &= \alpha, \quad y(b) = \beta.
\end{split}
\end{align}
One natural way to approach this problem is to study the initial value problem (IVP) associated with this differential equation:
\begin{align}
	\label{shooting_ivp}
	\begin{split}
y'' &= f(x,y,y'), \quad a \leq x \leq b, \\
y(a) &= \alpha, \quad y'(a) = t.
	\end{split}
\end{align}

\begin{warn}
Here, do not mistake $t$ as an independent time variable.
It is a parameter for the boundary condition.
The prime $'$ notation represents the derivative with respect to $x$, which is an important distinction later in this section.
\end{warn}
The goal is to determine an  appropriate value $t$ for the initial slope, so that the solution of the IVP is also a solution of the boundary value problem.

Let $y(x,t)$ be the solution of \eqref{shooting_ivp}.
We can rewrite the initial value conditions as
\begin{align}
y(a, t) = \alpha, \quad y'(a, t) = t
\end{align}
We wish to find a value of $t$ so that $y(b,t) - \beta = 0$.
Applying Newton's method to the function $h(t) = y(b,t) - \beta$, we obtain the iterative method
\begin{align*}
	t_{n+1} &= t_n - \frac{ h(t_n)}{h'(t_n) }, \\
	&= t_n - \frac{ y(b,t_n) - \beta}{\frac{d}{dt} \left.y(b,t)\right|_{t_n} },\quad n = 0,1,\ldots .
\end{align*}

We recall that Newton's method requires a good initial guess $t_0$; a plausible initial guess would be the average rate of change of the solution across the entire interval, so that $t_0 =  (\beta - \alpha)/(b-a)$.
If this initial guess is not sufficient, the initial guess may be refined by looking at the solution $y(x,t_0)$ of the initial value problem.

This method requires us to evaluate or approximate the function $\frac{d}{dt} \left.y(b,t)\right|_{t_n}$.
This term may be approximated with a finite difference, giving us the iterative method
\[t_{n+1} = t_n - \frac{ (y(b,t_n) - \beta)(t_n - t_{n-1})}{y(b,t_n) - y(b,t_{n-1}) }, \,\, n = 1, 2,\hdots\]
This variation of the shooting algorithm is called the secant method, and requires two initial values instead of one.
Notice that finding $y(b,t_n)$ requires solving the initial value problem using RK4 or some other method.

For example, consider the boundary value problem
\begin{equation}
\begin{split}
\label{bvp1}
y'' &= -4y -9\sin(x), \,\, x \in [0,3\pi/4],\\
y(0) &= 1, \\
y(3 \pi/4) &= -\frac{1+3\sqrt{2}}{2}.
\end{split}
\end{equation}
The following code implements the secant method to solve \eqref{bvp1}.
Notice that \li{odeint} is the solver used for the initial value problems.

\lstinputlisting[style=FromFile]{secant_method.py}

% The following code employs the secant method to find the initial slope $y'(0) = t$ of a solution of \ref{bvp1}.
% The numerical solution may then be computed and plotted using \li{dopri5} and \li{matplotlib}.
% \ref{bvp1} has an exact solution $y(x) = \cos(2x) + (1/2)\sin(2x) -3\sin(x)$.

% Recall that the necessary dependencies are \li{numpy} and the \li{ode} class from \newline \li{scipy.integrate}.
% The first step to finding the initial slope $y'(0) = t$ is to define the ODE as a first order system of differential equations, and to define the necessary parameters:
% \begin{lstlisting}
% def ode_f(x,y): return numpy.array([y[1] , -4.*y[0] - 9.*numpy.sin(x)])
%
% a, b = 0., 3*numpy.pi/4.
% alpha, beta =  1., -(1.+3*numpy.sqrt(2))/2.
%
% \end{lstlisting}
% To calculate $y(b,t_0)$ we use the \li{ode} class:
% \begin{lstlisting}
% reltol, abstol = 1e-9,1e-8
% example = ode(ode_f).set_integrator('dopri5',atol=abstol,rtol=reltol)
% example.set_initial_value(np.array([alpha,t0]),a)
% y0 = example.integrate(b)[0]
% \end{lstlisting}

% \begin{problem} Use the secant method to solve the bvp
% \begin{equation*}
% \begin{split}
% y'' &= -4y -9\sin(x), \quad x \in [0,3\pi/4],\\
% y(0) &= 1, \\
% y(3\pi/4) &=-\frac{1+3\sqrt{2}}{2}.
% \end{split}
% \end{equation*}
% When you code the secant method, be sure to include a maximum number of iterations, as well as an appropriate stopping criteria.
% For example, if $|y(b,t_n)-\beta|<10^{-8},$ you have likely found a solution.
% \end{problem}

\begin{problem}
Appropriately defined initial value problems will usually have a unique solution.
Boundary value problems are not so straightforward; they may have no solution or they may have several.
You may have to determine which solution is physically interesting.
The following bvp has at least two solutions.
Using the secant method, find both numerical solutions and their initial slopes.
(Their plots are given in Figure \ref{prob:shooting1}.)
What initial values $t_0, t_1$ did you use to find them?
\begin{equation*}
\begin{split}
y'' &= -4y -9\sin(x), \,\, x \in [0,\pi],\\
y(0) &= 1, \\
y(\pi) &=1.
\end{split}
\end{equation*}

\begin{figure}[H]
\includegraphics[width=\textwidth]{Fig1.pdf}
\caption{Two solutions of $y'' = -4y -9\sin(x),$ both satisfying the boundary conditions $y(0) = y(\pi) = 1.$}
\label{prob:shooting1}
\end{figure}
\end{problem}

Let us consider how to solve for $\frac{d}{dt} y(b,t)$.
We will assume that the function $y(x,t)$ can be differentiated with respect to $x$ and $t$ in any order, and let  $z(x,t) = \frac{d}{dt} y(x,t).$
Using the chain rule, we obtain
\begin{eqnarray*}
z'' = \frac{d}{dt} y''(x,t) &=& \frac{\partial f}{\partial y} (x,y(x,t),y'(x,t)) \cdot \frac{dy}{dt}(x,t) ,\\
&+& \frac{\partial f}{\partial y'} (x,y(x,t),y'(x,t)) \cdot \frac{dy'}{dt}(x,t),
\end{eqnarray*}
Using the initial conditions associated with $y(x,t)$ and noting that $z(x, t) = \frac{d}{dt}y(x, t)$ and $z'(x, t) = \frac{d}{dt}y'(x, t)$, we obtain the following initial value problem for $z(x,t)$:
\begin{eqnarray*}
z'' &=& \frac{\partial f}{\partial y} (x,y,y') z + \frac{\partial f}{\partial y'} (x,y,y') z'
,\,\,a \leq x \leq b, \\
 z(a, t) &=& 0,\ z'(a, t) = 1.
\end{eqnarray*}

To use Newton's method, the (coupled) IVPs for $y$ and $z$ must be solved simultaneously.
The iterative method then becomes
\[t_{n+1} = t_n - \frac{ y(b,t_n) - \beta}{z(b,t_n)}, \,\, n = 0,1,\hdots\]

\begin{problem}
Use Newton's method to solve the BVP
\begin{equation*}
\begin{split}
y'' &= 3 + \frac{2y}{x^2}, \,\, x \in [1,e],\\
y(1) &= 6, \\
y(e) &= e^2 + 6/e.
\end{split}
\end{equation*}
Plot your solution.
(Compare with Figure \ref{prob:shooting2}.)
What is an appropriate initial guess?

Hint: Update the ode() function from the previous problem to solve for $y$, $y'$, $z$, $z'$ simultaneously.
This can be done by first rewriting the equations for $y"$ and $z"$ as a system of first order differential equations.

\begin{figure}[H]
\includegraphics[width=\textwidth]{Fig2.pdf}
\caption{The solution of  $y'' = 3 + 2y/x^2,$ satisfying the boundary conditions $y(1) = 6$, $ y(e) =  e^2 + 6/e$.}
\label{prob:shooting2}
\end{figure}
\end{problem}

\section*{The Cannon Problem}

Consider the problem of aiming a projectile at a given target.
Here we will construct a differential equation that describes the path of the projectile and takes into account air resistance.
We will then use the shooting method to determine the angle at which the projectile should be launched.

Let the coordinates of the projectile be given by $\vec{r}(t) = \langle x(t), y(t) \rangle$.
If $\theta(t)$ represents the angle of the velocity vector from the positive $x$-axis and $v(t)$ represents the speed of the projectile ($ |\vec{v}(t) |$), then we have
\begin{align*}
\dot{x} &= v\cos{\theta},\\
\dot{y} &= v\sin{\theta}.
%x' &= v\cos{\theta},\\
%y' &= v\sin{\theta}.
\end{align*} Note that each of $x,y,\theta$, and $v$ are functions of $t$, so the dot %prime
denotes $\dfrac{d}{dt}$.
The tangent vector to the path traced by the projectile is the unit vector in the direction of the projectile's velocity, so $\vec{T}(t) = \langle \cos{\theta}, \sin{\theta} \rangle$.
The unit normal vector $\vec{N} (t)$ is given by $\vec{N} (t)= \langle -\sin{\theta}, \cos{\theta} \rangle$.
Thus the relationship between basis vectors $\vec{i}, \vec{j}$, and $\vec{T(t)}, \vec{N}(t)$ is given by
\[\left[\begin{array}{cc}\cos{\theta} & \sin{\theta} \\-\sin{\theta} & \cos{\theta}\end{array}\right] \left[\begin{array}{c}\vec{i} \\\vec{j}\end{array}\right] = \left[\begin{array}{c}\vec{T(t)} \\\vec{N(t)}\end{array}\right]\]
Let $F_g$ represent the force on the projectile due to gravity, and $F_d$ represent the force on the projectile due to air resistance. (We assume the air is still.)
From Newton's law we have
\begin{align*}
m \dot{\vec{v}} &= F_g + F_d.
%m \vec{v}\ ' &= F_g + F_d.
\end{align*}

The drag equation from fluid dynamics says that the force on the projectile due to air resistance is $k v^2 = (1/2)\rho c_D A v^2$, where $\rho$ is the mass density of air (about $1.225$ $\text{kg}/\text{m}^3$), $v$ is the speed of the projectile, and $A$ is its cross-sectional area.
The drag coefficient $c_D$ is a dimensionless quantity that changes with respect to the shape of the object.
(If we assume our projectile is spherical with a diameter of $.2$ m, then its drag coefficient $c_D \approx 0.47$, its cross-sectional area is $\pi/100$ $ \text{m}^2$, and we obtain $k \approx 0.009$.)

Thus the total force on the shell is
\begin{align}
m \dot{\vec{v}} &= -mg \vec{j} - kv^2 \vec{T},\nonumber \\
%m \vec{v}\ ' &= -mg \vec{j} - kv^2 \vec{T},\nonumber \\
&= -mg( \sin{\theta} \vec{T} + \cos{\theta} \vec{N} ) - kv^2 \vec{T},\nonumber\\
&= (-mg \sin{\theta} - k v^2 ) \vec{T} - mg \cos{\theta} \vec{N}.\label{eqn:TForce1}
\end{align}
From the identity
$\vec{v} = \langle \dot{x}, \dot{y} \rangle = \langle v \cos{\theta}, v \sin{\theta} \rangle$
%$\vec{v} = \langle x', y' \rangle = \langle v \cos{\theta}, v \sin{\theta} \rangle$
we have
\begin{align}
m \dot{\vec{v}} = {} & m\langle \dot{v} \cos{\theta} - v\sin{\theta} \cdot \dot{\theta} ,\dot{v}\sin{\theta} + v\cos{\theta} \cdot \dot{\theta} \rangle \nonumber \\
= {} & m(\dot{v}\cos{\theta} - v\sin{\theta} \cdot \dot{\theta})(\cos{\theta} \vec{T} - \sin{\theta}\vec{N}) \nonumber \\
& + m(\dot{v} \sin{\theta} + v\cos{\theta} \cdot \dot{\theta})( \sin{\theta} \vec{T} + \cos{\theta} \vec{N}) ,  \nonumber \\
= {} & m(\vec{T} \cdot \dot{v} + \vec{N} \cdot v \cdot \dot{\theta}) .\label{eqn:TForce2}
%
%m \vec{v}' = {} & m\langle v' \cos{\theta} - v\sin{\theta} \cdot \theta' ,v'\sin{\theta} + v\cos{\theta} \cdot \theta' \rangle \nonumber \\
%= {} & m(v'\cos{\theta} - v\sin{\theta} \cdot \theta')(\cos{\theta} \vec{T} - \sin{\theta}\vec{N}) \nonumber \\
%& + m(v' \sin{\theta} + v\cos{\theta} \cdot \theta')( \sin{\theta} \vec{T} + \cos{\theta} \vec{N}) ,  \nonumber \\
%= {} & m(\vec{T} \cdot v' + \vec{N} \cdot v \cdot \theta') .\label{eqn:TForce2}
\end{align}
From equations \eqref{eqn:TForce1} and \eqref{eqn:TForce2} we have
\begin{align*}
%m v' &= -mg\sin{\theta} - k v^2,\\
m \dot{v} &= -mg\sin{\theta} - k v^2,\\
mv\dot{\theta} &= -mg \cos{\theta}.
%mv\theta' &= -mg \cos{\theta}.
\end{align*}
Thus we have the coupled system of differential equations
\begin{align}
\dot{x} &= v\cos{\theta}, \nonumber \\
\dot{y} &= v\sin{\theta},\nonumber \\
\dot{v} &= -g\sin{\theta} -  k v^2/m,\nonumber \\
\dot{\theta} &= -g \cos{\theta}/v. \nonumber
%x' &= v\cos{\theta}, \nonumber \\
%y' &= v\sin{\theta},\nonumber \\
%v' &= -g\sin{\theta} -  k v^2/m,\nonumber \\
%\theta' &= -g \cos{\theta}/v. \nonumber
\end{align}

The independent variable $t$ used above is unessential to our problem.
If we assume that $t$ is an smooth invertible function of $x$ ($t = t(x)$), then we obtain
\begin{align*}
\frac{dy}{dx} &= \frac{dy}{dt}\frac{dt}{dx} ,\\
&= \frac{dy}{dt} \frac{1}{v\cos{\theta}}, \\
&= \frac{v \sin{\theta}}{v\cos{\theta}} = \tan{\theta}.
\end{align*}
We find $\frac{dv}{dx}$ and $\frac{d\theta}{dx}$ in a similar manner.
Thus our system of differential equations becomes
\begin{align}
	\begin{split}
\frac{dy}{dx} &= \tan {\theta} ,\\
\frac{dv}{dx} &= -\frac{g \sin{\theta} + \mu v^2}{v \cos{\theta}},\\
\frac{d\theta}{dx} &= -\frac{g}{v^2}, \label{eqn:cannon_DEs}
	\end{split}
\end{align}
where $\mu = k/m.$
In the next problem we will assume that the projectile has a mass of about $60$ kg, so that $\mu \approx .0003$.

\begin{problem}
Suppose a projectile is fired from a cannon with velocity $45\text{ m/s}^2$.
At what angle $\theta(0)$ should it be fired to land at a distance of $195\text{ m}$?

There should be two initial angles $\theta(0)$ that produce a solution for this bvp.
Use the secant method to numerically compute and then plot both trajectories.
\begin{align}
	\label{eqn:cannon_shooting}
	\begin{split}
\frac{dy}{dx} &= \tan {\theta} ,\\
\frac{dv}{dx} &= -\frac{g \sin{\theta} + \mu v^2}{v \cos{\theta}},\\
\frac{d\theta}{dx} &= -\frac{g}{v^2},\\
y(0)&= y(195) = 0,\\
v(0) &= 45 \text{ m/s}^2
	\end{split}
\end{align}
($g = 9.8067\text{ m/s}^2$.)
Find both solutions for this boundary value problem when $\mu = .0003$.
Compare with the solutions when $\mu = 0.$
Their graphs are given in Figure \ref{fig:shooting_cannon_comparison2}.

Hint: This is a system of three first order differential equations, and so our secant method requires a slight modification.
Keeping in mind that the unknown initial condition is $\theta(0)$, not $y'(0)$, define an appropriate function $h(t)$.
\end{problem}

\begin{figure}
\includegraphics[width=\textwidth]{Cannon_with_AirResistance.pdf}
\caption{Two solutions of the system of equations \eqref{eqn:cannon_DEs}, both with initial conditions  $y(0) = 0 \text{ m}$, $ v(0) = 45 \text{ m/s}$, and $\theta(0)=\pi/3$.
The black curve is the trajectory of a projectile immune to air resistance ($\mu = 0$).
The red curve describes the trajectory of a more realistic projectile ($\mu = .0003$).}
\label{fig:shooting_cannon_comparison1}
\end{figure}

\begin{figure}
\includegraphics[width=\textwidth]{Cannon_Shooting.pdf}
\caption{Two solutions of the boundary value problem \eqref{eqn:cannon_shooting} when the air resistance is described by the parameter $\mu = .0003$.
Also both solutions when air resistance is not described in the model ($\mu = 0$).}
\label{fig:shooting_cannon_comparison2}
\end{figure} 