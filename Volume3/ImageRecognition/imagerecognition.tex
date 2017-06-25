\lab{Image Recognition Tasks}{Image Recognition Tasks}
\objective{Use the KNN and SVM algorithms to solve two image recognition problems.}

Two important image recognition problems are character recognition and face recognition. The first is generally framed as a post office problem. Every day, millions of pieces of mail are sent through the US Postal Service each day. This requires an automated way of routing much of the mail. The problem is to automatically determine the zip code of the addressee for a piece of mail. There are two parts to this problem: find the zip code on the letter, and then determine what it is. We will only consider the second part in this lab.

Given that we have an image of a single digit, how can we decide what it is without human intervention? This is a classification problem, with the classes being the digits $0$ through $9$. We will use both the KNN and SVM classifiers to predict each digit.

We will use the \li{digits} data set from \li{sklearn.datasets} for our data, using the method \li{sklearn.datasets.load\_digits()}. Each sample is an $8 \times 8$ image which has been flattened into a length-$64$ vector.

\begin{problem}
Load the digits data and separate it into a training set and a test set.
\end{problem}

The module \li{sklearn.neighbors} has a nice class \li{KNeighborsClassifier} that implements the KNN classifier.

\begin{problem}
Find and read some of the documentation for the aforementioned class. Implement a KNN classifier on the training set. What is the misclassification rate on your test set?
\end{problem}

While the SVM was originally designed as a binary classifier, it has been extended into a multi-class classifier as well. We won't go into the details here, but one common extension is to train $K$ different SVMs (where $K$ is the number of classes), each being a ``one-versus-all'' classifier. After some calibration, a new sample is predicted to be the class $k$ where $f_{k}(\mathbf{x})$ is greatest, $f_{k}$ being the function defining the hyperplane for class $k$ against all other classes. Again, \li{sklearn.svm} has a nice class \li{SVC} that implements this.

The module \li{sklearn.grid\_search} provides a nice way to find the classifier that performs the best on the training set, considering a grid of parameters. We will use this to help us find an optimal SVM for the digits data set, where we use a radial basis function for the kernel.
\begin{lstlisting}
>>> from sklearn.grid_search import GridSearchCV
>>> from sklearn.svm import SVC
>>> param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5], 'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],}
>>> clf = GridSearchCV(SVC(kernel='rbf',class_weight='auto'), param_grid)
>>> clf = clf.fit(training_data, training_target)
\end{lstlisting}

\begin{problem}
Predict the values for the test set using the SVM we just trained. What is your misclassification rate? How does the SVM's performance compare to the KNN classifier?
\end{problem}

We now consider our second image recognition problem: face recognition. This is much harder than simply recognizing a digit on a white envelope, as there is bound to be so much more noise and variation.

We use as our data set the ``Labeled Faces in the Wild", a database of face photographs. In fact, we will only consider a small subset of this database, including only images of Ariel Sharon, Colin Powell, Donald Rumsfeld, George W Bush, Gerhard Schroeder, Hugo Chavez, and Tony Blair. Through \li{sklearn.datasets} we can download and process this data set rather easily, though it might take some time.
\begin{lstlisting}
>>> from sklearn.datasets import fetch_lfw_people
>>> people = fetch_lfw_people(min_faces=70,resize=0.4)
>>> data = people.data
>>> target = lfw_people.target
\end{lstlisting}

This data set consists of $1288$ images of size $50 \times 37$, each flattened. The targets are digits from $0$ to $6$, corresponding with the ordered names above. This might seem counterintuitive, considering the main ideas of SVMs, but it is sometimes useful to reduce the dimensionality of our feature space before implementing an SVM, using PCA so we can retain as much information as possible while still reducing the dimensionality.
\begin{lstlisting}
>>> from sklearn.decomposition import PCA
>>> pca = PCA(n_components=150, whiten=True).fit(data)
>>> data_pca = pca.transform(data)
\end{lstlisting}

\begin{problem}
Separate the data set into training data and test data. Create a PCA object fit to the training data. With this object, reduce the dimensionality of both the training data and the test data.
\end{problem}

\begin{problem}
Train an SVM on the image set with the same parameter grid search used above. Label the test data. What is your misclassification rate?
\end{problem}

Let's also compare and see how well the KNN classifier does on this data set.

\begin{problem}
Train a KNN classifier on the image data set. What is your misclassification rate on the test data? Does this surprise you?
\end{problem}

This allows us to end this course with a very important take-home message: the No Free Lunch Theorem. In essence, this theorem states that there is no single machine learning classifier to rule them all--each has its strengths and weaknesses. More specifically, if there is a ML classifier that outperforms all other classifiers on a data set, then we can find a data set where a different classifier will be superior. This means that we have to be intelligent in how we choose which classifiers to try, because there isn't any ``go-to'' classifier that will always work.
