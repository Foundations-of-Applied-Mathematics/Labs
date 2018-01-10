\lab{MongoDB}{MongoDB}
% TODO: redo introduction.
\objective{Relational databases, including those managed with SQL or pandas, require data to be organized into tables.
However, many data sets have an inherently dynamic structure that cannot be efficiently represented as tables.
MongoDB is a non-relational database management system that is well-suited to large, fast-changing datasets.
In this lab we introduce the Python interface to MongoDB, including common commands and practices.
% MongoDB communication is formatted almost entirely as JSON strings and includes many of the same properties.
}

\begin{comment} % unnecessary historical exposition, covered by intro.

\section*{NoSQL Databases}

Relational databases, such as those accessed using SQL, were developed in the 1970s, and were the most popular database type for many years.
These databases rely on the data having relational attributes, meaning that each item in the data set has the same attributes.
These databases can be visualized as tables, with each column containing one attribute.
Over time, relational databases became too structured for sets of data with unique attributes or  which were rapidly changing and expanding, especially with the expansion of large internet-based companies in the early 21st century.
As a simple example, in a data set of wildlife, a salamander and an apple both have attributes of size and color, but an apple does not need a gender attribute and a salamander does not need a ripeness attribute.
Because relational databases store items with the same attributes, if a salamander and an apple were to be stored in the same database, a different type of database would be required.
This is the purpose of Non-relational databases (commonly called NoSQL databases), which are built to allow for these types of data sets and have opened the door to massively scalable databases that can store data in many forms and physical locations.

With these new databases, a new family of database management systems arose to properly interface with them.
Instead of designing a new relational database to meet every need, non-relational systems were created that can adapt for specific scenarios.
MongoDB is such a system.
Many other database management systems, such as Cassandra, Redis, and Neo4j serve similar purposes.
This lab focuses on MongoDB.

\end{comment}

\section*{Database Initialization} % ==========================================

Suppose the manager of a general store has all sorts of inventory: food, clothing, tools, toys, etc.
There are some common attributes shared by all items: name, price, and producer.
However, other attributes are unique to certain items: sale price, number of wheels, or whether or not the product is gluten-free.
A relational database housing this data would be full of mostly-blank rows, which is extremely inefficient.
In addition, adding new items to the inventory requires adding new columns, causing the size of the database to rapidly increase.
To efficiently store the data, the whole database would have to be restructured and rebuilt often.

To avoid this problem, NoSQL databases like MongoDB avoid using relational tables.
Instead, each item is a JSON-like object, and thus can contain whatever attributes are relevant to the specific item, without including any meaningless attribute columns.

\begin{info}
MongoDB is a database management system (DBMS) that runs on a server, which should be running in its own dedicated terminal.
Refer to the Additional Material section for installation instructions.
\end{info}

% MongoDB has both a command line interface and Python bindings.
% This lab will use the official supported Python bindings, \li{PyMongo}.
% To install, you may use a package manager such as \li{pip} or download the binaries from the PyMongo website.
% More information for installation may be found at \url{http://api.mongodb.com/python/current/installation.html}.

The Python interface to MongoDB is called \li{pymongo}.
After installing \li{pymongo} \textbf{and} with the MongoDB server running, use the following code to connect to the server.

\begin{lstlisting}
>>> from pymongo import MongoClient
# Create an instance of a client connected to a database running
# at the default host IP and port of the MongoDB service on your machine.
>>> client = MongoClient()
\end{lstlisting}

\subsection*{Creating Collections and Documents}

A MongoDB database stores \emph{collections}, and a collection stores \emph{documents}.
The syntax for creating databases and collections is a little unorthodox, as it is done through attributes instead of methods.

\begin{lstlisting}
# Create a new database.
>>> db = client.db1

# Create a new collection in the db database.
>>> col = db.collection1
\end{lstlisting}

Documents in MongoDB are represented as JSON-like objects, and therefore do not adhere to a set schema.
Each document can have its own \emph{fields}, which are completely independent of the fields in other documents.

\begin{lstlisting}
# Insert one document with fields 'name' and 'age' into the collection.
>>> col.insert_one({'name': 'Jack', 'age': 23})

# Insert another document. Notice that the value of a field can be a string,
# integer, truth value, or even an array.
>>> col.insert_one({'name': 'Jack', 'age': 22, 'student': True,
...                 'classes': ['Math', 'Geography', 'English']})

# Insert many documents simultaneously into the collection.
>>> col.insert_many([
...     {'name': 'Jill', 'age': 24, 'student': False},
...     {'name': 'John', 'nickname': 'Johnny Boy', 'soldier': True},
...     {'name': 'Jeremy', 'student': True, 'occupation': 'waiter'}  ])
\end{lstlisting}

\begin{info}
Once information has been added to the database it will remain there, even if the python environment you are working with is shut down.
It can be reaccessed anytime using the same commands as before.

\begin{lstlisting}
>>> client = MongoClient()
>>> db = client.db1
>>> col = db.collection1
\end{lstlisting}

To delete a collection, use the database's \li{drop_collection()} method.
To delete a database, use the client's \li{drop_database()} method.
\end{info}

\begin{problem} % Load a collection with trump-related tweets.
The file \texttt{trump.json} contains posts from \url{http://www.twitter.com} (tweets) over the course of an hour that have the key word ``trump''.\footnote{See the Additional Materials section for an example of using the Twitter API.}
Each line in the file is a single JSON message that can be loaded with \li{json.loads()}.

Create a MongoDB database and initialize a collection in the database.
Use the collection's \li{delete_many()} method with an empty set as input to clear existing contents of the collection, then fill the collection one line at a time with the data from \texttt{trump.json}.
Check that your collection has 95,643 entries with its \li{count()} method.
\label{prob:mongo-fill-db}
\end{problem}

\section*{Querying a Collection} % ============================================

MongoDB uses a \emph{query by example} pattern for querying.  This means that to query a database, an example must be provided for the database to use in matching other documents.
\begin{lstlisting}
# Find all the documents that have a 'name' field containing the value 'Jack'.
>>> data = col.find({'name': 'Jack'})

# Find the FIRST document with a 'name' field containing the value 'Jack'.
>>> data = col.find_one({'name': 'Jack'})
\end{lstlisting}

The \li{find_one()} method returns the first matching document as a dictionary.
The \li{find()} query may find any number of objects, so it will return a \li{Cursor}, a Python object that is used to iterate over the query results.
There are many useful functions that can be called on a \li{Cursor}, for more information see \url{http://api.mongodb.com/python/current/api/pymongo/cursor.html}.

\begin{lstlisting}
# Search for documents containing True in the 'student' field.
>>> students = col.find({'student': True})
>>> students.count()                # There are 2 matching documents.
2

# List the first student's data.
# Notice that each document is automatically assigned an ID number as '_id'.
>>> students[0]
<<{'_id': ObjectId('59260028617410748cc7b8c7'),
 'age': 22,
 'classes': ['Math', 'Geography', 'English'],
 'name': 'Jack',
 'student': True}>>

# Get the age of the first student.
>>> students[0]['age']
22

# List the data for every student.
>>> list(students)
<<[{'_id': ObjectId('59260028617410748cc7b8c7'),
  'age': 22,
  'classes': ['Math', 'Geography', 'English'],
  'name': 'Jack',
  'student': True},
 {'_id': ObjectId('59260028617410748cc7b8ca'),
  'name': 'Jeremy',
  'occupation': 'waiter',
  'student': True}]>>
\end{lstlisting}

The Logical operators listed in the following table can be used to do more complex queries.
% There are more operators available with other Python Modules.

\begin{table}[H]
\begin{tabular}{l|l}
    Operator & Description \\ \hline
    \li{\$lt}, \li{\$gt} & \li{<}, \li{>} \\
    \li{\$lte},\li{\$gte} & \li{<=}, \li{>=} \\
    \li{\$eq}, \li{\$ne} & \li{==}, \li{\!=} \\
    \li{\$in}, \li{\$nin} & \li{in}, \li{not in} \\
    % \hline
    \li{\$or}, \li{\$and}, \li{\$not} & \li{or}, \li{and}, \li{not} \\
    % & It also matches if the field doesn't exist. \\
    \hline
    \li{\$exists} & Match documents with a specific field \\
    \li{\$type} & Match documents with values of a specific type \\
     % (either the name in quotes. \\
    % & or a number associated with the type. More information can be found at \\
    % & \url{https://docs.mongodb.com/manual/reference/operator/query/type/} ).  \\
    \li{\$all} & Match arrays that contain all queried elements \\
    \li{\$size} & Match arrays with a specified number of elements \\
    \hline
    \li{\$regex} & Search documents with a regular expression \\
\end{tabular}
\caption{MongoDB Query Operators}
\label{table:queryoperators}
\end{table}

\begin{lstlisting}
# Query for everyone that is either above the age of 23 or a soldier.
>>> results = col.find({'$or':[{'age':{'$gt': 23}},{'soldier': True}]})

# Query for everyone that is a student (those that have a 'student' attribute
# and haven't been expelled).
>>> results = col.find({'student': {'$not': {'$in': [False, 'Expelled']}}})

# Query for everyone that has a student attribute.
>>> results = col.find({'student': {'$exists': True}})

# Query for people whose name contains a the letter 'e'.
>>> import re
>>> results = col.find({'name': {'$regex': re.compile('e')}})
\end{lstlisting}

It is likely that a database will hold more complex JSON entries then these, with many nested attributes and arrays.
For example, an entry in a database for a school might look like this.

\begin{lstlisting}
{'name': 'Jason', 'age': 16,
 'student': {'year':'senior', 'grades': ['A','C','A','B'],'flunking': False},
 'jobs':['waiter', 'custodian']}
\end{lstlisting}

To query the nested attributes and arrays use a dot, as in the following examples.

\begin{lstlisting}
# Query for student that are seniors
>>> results = col.find({'student.year': 'senior'})

# Query for students that have an A in their first class.
>>> results = col.find({'student.grades.0': 'A'})
\end{lstlisting}

The Twitter JSON files are large and complex.
To see what they look like, either look at the JSON file used to populate the \li{collection} or print any tweet from the database.
The following website also contains useful information about the fields in the JSON file \url{https://dev.twitter.com/overview/api/tweets}.

The \li{distinct} function is also useful in seeing what the possible values are for a given field.

\begin{lstlisting}
# Find all the values in the names field.
>>> col.distinct("name")
<<['Jack', 'Jill', 'John', 'Jeremy']>>
\end{lstlisting}

\begin{problem}
Query the Twitter collection from Problem \ref{prob:mongo-fill-db} for the following information.
\begin{itemize}
    \item How many tweets include the word Russia? Use \li{re.IGNORECASE}.
    \item How many tweets came from one of the main continental US time zones? These are listed as \li{"Central Time (US \& Canada)"}, \li{"Pacific Time (US \& Canada)"}, \li{"Eastern Time (US \& Canada)"}, and \li{"Mountain Time (US \& Canada)"}.
    \item How often did each language occur? Construct a dictionary with each language and it's frequency count.
    \\(Hint: use \li{distinct()} to get the language options.)
\end{itemize}
\end{problem}

\section*{Deleting and Sorting Documents}

Items can be deleted from a database using the same syntax that is used to find them. Use \li{delete_one} to delete just the first item that matches your search, or \li{delete_many} to delete all items that match your search.

\begin{lstlisting}
# Delete the first person from the database whose name is Jack.
>>> col.delete_one({'name':'Jack'})

# Delete everyone from the database whose name is Jack.
>>> col.delete_many({'name':'Jack'})

# Clear the entire collection.
>>> col.delete_many({})
\end{lstlisting}

Another useful function is the \li{sort} function, which can sort the data by some attribute. It takes in the attribute by which the data will be sorted, and then the direction (1 for ascending and -1 for descending). Ascending is the default. The following code is an example of sorting.

\begin{lstlisting}
# Sort the students by name in alphabetic order.
>>> results = col.find().sort('name', 1)
>>> for person in results:
...     print(person['name'])
...
Jack
Jack
Jeremy
Jill
John

# Sort the students oldest to youngest, ignoring those whose age is not listed.
>>> results = col.find({'age': {'$exists': True}}).sort('age', -1)
>>> for person in results:
...    print(person['name'])
...
Jill
Jack
Jack
\end{lstlisting}

\begin{problem}
Query the Twitter collection from Problem \ref{prob:mongo-fill-db} for the following information.
\begin{itemize}
    \item What are the usernames of the 5 most popular (defined as having the most followers) tweeters? Don't include repeats.
    \item Of the tweets containing at least 5 hashtags, sort the tweets by how early the 5th hashtag appears in the text.
    What is the earliest spot (character count) it appears?
    \item What are the coordinates of the tweet that came from the northernmost location?
    Use the latitude and longitude point in \li{"coordinates"}.
\end{itemize}
\end{problem}

\section*{Updating Documents}

Another useful attribute of MongoDB is that data in the database can be updated. It is possible to change values in existing fields, rename fields, delete fields, or create new fields with new values. This gives much more flexibility than a relational database, in which the structure of the databse must stay the same. To update a database, use either \li{update_one} or \li{update_many}, depending on whether one or more documents should be changed (the same as with \li{delete}). Both of these take two parameters;  a find query, which finds documents to change, and the update parameters, telling these things what to update. The syntax is \li{update_many(\{find query\},\{update parameters\})}.

The update parameters must contain update operators. Each update operator is followed by the field it is changing and the value to change it. The syntax is the same as with query operators. The operators are shown in the table below.

\begin{table}[H]
\begin{tabular}{l|l}
Operator & Description \\ \hline
\li{\$inc} , \li{\$mul} & \li{+=}, \li{*=} \\
\li{\$min}, \li{\$max} & \li{min()}, \li{max()}  \\
\hline
\li{\$rename} & Rename a specified field to the given new name \\
\li{\$set} & Assign a value to a specified field (creating the field if necessary) \\
\li{\$unset} & Remove a specified field \\
\hline
\li{\$currentDate} & Set the value of the field to the current date.\\
                   & With \li{"\$type": "date"}, use a \li{datetime} format; \\
                   & with \li{"\$type": "timestamp:}, use a timestamp. \\
\end{tabular}
\caption{MongoDB Update Operators}
\label{table:updateoperators}
\end{table}

\begin{lstlisting}
# Update the first person from the database whose name is Jack to include a
# new field 'lastModified' containing the current date.
>>> col.update_one({'name':'Jack'},
...                {'$currentDate': {'lastModified': {'$type': 'date'}}})

# Increment everyones age by 1, if they already have an age field.
>>> col.update_many({'age': {'$exists': True}}, {'$inc': {'age': 1}})

# Give the first John a new field 'best_friend' that is set to True.
>>> col.update_one({'name':'John'}, {'$set': {'best_friend': True}})
\end{lstlisting}

\begin{problem}
Clean the twitter collection in the following ways.
\begin{itemize}
\item Get rid of the \li{"retweeted_status"} field in each tweet.

\item Update every tweet from someone with at least 1000 followers to include a \li{popular} field whose value is \li{True}.
Report the number of popular tweets.

\item (OPTIONAL) The geographical coordinates used before in \li{coordinates.coordinates} are turned off for most tweets. But many more have a bounding box around the coordinates in the \li{place} field. Update every tweet without coordinates that contains a bounding box so that the coordinates contains the average value of the points that form the bounding box. Make the structure of \li{coordinates} the same as the others, so it contains \li{coordinates} with a longitude, latitude array and a \li{type}, the value of which should be 'Point'.
\\(Hint: Iterate through each tweet in with a bounding box but no coordinates. Then for each tweet, grab it's id and the bounding box coordinates. Find the average, and then update the tweet. To update it search for it's id and then give the needed update parameters. First unset coordinates, and then set coordinates.coordinates and coordinates.type to the needed values.)
\end{itemize}
\end{problem}

\newpage

\section*{Additional Material} % ==============================================

\subsection*{Installation of MongoDB}

MongoDB runs as an isolated program with a path directed to its database storage.
To run a practice MongoDB server on your machine, complete the following steps:

\subsubsection*{Create Database Directory}
To begin, navigate to an appropriate directory on your machine and create a folder called \li{data}.
Within that folder, create another folder called \li{db}.
Make sure that you have read, write, and execute permissions for both folders.

\subsubsection*{Retrieve Shell Files}
To run a server on your machine, you will need the proper executable files from MongoDB.
The following instructions are individualized by operating system.
For all of them, download your binary files from \url{https://www.mongodb.com/download-center?jmp=nav#community}.

\begin{enumerate}
\item For Linux/Mac:

Extract the necessary files from the downloaded package.
In the terminal, navigate into the \texttt{bin} directory of the extracted folder.
You may then start a Mongo server by running in a terminal: \li{./mongod --dbpath /pathtoyourdatafolder}.

\item For Windows:

Go into your Downloads folder and run the Mongo \li{.msi} file.
Follow the installation instructions.
You may install the program at any location on your machine, but do not forget where you have installed it.
You may then start a Mongo server by running in command prompt: C:\textbackslash locationofmongoprogram\textbackslash mongod.exe --dbpath C:\textbackslash pathtodatafolder\textbackslash data\textbackslash db.
\end{enumerate}

MongoDB servers are set by default to run at address:port \li{127.0.0.1:27107} on your machine.

You can also run Mongo commands through a mongo terminal shell.
More information on this can be found at \url{https://docs.mongodb.com/getting-started/shell/introduction/}.

\subsection*{Twitter API}

Pulling information from the Twitter API is simple.
First you must get a Twitter account and register your app with them on \url{apps.twitter.com}.
This will enable you to have a consumer key, consumer secret, access token, and access secret, all required by the Twitter API.

You will also need to install \li{tweepy}, an open source library that allows python to easily work with the Twitter API. This can be installed with pip by running from the command line

\begin{lstlisting}
$pip install tweepy
\end{lstlisting}

The data for this lab was then pulled using the following code on May 26, 2017.

\begin{lstlisting}
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import json

#Set up the databse
client = MongoClient()
mydb = client.db1
twitter = mydb.collection1

f = open('trump.txt','w') #If you want to write to a file

consumer_key = #Your Consumer Key
consumer_secret = #Your Consumer Secret
access_token = #Your Access Token
access_secret = #Your Access Secret

my_auth = OAuthHandler(consumer_key, consumer_secret)
my_auth.set_access_token(access_token, access_secret)

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        try:
            twitter.insert_one(json.loads(data)) #Puts the data into your MongoDB
            f.write(str(data)) #Writes the data to an output file
            return True
        except BaseException as e:
            print(str(e))
            print("Error")
        return True

    def on_error(self, status):
        print(status)
        if status_code == 420: #This means twitter has blocked us temporarily, so we want to stop or they will get mad. Wait 30 minutes or so and try again. Running this code often in a short period of time will cause twitter to block you. But you can stream tweets for as long as you want without any problems.
            return False
        else:
            return True

stream_listener = StreamListener()
stream = tweepy.Stream(auth=my_auth, listener=stream_listener)
stream.filter(track=["trump"]) #This pulls all tweets that include the keyword "trump". Any number of keywords can be searched for.

\end{lstlisting}


\begin{comment} %Commented out code

%Chunk 1
I'm debating whether or not the paragraph is needed. Seems kind of useless.
MongoDB is a document database.
It is best suited for storing data that does not have a fixed schema.
Each MongoDB database is made up of collections of one or more documents.
These documents are a special type of JSON object called BSON (Binary JSON).
For the most part, BSON objects, JSON objects, and Python dictionaries can be used in much the same matter.
However, there are a few subtle differences, such as with special characters.
Trying to use a Python dictionary that contains the `$\$$' character will often throw errors if it is used as though it were a BSON object.

%Chunk 2
We can update documents in a collection using \li{update}.  Note that a simple update acts like a replace.
\begin{lstlisting}
col.update({'name': 'Jack','student': True})
\end{lstlisting}

\begin{problem}
The file \li{mylans_bistro.json} contains a json object describing one additional restaurant.  Insert it into the collection. Note that this entry contains an additional key value not present in any other.  A SQL database would have to be entirely rebuilt to support this insertion, but with MongoDB this is not an issue.

After this insert, use a query to list every restaurant that closes at eighteen o'clock (Mylan's Bistro should be one of these).
\end{problem}

\subsection*{Query Operators}
There are several special operators that we can use to define conditions in a query.

These query operators are used as keys and the queries are values.
\begin{lstlisting}
f = list(col.find({'age': {'$lt': 24}, 'classes': {'$in': ['Art', 'English']}}))
\end{lstlisting}

\begin{problem}
Query your new collection to answer the following questions:
\begin{itemize}
\item How many of the restaurants are in Manhattan?
\item How many restaurants have gotten a grade other than an ``A" on a health inspection?
\item Which are the ten northernmost restaurants?
\item Which restaurants have ``grill" (case-insensitive) in their names?
\end{itemize}
\end{problem}

%Chunk 3
Understand that MongoDB is not a relational database, therefore there is no concept of a join.  This also means that we cannot define database relationships between documents.  We can associate two documents by including a field that contains the unique ObjectID of the other document.  When we request one document, we see it has an ObjectID, and then we run a second query to get the other document.  Any ``relational'' things must be handled by the developer.  This means that a document needs to contain all the information needed to find or retrieve it again.

\begin{problem}
Use update operators to perform the following tasks:
\begin{itemize}
\item Whenever a restaurant has ``grill" in its name, replace ``grill" with ``Magical Fire Table".
\item Increase all of the restaurant IDs by 1000.
\item Delete the entries of every restaurant that has ever gotten a ``C" health inspection grade.
\end{itemize}
\end{problem}


\end{comment}
