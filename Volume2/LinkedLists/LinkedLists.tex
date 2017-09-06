\lab{Linked Lists}{Linked Lists}
\label{lab:Python_DataStructures}

\objective{Analyzing and manipulating data are essential skills in scientific computing.
Storing, retrieving, and rearranging data take time.
As a dataset grows, so does the amount of time it takes to access and analyze it.
To write effecient algorithms involving large data sets, it is therefore essential to be able to design or choose the data structures that are most optimal for a particular problem.
In this lab we begin our study of data structures by constructing a generic linked list, then using it to implement a few common data structures.}

\section*{Introduction} % =====================================================

\emph{Data structures} are specialized objects for organizing data efficiently.
There are many kinds, each with specific strengths and weaknesses, and different applications require different structures for optimal performance.
For example, some data structures take a long time to build, but once built their data are quickly accessible.
Others are built quickly, but are not as efficiently accessible.
These strengths and weaknesses are determined by how the structure is implemented.

Python has several built-in data structure classes, namely \li{list}, \li{set}, \li{dict}, and \li{tuple}.
Being able to use these structures is important, but selecting the correct data structure to begin with is often what makes or breaks a good program.
In this lab we create a structure that mimics the built-in list class, but that has a different underlying implementation.
Thus our class will be better than a plain Python list for some tasks, but worse for others.

\subsection*{Nodes} % ---------------------------------------------------------

Think of data as several types of objects that need to be stored in a warehouse.
A \emph{node} is like a standard size box that can hold all the different types of objects.
For example, suppose a particular warehouse stores lamps of various sizes.
Rather than trying to carefully stack lamps of different shapes on top of each other, it is preferable to first put them in boxes of standard size.
Then adding new boxes and retrieving stored ones becomes much easier.
A \emph{data structure} is like the warehouse, which specifies where and how the different boxes are stored.

A node class is usually simple.
The data in the node is stored as an attribute.
Other attributes may be added (or inherited) specific to a particular data structure.

\begin{problem} % Restricting data types of the Node class.
Consider the following generic node class.
\begin{lstlisting}
class Node:
    """A basic node class for storing data."""
    def __init__(self, data):
        """Store 'data' in the 'value' attribute."""
        self.value = data
\end{lstlisting}

Modify the constructor so that it only accepts data of type \li{int}, \li{float}, or \li{str}.
If another type of data is given, raise a \li{TypeError} with an appropriate error message.
Modify the constructor docstring to document these restrictions.
\end{problem}

\begin{info}
Often the data stored in a node is actually a \emph{key} value.
The key might be a memory address, a dictionary key, or the index of an array where the true desired information resides.
For simplicity, in this and the following lab we store actual data in node objects, not references to data located elsewhere.
\end{info}

\section*{Linked Lists} % =====================================================

A \emph{linked list} is a data structure that chains nodes together.
Every linked list needs a reference to the first node in the chain, called the \li{head}.
A reference to the last node in the chain, called the \li{tail}, is also often included.
Each node instance in the list stores a piece of data, plus at least one reference to another node in the list.

The nodes of a \emph{singly linked list} have a single reference to the next node in the list (see Figure \ref{fig:singly_linked}), while the nodes of a \emph{doubly linked list} have two references: one for the previous node, and one for the next node in the list (see Figure \ref{fig:doubly_linked}).
This allows for a doubly linked list to be traversed in both directions, whereas a singly linked list can only be traversed in one direction.

\begin{lstlisting}
class LinkedListNode(Node):
    """A node class for doubly linked lists. Inherits from the 'Node' class.
    Contains references to the next and previous nodes in the linked list.
    """
    def __init__(self, data):
        """Store 'data' in the 'value' attribute and initialize
        attributes for the next and previous nodes in the list.
        """
        Node.__init__(self, data)       # Use inheritance to set self.value.
        self.<<next>> = None
        self.prev = None
\end{lstlisting}

\begin{figure} % Singly linked list.
\centering
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto, node distance=1.5cm,thick,main node/.style={rectangle,draw}, minimum size=.5cm]
\tikzset{rect node/.style={rectangle, draw, minimum height = .5cm, minimum width=.2cm}}
    \node[main node] (1) {A};
    \node[main node] (2) [right of=1] {B};
    \node[main node] (3) [right of=2] {C};
    \node[main node] (4) [right of=3] {D};
    \node[draw = none, black!20!blue, node distance=1.5cm] [above left of=1](H) {Head};
\foreach \r in {1, 2, 3, 4}{
    \node[rect node][right of=\r, node distance = .36cm]{};}
\node[draw = none, node distance = 1.5cm] [right of=4]{};
\foreach \s/\t  in {1/2, 2/3, 3/4}{\path[draw](\s) edge[shorten <=.1cm](\t);}
    \draw[black!20!blue] (H) edge (1.north);
\end{tikzpicture}
\caption{A singly linked list. Each node has a reference to the next node in the list. The head attribute is always assigned to the first node.}
\label{fig:singly_linked}
\end{figure}

\begin{figure} % Doubly linked list.
\centering
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto, node distance=1.5cm, thick,main node/.style={rectangle,draw}, minimum size=.5cm]
\tikzset{rect node/.style={rectangle, draw, minimum height = .5cm, minimum width=.9cm}}
    \node[main node] (1) {A};
    \node[main node] (2) [right of=1] {B};
    \node[main node] (3) [right of=2] {C};
    \node[main node] (4) [right of=3] {D};
    \node[draw=none, node distance=.07cm] (1up) [above of=1] {};
    \node[draw=none, node distance=.07cm] (1dn) [below of=1] {};
    \node[draw=none, node distance=.07cm] (2up) [above of=2] {};
    \node[draw=none, node distance=.07cm] (2dn) [below of=2] {};
    \node[draw=none, node distance=.07cm] (3up) [above of=3] {};
    \node[draw=none, node distance=.07cm] (3dn) [below of=3] {};
    \node[draw=none, node distance=.07cm] (4up) [above of=4] {};
    \node[draw=none, node distance=.07cm] (4dn) [below of=4] {};
    \node[draw = none, black!20!blue, node distance = 1.5cm] [above right of=4] (T) {Tail};
    \node[draw = none, black!20!blue, node distance = 1.5cm] [above left of=1] (H) {Head};
    \node[rect node](1.5)[]{};
    \node[rect node](2.5)[right of=1.5]{};
    \node[rect node](3.5)[right of=2.5]{};
    \node[rect node](4.5)[right of=3.5]{};
\foreach \s/\t  in {1up/2up, 2dn/1dn, 2up/3up, 3dn/2dn, 3up/4up, 4dn/3dn}{
        \path[draw](\s) edge[shorten <=.1cm, shorten >=.1cm](\t);}
    \draw[black!20!blue] (H) edge (1.north);
    \draw[black!20!blue] (T) edge (4.north);
\end{tikzpicture}
\caption{A doubly linked list. Each node has a reference to the node before it and a reference to the node after it. In addition to the head attribute, this list has a tail attribute that is always assigned to the last node.}
\label{fig:doubly_linked}
\end{figure}

Now we create a new class, \li{LinkedList}, that will link \li{LinkedListNode} instances together by modifying each node's \li{<<next>>} and \li{prev} attributes.
The list is empty initially, so we assign the \li{head} and \li{tail} attributes the placeholder value \li{None}.

%\subsection*{append()}

We also need a method for adding data to the list.
The \li{append()} makes a new node and adds it to the very end of the list.
There are two cases to consider: appending to an empty list, and appending to a nonempty list.
See Figure \ref{fig:append}.

\begin{lstlisting}
class LinkedList:
    """Doubly linked list data structure class.

    Attributes:
        head (LinkedListNode): the first node in the list.
        tail (LinkedListNode): the last node in the list.
    """
    def __init__(self):
        """Initialize the 'head' and 'tail' attributes by setting
        them to 'None', since the list is empty initially.
        """
        self.head = None
        self.tail = None

    def append(self, data):
        """Append a new node containing 'data' to the end of the list."""
        # Create a new node to store the input data.
        new_node = LinkedListNode(data)
        if self.head is None:
            # If the list is empty, assign the head and tail attributes to
            # new_node, since it becomes the first and last node in the list.
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty, place new_node after the tail.
            self.tail.<<next>> = new_node               # tail --> new_node
            new_node.prev = self.tail               # tail <-- new_node
            # Now the last node in the list is new_node, so reassign the tail.
            self.tail = new_node
\end{lstlisting}

\begin{figure} % append().
\centering
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto, node distance=1.6cm,thick,main node/.style={rectangle,draw}, minimum size=.5cm]
\tikzset{rect node/.style={rectangle, draw, minimum height = .5cm, minimum width=.2cm}}
    \node[main node] (1) {A};
    \node[main node] (2) [right of=1] {B};
    \node[main node] (3) [right of=2] {C};
    \node[main node] (5) [right of=3, node distance=3.5cm] {A};
    \node[main node] (6) [right of=5] {B};
    \node[main node] (7) [right of=6] {C};
    \node[draw=none, node distance=.07cm] (1up) [above of=1] {};
    \node[draw=none, node distance=.07cm] (1dn) [below of=1] {};
    \node[draw=none, node distance=.07cm] (2up) [above of=2] {};
    \node[draw=none, node distance=.07cm] (2dn) [below of=2] {};
    \node[draw=none, node distance=.07cm] (3up) [above of=3] {};
    \node[draw=none, node distance=.07cm] (3dn) [below of=3] {};
    \node[draw=none, node distance=.07cm] (5up) [above of=5] {};
    \node[draw=none, node distance=.07cm] (5dn) [below of=5] {};
    \node[draw=none, node distance=.07cm] (6up) [above of=6] {};
    \node[draw=none, node distance=.07cm] (6dn) [below of=6] {};
    \node[draw=none, node distance=.07cm] (7up) [above of=7] {};
    \node[draw=none, node distance=.07cm] (7dn) [below of=7] {};
    \node[draw=none, black!20!blue, node distance=1.5cm] [above left of=1](H1) {Head};
    \node[draw = none, black!20!blue, node distance=1.5cm] [above right of=2](T1) {Tail};
    \node[draw=none, black!20!blue, node distance=1.5cm] [above left of=5](H2) {Head};
    \node[draw = none, black!20!blue, node distance=1.5cm] [above right of=7](T2) {Tail};
\foreach \r in {1, 2, 3, 5, 6, 7}{
        \node[rect node][right of=\r, node distance = .36cm]{};
        \node[rect node][left  of=\r, node distance = .36cm]{};}
\foreach \s/\t in {1up/2up, 2dn/1dn, 5up/6up, 6dn/5dn}{
        \path[draw](\s) edge[shorten <=.1cm, shorten >=.1cm](\t);}
\foreach \s/\t in {6up/7up, 7dn/6dn}{
        \path[draw](\s) edge[red, shorten <=.1cm, shorten >=.1cm](\t);}
    \draw[black!20!blue, shorten >=.1cm] (H1) edge (1.north);
    \draw[black!20!blue, shorten >=.1cm] (T1) edge (2.north);
    \draw[black!20!blue, shorten >=.1cm] (H2) edge (5.north);
    \draw[black!20!blue, shorten >=.1cm] (T2) edge (7.north);
\end{tikzpicture}
\caption{Appending a new node to the end of a nonempty doubly linked list. The red arrows are the new connections. Note that the \li{tail} attribute is adjusted.}
\label{fig:append}
\end{figure}

\begin{warn} % Warning about 'is' vs '=='.
The \li{is} comparison operator is \textbf{not} the same as the \li{==} comparison operator.
While \li{==} checks for numerical equality, \li{is} evaluates whether or not two objects are at the same location in memory.

\begin{lstlisting}
# This evaluates to True since the numerical values are the same.
>>> 7 == 7.0
True

# 7 is an int and 7.0 is a float, so they cannot be stored at the same
# location in memory. Therefore 7 'is not' 7.0.
>>> 7 is 7.0
False
\end{lstlisting}

For numerical comparisons, always use \li{==}.
When comparing to built-in Python constants such as \li{None}, \li{True}, \li{False}, or \li{NotImplemented}, use \li{is} instead.
\end{warn}

\subsection*{find()} % --------------------------------------------------------

The \li{LinkedList} class only explicitly keeps track of the first and last nodes in the list via the \li{head} and \li{tail} attributes.
To access any other node, we must use each successive node's \li{<<next>>} and \li{prev} attributes.

\begin{lstlisting}
>>> my_list = LinkedList()
>>> my_list.append(2)
>>> my_list.append(4)
>>> my_list.append(6)

# To access each value, we use the 'head' attribute of the LinkedList
# and the 'next' and 'value' attributes of each node in the list.
>>> my_list.head.value
2
>>> my_list.head.<<next>>.value
4
>>> my_list.head.<<next.next>>.value
6
>>> my_list.head.<<next.next>> is my_list.tail
True
>>> my_list.tail.prev.prev is my_list.head
True
\end{lstlisting}

% Problem 2: LinkedList.find()
\begin{problem}
Add a method called \li{find(self, data)} to the \li{LinkedList} class that
returns the first node in the list containing \li{data} (return the actual \li{LinkedListNode} object, not its \li{value}).
If no such node exists, or if the list is empty, raise a \li{ValueError} with an appropriate error message.
\\
(Hint: if \li{current} is assigned to one of the nodes the list, what does the following line do?)
\begin{lstlisting}
current = current.<<next>>
\end{lstlisting}
\end{problem}

\subsection*{Magic Methods} % -------------------------------------------------

Endowing data structures with magic methods makes it much easier to use it intuitively.
Consider, for example, how a Python list responds to built-in functions like \li{len()} and \li{print()}.
At the bare minimum, we should give our linked list the same functionality.

\begin{problem} % __len__() and __str__() for the LinkedList class.
Add magic methods to the \li{LinkedList} class so it behaves more like the built-in Python list.
\begin{enumerate}
\item Write the \li{__len__()} method so that the length of a \li{LinkedList} instance is equal to the number of nodes in the list.
To accomplish this, consider adding an attribute that tracks the current size of the list.
It should be updated every time a node is successfully added or removed.

\item Write the \li{__str__()} method so that when a \li{LinkedList} instance is printed, its output matches that of a Python list.
Entries are separated by a comma and one space, and strings are surrounded by single quotes.
Note the difference between the string representations of the following lists:

\begin{lstlisting}
>>> num_list = [1, 2, 3]
>>> str_list = ['1', '2', '3']
>>> print(num_list)
[1, 2, 3]
>>> print(str_list)
<<['1', '2', '3']>>
\end{lstlisting}
\end{enumerate}
\end{problem}

\subsection*{remove()} % ------------------------------------------------------

In addition to adding new nodes to the end of a list, it is also useful to remove nodes and insert new nodes at specified locations.
To delete a node, all references to the node must be removed.
Then Python will automatically delete the object, since there is no way for the user to access it.
Na{\"i}vely, this might be done by finding the previous node to the one being removed, and setting its \li{<<next>>} attribute to \li{None}.

\begin{lstlisting}
class LinkedList:
    # ...
    def remove(self, data):
        """Attempt to remove the first node containing 'data'.
        This method incorrectly removes additional nodes.
        """
        # Find the target node and sever the links pointing to it.
        target = self.find(data)
        target.prev.<<next>> = None                     # -/-> target
        target.<<next>>.prev = None                     # target <-/-
\end{lstlisting}

Removing all references to the target node will delete the node (see Figure \ref{fig:remove_bad}).
However, the nodes before and after the target node are no longer linked.

\begin{lstlisting}
>>> my_list = LinkedList()
>>> for i in range(10):
...     my_list.append(i)
...
>>> print(my_list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> my_list.remove(4)               # Removing a node improperly results in
>>> print(my_list)                  # the rest of the chain being lost.
[0, 1, 2, 3]                        # Should be [0, 1, 2, 3, 5, 6, 7, 8, 9].
\end{lstlisting}

\begin{figure}[H] % Incorrect remove().
\centering
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto, node distance=1.5cm,thick,main node/.style={rectangle,draw}, minimum size=.5cm]
\tikzset{rect node/.style={rectangle, draw, minimum height = .5cm, minimum width=.2cm}}
    \node[main node] (1) {A};
    \node[main node] (2) [right of=1] {B};
    \node[main node] (3) [right of=2] {C};
    \node[main node] (4) [right of=3] {D};
    \node[main node] (5) [right of=4, node distance=2.6cm] {A};
    \node[main node] (6) [right of=5] {B};
    \node[main node] (7) [right of=6] {C};
    \node[main node] (8) [right of=7] {D};
    \node[draw=none, node distance=.07cm] (1up) [above of=1] {};
    \node[draw=none, node distance=.07cm] (1dn) [below of=1] {};
    \node[draw=none, node distance=.07cm] (2up) [above of=2] {};
    \node[draw=none, node distance=.07cm] (2dn) [below of=2] {};
    \node[draw=none, node distance=.07cm] (3up) [above of=3] {};
    \node[draw=none, node distance=.07cm] (3dn) [below of=3] {};
    \node[draw=none, node distance=.07cm] (4up) [above of=4] {};
    \node[draw=none, node distance=.07cm] (4dn) [below of=4] {};
    \node[draw=none, node distance=.07cm] (5up) [above of=5] {};
    \node[draw=none, node distance=.07cm] (5dn) [below of=5] {};
    \node[draw=none, node distance=.07cm] (6up) [above of=6] {};
    \node[draw=none, node distance=.07cm] (6dn) [below of=6] {};
    \node[draw=none, node distance=.07cm] (7up) [above of=7] {};
    \node[draw=none, node distance=.07cm] (7dn) [below of=7] {};
    \node[draw=none, node distance=.07cm] (8up) [above of=8] {};
    \node[draw=none, node distance=.07cm] (8dn) [below of=8] {};
\foreach \r in {1, 2, 3, 4, 5, 6, 7, 8}{
    \node[rect node][right of=\r, node distance = .36cm]{};
    \node[rect node][left of=\r, node distance = .36cm]{};}
\foreach \s/\t in {1up/2up, 2dn/1dn, 2up/3up, 3dn/2dn, 3up/4up, 4dn/3dn, 5up/6up, 6dn/5dn, 7dn/6dn, 7up/8up}{
        \path[draw](\s) edge[shorten <=.1cm, shorten >=.1cm](\t);}
    \node[draw=none, node distance=1.5cm] [right of=8]{};  % Centralize
\end{tikzpicture}
\caption{Na{\"i}ve Removal for Doubly linked Lists. Deleting all references pointing to $C$ deletes the node, but it also separates nodes $A$ and $B$ from node $D$.}
\label{fig:remove_bad}
\end{figure}

This can be remedied by pointing the previous node's \li{<<next>>} attribute to the node after the deleted node, and similarly changing that node's \li{prev} attribute.
Then there will be no reference to the removed node and it will be deleted, but the chain will still be connected.

\begin{figure}[H] % Correct remove().
\centering
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto, node distance=1.5cm,thick,main node/.style={rectangle,draw}, minimum size=.5cm]
\tikzset{rect node/.style={rectangle, draw, minimum height = .5cm, minimum width=.2cm}}
    \node[main node] (1) {A};
    \node[main node] (2) [right of=1] {B};
    \node[main node] (3) [right of=2] {C};
    \node[main node] (4) [right of=3] {D};
    \node[main node] (5) [right of=4, node distance=2.6cm] {A};
    \node[main node] (6) [right of=5] {B};
    \node[main node] (7) [right of=6] {C};
    \node[main node] (8) [right of=7] {D};
    \node[draw=none, node distance=.07cm] (1up) [above of=1] {};
    \node[draw=none, node distance=.07cm] (1dn) [below of=1] {};
    \node[draw=none, node distance=.07cm] (2up) [above of=2] {};
    \node[draw=none, node distance=.07cm] (2dn) [below of=2] {};
    \node[draw=none, node distance=.07cm] (3up) [above of=3] {};
    \node[draw=none, node distance=.07cm] (3dn) [below of=3] {};
    \node[draw=none, node distance=.07cm] (4up) [above of=4] {};
    \node[draw=none, node distance=.07cm] (4dn) [below of=4] {};
    \node[draw=none, node distance=.07cm] (5up) [above of=5] {};
    \node[draw=none, node distance=.07cm] (5dn) [below of=5] {};
    \node[draw=none, node distance=.07cm] (6up) [above of=6] {};
    \node[draw=none, node distance=.07cm] (6dn) [below of=6] {};
    \node[draw=none, node distance=.07cm] (7up) [above of=7] {};
    \node[draw=none, node distance=.07cm] (7dn) [below of=7] {};
    \node[draw=none, node distance=.07cm] (8up) [above of=8] {};
    \node[draw=none, node distance=.07cm] (8dn) [below of=8] {};
\foreach \r in {1, 2, 3, 4, 5, 6, 7, 8}{
    \node[rect node][right of=\r, node distance = .36cm]{};
    \node[rect node][left of=\r, node distance = .36cm]{};}
\foreach \s/\t in {1up/2up, 2dn/1dn, 2up/3up, 3dn/2dn, 3up/4up, 4dn/3dn, 5up/6up, 6dn/5dn, 7dn/6dn, 7up/8up}{
        \path[draw](\s) edge[shorten <=.1cm, shorten >=.1cm](\t);}
    \path[draw, shorten <=.2cm](6) edge[red, bend left] (8);
    \path[draw, shorten <=.2cm](8) edge[red, bend left] (6);
    \node[draw=none, node distance=1.5cm] [right of=8]{};  % Centralize
\end{tikzpicture}
\caption{Correct Removal for Doubly linked Lists. To avoid gaps in the chain, nodes $B$ and $D$ must be linked together.}
\label{fig:remove_good}
\end{figure}

\begin{problem} % LinkedList.remove().
Modify the \li{remove()} method given above so that it correctly removes the first node in the list containing the specified data.
Account for the special cases of removing the first, last, or only node.
\end{problem}

\begin{warn} % Garbage collection warning.
Python keeps track of the variables in use and automatically deletes a variable if there is no access to it.
In many other languages, leaving a reference to an object without explicitly deleting it could cause a serious memory leak.
See \url{https://docs.python.org/2/library/gc.html} for more information on Python's auto-cleanup system.
\end{warn}

\subsection*{insert()} % ------------------------------------------------------

\begin{problem} % LinkedList.insert()
Add a method called \li{insert(self, data, place)} to the \li{LinkedList} class that inserts a new node containing \li{data} immediately before the first node in the list containing \li{place}.
Account for the special case of inserting before the first node.

See Figure \ref{fig:insert} for an illustration.
Note that since \li{insert()} places a new node before an existing node, it is not possible to use \li{insert()} to put a new node at the end of the list or in an empty list (use \li{append()} instead).
\end{problem}

\begin{figure}[H] % insert().
\centering
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto, node distance=1.6cm,thick,main node/.style={rectangle,draw}, minimum size=.5cm]
\tikzset{rect node/.style={rectangle, draw, minimum height = .5cm, minimum width=.2cm}}
    \node[main node] (1) {A};
    \node[main node] (2) [right of=1] {B};
    \node[main node] (3) [right of=2] {D};
    \node[main node] (4) [below right of=2] {C};
    \node[main node] (5) [right of=3, node distance=3.5cm] {A};
    \node[main node] (6) [right of=5] {B};
    \node[main node] (7) [right of=6, node distance=2.2cm] {D};
    \node[main node] (8) [below right of=6] {C};
    \node[draw=none, node distance=.07cm] (1up) [above of=1] {};
    \node[draw=none, node distance=.07cm] (1dn) [below of=1] {};
    \node[draw=none, node distance=.07cm] (2up) [above of=2] {};
    \node[draw=none, node distance=.07cm] (2dn) [below of=2] {};
    \node[draw=none, node distance=.07cm] (3up) [above of=3] {};
    \node[draw=none, node distance=.07cm] (3dn) [below of=3] {};
    \node[draw=none, node distance=.07cm] (4up) [above of=4] {};
    \node[draw=none, node distance=.07cm] (4dn) [below of=4] {};
    \node[draw=none, node distance=.07cm] (5up) [above of=5] {};
    \node[draw=none, node distance=.07cm] (5dn) [below of=5] {};
    \node[draw=none, node distance=.07cm] (6up) [above of=6] {};
    \node[draw=none, node distance=.07cm] (6dn) [below of=6] {};
    \node[draw=none, node distance=.07cm] (7up) [above of=7] {};
    \node[draw=none, node distance=.07cm] (7dn) [below of=7] {};
    \node[draw=none, node distance=.07cm] (8up) [above of=8] {};
    \node[draw=none, node distance=.07cm] (8dn) [below of=8] {};
    \node[draw=none, black!20!blue, node distance=1.5cm] [above left of=1](H1) {Head};
    \node[draw = none, black!20!blue, node distance=1.5cm] [above right of=3](T1) {Tail};
    \node[draw=none, black!20!blue, node distance=1.5cm] [above left of=5](H2) {Head};
    \node[draw = none, black!20!blue, node distance=1.5cm] [above right of=7](T2) {Tail};
\foreach \r in {1, 2, 3, 4, 5, 6, 7, 8}{
        \node[rect node][right of=\r, node distance = .36cm]{};
        \node[rect node][left  of=\r, node distance = .36cm]{};}
\foreach \s/\t in {1up/2up, 2dn/1dn, 2up/3up, 3dn/2dn, 5up/6up, 6dn/5dn}{
        \path[draw](\s) edge[shorten <=.1cm, shorten >=.1cm](\t);}
\foreach \s/\t in {6up/8up, 8dn/6dn, 8up/7up, 7dn/8dn}{
        \path[draw](\s) edge[red, shorten <=.1cm, shorten >=.1cm](\t);}
    \draw[black!20!blue, shorten >=.1cm] (H1) edge (1.north);
    \draw[black!20!blue, shorten >=.1cm] (T1) edge (3.north);
    \draw[black!20!blue, shorten >=.1cm] (H2) edge (5.north);
    \draw[black!20!blue, shorten >=.1cm] (T2) edge (7.north);
    \node[draw = none, node distance = 1.5cm] [right of=8]{};  % Centralize
\end{tikzpicture}
\caption{Insertion for Doubly linked Lists.}
\label{fig:insert}
\end{figure}

\begin{info} % Big-O rates for linked lists.
The temporal complexity for inserting to the beginning or end of a linked list is $O(1)$, but inserting anywhere else is $O(n)$, where $n$ is the number of nodes in the list.
This is quite slow compared other data structures.
In the next lab we turn our attention to \emph{trees}, special kinds of linked lists that allow for much quicker sorting and data retrieval.
\end{info}

\section*{Restricted-Access Lists} % ==========================================

It is sometimes wise to restrict the user's access to some of the data within a structure.
The three most common and basic restricted-access structures are \emph{stacks}, \emph{queues}, and \emph{deques}.
Each structure restricts the user's access differently, making them ideal for different situations.

\begin{itemize}
\item \textbf{Stack}: \emph{Last In, First Out} (LIFO).
Only the last item that was inserted can be accessed.
A stack is like a pile of plates: the last plate put on the pile is (or should be) the first one to be taken off.
Stacks usually have two main methods: \li{push()}, to insert new data, and \li{pop()}, to remove and return the last piece of data inserted.

\item \textbf{Queue} (pronounced ``cue''): \emph{First In, First Out} (FIFO).
New nodes are added to the end of the queue, but an existing node can only be removed or accessed if it is at the front of the queue.
A queue is like a line at the bank: the person at the front of the line is served next, while newcomers add themselves to the back of the line.
Queues also usually have a \li{push()} and a \li{pop()} method, but \li{push()} inserts data to the end of the queue while \li{pop()} removes and returns the data at the front of the queue.\footnote{\li{push()} and \li{pop()} for queues are sometimes called \li{enqueue()} and \li{dequeue()}, respectively)}

\item \textbf{Deque} (pronounced ``deck''): a double-ended queue.
Data can be inserted or removed from either end, but data in the middle is inaccessible.
A deque is like a deck of cards, where only the top and bottom cards are readily accessible.
A deque has two methods for insertion and two for removal, usually called \li{append()}, \li{appendleft()}, \li{pop()}, and \li{popleft()}.
\end{itemize}

\begin{problem} % Deque class.
Write a \li{Deque} class that inherits from the \li{LinkedList} class.
%
\begin{enumerate}
\item Use inheritance to implement the following methods:
%
\begin{itemize}
    \item \li{pop(self)}: Remove the last node in the list and return its data.
    \item \li{popleft(self)}: Remove the first node in the list and return its data.
    \item \li{appendleft(self, data)}: Insert a new node containing \li{data} at the beginning of the list.
\end{itemize}
The \li{LinkedList} class already implements the \li{append()} method.

\item Override the \li{remove()} method with the following:

\begin{lstlisting}
def remove(*args, **kwargs):
    raise NotImplementedError("Use pop() or popleft() for removal")
\end{lstlisting}

This effectively disables \li{remove()} for the \li{Deque} class, preventing the user from removing a node from the middle of the list.

\item Disable the \li{insert()} method as well.
\end{enumerate}
\end{problem}

\begin{info}
The \li{*args} argument allows the \li{remove()} method to receive any number of positional arguments without raising a \li{TypeError}, and the \li{**kwargs} argument allows it to receive any number of keyword arguments.
This is the most general form of a function signature.
\end{info}

Python lists have \li{append()} and \li{pop()} methods, so they can be used as stacks.
However, data access and removal from the front is much slower, as Python lists are not implemented as linked lists.

The \li{collections} module in the standard library has a \li{deque} object, implemented as a doubly linked list.
This is an excellent object to use in practice instead of a Python list when speed is of the essence and data only needs to be accessed from the ends of the list.

\begin{problem} % Reverse a file using a stack/deque.
Write a function that accepts the name of a file to be read and a file to write to.
Read the first file, adding each line to the end of a deque.
After reading the entire file, pop each entry off of the end of the deque one at a time, writing the result to a line of the second file.

For example, if the file to be read has the list of words on the left, the resulting file should have the list of words on the right.

\begin{lstlisting}
<<My homework is too hard for me.         I am a mathematician.
I do not believe that                   Programming is hard, but
I can solve these problems.             I can solve these problems.
Programming is hard, but                I do not believe that
I am a mathematician.                   My homework is too hard for me.
\end{lstlisting}

You may use a Python list, your \li{Deque} class, or \li{collections.deque} for the deque.
Test your function on the file \texttt{english.txt}, which contains a list of over 58,000 English words in alphabetical order.
\end{problem}

\newpage

\section*{Additional Material} % ==============================================

\subsection*{Improvements to the Linked List Class} % -------------------------

\begin{enumerate}
\item Add a keyword argument to the constructor so that if an iterable is input, each element of the iterable is immediately added to the list.
This makes it possible to cast an iterable as a \li{LinkedList} the same way that an iterable can be cast as one of Python's standard data structures.

\begin{lstlisting}
>>> my_list = [1, 2, 3, 4, 5]
>>> my_linked_list = LinkedList(my_list)  # Cast my_list as a LinkedList.
>>> print(my_linked_list)
[1, 2, 3, 4, 5]
\end{lstlisting}

\item Add new methods:
\begin{itemize}
\item \li{count()}: return the number of occurrences of a specified value.
\item \li{reverse()}: reverse the ordering of the nodes (in place).
\item \li{rotate()}: rotate the nodes a given number of steps to the right (in place).
\item \li{sort()}: sort the nodes by their data (in place).
\end{itemize}

\item Implement more magic methods:
\begin{itemize}
\item \li{__add__()}: concatenate two lists.
\item \li{__getitem__()} and \li{__setitem__()}: enable standard bracket indexing.
\item \li{__iter__()}: support \li{for} loop iteration, the \li{iter()} built-in function, and the \li{in} statement.
\end{itemize}
\end{enumerate}

\subsection*{Other Linked List} % ---------------------------------------------

The \li{LinkedList} class can also be used as the backbone for other data structures.
%
\begin{enumerate}
\item A \emph{sorted list} adds new nodes strategically so that the data is always kept in order.
A \li{SortedLinkedList} class that inherits from the \li{LinkedList} class should have a method called \li{add(self, data)} that inserts a new node containing \li{data} before the first node in the list that has a \li{value} that is greater or equal to \li{data} (thereby preserving the ordering).
Other methods for adding nodes should be disabled.

A linked list is \textbf{not} an ideal implementation for a sorted list (try sorting \texttt{english.txt}).

\item In a \emph{circular linked list}, the ``last'' node connects back to the ``first'' node.
Thus a reference to the tail is unnecessary.
\end{enumerate}
