\lab{Web Technologies}{Web Technologies}
\objective{The Internet is an umbrella term for the collective grouping of all publicly accessible computer networks in the world.
This collective network can be traversed to access services such as social communication, maps, video streaming, and accessibility to large datasets, all of which are hosted on computers across the world.
Using these technologies requires an understanding of data serialization, data transportation protocols, and how programs such as servers, clients, and APIs are created to facilitate this communication.
}

\section*{Data Serialization} % ==============================================

\emph{Serialization} is the process of packaging data in a form that makes it easy to transmit the data and quickly reconstruct it on another computer or in a different programming language.
One of the most prevalent serialization metalanguages is \emph{JSON}, which stands for \emph{JavaScript Object Notation}.\footnote{Despite having ``JavaScript'' in its name, JSON is a language-independent format. In fact, JSON is frequently used for transmitting data between different programming languages.}
It stores information about objects as a specially formatted string that is easy for both humans and machines to read and write.
\emph{Deserialization} is the process of reconstructing an object from the string.
% When JSON is \emph{deserialized}, this special string is parsed and the objects are reconstructed.

JSON is built on two types of data structures: a collection of key/value pairs and an ordered list of values, similar to Python's built-in \li{dict} and \li{list} structures, respectively.
% The following is a very simple example of the characteristics of a family expressed in JSON.
%
\begin{lstlisting}
{                                   # A family's info written in JSON format.
    "lastname": "Smith",            # The outer dictionary has two keys:
    "children": [                   # "lastname" and "children".
        {                           # The "children" key maps to a list of
            "name": "Timmy",        # two dictionaries, one for each of the
            "age": 8                # two children.
        },
        {
            "name": "Missy",
            "age": 5
        }
    ]
}
\end{lstlisting}

\begin{info}
To see a longer example of what JSON looks like, try opening a Jupyter Notebook (a \li{.ipynb} file) in a plain text editor.
The file lists the Notebook cells, each of which has attributes like \li{"cell_type"} (usually code or markdown) and \li{"source"} (the actual code in the cell).
\end{info}

The JSON libraries of various languages have a fairly standard interface.
The Python standard library module for JSON is called \li{json}; if performance speed is critical, consider using the \li{ujson} or \li{simplejson} modules that are written in C.

% Most JSON libraries support the dump[s]/load[s] interface.
A string written in JSON format that represents a piece of data is called a \emph{JSON message}.
To generate the JSON message for a single Python object, use \li{json.dumps()}.
Alternatively, the function \li{json.dump()} generates the JSON message of an object and writes it to an open file.
To load a JSON string or file, use \li{json.loads()} or \li{json.load()}, respectively.

\begin{lstlisting}
>>> import json

# Store info about a car in a nested dictionary.
>>> my_car = {
...     "car": {
...         "make": "Ford",
...         "color": [255, 30, 30]  },
...     "owner": "me" }

# Get the JSON message corresponding to my_car.
>>> car_str = json.dumps(my_car)
>>> car_str
<<'{"car": {"make": "Ford", "color": [255, 30, 30]}, "owner": "me"}'>>

# Load the JSON message into a Python object, reconstructing my_car.
>>> car_object = json.loads(car_str)
>>> for key in car_object:          # The loaded object is a dictionary.
...     print(key + ':', car_object[key])
...
<<car: {'make': 'Ford', 'color': [255, 30, 30]}
owner: me>>

# Write the car info to an external file.
>>> with open("my_car.json", 'w') as outfile:
...     json.dump(my_car, outfile)
...
# Read the file to check that it saved correctly.
>>> with open("my_car.json", 'r') as infile:
...     new_car = json.load(infile)
...
>>> print(new_car.keys())           # This loaded object is also a dictionary.
<<dict_keys(['car', 'owner'])>>
\end{lstlisting}

\begin{problem} % NYC Restaurant cleanliness data.
The file \texttt{nyc\_traffic.json} contains information about 1000 traffic accidents in New York City during the summer of 2017.\footnote{See \url{https://opendata.cityofnewyork.us/}.}
Each entry lists one or more reasons for the accident, such as ``Unsafe Speed'' or ``Fell Asleep.''

Write a function that loads the data from the JSON file.
Look at the first few entries of the dataset and decide how to gather information about the cause(s) of each accident.
Make a readable, sorted bar chart showing the total number of times that each of the $7$ most common reasons for accidents are listed in the data set.
\\ (Hint: the \li{collections.Counter} data structure may be useful here.)

To check your work, the $6$th most common reason is ``Backing Unsafely,'' listed $59$ times.
\end{problem}

\begin{comment} % Removed because Basemap is just the worst. Except for Bokeh.
\begin{problem} % Analyze LA Water.
% JSON files are often used to package and send data from online database locations.
The file \texttt{LA\_water.json} contains data on water usage in Los Angeles from 2005 through 2012.\footnote{See \url{https://data.lacity.org}.}
The \li{"data"} section of the file contains a list of lists, with each inner list containing some logistic information, a newline, the usage values for the eight fiscal years (8 values), and a list of location information that includes the zip code and GPS coordinates.
The data is organized by zip code (with latitude and longitude), and is measured in hundreds of cubic feet.


Write a function that loads \texttt{LA\_water.json} and plots the water usage of each zip code on a map of Los Angeles.
Plot the zip codes with more average usage over the recorded years as points of larger size or more severe color.

% Each element in the \li{data} key is a list with some logistic information, a newline, the usage values for the eight fiscal years (8 values), and a list of location information that includes the zip code and GPS coordinates.

Use the following code to present the data on a map of Los Angeles via Matplotlib's Basemap tool.

\begin{lstlisting}
from mpl_toolkits.basemap import Basemap

plt.figure(figsize=(9,5))
my_map = Basemap(projection='tmerc', lat_0=34.0522, lon_0=-118.2437,
                    llcrnrlon=-118.7, llcrnrlat=33.8,
                    urcrnrlon=-118.1, urcrnrlat=34.4,
                    resolution='c', epsg=2229)
my_map.arcgisimage(service="ESRI_Imagery_World_2D")

# The 'longs' and 'lats' parameters are the coordinates of zip codes as lists.
x, y = my_map(longs, lats)
# 'averages' is a list of average water use by zip code.
my_map.scatter(x, y, s=averages, c=averages, label='Zip Code')

plt.colorbar(label='Water Use (Hundreds of Cubic Feet)')
plt.title('Water Usage in Los Angeles from 2005-2012')
plt.legend()
plt.show()
\end{lstlisting}
\end{problem}
\end{comment}

\subsection*{Custom Encoders and Decoders for JSON} % -------------------------

The default JSON encoder and decoder do not support serialization for every kind of data structure.
For example, a \li{set} cannot be serialized using only \li{json} functions.
However, the default JSON encoder can be subclassed to handle sets or custom data structures.
A custom encoder must organize the information in an object as nested lists and dictionaries.
The corresponding custom decoder uses the way that the encoder organizes the information to reconstruct the original object.

For example, one way to serialize a \li{set} is to express it as a dictionary with one key that indicates its data type, and another key mapping to the actual data.

\begin{lstlisting}
>>> class SetEncoder(json.JSONEncoder):
...     """A custom JSON encoder for Python sets."""
...     def default(self, obj):
...         if not isinstance(obj, set):
...             raise TypeError("expected a set for encoding")
...         return {"dtype": "set", "data": list(obj)}
...
# Use the custom encoder to convert a set to its custom JSON message.
>>> set_message = json.dumps(set('abca'), cls=SetEncoder)
>>> set_message
<<'{"dtype": "set", "data": ["a", "b", "c"]}'>>

# Define a custom decoder for JSON messages generated by the SetEncoder.
>>> def set_decoder(item):
...     if "dtype" in item:
...         if item["dtype"] != "set" or "data" not in item:
...             raise ValueError("expected a JSON message from SetEncoder")
...         return set(item["data"]
...     raise ValueError("expected a JSON message from SetEncoder")
...
# Use the custom decoder to convert a JSON message to the original object.
>>> json.loads(set_message, object_hook=set_decoder)
<<{'a', 'b', 'c'}>>
\end{lstlisting}

Checks for errors like in the previous example are good practice to ensure that custom encoders and decoders are only used when intended.

\begin{problem}
The following class facilitates a regular $3\times 3$ game of tic-tac-toe, where the boxes in the board have the following coordinates.
\[
\begin{array}{c|c|c}
(0,0) & (0,1) & (0,2) \\ \hline
(1,0) & (1,1) & (1,2) \\ \hline
(2,0) & (2,1) & (2,2)
\end{array}
\]
\begin{lstlisting}
class TicTacToe:
    def __init__(self):
        """Initialize an empty board. The O's go first."""
        self.board = [[' ']*3 for _ in range(3)]
        self.turn, self.winner = "O", None

    def move(self, i, j):
        """Mark an O or X in the (i,j)th box and check for a winner."""
        if self.winner is not None:
            raise ValueError("the game is over!")
        elif self.board[i][j] != ' ':
            raise ValueError("space ({},{}) already taken".<<format>>(i,j))
        self.board[i][j] = self.turn

        # Determine if the game is over.
        b = self.board
        if any(sum(s == self.turn for s in r)==3 for r in b):
            self.winner = self.turn     # 3 in a row.
        elif any(sum(r[i] == self.turn for r in b)==3 for i in range(3)):
            self.winner = self.turn     # 3 in a column.
        elif b[0][0] == b[1][1] == b[2][2] == self.turn:
            self.winner = self.turn     # 3 in a diagonal.
        elif b[0][2] == b[1][1] == b[2][0] == self.turn:
            self.winner = self.turn     # 3 in a diagonal.
        else:
            self.turn = "O" if self.turn == "X" else "X"

    def empty_spaces(self):
        """Return the list of coordinates for the empty boxes."""
        return [(i,j) for i in range(3) for j in range(3)
                                        if self.board[i][j] == ' ' ]
    def __str__(self):
        return "\n---------\n".join(" | ".join(r) for r in self.board)
\end{lstlisting}

Write a custom encoder and decoder for the \li{TicTacToe} class.
If the custom encoder receives anything other than a \li{TicTacToe} object, raise a \li{TypeError}.
\label{prob:tictactoe-serialization}
\end{problem}

\begin{info} % Pickle and other metalanguages.
JSON is a good option for transferring data between two different languages.
Python's \li{pickle} module is particularly good for serialization when the stored object will only be unpacked in Python.
The main functions are almost identical to \li{json.dumps()} and its companions.

\begin{lstlisting}
>>> import pickle

>>> item = pickle.dumps([1, 2, 3, 4, 5, 6])
>>> item
<<b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04K\x05K\x06e.'>>

>>> pickle.loads(item)
[1, 2, 3, 4, 5, 6]
\end{lstlisting}

In addition, there are many other serialization formats such as YAML and XML.
However, JSON is the dominant format for serialization in web applications.
\end{info}

\section*{Servers and Clients} % ==============================================

The Internet is like a network of roads connecting the buildings of a city where each building represents a computer and each road represents the physical wires or wireless pathways that allow for intercommunication.
Navigating the road properly, requires using the correct kinds of vehicles and following the established laws for road travel.
There are also various kinds of vehicles for different purposes and with different capabilities that are used to transport items from building to building.
In a similar fashion, the Internet has specific protocols that allow for standardized communication within and between computers.

The most common communication protocols in computer networks are contained in the Internet Protocol Suite.
Among these is \emph{Transmission Control Protocol} (TCP), used to establish a connection between two computers, exchange bits of information called \emph{packets}, and then close the connection.
% Built for computers on an IP network, TCP allows for a very reliable, ordered, and error-checked stream of data \emph{bytes} (eight binary bits).
More specifically, TCP creates network \emph{socket} objects that are used to send and receive data packets from a computer.
A socket is basically an address within a computer on which a program can send or receive data, like a P.O. box within a post office.
The post office is the computer that receives mail, but the mail is distributed to individual programs that check the P.O. box for their personal communications.
% Though data is normally sent between sockets on two different machines, two sockets on the same machine can also communicate using TCP.
% Using the Python \li{socket} module, we will demonstrate how to create a network socket to listen for incoming data (a \emph{server}), and how to create a second socket to send data (a \emph{client}).

\subsection*{Creating a Server} % ---------------------------------------------

A \emph{server} is a program that interacts with and provides functionality to \emph{client} programs.
A client program contacts a server to receive some sort of response that assists it in fulfilling its function.
Servers are fundamental to modern networks and provide services such as file sharing, authentication, webpage information, databases, etc.

One simple way to create a server in Python is via the \li{socket} module.
The server socket must first be initialized by specifying the type of connection and the address that clients can find the server at.
The server socket then listens and waits for a connection from a client, receives and processes data, then eventually sends a response back to the client.
After exchanges between the server and the client are finished, the server closes the connection to the client.

\begin{lstlisting}
def mirror_server(server_address=("0.0.0.0", 33333)):
    """A server for reflecting strings back to clients in reverse order."""
    print("Starting mirror server on {}".<<format>>(server_address))

    # Specify the socket type, which determines how clients will connect.
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(server_address)    # Assign this socket to an address.
    server_sock.listen(1)               # Start listening for clients.

    while True:
        # Wait for a client to connect to the server.
        print("\nWaiting for a connection...")
        connection, client_address = server_sock.accept()
        try:
            # Receive data from the client.
            print("Connection accepted from {}.".<<format>>(client_address))
            in_data = connection.recv(1024).decode()    # Receive data.
            print("Received '{}' from client".<<format>>(in_data))

            # Process the received data and send something back to the client.
            out_data = in_data[::-1]
            print("Sending '{}' back to the client".<<format>>(out_data))
            connection.sendall(out_data.encode())       # Send data.

        finally:    # Make sure the connection is closed securely.
            connection.close()
            print("Closing connection from {}".<<format>>(client_address))
\end{lstlisting}

The two parameters for \li{socket.socket()} specify the socket type.\footnote{See \url{https://docs.python.org/3/library/socket.html} for details on these parameters.}
The server address is a tuple (host, port).
The host is the IP address, which in this case is \li{"localhost"} or \li{"0.0.0.0"}---the default address that specifies the local machine and allows connections on all interfaces.
The port number is an integer from $0$ to $65535$.
About $250$ port numbers are commonly used, and certain ports have pre-defined uses.
\begin{warn}
Only use port numbers greater than $1023$ to avoid interrupting standard system services.
\end{warn}
% \begin{itemize}
%     \item $0$--$1023$: Special reserved ports
%     \item  $80$, $443$: Web traffic
%     \item $25$, $110$, $143$, $465$: Email servers
% \end{itemize}

After setting up the server socket, it waits for a client to connect.
The \li{accept()} method returns a new socket object (\li{connection}) and the client's address.
Data is received through the connection socket's \li{recv()} method, which takes an integer specifying the number of bits of data to receive.
The data is transferred as a raw byte stream (of type \li{bytes}), so the \li{decode()} method is necessary to translate the data into a string.
Likewise, data that is sent back to the client through the connection socket's \li{sendall()} method must be encoded into a byte stream via the \li{encode()} method.

Finally, the \li{try}-\li{finally} blocks ensure that the connection is always closed securely.
To stop a server, raise a \li{KeyBoardInterrupt} (press \li{ctrl+c}) in the terminal where it is running.

\begin{info}
When running \li{mirror_server()}, the program hangs on the following line.
\begin{lstlisting}
connection, client_address = server_sock.accept()
\end{lstlisting}
This is because the \li{accept()} method does not return until a connection is made with a client.
Therefore, this server program cannot be executed in its entirety without a client.
Client creation is addressed in the next section.
\end{info}

\begin{warn}
It often takes some time for a computer to reopen a port after closing a server connection.
This is due to the timeout functionality of specific protocols that check connections for errors and disruptions.
While testing code, wait a few seconds before running the program again, or use different ports for each test.
\end{warn}

% \begin{table}[H]
% \begin{tabular}{r|l}
%     Method & Description\\
%     \hline
%     \li{bind()}&  Bind the socket to a port and an address.\\
%     \li{listen()} & Start listening for requests.\\
%     \li{accept()} & Accept a connection from a client.\\
%     \li{recv()} & Read and return a block of incoming data.\\
%     \li{sendall()} & Send data to the other end of the connection.\\
%     \li{close()} & Close the socket.\\
%     \li{gethostname()} & Return the host name of the machine.\\
%     \li{getsockname()} & Return the socket's own address.\\
% \end {tabular}
% \caption{Socket Object Methods}
% \end{table}

\begin{problem}
Write a function that accepts a (host, port) tuple and starts up a tic-tac-toe server at the specified location.
Wait to accept a connection, then while the connection is open, repeat the following operations.
\begin{enumerate}
\item Receive a JSON serialized \li{TicTacToe} object (serialized with your custom encoder from Problem \ref{prob:tictactoe-serialization}) from the client.
\item Deserialize the \li{TicTacToe} object using your custom decoder from Problem \ref{prob:tictactoe-serialization}.
\item If the client has just won the game, send \li{"WIN"} back to the client and close the connection.
\item If there is no winner but board is full, send \li{"DRAW"} to the client and close the connection.
\item If the game still isn't over, make a random move on the tic-tac-toe board and serialize the updated \li{TicTacToe} object.
If this move wins the game, send \li{"LOSE"} to the client, then send the serialized object separately (as proof), and close the connection.
Otherwise, send only the updated \li{TicTacToe} object back to the client but keep the connection open.
\end{enumerate}
(Hint: print information at each step so you can see what the server is doing.)

Ensure that the connection closes securely even if an exception is raised.
Note that you will not be able to fully test your server until you have written a client (see Problem \ref{prob:tictactoe-client}).
\label{prob:tictactoe-server}
\end{problem}

\subsection*{Creating a Client} % ---------------------------------------------

The \li{socket} module also has tools for writing client programs.
First, create a socket object with the same settings as the server socket, then call the \li{connect()} method with the server address as a parameter.
Once the client socket is connected to the server socket, the two sockets can transfer information between themselves.

\begin{lstlisting}
def mirror_client(server_address=("0.0.0.0", 33333)):
    """A client program for mirror_server()."""
    print("Attempting to connect to server at {}...".<<format>>(server_address))

    # Set up the socket to be the same type as the server.
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(server_address)    # Attempt to connect to the server.

    # Send some data from the client user to the server.
    out_data = input("Type a message to send to the server: ")
    client_sock.sendall(out_data.encode())              # Send data.

    # Wait to receive a response back from the server.
    in_data = client_sock.recv(1024).decode()           # Receive data.
    print("Received '{}' from the server".<<format>>(in_data))

    # Close the client socket.
    client_sock.close()
\end{lstlisting}

Note that unlike the server socket, the client socket sends and reads the data itself instead of creating a new connection socket.
When the client program is complete, close the client socket.
The server will keep running, waiting for another client to serve.

To see a client and server communicate, open a terminal and run the server, then run the client in a separate terminal.

\begin{lstlisting}
# TERMINAL 1
>>> mirror_server()                 # First start up the server.
Starting mirror server on ('0.0.0.0', 33333)

<<Waiting for a connection...>>         # At this point, start the client.
<<Connection accepted from ('127.0.0.1', 50679).
Received 'racecars and lollipops' from client
Sending 'spopillol dna sracecar' back to the client
Closing connection from ('127.0.0.1', 50679)

Waiting for a connection...>>
# The client program is over, but the server waits to keep serving clients.
\end{lstlisting}

\begin{lstlisting}
# TERMINAL 2
>>> mirror_client()                 # Start the client after the server.
<<Attempting to connect to server at ('0.0.0.0', 33333)...
Connected!
Type a message to send: >><r<racecars and lollipops>r>
<<Received 'spopillol dna sracecar' from the server>>
\end{lstlisting}

\begin{problem}
Write a function that accepts a (host, port) tuple and connects to the tic-tac-toe server at the specified location.
Start by initializing a new \li{TicTacToe} object, then repeat the following steps until the game is over.
\begin{enumerate}
\item Print the board and prompt the player for a move.
Continue prompting the player until they provide valid input.
\item Update the board with the player's move, then serialize it using your custom encoder from Problem \ref{prob:tictactoe-serialization}, and send the serialized version to the server.
\item Receive a response from the server.
If the game is over, congratulate or mock the player appropriately.
If the player lost, receive a second response from the server (the final game board), deserialize it, and print it out.
\end{enumerate}
Close the connection once the game ends.
\label{prob:tictactoe-client}
\end{problem}

\subsection*{APIs}

An \emph{Application Program Interface} (API) is a particular kind of server that listens for requests from authorized users and responds with data.
For example, a list of twenty different locations can be sent with the proper request syntax to a Google Maps API, and it will respond with the calculated driving time from each location to every other.
Every API has \emph{endpoints} where clients send their requests.
Though standards exist for creating and communicating with APIs, most APIs have a unique syntax for authentication and requests that is documented by the organization providing the service.

% In addition to providing services for individual people, APIs allow automated programs to access and use web services.
% For example, some webpages have small windows with an embedded version of Google Maps in them.
% Though the webpages themselves are not managed by Google, they automatically make requests to a Google Maps API to retrieve the data used to display Google Maps in that window.

% There are also APIs which facilitate access to online databases.
% For example, \li{waterUsage.json} used in Problem 1 was retrieved by making an HTTP GET request to \url{https://data.lacity.org/resource/v87k-wgde.json} using the \li{requests} module.
% This URL is the API endpoint for retrieving this dataset in JSON format.

% A list of a few public APIs where datasets can be collected are found at \url{http://catalog.data.gov/dataset?q=-aapi+api+OR++res_format%3Aapi#topic=developers_navigation}.
% More information on the Google Maps APIs can be found at \url{https://developers.google.com/maps/}

\begin{warn}
Each website and API has a policy that specifies appropriate behavior for automated data retrieval and usage.
If data is requested without complying with these requirements, there can be severe legal consequences.
Most websites detail their policies in a file called \emph{robots.txt} on their main page.
See, for example, \url{https://www.google.com/robots.txt}.
\end{warn}


\begin{problem} % Download New York Data.
The \li{requests} module is the standard way to send a download request to an API.
\begin{lstlisting}
>>> import requests
>>> requests.get(endpoint).json()   # Download and extract the data.
\end{lstlisting}

Write a function that makes requests to download data from the following API endpoints managed by New York City.
% \footnote{See \url{https://data.cityofnewyork.us/Environment/Public-Recycling-Bins/sxx4-xhzg} and \url{https://data.cityofnewyork.us/City-Government/NYC-Address-Points/g6pj-hd8k}.}
{\scriptsize
\begin{itemize}
\item Recycling bin locations: https://data.cityofnewyork.us/api/views/sxx4-xhzg/rows.json?accessType=DOWNLOAD
\item Residential addresses: https://data.cityofnewyork.us/api/views/7823-25a9/rows.json?accessType=DOWNLOAD
\end{itemize}}
\noindent Save the recycling data as \texttt{nyc\_recycling.json} and the address data as \texttt{nyc\_addresses.json}.
\label{prob:wt-download-nyc-data}
\end{problem}

\begin{problem} % Analyze New York data.
Write a function that loads the data files generated in Problem \ref{prob:wt-download-nyc-data} but \textbf{does not} call the actual function from Problem \ref{prob:wt-download-nyc-data}.
Determine how close the residential addresses in New York City are to the nearest recycling bin.
\begin{enumerate}
\item Retrieve the latitude and longitude of each recycling bin and, separately, the latitude and longitude of each residential address (ignore entries without these coordinates).
Note carefully that the coordinates for the recycling data are in (latitude, longitude) format, but the coordinates for the address data are in (longitude, latitude) format.
\\(Hint: Both datasets are, at the highest level, dictionaries with two keys: \li{"meta"}, which has information about the data; and \li{"data"}, which has the actual data.
All of the information needed is contained in the \li{"data"} key value.)
\item Load the recycling bin data into a k-d tree.
\label{step:nyc-load-tree}
\item For each address, query the tree to find the distance to the nearest recycling bin, in terms of the coordinates.
\label{step:nyc-query-tree}
\item Plot a histogram of the distances.
\end{enumerate}

For steps \ref{step:nyc-load-tree}--\ref{step:nyc-query-tree}, recall the following syntax for using a k-d tree in SciPy.
\begin{lstlisting}
from scipy.spatial import KDTree

tree = KDTree(data)                         # Initialize the tree.
min_distance, index = tree.query(target)    # Query for a point.
\end{lstlisting}
\label{prob:wt-analyze-nyc-data}
\end{problem}

% The two data sets examined in this Problems \ref{prob:wt-download-nyc-data} and \ref{prob:wt-analyze-nyc-data} have very different data formats.
% Due to the lack of exact standards for data collection and organization, a wide variety of data formats is commonplace.


\begin{comment}
\newpage

\section*{Additional Material} % ==============================================

\subsection*{Other Internet Protocols}

There are many other protocols in the Internet Protocol Suite other than TCP that are used for different purposes.
The Protocol Suite can be divided into four categorical layers:
\begin{enumerate}
\item \textbf{Application}: Software that utilizes transport protocols to move information between computers.
This layer includes protocols important for email, file transfers, and browsing the web.
\item \textbf{Transport}: Protocols that assist in basic high level communication between two computers in areas such as data-streaming, reliability control, and flow control.
\item \textbf{Internet}: Protocols that handle routing, assignment of addresses, and movement of data on a network.
\item \textbf{Link}: Protocols that communicate with local networking hardware such as routers and switches.
\end{enumerate}


Although these examples are simple, every data transfer with TCP follows a similar pattern.
For basic connections, these interactions are simple processes.
However, requesting a webpage would require management of possibly hundreds of connections.
In order to make this more feasible, there are higher level protocols that handle smaller TCP/IP details.
The most predominant of these protocols is HTTP.

\section*{HTTP} % =============================================================

HTTP stands for Hypertext Transfer Protocol, which is an application layer networking protocol.
It is a higher level protocol than TCP but uses TCP protocols to manage connections and provide network capabilities.
%and takes care of many of the small details of TCP for us but relies on underlying TCP protocol to provide network capabilities.
The protocol is centered around a request and response paradigm in which a client makes a request to a server and the server replies with response.
There are several methods, or \emph{requests}, defined for HTTP servers, the three most common of which are GET, POST, and PUT.
GET requests request information from a server, POST requests modify the state of the server, and PUT requests add new pieces of data to the server.

Every HTTP request or response consists of two parts: a header and a body.
The headers contain important information about the request including: the type of request, encoding, and a timestamp.
Custom headers may be added to any request to provide additional information.
The body of the request or response contains the appropriate data or may be empty.

An HTTP connection can be setup in Python by using the standard Python library \li{http}.
Though it is the standard, the process can be greatly simplified by using an additional library called \li{requests}.
The following demonstrates a simple GET request with the \li{http} library.

\begin{lstlisting}
>>> import http
>>> conn = http.client.HTTPConnection("www.example.net") # Establish connection
>>> conn.request("GET", "/") # Send GET request
>>> resp = conn.getresponse() # Server response message
>>> print(resp.status)
<<200>> # A status of 200 is the standard sign for successful communication
>>> print(resp.getheaders())
<<[('Cache-Control', 'max-age=604800'), ... , ('Content-Length', '1270')]>> # Header information about request
>>> print(resp.read())
<<b'<!doctype html>\n<html> ... n</html>\n'>>     # Long string with HTML from webpage
>>> conn.close() # When the request is finished, the connection is closed
\end{lstlisting}

%The above code creates a connection to specific host and then sends a GET request.
%After the host responds, we retrieve the response and check the response message from the server for a status code.
%A status code of $200$ means that everything went alright.
%We can now read the data of the response and then explicitly close the connection.

As previously mentioned, this exchange is greatly simplified by the \li{requests} library:

\begin{lstlisting}
>>> import requests
>>> r = requests.get("http://www.example.net")
>>> print(r.headers)
<<{'Cache-Control': 'max-age=604800', ... , 'Content-Length': '606'}>>
>>> print(r.content)
<<b'<!doctype html>\n<html> ... n</html>\n'>>
\end{lstlisting}

This process is how a web browser (a client program) retrieves a webpage.
It first sends an HTTP request to the web server (a server program) and receives the HTML, CSS, and other code files for a webpage, which are compiled and run in the web browser.

Requests also often include parameters which are keys to tell the server what is being requested or placed.
These parameters can be included in the URL that requests from the server, or in parameters that the \li{requests} library can implement.
For example:

\begin{lstlisting}
>>> r = requests.get("http://httpbin.org/get?key2=value2&key1=value1")
>>> print(r.text)
<< {
  "args": {
    "key1": "value1",
    "key2": "value2"
  },
  ...
  },
  "origin": "128.187.116.7",
  "url": "http://httpbin.org/get?key2=value2&key1=value1"
} >>
>>> r = requests.get("http://httpbin.org/get", params={'key1':'value1','key2':'value2'})
>>> print(r.url)
<< http://httpbin.org/get?key2=value2&key1=value1 >>
>>> print(r.text)
<< {
  "args": {
    "key1": "value1",
    "key2": "value2"
  },
  ...
  },
  "origin": "128.187.116.7",
  "url": "http://httpbin.org/get?key2=value2&key1=value1"
} >>
\end{lstlisting}

\begin{problem}
The file \texttt{waterserver.py} is an example of a simple HTTP server using the Python submodules \li{http.server} and \li{urllib.parse}.
It stores a small sampling of water information from the first problem.
When a client submits a GET request with a query for a particular zip code, the server returns a list of the water usage for that zip code from 2005-2012.

For example, the following code returns the message \li{'[32, 36, 34, 32, 27, 26, 36, 16]'} from the server.

\begin{lstlisting}
# Option 1 - Include query in the URL (? signifies start of query)
r = requests.get("http://localhost:8000?zip=91342").text
# Option 2 - Use requests library to append query to URL
r = requests.get("http://localhost:8000", params={'zip':91342}).text
\end{lstlisting}
All messages from the server are formatted as JSON strings.

Expand the functionality of the server to accept a request with \li{'zip=all'} and return a JSON string of the \li{data} dictionary in \texttt{waterserver.py}.
\end{problem}

A similar format to GET requests can also be used for PUT or POST requests.
These special requests alter the state of the server or send a piece of data to the server, respectively.
In addition, for PUT and POST requests, a data string or dictionary may be sent as a binary stream attachment.
The \li{requests} library attaches these data objects with the \li{data} parameter.
For example:

\begin{lstlisting}
>>> r = requests.put('http://httpbin.org/put', data='{key1:value1,key2:value2}')
>>> print(r.text)
<< {
  "args": {},
  "data": "{key1:value1,key2:value2}",
  "files": {},
  "form": {},
  ...
  "json": null,
  "origin": "128.187.116.7",
  "url": "http://httpbin.org/put"
} >>

\end{lstlisting}

Note that the \li{data} parameter accepts input in the form of a JSON string.

Frequently, when these requests arrive at the server, they are in the form of a binary stream, which can be read with similar notation to the Python \li{open} function.
Below is an example of reading the previous PUT request with a data attachment as a binary stream using \li{read}.

\begin{lstlisting}
>>> data = r.json()['data'] # Retrieve the sent data string
>>> print(data)
<< '{key1:value1,key2:value2}' >>
>>> print(len(data.encode())) # Show the string's length in bytes
<< 25 >>
>>> with open('request.txt', 'w') as file:
>>>         file.write(data) # Write the string to a file
>>> with open('request.txt', 'rb') as file: # Open the file as a binary stream
>>>         file.read(25) # Read the correct number of bytes
<< b'{key1:value1,key2:value2}' >>
\end{lstlisting}

For more information on the \li{requests} library, see the documentation at \url{http://docs.python-requests.org/}.


\begin{problem}
Expand the functionality of your new file from the previous problem to accept a PUT request with attached data as a JSON string.
The inputed string should be loaded and inserted into the \li{data} dictionary as new dictionary keys and values.

Hints: All HTTP server functions must send a status code and a header back to the client.
The class used in \texttt{waterserver.py} has a class attribute named \li{self.rfile} to read data inputs from the client.
The \li{self.rfile} attribute is a buffered binary stream that can be read using the \li{read()} function.
As previously demonstrated, the read function will only read as many bytes as it is instructed to.
Consider using the \li{self.headers['Content-Length']} attribute to find the number of bytes to read.
\end{problem}

These problems have illustrated a simple mechanism for data distribution using the main HTTP requests for website communication.
The file created effectuates an online database that can be requested for information with HTTP protocols and JSON serialization.
%Once run, it will act as an online database that can be requested for information using proper Internet protocols and JSON serialization.

\end{comment}
