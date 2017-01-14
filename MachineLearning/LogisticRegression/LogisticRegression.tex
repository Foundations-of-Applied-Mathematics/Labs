\lab{Logistic Regression}{Logistic Regression}
\objective{Understand the basics of Logistic Regression, and apply to the Titanic problem.}

\subsection*{Binary Logistic Regression}
A \emph{Logistic Regression Model} is a probability model that can be used to predict outcomes for a set of data.  Usually ``Logistic Regression" refers to what is more appropriately called \emph{binary logistic regression}.  This is a model which can assign data points to one of two sets, and is used in many different fields.  One common medical example is predicting whether or not a patient has a particular disease.  Based upon several factors, which may be both continuous (age, height, weight) and categorical (gender, race), we can quantify the probability of infection.  This probability is computed by way of the \emph{logistic function}, which, given the contributing factors, will return a probability value between $0$ and $1$.  This probability will then be used to assign a label to our input data (`infected' or `not infected', for example) by using some cut-off value, and will depend on the need for accuracy in the specific application.  Success corresponds to a label of $1$, and failure to a label of $0$.

The logistic function takes in as input any real number and returns a value between $0$ and $1$, and is defined explicitly as
\begin{equation}
\phi(t) = \frac{1}{1 + e^{-s}},
\end{equation}
where $s$ is some combination of the input variables $x_1, \cdots, x_n$.  The graph of this function can be seen in Figure ???.   $\phi(x)$ can then be interpreted as the probability of success.  In some cases it is not possible to find a closed-form expression for the correct combination of the input variables.  However, in many cases we can acheive reasonable accuracy by using a linear combination of $x_i, \cdots, x_n$, i.e.
\begin{equation*}
s = c_0 + c_1 x_1 + \cdots + c_n x_n.
\end{equation*}
This can be written more compactly as
\begin{equation*}
s = \bf{c}^{T}\bf{x},
\end{equation*}
where $\bf{x}$ $= (1, x_1, \cdots , x_n)^{T}$ and $\bf{c}$ $\in \mathbb{R}^{n+1}$.

Given a training set of labeled data points, a Logistic Regression Model will find the optimal $\bf{c}$ for the data, and can then be used to predict labels for further data points.

\subsection*{The Titanic Problem}
The Titanic dataset is especially useful for Logistic Regression.  This dataset is composed of actual data obtained concerning the passengers on the ill-fated Titanic voyage, given in the bulleted list below.  Using logistic regression, we can predict whether or not a passenger survived based on this data.  We do so by training a model on a portion of the dataset, the training set, and predicting labels for the remaining data, the test set.

Before beginning our classification, however, we will first need to process our data.  The Titanic dataset contains much more information than is currently relevant for our purposes.  You can obtain this data in Excel Spreadsheet form at [Insert link here].  We recommend using pandas to read in and process the data.  The columns are as follows:
\begin{itemize}
\item \li{pclass}: An integer in $\{1, 2, 3\}$ which describes the class the passenger was in.
\item \li{survived}:  The dependent variable.  $1$ indicates survival, and $0$ death.
\item \li{name}: A string containing the passenger's name.
\item \li{sex}: A string, either `male' or `female'.
\item \li{age}: Either an integer or a float.
\item \li{sibsp}: An integer giving the number of siblings and/or spouse who embarked with the passenger.
\item \li{parch}: An integer giving the number of parents and/or children who embarked with the passenger.
\item \li{ticket}: A string containing the transaction code for the ticket(s) purchased.
\item \li{fare}: A float giving the cost of the ticket purchased.
\item \li{cabin}: A string giving the assigned sleeping cabin for the passenger (note that the majority of this column is blank).
\item \li{embarked}: A string in $\{S, C, Q\}$ corresponding to the location of the passenger's embarkment, Southampton (UK), Cherbourg (France), or Queenstown (Ireland), respectively.
\item \li{boat}: An int or string for those who survived giving which life boat they rode in.
\item \li{body}: An int giving the number of body for those who died who were found and identified.
\item \li{home.dest}: A string giving the home of or location to which the passenger was headed.
\end{itemize}

\begin{problem}
Create a function called \li{initialize} which will process the Titanic data set into useable format by doing the following:
\begin{enumerate}
\item Choose the coulmns that you believe will be relevant in predicting the survival of the passengers, and drop the other columns.  You may not use \li{boat} or \li{body}, as these are dependent on whether or not the passenger survived.  Be sure to include \li{survived}, which will be separated later as the independent variable, as well as \li{sex} and \li{pclass}.
\item Since \li{sex} is really a binary variable, make it one explicitly by changing ``female" and ``male" to be binary values.
\item Drop the rows that contain missing values.  Make sure you have a significant number of rows left.  If you have too few, you may need to choose fewer columns to keep before deleting the incomplete rows.
\item Because the \li{pclass} column is an integer in $\{1, 2, 3\}$, it will be treated as a ranked variable instead of simply a categorical variable.  It may be useful to rank this variable, or it may mess up our classification.  Include a keyword argument \li{pclass_change} with default \li{True}.  If it is set to \li{True}, eliminate this ranking by dividing \li{pclass} into two binary columns.  Make one column a boolean for being $1^{st}$ class and the other a boolean for being $2^{nd}$ class. (This means that a value of $1$ would correspond to $[1, 0]$, $2$ to $[0, 1]$, and $3$ to $[0, 0]$.)
\item Split the remaining rows into a training and a test set using a $60/40$ split.  Be sure and pick random rows for each group and not rows in any particular order.
\end{enumerate}
Have your function return the training set and the test set, in that order.
\end{problem}

\subsection*{Model Evaluation}
Now that we have our training set, we can train a model, which can be used to obtain the probability of success for each data point.  The label chosen depends heavily on the probability cut-off value mentioned previously, which we represent as $\tau$.  In the simplest manner, we can simply pick a value of $\tau = 0.5$, which will then assign the label with the highest likelihood.  However, it is often beneficial to choose a different value of $\tau$.  In regards to the probability of infection for serious diseases, it might be best to give a patient medicine if they have even a $10$ percent chance of infection.  So how can we find the ``best" cut-off value?

In order to determine this, we need to discuss how to measure the accuracy of the labels predicted.  Say that we have picked a cut-off value $\tau$, and have assigned labels to the test set.  Using the predicted labels and the actual labels, we can obtain four important values: the number of \emph{true positives}, \emph{false positives}, \emph{true negatives}, and \emph{false positives}, which are abbreviated TP, FP, TN, and FP, respectively.  These values are integers which together sum to the number of labels predicted.  You can see the definition of these in Table ??? (until the figure is up, true positives are the points with predicted label 1 and true label 1, false positives have predicted label 1 true label 0, true negatives predicted label 0 true label 0, and false negatives true label 1 predicted label 0).  We can now use these to report our accuracy in various metrics:
\begin{itemize}
\item \emph{Prediction accuracy} is defined as $\frac{TP+TN}{TP+FN+FP+TN}$, and is the percentage of correctly predicted cases.
\item \emph{Sensitivity}, also known as the \emph{true positive rate} or $TPR$, is given by the fraction of correctly predicted cases where the actual outcome is $1$, $\frac{TP}{TP+FN}$.
\item \emph{Specificity}, the \emph{true negative rate}, or $TNR$ is the proportion of correctly predicted cases where the true outcome is $0$, $\frac{TN}{FP+TN}$.
\item \emph{False Positive Rate}, or $FPR$, is the proportion of incorrectly predicted cases where the true outcome is $0$, and is given by $\frac{FP}{FP+TN}$.
\end{itemize}
All of these depend strongly on the value chosen for $\tau$.

A \emph{roc curve} is useful in measuring the accuracy of a model.  To make a roc curve, we pick many values for $\tau$, and obtain the False Positive Rate and the True Positive Rate for each.  Then we plot the data points  $(FPR_{\tau},TPR_{\tau})$ for each value of $\tau$ chosen and connect them into a curve.  A completely random label assignment would result in a nearly-linear roc curve, while a more accurate assignment would result in a more steeply-rising curve (see Figure ???).  A good choice for $\tau$ is the one that intersects the family of lines $y=x+b$ at only one point, which intuitively is the point closest to the vertex $(0, 1)$.  Mathematically, this is given by
\begin{equation}
\operatorname*{arg\,max}_{\tau} (TPR_{\tau} - FPR_{\tau}).
\end{equation}

\begin{problem}
Use the function declaration below to find the best value for $\tau$.  You should use evenly spaced values from $0$ to $1$, exclusive.
\begin{lstlisting}
def best_tau(predicted_labels, true_labels, n_tau=100, plot=True):
    """
    Parameters
    ----------
    predicted_labels : ndarray of shape (n,)
        The predicted labels for the data
    true_labels : ndarray of shape (n,)
        The actual labels for the data
    n_tau : int
        The number of values to try for tau
    plot : boolean
        Whether or not to plot the roc curve

    Returns
    -------
    best_tau : float
        The optimal value for tau for the data.
    """
    pass
\end{lstlisting}
\end{problem}

Now that we have a good value for $\tau$, we can quantify the accuracy of a model. We will do so for a few different types of models for the Titanic data you initialized previously.  For the first two, we will use the logistic classifier found in \li{sklearn.linear_model.LogisticRegression}.  The first model we use will be our ``Unchanged Logistic Classifier", which will use our Titanic data with \li{pclass} unchanged.  The second model is the ``Changed Logistic Classifier", which use the data with \li{pclass} changed.

When using this package to create a classifier, we need to input a keyword argument \li{C}.  This value represents the inverse of the regularization strength.  Different values will yield different results.  A better value for \li{C} will yield a more steeply-rising roc curve.  The model can find the coefficients (the vector $\bf{c}$), along with the probabilities of failure and success for each label.  With these in hand, we can use the function \li{sklearn.metrics.roc_curve} to obtain the False Positive Rates, the True Positive Rates, and the optimal value for $\tau$.  You will need to pass in the test data, the probability of success, and the keyword argument \li{pos_label} $= 1$.  The accuracy of the model with input value \li{C} can then be obtained using \li{sklearn.metrics.auc}, which will give the area under the curve.  The larger the area, the more steeply-rising curve we have, and the better the model.  Note that we create a single roc curve using one value for \li{C} and multiple values for $\tau$.

\begin{problem}
Use the following function declaration to return the auc score for the two Logistic Regression models described.
\begin{lstlisting}
def auc_scores(unchanged_logreg, changed_logreg):
    """
    Parameters
    ----------
    unchanged_logreg : float in (0,1)
        The value to use for C in the unchanged model
    changed_logreg : float in (0,1)
        The value to use for C in the changed model

    Returns
    -------
    unchanged_auc : float
        The auc for the unchanged model
    changed_auc : float
        The auc for the changed model
    """
    pass
\end{lstlisting}
\end{problem}

We can test a Naive Bayes model against our Logistic Regression model for both the unchanged and changed models to see the comparative accuracy.  Use the model \li{MultinomialNB}, found in \li{sklearn.naive_bayes}.  You can use it in the same manner as \li{LogisticRegression}, except instead of passing in the keyword argument \li{C}, you will pass in a keyword argument \li{alpha} corresponding to a smoothing parameter.
\begin{problem}
Add input variables \li{unchanged_bayes} and \li{changed_bayes} to your function from the previous problem to obtain the auc for each of these models.  Your function should return all four areas, unchanged logistic regression, changed logistic regression, unchanged Bayes, and changed Bayes, in that order.
\end{problem}

Different values for \li{C} and \li{alpha} will yield different results.  We seek to find those that will maximize the area under the curve.  One way to do so is to pick a number of evenly-spaced points between $0$ and $1$, exclusive, and try each one in turn, keeping the value that yields the greatest accuracy.
\begin{problem}
Use the function declaration below to find the optimal values for \li{C} and $alpha$ as described.
\begin{lstlisting}
def find_best_parameters(choices):
    """
    Parameters
    ----------
    choices : int
        The number of values to try for C and alpha

    Returns
    -------
    best : list of length 4
        The best values for C for the unchanged and changed logistic
         regression models, and the best values for alpha for the
         unchanged and changed Naive Bayes models, respectively.
    """
    pass
\end{lstlisting}
\end{problem}

Now that we have found the optimal inputs for these functions, we can test them against one another.
\begin{problem}
Create a function called \li{results} which will graph of the roc curves for each of the methods, and will print out the names of the models with their corresponding areas, in numerically descending order.
\end{problem}
