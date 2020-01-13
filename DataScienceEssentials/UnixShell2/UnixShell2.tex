\lab{Unix Shell 2}{Unix Shell 2}

\objective{Introduce system management, calling Unix Shell commands within Python, and other advanced topics.
As in the last lab, the majority of learning will not be had in finishing the problems, but in following the examples.
}

\section*{File Security} % ====================================================

To begin, run the following command while inside the \texttt{Shell2/Python/} directory (\texttt{Shell2/} is the end product of \texttt{Shell1/} from the previous lab).
Notice your output will differ from that printed below; this is for learning purposes.

\begin{lstlisting}
$ ls -l
-rw-rw-r-- 1 username groupname 194 Aug  5 20:20 calc.py
-rw-rw-r-- 1 username groupname 373 Aug  5 21:16 count_files.py
-rwxr-xr-x 1 username groupname  27 Aug  5 20:22 mult.py
-rw-rw-r-- 1 username groupname 721 Aug  5 20:23 project.py
\end{lstlisting}

Notice the first column of the output.
The first character denotes the type of the item whether it be a normal file, a directory, a symbolic link, etc.
The remaining nine characters denote the permissions associated with that file.
Specifically, these permissions deal with reading, wrtiting, and executing files.
There are three categories of people associated with permissions.
These are the user (the owner), group, and others.
For example, look at the output for \texttt{mult.py}.
The first character \li{-} denotes that \texttt{mult.py} is a normal file.
The next three characters, \li{rwx} tell us the owner can read, write, and execute the file.
The next three characters \li{r-x} tell us members of the same group can read and execute the file.
The final three characters \li{--x} tell us other users can execute the file and nothing more.

Permissions can be modified using the \li{chmod} command.
There are two different ways to specify permissions, \emph{symbolic permissions} notation and \emph{octal permissions} notation.
Symbolic permissions notation is easier to use when we want to make small modifications to a file's permissions.
See Table \ref{table:symbolic}.

\begin{table}
\begin{tabular}{l|l}
Command & Description
\\ \hline
\li{chmod u+x file1} & Add executing (\li{x}) permissions to user (\li{u}) \\
\li{chmod g-w file1} & Remove writing (\li{w}) permissions from group (\li{g}) \\
\li{chmod o-r file1} & Remove reading (\li{r}) permissions from other other users (\li{o}) \\
\li{chmod a+w file1} & Add writing permissions to everyone (\li{a}) \\
\end{tabular}
\caption{Symbolic permissions notation}
\label{table:symbolic}
\end{table}

Octal permissions notation is easier to use when we want to set all the permissions as once.
The number 4 corresponds to reading, 2 corresponds to writing, and 1 corresponds to executing.
See Table \ref{table:octal}.

\begin{table}
\begin{tabular}{l|l}
Command & Description
\\ \hline
\li{chmod 760 file1} & Sets \li{rwx} to user, \li{rw-} to group, and \li{---} to others \\
\li{chmod 640 file1} & Sets \li{rw-} to user, \li{r--} to group, and \li{---} to others \\
\li{chmod 775 file1} & Sets \li{rwx} to user, \li{rwx} to group, and \li{r-x} to others \\
\li{chmod 500 file1} & Sets \li{r-x} to user, \li{---} to group, and \li{---} to others \\
\end{tabular}
\caption{Octal permissions notation}
\label{table:octal}
\end{table}

The commands in Table \ref{table:chown} are also helpful when working with permissions.

\begin{table}
\begin{tabular}{l|l}
Command & Description
\\ \hline
\li{chown} & change owner \\
\li{chgrp} & change group \\
\li{getfacl} & view all permissions of a file in a readable format. \\
\end{tabular}
\caption{Other commands when working with permissions}
\label{table:chown}
\end{table}

\section*{Scripts} % ==========================================================

A shell script is a series of shell commands saved in a file.
Scripts are useful when we have a process that we do over and over again.
The following is a very simple script.

\begin{lstlisting}
#!/bin/bash
echo "Hello World"
\end{lstlisting}

The first line starts with \li{"#\!"}.
This is called the \emph{shebang} or \emph{hashbang} character sequence.
It is followed by the absolute path to the \li{bash} interpreter.
If we were unsure where the \li{bash} interpreter is saved, we run \li{which bash}.

\begin{problem}
Create a file called \texttt{hello.sh} that contains the previous text and save it in the \texttt{Scripts/} directory.
The file extension \texttt{.sh} is technically unnecessary, but it is good practice to always include an extension.
\end{problem}

To execute a script, type the script name preceded by \li{./}

\begin{lstlisting}
$ cd Scripts
$ ./hello.sh
<<bash: ./hello.sh: Permission denied>>

# Notice you do not have permission to execute this file. This is by default.
$ ls -l hello.sh
-rw-r--r-- 1 username groupname 31 Jul 30 14:34 hello.sh
\end{lstlisting}

\begin{problem}
Add executable permissions to \texttt{hello.sh}.
Run the script to verify that it worked.
\end{problem}

You can do this same thing with Python scripts.
All you have to do is change the path following the shebang.
To see where the Python interpreter is stored, run \li{which python}.

\begin{problem}
The \texttt{Python/} directory contains a file called \texttt{count\_files.py}, a Python script that counts all the files within the \texttt{Shell2/} directory.
Modify this file so it can be run as a script and change the permissions of this script so the user and group can execute the script.
\end{problem}

\begin{info}
If you would like to learn how to run scripts on a set schedule, consider researching \emph{cron jobs}.
\end{info}

\section*{Resource Management} % ==============================================

To be able to optimize performance, it is valuable to always be aware of the resources we are using.
Hard drive space and computer memory are two resources we must constantly keep in mind.
The commands found in Table \ref{table:resource} are essential to managing resources.

\begin{table}
\begin{tabular}{l|l}
Command & Description
\\ \hline
\li{df dir1} & Display available disk space in file system containing \li{dir1} \\
\li{du dir1} & Display disk usage within \li{dir1} [\li{-a}, \li{-h}] \\
\li{free} & Display amount of free and used memory in the system \\
\li{ps} & Display a snapshot of current processes \\
\li{top} & Display interactive list of current processes \\
\end{tabular}
\caption{Commands for resource management}
\label{table:resource}
\end{table}

\section*{Job Control} % ======================================================

Let's say we had a series of scripts we wanted to run.
If we knew that these would take a while to execute, we may want to start them all at the same time and let them run while we are working on something else.
In Table \ref{table:jobs}, we have listed some of the most common commands used in job control.
We strongly encourage you to experiment with these commands.

\begin{table}[H]
\begin{tabular}{l|l}
Command & Description
\\ \hline
\li{COMMAND \&} & Adding an ampersand to the end of a command \\
& runs the command in the background \\
\li{bg \%N} & Restarts the Nth interrupted job in the background \\
\li{fg \%N} & Brings the Nth job into the foreground \\
\li{jobs} & Lists all the jobs currently running \\
\li{kill \%N} & Terminates the Nth job \\
\li{ps} & Lists all the current processes \\
\li{Ctrl-C} & Terminates current job \\
\li{Ctrl-Z} & Interrupts current job \\
\li{nohup} & Run a command that will not be killed if the user logs out \\
\end{tabular}
\caption{Job control commands}
\label{table:jobs}
\end{table}

The \texttt{five\_secs.sh} and \texttt{ten\_secs.sh} scripts in the \texttt{Scripts/} directory take five seconds and ten seconds to execute respectively.
These will be particularly useful as you are experimenting with these commands.


\begin{lstlisting}
# Don't forget to change permissions if needed
$ ./ten_secs.sh &
$ ./five_secs.sh &
$ jobs
[1]+  Running       ./ten_secs.sh &
[2]-  Running       ./five_secs.sh &
$ kill %2
[2]-  Terminated    ./five_secs.sh &
$ jobs
[1]+  Running       ./ten_secs.sh &
\end{lstlisting}

\begin{problem}
In addition to the \texttt{five\_secs.sh} and \texttt{ten\_secs.sh} scripts, the \texttt{Scripts/} folder contains three scripts that each take about forty-five seconds to execute.
Execute each of these commands in the background so all three are running at the same time.
While they are all running, write the output of \li{jobs} to a new file \texttt{log.txt} saved in the \texttt{Scripts/} directory.
\end{problem}

\section*{Using Python for File Management} % =================================

Bash itself has control flow tools like if-else blocks and loops, but most of the syntax is highly unintuitive.
Python, on the other hand, has extremely intuitive syntax for these control flow tools, so using Python to do shell-like tasks can result in some powerful but specific file management programs.
Table \ref{table:shell-to-python} relates some of the common shell commands to Python functions, most of which come from the \li{os} module in the standard library.

\begin{table}
\begin{tabular}{c|l}
Shell Command & Python Function \\ \hline
\li{ls} & \li{os.listdir()} \\
\li{cd} & \li{os.chdir()} \\
\li{pwd} & \li{os.getcwd()} \\
\li{mkdir} & \li{os.mkdir()}, \li{os.mkdirs()} \\
\li{cp} & \li{shutil.copy()} \\
\li{mv} & \li{os.rename()}, \li{os.replace()} \\
\li{rm} & \li{os.remove()}, \li{shutil.rmtree()} \\
\li{du} & \li{os.path.getsize()} \\
\li{chmod} & \li{os.chmod()}
\end{tabular}
\caption{Shell-Python compatibility}
\label{table:shell-to-python}
\end{table}

In addition to these, Python has a few extra functions that are useful for file management and shell commands.
See Table \ref{table:shell2-more-python}.
The two functions \li{os.walk()} and \li{glob.glob()} are especially useful for doing searches like \li{find} and \li{grep}.

\begin{table}[H]
\begin{tabular}{r|l}
Function & Description \\ \hline
\li{os.walk()} & Iterate through the subfolders of a given directory. \\
\li{os.path.isdir()} & Return \li{True} if the input is a directory. \\
\li{os.path.isfile()} & Return \li{True} if the input is a file. \\
\li{os.path.join()} & Join several folder names or file names into one path. \\
\li{glob.glob()} & Return a list of file names that match a pattern. \\
\li{subprocess.call()} & Execute a shell command.\\
\li{subprocess.check_output()} & Execute a shell command and return its output as a string.
\end{tabular}
\caption{Other useful Python functions for shell operations.}
\label{table:shell2-more-python}
\end{table}

\begin{lstlisting}
>>> import os
>>> from glob import glob

# Get the names of all Python files in the Python/ directory.
>>> glob("Python/*.py")
<<['Python/calc.py',
 'Python/count_files.py',
 'Python/mult.py',
 'Python/project.py']>>

# Get the names of all .jpg files in any subdirectory.
>> glob("**/*.jpg", recursive=True)
<<['Photos/IMG_1501.jpg',
 'Photos/IMG_1510.jpg',
 'Photos/IMG_1595.jpg',
 'Photos/img_1796.jpg',
 'Photos/img_1842.jpg',
 'Photos/img_1879.jpg',
 'Photos/img_1987.jpg',
 'Photos/IMG_2044.jpg',
 'Photos/IMG_2164.jpg',
 'Photos/IMG_2182.jpg',
 'Photos/IMG_2379.jpg',
 'Photos/IMG_2464.jpg',
 'Photos/IMG_2679.jpg',
 'Photos/IMG_2746.jpg']>>

# Walk through the directory, looking for .sh files.
>>> for directory, subdirectories, files in os.walk('.'):
...     for filename in files:
...         if filename.endswith(".sh"):
...             print(os.path.join(directory, filename))
...
./Scripts/five_secs.sh
./Scripts/script1.sh
./Scripts/script2.sh
./Scripts/script3.sh
./Scripts/ten_secs.sh
\end{lstlisting}

\begin{problem}
Write a Python function \li{grep()} that accepts the name of target string and a file pattern.
Find all files in the current directory or its subdirectories that match the file pattern, then determine which ones contain the target string.
For example, \li{grep("*.py", "range(")} should search Python files for the command \li{range(}.

Validate your function by comparing it to \li{grep -lR} in the shell.
\end{problem}

The \li{subprocess} module allows Python to execute actual shell commands in the current working directory.
Use \li{subprocess.call()} to run a Unix command, or \li{subprocess.check_output()} to run a Unix command and record its output.

\begin{lstlisting}
$ cd Shell2/Scripts
$ python
>>> import subprocess
>>> subprocess.call(["ls", "-l"])
total 40
-rw-r--r--  1 username  groupname  20 Aug 26  2016 five_secs.sh
-rw-r--r--  1 username  groupname  21 Aug 26  2016 script1.sh
-rw-r--r--  1 username  groupname  21 Aug 26  2016 script2.sh
-rw-r--r--  1 username  groupname  21 Aug 26  2016 script3.sh
-rw-r--r--  1 username  groupname  21 Aug 26  2016 ten_secs.sh
0                               # decode() translates the result to a string.
>>> file_info = subprocess.check_output(["ls", "-l"]).decode()
>>> file_info.split('\n')
<<['total 40',
 '-rw-r--r--  1 username  groupname  20 Aug 26  2016 five_secs.sh',
 '-rw-r--r--  1 username  groupname  21 Aug 26  2016 script1.sh',
 '-rw-r--r--  1 username  groupname  21 Aug 26  2016 script2.sh',
 '-rw-r--r--  1 username  groupname  21 Aug 26  2016 script3.sh',
 '-rw-r--r--  1 username  groupname  21 Aug 26  2016 ten_secs.sh',
 '']>>
\end{lstlisting}

\begin{warn}
Be extremely careful when creating a shell process from Python.
If the commands depend on user input, the program is vulnerable to a \emph{shell injection attack}.
For example, consider the following function.
\begin{lstlisting}
>>> def inspect_file(filename):
...     """Return information about the specified file from the shell."""
...     return subprocess.check_output(["ls", "-l", filename]).decode()
\end{lstlisting}
If \li{inspect_file()} is given the input \li{".; rm -rf /"}, then \li{ls -l .} is executed innocently, and then \li{rm -rf /} destroys the computer.\footnote{See \url{https://en.wikipedia.org/wiki/Code_injection\#Shell_injection} for more example attacks.}
Be careful not to execute a shell command from within Python in a way that a malicious user could potentially take advantage of.
\end{warn}

% TODO: piping with subprocess.Popen().

\begin{problem}
Write a Python function that accepts an integer $n$.
Search the current directory and all subdirectories for the $n$ largest files.
Return a list of filenames, in order from largest to smallest.
\\(Hint: the shell commands \li{ls -s} and \li{du} show the file size.)
\end{problem}

\section*{Downloading Files} % ------------------------------------------------

The Unix shell has tools for downloading files from the internet.
The most popular are \li{wget} and \li{curl}.
At its most basic, \li{curl} is the more robust of the two while \li{wget} can download recursively.

When we want to download a single file, we just need the URL for the file we want to download.
This works for PDF files, HTML files, and other content simply by providing the right URL.

\begin{lstlisting}
$ wget https://github.com/Foundations-of-Applied-Mathematics/Data/blob/master/Volume1/dream.png
\end{lstlisting}
%$

The following are also useful commands using \li{wget}.

\begin{lstlisting}
# Download files from URLs listed in urls.txt
$ wget -i list_of_urls.txt

# Download in the background
$ wget -b URL

# Download something recursively
$ wget -r --no-parent URL
\end{lstlisting}
%$

\begin{problem}
The file \texttt{urls.txt} in the \texttt{Documents/} directory contains a list of URLs.
Download the files in this list using \li{wget} and move them to the \texttt{Photos/} directory.

When you finish this problem, archive and compress your entire \texttt{Shell2/} directory and save it as \texttt{ShellFinal.tar.gz}.
Include the \li{-p} flag on \li{tar} to preserve the file permissions.
\\(Hint: see the previous lab for a refresher on \li{tar}.
See also \url{https://xkcd.com/1168/}.)
\end{problem}

\section*{One Final Note} % ===================================================

Though there are multiple Unix shells, one of the most popular is the \emph{bash} shell.
The bash shell is highly customizable.
In your home directory, you will find a hidden file named \texttt{.bashrc}.
All customization changes are saved in this file.
If you are interested in customizing your shell, you can customize the prompt using the \li{PS1} environment variable.
As you become more and more familiar with the Unix shell, you will come to find there are commands you run over and over again.
You can save commands you use frequently using \li{alias}.
If you would like more information on these and other ways to customize the shell, you can find many quality reference guides and tutorials on the internet.

% TODO: move this to a "Customizing the Shell" subsection of Additional Material.

\newpage

\section*{Additional Material} % ==============================================

\subsection*{sed and awk} % ---------------------------------------------------

\li{sed} and \li{awk} are two different scripting languages in their own right.
Like Unix, these languages are easy to learn but difficult to master.
It is very common to combine Unix commands and \li{sed} and \li{awk} commands.
We will address the basics, but if you would like more information see <http://www.theunixschool.com/p/awk-sed.html>

\subsection*{Printing Specific Lines Using sed} % -----------------------------

We have already used the \li{head} and \li{tail} commands to print the beginning and end of a file respectively.
What if we wanted to print lines $30$ to $40$, for example?
We can accomplish this using \li{sed}.
In the \texttt{Documents/} folder, you will find the \texttt{lines.txt} file.
We will use this file for the following examples.

\begin{lstlisting}
# Same output as head -n3
$ sed -n 1,3p lines.txt
line 1
line 2
line 3

# Same output as tail -n3
$ sed -n 3,5p lines.txt
line 3
line 4
line 5

# Print lines 2-4
$ sed -n 3,5p lines.txt
line 2
line 3
line 4

# Print lines 1,3,5
$ sed -n -e 1p -e 3p -e 5p lines.txt
line 1
line 3
line 5
\end{lstlisting}

\subsection*{Find and Replace Using sed} % ------------------------------------

Using \li{sed}, we can also perform find and replace.
We can perform this function on the output of another commmand or we can perform this function in place on other files.
The basic syntax of this \li{sed} command is the following.

\begin{lstlisting}
sed s/str1/str2/g
\end{lstlisting}

This command will replace every instance of \li{str1} with \li{str2}. More specific examples follow.

\begin{lstlisting}
$ sed s/line/LINE/g lines.txt
LINE 1
LINE 2
LINE 3
LINE 4
LINE 5

# Notice the file didn't change at all
$ cat lines.txt
line 1
line 2
line 3
line 4
line 5

# To save the changes, add the -i flag
$ sed -i s/line/LINE/g lines.txt
$ cat lines.txt
LINE 1
LINE 2
LINE 3
LINE 4
LINE 5
\end{lstlisting}

\subsection*{Formatting output using awk} % -----------------------------------

Earlier in this lab we mentioned \li{ls -l} and as we have seen, this outputs lots of information.
Using \li{awk}, we can select which fields we wish to print.
Suppose we only cared about the file name and the permissions.
We can get this output by running the following command.

\begin{lstlisting}
$ ls -l | awk ' {print $1, $9} '
\end{lstlisting}
%$

Notice we pipe the output of \li{ls -l} to \li{awk}.
When calling a command using \li{awk}, we use quotation marks.
Note it is a common mistake to forget to add these quotation marks.
Inside these quotation marks, commands always take the same format.

\begin{lstlisting}
awk ' <options> {<actions>} '
\end{lstlisting}

In the remaining examples we will not be using any of the options, but we will address various actions.
For those interested in learning what options are available see <http://www.theunixschool.com/p/awk-sed.html>.

In the \texttt{Documents/} directory, you will find a \texttt{people.txt} file that we will use for the following examples.
In our first example, we use the \li{print} action.
The \li{\$1} and \li{\$9} mean that we are going to print the first and ninth fields.
Beyond specifying which fields we wish to print, we can also choose how many characters to allocate for each field.

\begin{lstlisting}
# contents of people.txt
$ cat people.txt
male,John,23
female,Mary,31
female,Sally,37
male,Ted,19
male,Jeff,41
female,Cindy,25

# Change the field separator (FS) to "," at the beginning of execution (BEGIN)
# By printing each field individually proves we have successfully separated the fields
$ awk ' BEGIN{ FS = "," }; {print $1,$2,$3} ' < people.txt
male John 23
female Mary 31
female Sally 37
male Ted 19
male Jeff 41
female Cindy 25

# Format columns using printf so everything is in neat columns in order (gender,age,name)
$ awk ' BEGIN{ FS = ","}; {printf "%-6s %2s %s\n", $1,$3,$2} ' < people.txt
male   23 John
female 31 Mary
female 37 Sally
male   19 Ted
male   41 Jeff
female 25 Cindy
\end{lstlisting}

The statement \li{"\%-6s \%2s \%s\\n"} formats the columns of the output.
This says to set aside six characters left justied, then two characters right justified, then print the last field to its full length.

\begin{comment}
\begin{problem}
Inside the \texttt{Documents/} directory, you should find a file named \texttt{files.txt}.
This file contains details on approximately one hundred files.
The different fields in the file are separated by tabs.
Using \li{awk}, \li{sort}, pipes, and redirects, write a file named \texttt{date\_modified.txt} with the following specifications:
\begin{itemize}
\item in the first column, print the date the file was modified
\item in the second column, print the name of the file
\item sort the file from newest to oldest based on the date last modified
\end{itemize}
All this can be accomplished using one command.
\end{problem}
\end{comment}

We have barely scratched the surface of what \li{awk} can do.
Performing an internet search for "awk one-liners" will give you many additional examples of useful commands you can run using \li{awk}.

\section*{System Management} % ================================================

In this section, we will address some of the basics of system management.
As an introduction, the commands in Table \ref{table:systemadmin} are used to learn more about the computer system.

\begin{table}[H]
\begin{tabular}{l|l}
Command & Description
\\ \hline
\li{passwd} & Change user password \\
\li{uname} & View operating system name \\
\li{uname -a} & Print all system information \\
\li{uname -m} & Print machine hardware \\
\li{w} & Show who is logged in and what they are doing \\
\li{whoami} & Print userID of current user \\
\end{tabular}
\caption{Commands for system administration.}
\label{table:systemadmin}
\end{table}

\subsection*{Secure Shell} % --------------------------------------------------

Let's say you are working for a company with a file server.
Hundreds of people need to be able to access the content of this machine, but how is that possible?
Or say you have a script to run that requires some serious computing power.
How are you going to be able to access your company's super computer to run your script?
We do this through \emph{Secure Shell} (SSH).

SSH is a network protocol encrypted using public-key cryptography.
The system we are connecting \emph{to} is commonly referred to as the \emph{host} and the system we are connecting \emph{from} is commonly referred to as the \emph{client}.
Once this connection is established, there is a secure tunnel through which commands and files can be exchanged between the client and host.
To end a secure connection, type \li{exit}.

As a warning, you cannot normally SSH into a Windows machine.
If you want to do this, search on the web for available options.

\begin{lstlisting}
$ whoami    # use this to see what your current login is
client_username
$ ssh my_host_username@my_hostname

# You will then be prompted to enter the password for my_host_username

$ whoami    # use this to verify that you are logged into the host
my_host_username

$ hostname
my_hostname

$ exit
logout
Connection to my_host_name closed.
\end{lstlisting}
%$

Now that you are logged in on the host computer, all the commands you execute are as though you were executing them on the host computer.

\subsection*{Secure Copy} % ---------------------------------------------------

When we want to copy files between the client and the host, we use the \emph{secure copy} command, \li{scp}.
The following commands are run when logged into the client computer.

\begin{lstlisting}
# copy filename to the host's system at filepath
$ scp filename host_username@hostname:filepath

#copy a file found at filepath to the client's system as filename
$ scp host_username@hostname:filepath filename

# you will be prompted to enter host_username's password in both these instances
\end{lstlisting}

\begin{comment}
\begin{problem}
You will either need a partner for this problem or have access to a username on another computer.
Experiment with SSH. Verify that you can connect from a client to a host.
Copy a few files between the host and the client.
\end{problem}
\end{comment}

\subsection*{Generating SSH Keys (Optional)} % --------------------------------

If there is a host that we access on a regular basis, typing in our password over and over again can get tedious.
By setting up SSH keys, the host can identify if a client is a trusted user without needing to type in a password.
If you are interested in experimenting with this setup, a Google search of "How to set up SSH keys" will lead you to many quality tutorials on how to do so.
