\lab{Random Forests}{Random Forests}
\objective{Understand how to build a random forest and use it to predict survival of Titanic passengers.}

A \emph{random forest} is just what it sounds like--a collection of trees. Each tree is trained randomly, meaning that at each node, only a small, random subset of the attributes is available by which to determine the next split. Each trained tree in the forest casts a vote for the labeling of a new sample, and the sample is labeled according to the majority vote of the trees.

Your approach to the classification tree may have been sloppy, depending on how careful you were about odd cases (say trying to split a data set on gender when each sample is male). It doesn't affect us much when all the attributes are available on which to split, unless we grow the tree too deeply. However, with the random forests these odd cases crop up more frequently, as we only have a small subset of attributes to choose from. We need to be more careful then, and keep track of which attributes are still available to split on and only consider these.

\begin{problem}
Modify your code for classification trees so that we keep track of which attributes are available to split on at each node. We can only split on an attribute if it assumes two or more distinct values present in the data set. For example, in the Titanic data set, once we have split on gender, we can never split on it again in any descendant node, since one child data set will only have males and the other will only have females.
\end{problem}

We must next add the randomness to our trees.

\begin{problem}
Modify your code for classification trees so that each tree is trained \emph{randomly}, i.e. when determining the optimal split, randomly select a small subset of the available variables, and use them to split on. You should be able to specify the size of the subset. If the number of available variables is smaller than the size of the random subset, then terminate the node (make it a leaf node).
\end{problem}

We can now train the whole forest.

\begin{problem}
Make a class \emph{Forest} which trains a collection of random trees.  Use the following implementation:

\begin{lstlisting}
class Forest(data, targets, Gini, max_depth, num_trees, num_vars):
    """
    Train a collection of random trees.

    Parameters
    ----------
    data : ndarray of shape (n,k)
        Each row is an observation.
    targets : ndarray of shape (K,)
        The possible labels or classes.
    Gini : float
        The Gini impurity tolerance
    max_depth : int
        The maximum depth for the the trees
    num_trees : int
        The number of trees in the forest.
    num_vars : int
        The number of variables randomly selected at each node.
    """
    pass
\end{lstlisting}

Note that \li{num_vars} should be small, i.e. \li{num_vars} $ \approx \sqrt{P}$ where $P$ is the total number of attributes in the data set. The number of trees in the forest should be somewhat large, say greater than $100$.
\end{problem}

\begin{problem}
Write a method that assigns a label to a new sample, by considering the majority vote of the trees.
\end{problem}

Let us reexamine the Titanic data set and see if we get any significant improvement.

\begin{problem}
Train a random forest on the Titanic data set, and for your inputs use \li{num_vars} $ = 2$ and $100$ trees. Let the Gini impurity tolerance be $0.1$ and the maximum depth be $10$. What is your misclassification rate? Was there any significant improvement?
\end{problem}
