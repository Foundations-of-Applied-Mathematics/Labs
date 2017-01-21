\lab{Unix Shell 1: Introduction}{Introduction to the Unix Shell}
\label{lab:Shell}
\objective{Explore the basics of the Unix Shell. Understand how to navigate and manipulate file directories. Introduce the Vim text editor for easy writing and editing of text or other similar documents.}

% TODO:
% - Organize some paragraphs / problem statements into tables.
% - Problem or demonstration using `cat' or `less'
% - If more content in the Problems is needed, in Problem 6, we could add:
%     "edit count_files.py to exclude the files in the test/ directory"

Unix was first developed by AT\&T Bell Labs in the 1970s. In the 1990s, Unix became the foundation of Linux and MacOSX.
The Unix shell is an interface for executing commands to the operating system.
The majority of servers are Linux based, so having a knowledge of Unix shell commands allows us to interact with these servers.

As you get into Unix, you will find it is easy to learn but difficult to master.
We will build a foundation of simple file system management and a basic introduction to the Vim text editor.
We will address some of the basics in detail and also include lists of commands that interested learners are encouraged to research further.

\begin{info} % Windows sucks.
Windows is not built off of Unix, but it does come with a command line tool.
We will not cover the equivalent commands in Windows command line, but you could download a Unix-based shell such as Git Bash or Cygwin to complete this lab (you will still lose out on certain commands).
\end{info}

\section*{File System} % ======================================================

\begin{warn}
In this lab you will work with files on your computer. Be careful as you go through each problem and as you experiment on your own.
Be sure you are in the right directories and subfolders before you start creating and deleting files; some actions are irreversible.
\end{warn}

\subsection*{Navigation} % ----------------------------------------------------

Typically you have probably navigated your comptuer by clicking on icons to open directories and programs.
In the terminal, instead of point and click we use typed commands to move from directory to directory.

Begin by opening the Terminal. The text you see in the upper left of the Terminal is called the \emph{prompt}.
As you navigate through the file system you will want to know \emph{where} you are so that you know you aren't creating or deleting files in the wrong locations.

To see what directory you are currently working in, type \li{pwd} into the prompt.
This command stands for \textbf{p}rint \textbf{w}orking \textbf{d}irectory, and as the name suggests it prints out the string of your current location.

Once you know where you are, you'll want to know where you can move.
The \li{ls}, or \textbf{l}ist \textbf{s}egments, command will list all the files and directories in your current folder location.
Try typing it in.

When you know what's around you, you'll want to navigate directories.
The \li{cd}, or \textbf{c}hange \textbf{d}irectory, command allows you to move through directories.
To change to a new directory, type the \li{cd} command followed by the name of the directory to which you want to move (if you cd into a file, you will get an error).
You can move up one directory by typing \li{cd ..}.

Two important directories are the root directory and the home directory.
You can navigate to the home directory by typing \li{cd} $\thicksim$ or just \li{cd}.
You can navigate to root by typing \li{cd /}.

\begin{problem}
Using these commands, navigate to the \texttt{Shell1/} directory provided with this lab. We will use this directory for the remainder of the lab. Use the \li{ls} command to list the contents of this directory. NOTE: You will find a directory within this directory called \texttt{Test/} that is availabe for you to experiment with the concepts and commands found in this lab. The other files and directories are necessary for the exercises we will be doing, so take care not to modify them.
\end{problem}

\subsection*{Getting Help} % --------------------------------------------------

As you go through this lab, you will come across many commands with functionality beyond what is taught here.
The Terminal has two nice commands to help you with these commands.
The first is \li{man <command>}, which opens the manual page for the command following \li{man}.
Try typing in \li{man ls}; you will see a list of the name and description of the \li{ls} command, among other things.
If you forget how to use a command the manual page is the first place you should check to remember.

The \li{apropos <keyword>} command will list all Unix commands that have \li{<keyword>} contained somewhere in their manual page names and descriptions.
For example, if you forget how to copy files, you can type in \li{apropos copy} and you'll get a list of all commands that have \li{copy} in their description.

\subsection*{Flags} % ---------------------------------------------------------

When you typed in \li{man ls} up above, you may have noticed several options listed in the description, such as \li{-a}, \li{-A}, \li{--author}.
These are called flags and change the functionality of commands.
Most commands will have flags that change their behavior.
Table \ref{table:ls_flags} contains some of the most common flags for the \li{ls} command.

\begin{table}
\begin{tabular}{l|l}
    Flags & Description
    \\ \hline
    \li{-a} & Do not ignore hidden files and folders \\
    \li{-l} & List files and folders in long format \\
    \li{-r} & Reverse order while sorting \\
    \li{-R} & Print files and subdirectories recursively \\
    \li{-s} & Print item name and size \\
    \li{-S} & Sort by size \\
    \li{-t} & Sort output by date modified \\
\end{tabular}
\caption{Common flags of the \li{ls} command.}
\label{table:ls_flags}
\end{table}

Multiple flags can be combined as one flag.
For example, if we wanted to list all the files in a directory in long format sorted by date modified, we would use \li{ls -a -l -t} or \li{ls -alt}.

\subsection*{Manipulating Files and Directories} % ----------------------------

% TODO: make a table here.

In this section we will learn how to create, copy, move, and delete files and folders.
Before you begin, \li{cd} into the \texttt{Test/} directory in \texttt{Shell1/}.

To create a text file, use \li{touch <filename>}.
To create a new directory, use \li{mkdir <dir_name>}.

To copy a file into a directory, use \li{cp <filename> <dir_name>}.
When making a copy of a directory, the command is similar but must use the \li{-r} flag.
This flag stands for recursively copying files in subdirectories.
If you try to copy a file without the \li{-r} the command will return an error.

Moving files and directories follows a similar format, except no \li{-r} flag is used when moving one directory into another.
The command \li{mv <filename> <dir_name>} will move a file to a folder and \li{mv <dir1> <dir2>} will move the first directory into the second.
If you want to rename a file, use \li{mv <file_old> <file_new>}; the same goes for directories.

When deleting files, use \li{rm <filename>}, or \li{rm -r <dir_name>} when deleting a directory.
Again, the \li{-r} flag tells the Terminal to recursively remove all the files and subfolders within the targeted directory.

If you want to make sure your command is doing what you intend, the \li{-v} flag tells \li{rm}, \li{cp}, or \li{mkdir} to have the Terminal print strings of what it is doing.
When your Terminal gets too cluttered, use \li{clear} to clean it up.

Below is an example of all these commands in action.

\begin{lstlisting}[language=bash]
$ cd Test
$ touch data.txt				# create new empty file data.txt
$ mkdir New						# create directory New
$ ls							# list items in test directory
New 	data.txt
$ cp data.txt New/				# copy data.txt to New directory
$ cd New/						# enter the New directory
$ ls							# list items in New directory
data.txt
$ mv data.txt new_data.txt		# rename data.txt new_data.txt
$ ls							# list items in New directory
new_data.txt
$ cd ..							# Return to test directory
$ rm -rv New/					# Remove New directory and its contents
removed 'New/data.txt'
removed directory: 'New/'
$ clear							# Clear terminal screen
\end{lstlisting}

Table \ref{table:other_commands} contains all the commands we have discussed so far.
Notice the common flags are contained in square brackets; use \li{man} to see what these mean.

\begin{table}
\begin{tabular}{l|l}
    Commands & Description
    \\ \hline
    \li{clear} & Clear the terminal screen \\
    \li{cp file1 dir1} & Create a copy of \texttt{file1} and move it to \texttt{dir1/}\\
    \li{cp file1 file2} & Create a copy of \texttt{file1} and name it \texttt{file2} \\
    \li{cp -r dir1 dir2} & Create a copy of
    \texttt{dir1/} and all its contents into \texttt{dir2/} \\
    \li{mkdir dir1} & Create a new directory named \texttt{dir1/} \\
    \li{mkdir -p path/to/new/dir1} & Create \texttt{dir1/} and all intermediate directories \\
    \li{mv file1 dir1} & Move \texttt{file1} to \texttt{dir1/} \\
    \li{mv file1 file2} & Rename \texttt{file1} as \texttt{file2} \\
    \li{rm file1} & Delete \texttt{file1} [\li{-i}, \li{-v}] \\
    \li{rm -r dir1} & Delete \texttt{dir1/} and all items within \texttt{dir1/} [\li{-i}, \li{-v}] \\
    \li{touch file1} & Create an empty file named \texttt{file1} \\
\end{tabular}
\caption{The commands discussed in this section.}
\label{table:other_commands}
\end{table}

\begin{problem}
Inside the \texttt{Shell1/} directory, delete the \texttt{Audio/} folder along with all its contents.
Create \texttt{Documents/}, \texttt{Photos/}, and \texttt{Python/} directories.
\end{problem}

\subsection*{Wildcards} % -----------------------------------------------------

As we are working in the file system, there will be times that we want to perform the same command to a group of similar files.
For example, if you needed to move all text files within a directory to a new directory.
Rather than copy each file one at a time, we can apply one command to several files using \emph{wildcards}.
We will use the \li{*} and \li{?} wildcards.
The \li{*} wildcard represents any string and the \li{?} wildcard represents any single character.
Though these wildcards can be used in almost every Unix command, they are particularly useful when dealing with files.

\begin{lstlisting}[language=bash]
$ ls
File1.txt	File2.txt	File3.jpg	text_files
$ mv -v *.txt text_files/
File1.txt -> text_files/File1.txt
File2.txt -> text_files/File2.txt
$ ls
File3.jpg	text_files
\end{lstlisting}

See Table \ref{table:wildcards} for examples of common wildcard usuage.

\begin{table}
\begin{tabular}{l|l}
    Command & Description
    \\ \hline
    \li{*.txt} & All files that end with \texttt{.txt}. \\
    \li{image*} & All files that have \texttt{image} as the first 5 characters. \\
    \li{*py*} & All files that contain \texttt{py} in the name. \\
    \li{doc*.txt} & All files of the form \texttt{doc1.txt}, \texttt{doc2.txt}, \texttt{docA.txt}, etc. \\
\end{tabular}
\caption{Common uses for wildcards.}
\label{table:wildcards}
\end{table}

\begin{problem}
Within the \texttt{Shell1/} directory, there are many files.
We will organize these files into directories.
Using wildcards, move all the \texttt{.jpg} files to the \texttt{Photos/} directory, all the \texttt{.txt} files to the \texttt{Documents/} directory, and all the \texttt{.py} files to the \texttt{Python/} directory.
You will see a few other folders in the \texttt{Shell1/} directory.
Do not move any of the files within these folders at this point.
\end{problem}

\subsection*{Displaying File Contents} % --------------------------------------

When using the file system, you may be interested in checking file content to be sure you're looking at the right file.
Several commands are made available for ease in reading file content.

The \li{cat} command, followed by the filename will display all the contents of a file on the screen.
If you are dealing with a large file, you may only want to view a certain number of lines at a time.
Use \li{less <filename>} to restrict the number of lines that show up at a time.
Use the arrow keys to navigate up and down.
Press \textbf{q} to exit.

For other similar commands, look at table \ref{table:print}.

\begin{table}
\begin{tabular}{l|l}
    Command & Description
    \\ \hline
    \li{cat} & Print the contents of a file in its entirety \\
    \li{more} & Print the contents of a file one page at a time \\
    \li{less} & Like more, but you can navigate forward and backward \\
    \li{head} & Print the first 10 lines of a file \\
    \li{head -nK} & Print the first \li{K} lines of a file \\
    \li{tail} & Print just the last 10 lines of a file \\
    \li{tail -nK} & Print the last \li{K} lines of a file \\
\end{tabular}
\caption{Commands for printing contents of a file}
\label{table:print}
\end{table}

\begin{comment} % TODO: this problem.
\begin{problem}
We should have an exercise (or demonstration) here where they use cat or less to look at a file, just to make sure they do it.
I don't have access to the toy directory, so I don't know the filenames to write one myself.
It should only take 5 minutes though.
\end{problem}
\end{comment}

\subsection*{Searching the File System} % -------------------------------------

There are two commands we use for searching through our directories.
The \li{find} command is used to find files or directories in a directory hierarchy.
The \li{grep} command is used to find lines matching a string.
More specifically, we can use \li{grep} to find words inside files.
We will provide a basic template in Table \ref{table:find} for using these two commands and leave it to you to explore the uses of the other flags.
The \li{man} command can help you learn about them.

\begin{problem}
In addition to the \texttt{.jpg} files you have already moved into the \texttt{Photot/} folder, there are a few other \texttt{.jpg} files in a few other folders within the \texttt{Shell1/} directory.
Find where these files are using the \li{find} command and move them to the \texttt{Photos/} folder.
\end{problem}

\begin{table}
\begin{tabular}{l|l}
    Command & Description
    \\ \hline
    \li{<<find dir1 -type f -name "word">>} &  Find all files in \texttt{dir1/} (and its subdirectories) called \texttt{word} \\
    & (\li{<<-type f>>} is for files; \li{<<-type d>>} is for directories) \\
    \li{<<grep "word" filename>>} & Find all occurences of \li{word} within \texttt{filename} \\
    \li{grep -nr <<"word" dir1>>} & Find all occurences of \li{word} within the files inside \texttt{dir1/} \\
     & (\li{-n} lists the line number; \li{-r} performs a recursive search)\\
\end{tabular}
\caption{Commands using \li{find} and \li{grep}.}
\label{table:find}
\end{table}

\subsection*{Pipes and Redirects} % -------------------------------------------

Terminal commands can be combined using \emph{pipes}.
When combined, or \emph{piped}, the output of one command is passed to the another.
Two commands are piped together using the \li{|} operator.
To demonstrate pipes we will first introduce commands that allow us to view the contents of a file in Table \ref{table:print}.

In the first example below, the \li{cat} command output is piped to \li{wc -l}.
The \li{wc} command stands for \textbf{w}ord \textbf{c}ount.
This command can be used to count words or lines.
The \li{-l} flag tells the \li{wc} command to count lines.
Therefore, this first example counts the number of lines in \texttt{assignments.txt}.
In the second example below, the command lists the files in the current directory sorted by size in descending order. For details on what the flags in this command do, consult \li{man sort}.

\begin{lstlisting}[language=bash]
$ cd Shell1/Files/Feb
$ cat assignments.txt | wc -l
9

$ ls -s | sort -nr
12 project3.py
12 project2.py
12 assignments.txt
 4 pics
total 40
\end{lstlisting}

In the previous example, we pipe the contents of \texttt{assignments.txt} to \li{wc -l} using \li{cat}.
When working with files specifically, you can also use \emph{redirects}.
The \li{<} operator gives a file to a Terminal command.
The same output from the first example above can be achieved by running the following command:

\begin{lstlisting}[language=bash]
$ wc -l < assignments.txt
9
\end{lstlisting}

If you are wanting to save the resulting output of a command to a file, use \li{>} or \li{>>}.
The \li{>} operator will overwrite anything that may exist in the output file whereas \li{>>} will append the output to the end of the output file.
For example, if we want to append the number of lines in \texttt{assignments.txt} to \texttt{word\_count.txt}, we would run the following commmand:

\begin{lstlisting}[language=bash]
$ wc -l < assignements.txt >> word_count.txt
\end{lstlisting}

Since \li{grep} is used to print lines matching a pattern, it is also very useful to use in conjunction with piping.
For example, \li{ls -l | grep root} prints all files associated with the root user.

\begin{problem}
The \texttt{words.txt} file in the \texttt{Documents/} directory contains a list of words that are not in alphabetical order.
Write the number of words in \texttt{words.txt} and an alphabetically sorted list of words to \texttt{sortedwords.txt} using pipes and redirects.
Save this file in the \texttt{Documents/} directory.
Try to accomplish this with a total of two commands or fewer.
\end{problem}

\section*{Archiving and Compression}
In file management, the terms archiving and compressing are commonly used interchangeably.
However, these are quite different.
To archive is to combine a certain number of files into one file.
The resulting file will be the same size as the group of files that were archived.
To compress is to take a file or group of files and shrink the file size as much as possible.
The resulting compressed file will need to be extracted before being used.

The \li{ZIP} file format is the most popular for archiving and compressing files.
If the \li{zip} Unix command is not installed on your system, you can download it by running \li{sudo apt-get install zip}.
Note that you will need to have administrative rights to download this package.
To unzip a file, use \li{unzip}.

\begin{lstlisting}[language=bash]
$ cd Shell1/Documents
$ zip zipfile.zip doc?.txt
 adding: doc1.txt (deflated 87%)
 adding: doc2.txt (deflated 90%)
 adding: doc3.txt (deflated 85%)
 adding: doc4.txt (deflated 97%)

# use -l to view contents of zip file
$ unzip -l zipfile.zip
Archive:  zipfile.zip
  Length     Date     Time    Name
---------  ---------- -----   ----
     5234  2015-08-26 21:21   doc1.txt
     7213  2015-08-26 21:21   doc2.txt
     3634  2015-08-26 21:21   doc3.txt
     4516  2015-08-26 21:21   doc4.txt
---------                     -------
    16081                     3 files

$ unzip zipfile.zip
  inflating: doc1.txt
  inflating: doc2.txt
  inflating: doc3.txt
  inflating: doc4.txt
\end{lstlisting}
%$

While the zip file format is more popular on the Windows platform, the \li{tar} utility is more common in the Unix environment. The following commands use \li{tar} to archive the files and \li{gzip} to compress the archive.

Notice that all the commands below have the \li{-z}, \li{-v}, and \li{-f} flags. The \li{-z} flag calls for the \li{gzip} compression tool, the \li{-v} flag calls for a verbose output, and \li{-f} indicates the next parameter will be the name of the archive file.

\begin{lstlisting}[language=bash]
$ ls
doc1.txt	doc2.txt	doc3.txt	doc4.txt

# use -c to create a new archive
$ tar -zcvf docs.tar.gz doc?.txt
doc1.txt
doc2.txt
doc3.txt
doc4.txt

$ ls
docs.tar.gz

# use -t to view contents
$ tar -ztvf <archive>
-rw-rw-r-- username/groupname 5119 2015-08-26 16:50 doc1.txt
-rw-rw-r-- username/groupname 7253 2015-08-26 16:50 doc2.txt
-rw-rw-r-- username/groupname 3524 2015-08-26 16:50 doc3.txt
-rw-rw-r-- username/groupname 4516 2015-08-26 16:50 doc4.txt

# use -x to extract
$ tar -zxvf <archive>
doc1.txt
doc2.txt
doc3.txt
doc4.txt
\end{lstlisting}
%$

\begin{problem}
Archive and compress the files in the \texttt{Photos/} directory using \li{tar} and \li{gzip}. Name the arhive \texttt{pics.tar.gz} and save it inside the \texttt{Photos/} directory. Use \li{ls -l} to see how much the files were compressed in the process.
\end{problem}

\section*{Vim: A Terminal Text Editor} % ======================================

Today many have become accustomed to having GUIs (Graphic User Interfaces) for all their applications.
Before modern text editors (i.e. Microsoft Word, Pages for Mac, Google Docs) there were terminal text editors.
Vim is one of the most popular terminal text editors.
While vim may be intimidating at first, as you become familiar with vim it may become one of your preferred text editors for writing code.

One of the major philosophies of vim is to be able to keep your fingers on the keyboard at all times.
Thus, vim has many keyboard shortcuts that allow you to navigate the file and execute commands without relying on a mouse, toolbars, or arrow keys.

In this section, we will go over the basics of navigation and a few of the most common commands.
We will also provide a list of commands that interested readers are encouraged to research.

It has been said that at no point does somebody finish learning Vim.
You will find that you will constantly be able to add something new to your arsenal.

\subsection*{Getting Started} % -----------------------------------------------

Start Vim with the following command:

\begin{lstlisting}[language=bash]
$ vim my_file.txt
\end{lstlisting}

When executing this command, if \texttt{my\_file.txt} already exists, vim will open the file and we may begin editing the existing file.
If \texttt{my\_file.txt} does not exist, it will be created and we may begin editing the file.

You may notice if you start typing the characters may or may not appear on your screen.
This is because vim has multiple modes.
When vim starts, we are placed in \emph{command mode}.
We want to be in \emph{insert mode} to begin entering text.
To enter insert mode from command mode, hit the \li{i} key.
You should see \li{-- INSERT --} at the bottom of your terminal window.
In insert mode vim act like a typical word processor.
Letters will appear in the document as you type them.
If you ever need to leave insert mode and return to command mode, hit the \li{Esc} key.

\subsection*{Saving/Quitting Vim} % -------------------------------------------

To save or quit the current document, first enter last line mode by pressing the \textbf{:} key.
To just save, type \textbf{w} and hit enter.
To save and quit, type \textbf{wq}.
To quit without saving, run \textbf{q!}

\begin{problem}
Using vim, create a new file in the \texttt{Documents/} directory named \texttt{first\_vim.txt}.
Write least multiple lines to this file.
Save and exit the file you have created.
\end{problem}

\subsection*{Navigation} % ----------------------------------------------------

We are accustomed to navigating GUI text editors using a mouse and arrow keys. In vim, we navigate using keyboard shortcuts while in command mode.

\begin{table}
\begin{tabular}{l|l}
    Command & Description
    \\ \hline
    \li{a} & \textbf{a}ppend text after cursor \\
    \li{A} & \textbf{A}ppend text to end of line \\
    \li{o} & Begin a new line below the cursor \\
    \li{O} & Begin a new line above the cursor \\
    \li{s} & Substitute characters under cursor \\
\end{tabular}
\caption{Commands for entering insert mode}
\label{table:viminsert}
\end{table}

% TODO: turn this into a table.
\begin{problem}
Become accustomed to navigating in command mode using the following keys:
\begin{table}[H]
\begin{tabular}{r|l}
    Command & Description
    \\ \hline
    \li{k} & up \\
    \li{j} & down \\
    \li{h} & left \\
    \li{l} & right \\
    \li{w} & beginning of next \textbf{w}ord \\
    \li{e} & \textbf{e}nd of next word \\
    \li{b} & \textbf{b}eginning of previous word \\
    \li{0} & (zero) beginning of line \\
    \li{\$} & end of line \\
    \li{gg} & beginning of file \\
    \li{<<\#gg>>} & go to line \li{<<\#>>} \\
    \li{G} & end of file
\end{tabular}
\end{table}
\end{problem}

\subsection*{Alternative Ways to Enter Insert Mode} % -------------------------

Hitting the \li{i} key is not the only way to enter insert mode.
Alternative methods are described in Table \ref{table:viminsert}.

\subsection*{Visual Mode} % ---------------------------------------------------

Visual mode allows you to select multiple characters.
Among other things, we can use this to replace words with the \li{s} command, and we can select text to cut or copy.

\begin{problem}
Open the document you created in the previous problem.
While in command mode, enter visual mode by pressing the \li{v} key.
Using the navigation keys discussed earlier, move the cursor to select a few words.
Copy this text using the \li{y} key (stands for \textbf{y}ank).
Return to command mode by pressing \li{Esc}.
Move the cursor to where you would like to paste the text and press the \li{p} key to paste.
Similarly, select text in visual mode and hit \li{d} to \textbf{d}elete the text and paste it somewhere else with the \li{p} key.
\end{problem}

\subsection*{Deleting Text in Command Mode} % ---------------------------------

Insert mode should only be used for inserting text.
Try to get in the habit of leaving insert mode as soon as you are done adding the text you want to add.
Deleting text is much more efficient and versatile in command mode.
The \li{x} and \li{X} commands are used to delete single characters.
The \li{d} command is always accompanied by another navigational command.
See Table \ref{table:delete} for a few examples.

\begin{table}
\begin{tabular}{l|l}
    Command & Description
    \\ \hline
    \li{x} & delete letter after cursor \\
    \li{X} & delete letter before cursor \\
    \li{dd} & delete line \\
    \li{dl} & \textbf{d}elete \textbf{l}etter \\
    \li{<<d\#l>>} & \textbf{d}elete \# \textbf{l}etters \\
    \li{dw} & \textbf{d}elete \textbf{w}ord \\
    \li{<<d\#w>>} & \textbf{d}elete \# \textbf{w}ords \\
\end{tabular}
\caption{Commands for deleting in command mode}
\label{table:delete}
\end{table}

\subsection*{A Few Closing Remarks} % -----------------------------------------

In the next lab, we will introduce how to access another machine through the terminal.
Vim will be essential in this situation since GUIs will not be an option.

If you are interested in continuing to use vim, you may be interested in checking out \emph{gvim}.
Gvim is a GUI that uses vim commands in a more traditional text editor window.

Also, in Table \ref{table:vim}, we have listed a few more commands that are worth exploring.
If you are interested in any of these features of vim, we encourage you to research these features further on the internet.
Additionally, many people have published their \texttt{vimrc} file on the internet so other vim users can learn what options are worth exploring.
It is also worth noting that we can use vim navigation commands in many other places in the shell.
For example, try using the navigation commands when viewing the \li{man vim} page.

\begin{table}
\begin{tabular}{r|l}
    Command & Description
    \\ \hline
    \li{<<:map>>} & customize \\
    \li{<<:help>>} & view vim docs \\
    \li{cw} & \textbf{c}hange \textbf{w}ord \\
    \li{u} & undo \\
    \li{Ctrl-R} & redo \\
    \li{.} & Repeat the previous command \\
    \li{*} & find next occurrence of word under cursor \\
    \li{<<#>>} & find previous occurrence of word under cursor \\
    \li{<</str>>} & find \li{<<str>>} in file \\
    \li{n} & find next match \\
    \li{N} & find previous match \\
\end{tabular}
\caption{Commands for entering insert mode}
\label{table:vim}
\end{table}

