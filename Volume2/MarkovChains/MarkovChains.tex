\lab{Markov Chains}{Markov Chains}
\label{lab:Markov}
\objective{
A Markov chain is a collection of states with specified probabilities for transitioning from one state to another.
They are characterized by the fact that the future behavior of the system depends only on its current state.
In this lab, we learn to construct, analyze, and interact with Markov chains, then apply a Markov chain to a natural language processing problem.}

\section*{State Space Models} % ===============================================

Many systems can be described by a finite number of states.
For example, a board game where players move around the board based on die rolls can be modeled by a Markov chain.
Each space represents a state, and a player is said to be in a state if their piece is currently on the corresponding space.
In this case, the probability of moving from one space to another only depends on the player's current location; where the player was on a previous turn does not affect their current turn.

Finite Markov chains have an associated \emph{transition matrix} that stores the information about the transitions between the states in the chain.
The $(i,j)$th entry of the matrix gives the probability of moving \textbf{from state $j$ to state $i$}.
Thus each of the columns of the transition matrix sum to $1$.

\begin{info} % Generate random row stochastic transitino matrices.
A transition matrix where the columns sum to 1 is called \emph{column stochastic} (or \emph{left stochastic}).
The rows of a \emph{row stochastic} (or \emph{right stochastic}) transition matrix each sum to 1 and the $(i,j)$th entry of the matrix is the probability of moving from state $i$ to state $j$.
Both representations are common, but in this lab we exclusively use column stochastic transition matrices for consistency.
\end{info}

Consider a very simple weather model where the probability of being hot or cold depends on the weather of the previous day.
If the probability that tomorrow is hot given that today is hot is 0.7, and the probability that tomorrow is cold given that today is cold is 0.4, then by assigning hot to the $0$th row and column, and cold to the $1^{st}$ row and column, this Markov chain has the following transition matrix.

\begin{align*}
\begin{blockarray}{ccc}
& \text{\textcolor{red}{hot today}} & \text{\textcolor{blue}{cold today}} \\
\begin{block}{c[cc]}
\text{\textcolor{red}{hot tomorrow}}   & 0.7 & 0.6 \\
\text{\textcolor{blue}{cold tomorrow}} & 0.3 & 0.4 \\
\end{block}\end{blockarray}
\end{align*}

The $0$th column of the matrix says that if it is hot today, there is a $70\%$ chance that tomorrow will be hot ($0$th row) and a $30\%$ chance that tomorrow will be cold ($1$st row).
The $1$st column says if it is cold today, then there is a $60\%$ chance of heat and a $40\%$ chance of cold tomorrow.

Markov chains can be represented by a \emph{state diagram}, a type of directed graph.
The nodes in the graph are the states, and the edges indicate the state transition probabilities.
The Markov chain described above has the following state diagram.

\begin{figure}[H] % 2-state chain.
\centering
\begin{tikzpicture}[normalcircle/.style={draw, circle, minimum size=1.5cm, thick, node distance=2.5cm}]
    % Place the circles
    \node[normalcircle] (Hot) {};
    \node[red] at (Hot) {Hot};

    \node[normalcircle, right=of Hot] (Cold) {};
    \node[blue] at (Cold) {Cold};

    % Draw loop, place number, draw line
    \draw[thick,->,>=stealth',red!50!black] (Hot)+(-.52,.52) arc (325:40:.35 and -.85);
    \node[left,red!50!black] at (Hot.west) [shift={+(-.5,0)}] {0.7};
    \draw[thick,->,>=stealth',red!50!black] (Hot.north east) -- node[above] {0.3} (Cold.north west);

    \draw[thick,->,>=stealth',blue!50!black] (Cold)+(.52,.52) arc (325:40:-.35 and -.85);
    \node[right,blue!50!black] at (Cold.east) [shift={+(.5,0)}] {0.4};
    \draw[thick,->,>=stealth',blue!50!black] (Cold.south west) -- node[below] {0.6} (Hot.south east);

\end{tikzpicture}
\end{figure}

%
\begin{problem} % Make a column stochastic matrix.
Transition matrices for Markov chains are efficiently stored as NumPy arrays.
Write a function that accepts an integer $n$ and returns the transition matrix for a random Markov chain with $n$ states.
\\ (Hint: use array broadcasting to avoid looping.)
\label{prob:random-markov-chain}
\end{problem}

\subsection*{Simulating State Transitions} % ----------------------------------

A single draw from a \emph{binomial distribution} with parameters $n$ and $p$ indicates the number of successes out of $n$ independent experiments, each with probability $p$ of success.
The classic example is a series of coin flips, where $p$ is the probability that the coin lands heads side up.
NumPy's \li{random} module has an efficient tool, \li{binomial()}, for drawing from a binomial distribution.

\begin{lstlisting}
>>> import numpy as np

# Draw from the binomial distribution with n = 1 and p = .5 (flip 1 coin).
>>> np.random.binomial(1, .5)
0                             # The coin flip resulted in tails.
\end{lstlisting}

Consider again the simple weather model and suppose that today is hot.
The column that corresponds to ``hot''in the transition matrix is $[0.7, 0.3]$.
To determine whether tomorrow is hot or cold, draw from the binomial distribution with $n = 1$ and $p = 0.3$.
If the draw is 1, which has $30\%$ likelihood, then tomorrow is cold.
If the draw is 0, which has $70\%$ likelihood, then tomorrow is hot.
The following function implements this idea.

\begin{lstlisting}
def forecast():
    """Forecast tomorrow's weather given that today is hot."""
    transition = np.array([[0.7, 0.6], [0.3, 0.4]])

    # Sample from a binomial distribution to choose a new state.
    return np.binomial(1, transition[1, 0])
\end{lstlisting}

\begin{problem} % 2-state chain with binomial transitioning.
Modify \li{forecast()} so that it accepts an integer parameter \li{days} and runs a simulation of the weather for the number of days given.
Return a list containing the day-by-day weather predictions (0 for hot, 1 for cold).
Assume the first day is hot, but do not include the data from the first day in the list of predictions.
The resulting list should therefore have \li{days} entries.
\label{prob:small-markov-transitions}
\end{problem}

\subsection*{Larger Chains} % -------------------------------------------------

The \li{forecast()} function makes one random draw from a binomial distribution to simulate a state change.
Larger Markov chains require draws from a \emph{multinomial distribution}, a multivariate generalization of the binomial distribution.
A draw from a multinomial distribution parameters $n$ and $(p_1,\ p_2,\ \ldots,\ p_k)$ indicates which of $k$ outcomes occurs in $n$ different experiments.
In this case the classic example is a series of dice rolls, with $6$ possible outcomes of equal probability.

\begin{lstlisting}
>>> die_probabilities = np.array([1./6, 1./6, 1./6, 1./6, 1./6, 1./6])

# Draw from the multinomial distribution with n = 1 (roll a single die).
>>> np.random.multinomial(1, die_probabilities)
array([0, 0, 0, 1, 0, 0])     # The roll resulted in a 4.
\end{lstlisting}

\begin{problem} % 4-state chain with multinomial transitioning.
Let the following matrix be the transition matrix for a Markov chain modeling weather with four states: hot, mild, cold, and freezing.

\begin{align*}
\begin{blockarray}{ccccc}
& \text{\textcolor{red}{hot}} & \text{\textcolor[rgb]{0,.6,0}{mild}} & \text{\textcolor{blue}{cold}} & \text{\textcolor{cyan}{freezing}} \\
\begin{block}{c[cccc]}
\text{\textcolor{red}{hot}}              & 0.5 & 0.3 & 0.1 & 0   \\
\text{\textcolor[rgb]{0,.6,0}{mild}}     & 0.3 & 0.3 & 0.3 & 0.3 \\
\text{\textcolor{blue}{cold}}            & 0.2 & 0.3 & 0.4 & 0.5 \\
\text{\textcolor{cyan}{freezing}}        &   0 & 0.1 & 0.2 & 0.2 \\
\end{block}\end{blockarray}
\end{align*}

Write a new function that accepts an integer parameter and runs the same kind of simulation as \li{forecast()}, but that uses this new four-state transition matrix.
This time, assume that the first day is mild.
Return a list containing the day-to-day results (0 for hot, 1 for mild, 2 for cold, and 3 for freezing).
\label{prob:markov-larger-chain}
\end{problem}

% TODO: Turn this into a Note down below?
% \begin{info}
% A single experiment with probability $p$ of success is called a \emph{Bernoulli trial}.
% In general, the binomial distribution is the sum of $n$ repeated Bernoulli trials.
% Like the Bernoulli is a special case of the binomial, the \emph{categorical distribution} is a special case of the \emph{multinomial distribution}, when n = 1.
% NumPy only has direct implementations for the binomial and multinomial distributions, since the Bernoulli and categorical distributions are just special cases of these.
% \end{info}


\section*{General State Distributions} % ======================================

\begin{comment} % The 1-Norm. Might be able to get away without this.
For an $n\times 1$ vector $\x$ with entries $x_i$ and an $n\times n$ matrix $A$ with entries $a_{ij}$, the \emph{1-norm} is defined as follows.
\begin{align*}
\|\x\|_1 = \sum_{i=1}^n|x_i| && \|A\|_1 = \sup_j \sum_{i=1}^n |a_{ij}|
\end{align*}
In other words, the $1$-norm for both vectors and matrices is the maximum absolute column sum.
Then if $A$ is a transition matrix, $\|A\|_1 = 1$, since each of the entries of the matrix are positive and each of the columns sum to $1$ by definition.
The power method with the 1-norm can be used to find the unique stable steady state distribution of $A$.
\end{comment}

For a Markov chain with $n$ states, the probability of being in each of the states can be encoded by a single $n \times 1$ vector $\x$, called a \emph{state distribution vector}.
The entries of $\x$ must be nonnegative and sum to 1.
Then the $i$th entry $x_i$ of $\x$ is the probability of being in state $i$.
For example, the state distribution vector $\x = [0.8,\ 0.2]\trp$ corresponding to the 2-state weather model of Problem \ref{prob:small-markov-transitions} indicates that there is a $80\%$ chance that today is hot and a $20\%$ chance that today is cold.
On the other hand, the vector $\x = [0, 1]\trp$ implies that today is, with $100\%$ certainty, cold.

If $A$ is an $n\times n$ transition matrix for a Markov chain and $\x$ is a state distribution vector, then $A\x$ is also a state distribution vector.
% To verify this fact, let $a_{ij}$ be the entries of $A$ and $x_i$ the entries of $\x$.
% The columns of $A$ sum to $1$, so $\sum_{j=1}^n a_{ij} = 1$ for $i = 1,\ 2,\ \ldots,\ n$.
% In addition, $\sum_{j=1}^n x_j = 1$ since the entries of $\x$ also sum to $1$.
% From matrix multiplication, the $i$th entry of $A\x$ is given by $\sum_{j=1}^n a_{ij}x_j$, so the sum of the entries of $A\x$ is
% \[\sum_{i=1}^n\sum_{j=1}^n a_{ij}x_j
% = \sum_{j=1}^n\left(x_j\left(\sum_{j=1}^n a_{ij}\right)\right)
% = \sum_{j=1}^n x_j = 1.\]
In fact, if $\x_k$ is the state distribution vector corresponding to a certain time $k$, then $\x_{k+1} = A\x_k$ contains the probabilities of being in each state after allowing the system to transition again.
For the weather model, this means that if there is an $80\%$ chance that it will be hot 5 days from now, written $\x_{5} = [0.8,\ 0.2]\trp$, then since
\[
\x_{6} = A\x_{5} =
\left[\begin{array}{cc}
0.7 & 0.6 \\
0.3 & 0.4 \\
\end{array}\right]
\left[\begin{array}{c}0.8 \\ 0.2\end{array}\right]
=
\left[\begin{array}{c}0.68 \\ 0.32\end{array}\right],
\]
there is a $68\%$ chance that 6 days from now will be a hot day.

\subsection*{Convergent Transition Matrices} % --------------------------------

Given an initial state distribution vector $\x_{0}$, defining $\x_{k+1} = A\x_k$ yields the following significant relation.
\[\x_k = A\x_{k-1} = A(A\x_{k-2}) = A(A(A\x_{x-3})) = \cdots = A^k\x_{0}\]

This indicates that the $(i,j)$th entry of $A^k$ is the probability of transition from state $j$ to state $i$ in $k$ steps.
For the transition matrix of the 2-state weather model, something curious happens to $A^k$ for even small values of $k$.
\[
A = \left[\begin{array}{cc}
0.7 & 0.6 \\
0.3 & 0.4 \\
\end{array}\right]
\quad
A^2 = \left[\begin{array}{cc}
0.67 & 0.66 \\
0.33 & 0.34 \\
\end{array}\right]
\quad
A^3 = \left[\begin{array}{cc}
0.667 & 0.666 \\
0.333 & 0.334 \\
\end{array}\right]
\]
As $k\rightarrow\infty$, the entries of $A^k$ converge, written as follows.
\begin{equation}
\lim_{k \rightarrow \infty} A^k = \left[\begin{array}{ccc}
2/3 & 2/3 \\
1/3 & 1/3 \\
\end{array}\right].
\label{eq:markov-steady-transition}
\end{equation}
In addition, for any initial state distribution vector $\x_{0} = [a,\ b]\trp$, $a + b = 1$,
\[
\lim_{k \rightarrow \infty} \x_k = \lim_{k \rightarrow \infty}A^k\x_{0}
=
\left[\begin{array}{ccc}
2/3 & 2/3 \\
1/3 & 1/3 \\
\end{array}\right]
\left[\begin{array}{c}a\\b\end{array}\right]
=
\left[\begin{array}{c}2(a+b)/3\\(a+b)/3\end{array}\right]
=
\left[\begin{array}{c}2/3\\1/3\end{array}\right].
\]

Thus as $k\rightarrow\infty$, $\x_k \rightarrow \x = [2/3,\ 1/3]\trp$, regardless of the initial state distribution $\x_{0}$.
So according to this model, no matter the weather today, the probability that it is hot a week from now is approximately $66.67\%$.
In fact, approximately 2 out of 3 days in the year should be hot.

\subsection*{Steady State Distributions} % ------------------------------------

The state distribution $\x = [2/3,\ 1/3]\trp$ has another important property.
\[
A\x =
\left[\begin{array}{cc}
7/10 & 3/5 \\
3/10 & 2/5 \\
\end{array}\right]
\left[\begin{array}{c}2/3 \\ 1/3\end{array}\right]
=
\left[\begin{array}{c}14/30 + 3/15 \\ 6/30 + 2/15\end{array}\right]
=
\left[\begin{array}{c}2/3 \\ 1/3\end{array}\right]
= \x.
\]
Any $\x$ satisfying $A\x = \x$ is called a \emph{steady state distribution} or a \emph{stable fixed point} of $A$.
In other words, a steady state distribution is an eigenvector of $A$ with corresponding eigenvalue $\lambda = 1$.

% TODO: Verify this paragraph.
Every Markov chain has at least one steady state distribution.
If some power $A^k$ of $A$ has all positive (nonzero) entries, then the steady state distribution is unique.%
\footnote{This is a consequence of the \emph{Perron-Frobenius theorem}, which is presented in conjunction with spectral calculus in Volume I.}
In this case, $\lim_{k\rightarrow\infty}A^k$ is the matrix whose columns are all equal to the unique steady state distribution, as in (\ref{eq:markov-steady-transition}).
Under these circumstances, the steady state distribution $\x$ can be found by iteratively calculating $\x_{k+1} = A\x_k$, as long as the initial vector $\x_{0}$ is a state distribution vector.

\begin{warn}
Though every Markov chain has at least one steady state distribution, the procedure described above fails if $A^k$ fails to converge.
Consider the following example.
\[
A = \left[\begin{array}{ccc}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{array}\right]
,\quad A^k = \begin{cases}
A\quad\text{if } k\ \text{is odd}
\\
I\quad\text{if } k\ \text{is even}
\end{cases}
\]
In this case as $k\rightarrow\infty$, $A^k$ oscillates between two different matrices.

Furthermore, the steady state distribution is not always unique; the transition matrix defined above, for example, has infinitely many.
\end{warn}

\begin{problem} % Use the power method (simple) to get the steady state.
Write a function that accepts an $n\times n$ transition matrix $A$, a convergence tolerance $\epsilon$, and a maximum number of iterations $N$.
Generate a random state distribution vector $\x_{0}$ and calculate $\x_{k+1} = A\x_k$ until $\|\x_{k-1} - \x_k\| < \epsilon$.
If $k$ exceeds $N$, raise a \li{ValueError} to indicate that $A^k$ does not converge.
Return the approximate steady state distribution $\x$ of $A$.

To test your function, use Problem \ref{prob:random-markov-chain} to generate a random transition matrix $A$.
Verify that $A\x = \x$ and that the columns of $A^k$ approach $\x$ as $k\rightarrow\infty$.
To compute $A^k$, use NumPy's (very efficient) algorithm for computing matrix powers. % (which is not part of \li{scipy.linalg}).

\begin{lstlisting}
>>> A = np.array([[.7, .6],[.3, .4]])
>>> np.linalg.matrix_power(A, 10)       # Compute A^10.
array([[ 0.66666667,  0.66666667],
       [ 0.33333333,  0.33333333]])
\end{lstlisting}

Finally, use your function to validate the results of Problems \ref{prob:small-markov-transitions} and \ref{prob:markov-larger-chain}:
\begin{enumerate}
    \item Calculate the steady state distributions corresponding to the transition matrices for each simulation.
    \item Run each simulation for a large number of days and verify that the results match the steady state distribution (for example, check that approximately 2/3 of the days are hot for the smaller weather model).
\end{enumerate}

\label{prob:markov-power-method}
\end{problem}

\begin{info}
Problem \ref{prob:markov-power-method} is a special case of the \emph{power method}, an algorithm for calculating an eigenvector of a matrix corresponding to the eigenvalue of largest magnitude.
The general version of the power method, together with a discussion of its convergence conditions, is discussed in another lab.
\end{info}

\section*{Using Markov Chains to Simulate English} % ==========================
% TODO: is it okay to make this reference?
One of the original applications of Markov chains was to study natural languages.
% \footnote{The term \emph{natural language} refers to a spoken language, like English or Russian. See \url{http://langvillea.people.cofc.edu/MCapps7.pdf} for some details on the early applications of Markov chains, including the study of natural languages.}
In the early $20$th century, Markov used his chains to model how Russian switched from vowels to consonants.
By mid-century, they had been used as an attempt to model English.
It turns out that Markov chains are, by themselves, insufficient to model very good English.
However, they can approach a fairly good model of bad English, with sometimes amusing results.

By nature, a Markov chain is only concerned with its current state.
Thus a Markov chain simulating transitions between English words is completely unaware of context or even of previous words in a sentence.
For example, a Markov chain's current state may be the word ``continuous.''
Then the chain would say that the next word in the sentence is more likely to be ``function'' rather than ``raccoon.''
However, without the context of the rest of the sentence, even two likely words stringed together may result in gibberish.

We restrict ourselves to a subproblem of modeling the English of a specific file.
The transition probabilities of the resulting Markov chain reflect the sort of English that the source authors speak.
Thus the Markov chain built from \emph{The Complete Works of William Shakespeare} differs greatly from, say, the Markov chain built from a collection of academic journals.
We call the source collection of works in the next problems the \emph{training set}.

\subsection*{Making the Chain} % ----------------------------------------------

With the weather models of the previous sections, we chose a fixed number of days to simulate.
However, English sentences are of varying length, so we do not know beforehand how many words to choose (how many state transitions to make) before ending the sentence.
To capture this feature, we include two extra states in our Markov model: a \emph{start state} (\textcolor[rgb]{0,.6,0}{\$tart}) marking the beginning of a sentence, and a \emph{stop state} (\textcolor{red}{\$top}) marking the end.
Thus a training set with $N$ unique words has an $(N+2)\times (N+2)$ transition matrix.

The start state only transitions to words that appear at the beginning of a sentence in the training set, and only words that appear at the end a sentence in the training set transition to the stop state.
The stop state is called an \emph{absorbing state} because once we reach it, we cannot transition back to another state.
% Because every state has a possible path to the stop state, this model is called an \emph{absorbing Markov chain}.

After determining the states in the Markov chain, we need to determine the transition probabilities between the states and build the corresponding transition matrix.
Consider the following small training set from Dr. Seuss as an example.

\begin{lstlisting}
<<I am Sam Sam I am.
Do you like green eggs and ham?
I do not like them, Sam I am.
I do not like green eggs and ham.>>
\end{lstlisting}

If we include punctuation (so ``ham?'' and ``ham.'' are counted as distinct words) and do not alter the capitalization (so ``Do'' and ``do'' are also different), there are 15 unique words in this training set:
%
\begin{align*}
\text{I\quad am\quad Sam\quad am.\quad Do\quad you\quad like\quad green}
\\
\text{eggs\quad and\quad ham?\quad do\quad not\quad them,\quad ham.}
\end{align*}

With start and stop states, the transition matrix should be $17 \times 17$.
Each state must be assigned a row and column index in the transition matrix.
As easy way to do this is to assign the states an index based on the order that they appear in the training set.
Thus our states and the corresponding indices will be as follows:
%
\begin{align*}
\begin{array}{ccccccc}
\text{\textcolor[rgb]{0,.6,0}{\$tart}} & \text{I} & \text{am} & \text{Sam} & \ldots & \text{ham.} & \text{\textcolor{red}{\$top}}
\\
0 & 1 & 2 & 3 & \ldots & 15 & 16
\end{array}
\end{align*}

The start state should transition to the words ``I'' and ``Do'', and the words ``am.'', ``ham?'', and ``ham.'' should each transition to the stop state.
We first count the number of times that each state transitions to another state:

\begin{align*}
\begin{blockarray}{cccccccc}
& \text{\textcolor[rgb]{.3,.6,.1}{\$tart}} & \text{I} & \text{am} & \text{Sam} & & \text{ham.} & \text{\textcolor[rgb]{1,0,0}{\$top}} \\
\begin{block}{c[ccccccc]}
\text{\textcolor[rgb]{.3,.6,.1}{\$tart}}    & 0 & 0 & 0 & 0 & \ldots & 0 & 0\\
\text{I}        & 3 & 0 & 0 & 2 & \ldots & 0 & 0\\
\text{am}       & 0 & 1 & 0 & 0 & \ldots & 0 & 0\\
\text{Sam}      & 0 & 0 & 1 & 1 & \ldots & 0 & 0\\
& \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots\\
\text{ham.}     & 0 & 0 & 0 & 0 & \ldots & 0 & 0\\
\text{\textcolor[rgb]{1,0,0}{\$top}}        & 0 & 0 & 0 & 0 & \ldots & 1 & 1\\
\end{block}\end{blockarray}
\end{align*}

Now divide each column by its sum so that each column sums to 1.

\begin{align*}
\begin{blockarray}{cccccccc}
& \text{\textcolor[rgb]{.3,.6,.1}{\$tart}} & \text{I} & \text{am} & \text{Sam} & & \text{ham.} & \text{\textcolor[rgb]{1,0,0}{\$top}} \\
\begin{block}{c[ccccccc]}
\text{\textcolor[rgb]{.3,.6,.1}{\$tart}} & 0 & 0 & 0 & 0 & \ldots & 0 & 0\\
\text{I}        & 3/4 & 0 & 0 & 2/3 & \ldots & 0 & 0\\
\text{am}       & 0 & 1/5 & 0 & 0 & \ldots & 0 & 0\\
\text{Sam}      & 0 & 0 & 1 & 1/3 & \ldots & 0 & 0\\
& \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots\\
\text{ham.}     & 0 & 0 & 0 & 0 & \ldots & 0 & 0\\
\text{\textcolor[rgb]{1,0,0}{\$top}}    & 0 & 0 & 0 & 0 & \ldots & 1 & 1\\
\end{block}\end{blockarray}
\end{align*}

The $3/4$ indicates that 3 out of 4 times, the sentences in the training set start with the word ``I''.
Similarly, the $2/3$ and $1/3$ tell us that ``Sam'' is followed by ``I'' twice and by ``Sam'' once in the training set.
Note that ``am'' (without a period) always transitions to ``Sam'' and that ``ham.'' (with a period) always transitions the stop state.
Finally, to avoid a column of zeros, we place a 1 in the bottom right hand corner of the matrix (so the stop state always transitions to itself).

The entire procedure of creating the transition matrix for the Markov chain with words from a file as states is summarized below.

\begin{algorithm} % Read a file and convert it into a Markov chain.
\begin{algorithmic}[1]
\Procedure{MakeTransitionMatrix}{}
\State Count the number of unique words in the training set.
\State Initialize a square array of zeros of the appropriate size to be the transition \par\quad matrix (remember to account for the start and stop states).
\State Initialize a list of states, beginning with \li{"\$tart"}.
\For {each sentence in the training set}
    \State Split the sentence into a list of words.
    \State Add each \textbf{new} word in the sentence to the list of states.
    \State Convert the list of words into a list of indices indicating which row and \par\qquad\enspace column of the transition matrix each word corresponds to.
    \State Add 1 to the entry of the transition matrix corresponding to
    \par\qquad\enspace transitioning from the start state to the first word of the sentence.
    \For {each consecutive pair $(x, y)$ of words in the list of words}
        \State Add 1 to the entry of the transition matrix corresponding to \par\qquad\qquad transitioning from state $x$ to state $y$.
    \EndFor
    \State Add 1 to the entry of the transition matrix corresponding to
    \par\qquad\enspace transitioning from the last word of the sentence to the stop state.
\EndFor
\State Make sure the stop state transitions to itself.
\State Normalize each column by dividing by the column sums.
\EndProcedure
\end{algorithmic}
\caption{Convert a training set of sentences into a Markov chain.}
\label{alg:MarkovSentencesTransitionMatrix}
\end{algorithm}

\begin{problem} % Class that makes a Markov chain from a file.
Write a class called \li{SentenceGenerator}.
The constructor should accept a filename (the training set).
Read the file and build a transition matrix from its contents as described in Algorithm \ref{alg:MarkovSentencesTransitionMatrix}.

You may assume that the file has one complete sentence written on each line, and your implementation may be either column- or row-stochastic.
\label{problem:markov-random-sentences-init}
\end{problem}

\begin{problem} % Create random sentences.
Add a method to the \li{SentenceGenerator} class called \li{babble()}.
Begin at the start state and use the strategy from Problem \ref{prob:markov-larger-chain} to repeatedly transition through the object's Markov chain.
Keep track of the path through the chain and the corresponding sequence of words.
When the stop state is reached, stop transitioning to terminate the simulation.
Return the resulting sentence as a single string.

For example, your \li{SentenceGenerator} class should be able to create random sentences that sound somewhat like Yoda speaking.

\begin{lstlisting}
>>> yoda = SentenceGenerator("yoda.txt")
>>> for _ in range(3):
... 	print(yoda.babble())
...
<<Impossible to my size, do not!
For eight hundred years old to enter the dark side of Congress there is.
But beware of the Wookiees, I have.>>
\end{lstlisting}

\label{prob:markov-random-sentences-babble}
\end{problem}

\newpage

\section*{Additional Material} % ==============================================

\subsection*{Large Training Sets} % -------------------------------------------

The approach in Problems \ref{problem:markov-random-sentences-init} and \ref{prob:markov-random-sentences-babble} begins to fail as the training set grows larger.
For example, a single Shakespearean play may not be large enough to cause memory problems, but \emph{The Complete Works of William Shakespeare} certainly will.

To accommodate larger data sets, consider use a sparse matrix from \li{scipy.sparse} for the transition matrix instead of a regular NumPy array.
Specifically, construct the transition matrix as a \li{lil_matrix} (which is easy to build incrementally), then convert it to the \li{csc_matrix} format (which supports fast column operations).
Ensure that the process still works on small training sets, then proceed to larger training sets.
How are the resulting sentences different if a very large training set is used instead of a small training set?

\subsection*{Variations on the English Model} % -------------------------------

Choosing a different state space for the English Markov model produces different results.
Consider modifying your \li{SentenceGenerator} class so that it can determine the state space in a few different ways.
The following ideas are just a few possibilities.

\begin{itemize}
\item Let each punctuation mark have its own state.
In the example training set, instead of having two states for the words ``ham?'' and ``ham.'', there would be three states: ``ham'', ``?'', and ``.'', with ``ham'' transitioning to both punctuation states.

\item Model paragraphs instead of sentences.
Add a \textcolor[rgb]{0,.6,0}{\$tartParagraph} state that always transitions to \textcolor[rgb]{0,.6,0}{\$tartSentence} and a \textcolor{red}{\$topParagraph} state that is sometimes transitioned to from \textcolor{red}{\$topSentence}.

\item Let the states be individual letters instead of individual words.
Be sure to include a state for the spaces between words.
We will explore this particular state space choice more in Volume III together with hidden Markov models.

\item Construct the state space so that the next state depends on both the current and previous states.
This kind of Markov chain is called a \emph{Markov chain of order 2}.
This way, every set of three consecutive words in a randomly generated sentence should be part of the training set, as opposed to only every consecutive pair of words coming from the set.

\item Instead of generating random sentences from a single source, simulate a random conversation between $n$ people.
Construct a Markov chain $M_i,$ for each person, $i=1,\ \ldots,\ n$, then create a Markov chain $C$ describing the conversation transitions from person to person; in other words, the states of $C$ are the $M_i$.
To create the conversation, generate a random sentence from the first person using $M_1$.
Then use $C$ to determine the next speaker, generate a random sentence using their Markov chain, and so on.
\end{itemize}

\subsection*{Natural Language Processing Tools} % -----------------------------

The Markov model of Problems \ref{problem:markov-random-sentences-init} and \ref{prob:markov-random-sentences-babble} is a \emph{natural language processing} application.
Python's \li{nltk} module (natural language toolkit) has many tools for parsing and analyzing text for these kinds of problems.
For example, \li{nltk.sent_tokenize()} reads a single string and splits it up into sentences.

\begin{lstlisting}
>>> from nltk import sent_tokenize
>>> with open("yoda.txt", 'r') as yoda:
...     sentences = sent_tokenize(yoda.read())
...
>>> print(sentences)
<<['Away with your weapon!',
 'I mean you no harm.',
 'I am wondering - why are you here?',
 ...>>
\end{lstlisting}

The \li{nltk} module is \textbf{not} part of the Python standard library.
For instructions on downloading, installing, and using \li{nltk}, visit \url{http://www.nltk.org/}.
