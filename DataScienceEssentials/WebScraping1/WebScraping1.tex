\lab{Web Scraping I: Introduction to BeautifulSoup}{Introduction to Beautiful Soup}
\objective{Web Scraping is the process of gathering data from websites on the internet.
Since almost everything rendered by an internet browser as a web page uses HTML, the first step in web scraping is being able to extract information from HTML.
In this lab, we introduce BeautifulSoup, Python's canonical tool for efficiently and cleanly navigating and parsing HTML.}

\section*{HTML} % =============================================================

\emph{Hyper Text Markup Language}, or \emph{HTML}, is the standard \emph{markup language}---a language designed for the processing, definition, and presentation of text---for creating webpages.
It provides a document with structure and is composed of pairs of \emph{tags} to surround and define various types of content.
Opening tags have a tag name surrounded by angle brackets (\li{<tag-name>}).
The companion closing tag looks the same, but with a forward slash before the tag name (\li{</tag-name>}).
A list of all current HTML tags can be found at \url{http://htmldog.com/reference/htmltags}.

Most tags can be combined with \emph{attributes} to include more data about the content, help identify individual tags, and make navigating the document much simpler.
In the following example, the \li{<a>} tag has \lstinline[language=HTML]{id} and \li{href} attributes.

\begin{lstlisting}[language=HTML]
<html>                                  <!-- Opening tags -->
   <body>
       <p>
           Click <a id='info' href='http://www.example.com'>here</a>
           for more information.
       </p>                             <!-- Closing tags -->
   </body>
</html>
\end{lstlisting}

In HTML, \li{href} stands for \emph{hypertext reference}, a link to another website.
Thus the above example would be rendered by a browser as a single line of text, with \li{here} being a clickable link to \url{http://www.example.com}:

\begin{center}
Click \href{http://www.example.com}{here} for more information.
\end{center}

Unlike Python, HTML does not enforce indentation (or any whitespace rules), though indentation generally makes HTML more readable.
The previous example can even be written equivalently in a single line.

\begin{lstlisting}[language=HTML]
<html><body><p>Click <a id='info' href='http://www.example.com/info'>here</a>
  for more information.</p></body></html>
\end{lstlisting}

Special tags, which don't contain any text or other tags, are written without a closing tag and in a single pair of brackets.
A forward slash is included between the name and the closing bracket.
Examples of these include \li{<hr/>}, which describes a horizontal line, and \li{<img/>}, the tag for representing an image.

\begin{problem} % Use View Page Source to see HTML source of a simple website.
The HTML of a website is easy to view in most browsers.
In Google Chrome, go to \url{http://www.example.com}, right click anywhere on the page that isn't a picture or a link, and select \li{View Page Source}.
This will open the HTML source code that defines the page.
Examine the source code.
What tags are used?
What is the value of the \li{<<type>>} attribute associated with the \li{style} tag?

Write a function that returns the set of names of tags used in the website, and the value of the \li{<<type>>} attribute of the \li{style} tag (as a string).
\\(Hint: there are ten unique tag names.)
\label{prob:look-at-example.com}
\end{problem}

\section*{BeautifulSoup} % ====================================================

BeautifulSoup (\li{bs4}) is a package%
\footnote{BeautifulSoup is not part of the standard library; install it with \li{conda install beautifulsoup4} or with \li{pip install beautifulsoup4}.} that makes it simple to navigate and extract data from HTML documents.
See \url{http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html} for the full documentation.

The \li{bs4.BeautifulSoup} class accepts two parameters to its constructor: a string of HTML code, and an HTML parser to use under the hood.
The HTML parser is technically a keyword argument, but the constructor prints a warning if one is not specified.
The standard choice for the parser is \li{"html.parser"}, which means the object uses the standard library's \li{html.parser} module as the engine behind the scenes.

\begin{info}
Depending on project demands, a parser other than \li{"html.parser"} may be useful.
A couple of other options are \li{"lxml"}, an extremely fast parser written in C, and \li{"html5lib"}, a slower parser that treats HTML in much the same way a web browser does, allowing for irregularities.
Both must be installed independently; see \url{https://www.crummy.com/software/BeautifulSoup/bs4/doc/\#installing-a-	parser} for more information.
\end{info}

A \li{BeautifulSoup} object represents an HTML document as a tree.
In the tree, each tag is a \emph{node} with nested tags and strings as its \emph{children}.
The \li{prettify()} method returns a string that can be printed to represent the BeautifulSoup object in a readable format that reflects the tree structure.

\begin{lstlisting}
>>> from bs4 import BeautifulSoup

>>> small_example_html = """
<html><body><p>
    Click <a id='info' href='http://www.example.com'>here</a>
    for more information.
</p></body></html>
"""

>>> small_soup = BeautifulSoup(small_example_html, 'html.parser')
>>> print(small_soup.prettify())
<<<html>
 <body>
  <p>
   Click
   <a href="http://www.example.com" id="info">
    here
   </a>
   for more information.
  </p>
 </body>
</html>>>
\end{lstlisting}

Each tag in a \li{BeautifulSoup} object's HTML code is stored as a \li{bs4.element.Tag} object, with actual text stored as a \li{bs4.element.NavigableString} object.
Tags are accessible directly through the \li{BeautifulSoup} object.

\begin{lstlisting}
# Get the <p> tag (and everything inside of it).
>>> small_soup.p
<<<p>
    Click <a href="http://www.example.com" id="info">here</a>
    for more information.
</p>>>

# Get the <a> sub-tag of the <p> tag.
>>> a_tag = small_soup.p.a
>>> print(a_tag, type(a_tag), sep='\n')
<<<a href="http://www.example.com" id="info">here</a>
<class 'bs4.element.Tag'>>>

# Get just the name, attributes, and text of the <a> tag.
>>> print(a_tag.name, a_tag.attrs, a_tag.string, sep="\n")
<<a
{'id': 'info', 'href': 'http://www.example.com'}
here>>
\end{lstlisting}

\begin{table}[H]
\centering
\begin{tabular}{c|l}
Attribute & Description \\ \hline
\li{name} & The name of the tag \\
\li{attrs} & A dictionary of the attributes \\
\li{string} & The single string contained in the tag \\
\li{strings} & Generator for strings of children tags \\
\li{stripped_strings} & Generator for strings of children tags, stripping whitespace \\
\li{text} & Concatenation of strings from all children tags
\end{tabular}
\caption{Data attributes of the \li{bs4.element.Tag} class.}
\label{table:bs4-tag-attributes}
\end{table}

\begin{problem} % Find tag names using BeautifulSoup.
The \li{BeautifulSoup} class has a \li{find_all()} method that, when called with \li{True} as the only argument, returns a list of all tags in the HTML source code.

Write a function that accepts a string of HTML code as an argument.
Use BeautifulSoup to return a list of the \textbf{names} of the tags in the code.
Use your function and the source code from \url{http://www.example.com} (see \texttt{example.html}) to check your answers from Problem \ref{prob:look-at-example.com}.
\end{problem}

\subsection*{Navigating the Tree Structure} % ---------------------------------

Not all tags are easily accessible from a \li{BeautifulSoup} object.
Consider the following example.

\begin{lstlisting}
>>> pig_html = """
<html><head><title>Three Little Pigs</title></head>
<body>
<p class="title"><b>The Three Little Pigs</b></p>
<p class="story">Once upon a time, there were three little pigs named
<a href="http://example.com/larry" class="pig" id="link1">Larry,</a>
<a href="http://example.com/mo" class="pig" id="link2">Mo</a>, and
<a href="http://example.com/curly" class="pig" id="link3">Curly.</a>
<p>The three pigs had an odd fascination with experimental construction.</p>
<p>...</p>
</body></html>
"""

>>> pig_soup = BeautifulSoup(pig_html, "html.parser")
>>> pig_soup.p
<<<p class="title"><b>The Three Little Pigs</b></p>>>

>>> pig_soup.a
<<<a class="pig" href="http://example.com/larry" id="link1">Larry,</a>>>
\end{lstlisting}

Since the HTML in this example has several \li{<p>} and \li{<a>} tags, only the \textbf{first} tag of each name is accessible directly from \li{pig_soup}.
The other tags can be accessed by manually navigating through the HTML tree.

Every HTML tag (except for the topmost tag, which is usually \li{<html>}) has a \emph{parent} tag.
Each tag also has and zero or more \emph{sibling} and \emph{children} tags or text.
Following a true tree structure, every \li{bs4.element.Tag} in a soup has multiple attributes for accessing or iterating through parent, sibling, or child tags.

\begin{table}[H]
\centering
\begin{tabular}{c|l}
Attribute & Description \\ \hline
\li{parent} & The parent tag \\
\li{parents} & Generator for the parent tags up to the top level \\
\li{next_sibling} & The tag immediately after to the current tag \\
\li{next_siblings} & Generator for sibling tags after the current tag \\
\li{previous_sibling} & The tag immediately before to the current tag \\
\li{previous_siblings} & Generator for sibling tags before the current tag \\
\li{contents} & A list of the immediate children tags\\
\li{children} & Generator for immediate children tags\\
\li{descendants} & Generator for all children tags (recursively)\\
\end{tabular}
\caption{Navigation attributes of the \li{bs4.element.Tag} class.}
\label{table:bs4-tag-attributes-2}
\end{table}

\begin{lstlisting}
>>> print(pig_soup.prettify())
<<<html>
 <head>>>                     # <head> is the parent of the <title>
  <<<title>
   Three Little Pigs
  </title>
 </head>
 <body>>>                     # <body> is the sibling of <head>
  <<<p class="title">>>         # and the parent of two <p> tags (title and story).
   <<<b>
    The Three Little Pigs
   </b>
  </p>
  <p class="story">
   Once upon a time, there were three little pigs named
   <a class="pig" href="http://example.com/larry" id="link1">
    Larry,
   </a>
   <a class="pig" href="http://example.com/mo" id="link2">
    Mo
   </a>
   , and
   <a class="pig" href="http://example.com/curly" id="link3">
    Curly.>>                  # The preceding <a> tags are siblings with each
   </a>                     # other and the following two <p> tags.
   <<<p>
    The three pigs had an odd fascination with experimental construction.
   </p>
   <p>
    ...
   </p>
  </p>
 </body>
</html>>>
\end{lstlisting}

\begin{lstlisting}
# Start at the first <a> tag in the soup.
>>> a_tag = pig_soup.a
>>> a_tag
<<<a class="pig" href="http://example.com/larry" id="link1">Larry,</a>>>

# Get the names of all of <a>'s parent tags, traveling up to the top.
# The name '[document]' means it is the top of the HTML code.
>>> [par.name for par in a_tag.parents]     # <a>'s parent is <p>, whose
<<['p', 'body', 'html', '[document]']>>         # parent is <body>, and so on.

# Get the next siblings of <a>.
>>> a_tag.next_sibling
<<'\n'>>                                        # The first sibling is just text.
>>> a_tag.next_sibling.next_sibling         # The second sibling is a tag.
<<<a class="pig" href="http://example.com/mo" id="link2">Mo</a>>>

# Alternatively, get all siblings past <a> at once.
>>> list(a_tag.next_siblings)
<<['\n',
 <a class="pig" href="http://example.com/mo" id="link2">Mo</a>,
 ', and\n',
 <a class="pig" href="http://example.com/curly" id="link3">Curly.</a>,
 '\n',
 <p>The three pigs had an odd fascination with experimental construction.</p>,
 '\n',
 <p>...</p>,
 '\n']>>
\end{lstlisting}

Note carefully that newline characters are considered to be children of a parent tag.
Therefore iterating through children or siblings often requires checking which entries are tags and which are just text.

\begin{lstlisting}
# Get to the <p> tag that has class="story".
>>> p_tag = pig_soup.body.p.next_sibling.next_sibling
>>> p_tag.attrs["class"]                # Make sure it's the right tag.
<<['story']>>

# Iterate through the child tags of <p> and print hrefs whenever they exist.
>>> for child in p_tag.children:
...     if hasattr(child, "attrs") and "href" in child.attrs:
...         print(child.attrs["href"])
<<http://example.com/larry
http://example.com/mo
http://example.com/curly>>
\end{lstlisting}

Note that the \li{"class"} attribute of the \li{<p>} tag is a list.
This is because the \li{"class"} attribute can take on several values at once; for example, the tag \li{<p class="story book">} is of class \li{'story'} and of class \li{'book'}.

\begin{info}
The behavior of the \li{string} attribute of a \li{bs4.element.Tag} object depends on the structure of the corresponding HTML tag.
\begin{enumerate}
    \item If the tag has a string of text and no other child elements, then \li{string} is just that text.
    \item If the tag has exactly one child tag and the child tag has only a string of text, then the tag has the same \li{string} as its child tag.
    \item If the tag has more than one child, then \li{string} is \li{None}.
    In this case, use \li{strings} to iterate through the child strings.
    Alternatively, the \li{get_text()} method returns all text belonging to a tag and to all of its descendants.
    In other words, it returns anything inside a tag that isn't another tag.
\end{enumerate}

\begin{lstlisting}
>>> pig_soup.head
<<<head><title>Three Little Pigs</title></head>>>

# Case 1: the <title> tag's only child is a string.
>>> pig_soup.head.title.string
<<'Three Little Pigs'>>

# Case 2: The <head> tag's only child is the <title> tag.
>>> pig_soup.head.string
<<'Three Little Pigs'>>

# Case 3: the <body> tag has several children.
>>> pig_soup.body.string is None
<<True>>
>>> print(pig_soup.body.get_text().strip())
<<The Three Little Pigs
Once upon a time, there were three little pigs named
Larry,
Mo, and
Curly.
The three pigs had an odd fascination with experimental construction.
...>>
\end{lstlisting}
\end{info}

\begin{problem}
The file \texttt{example.html} contains the HTML source for \url{http://www.example.com}.
Write a function that reads the file and loads the code into BeautifulSoup.
Find the only \li{<a>} tag with a hyperlink and return its text.
\end{problem}

\begin{comment}
\begin{problem} % TODO: give them the html file, don't download it.

% example.html
Write a function that returns the following line using three different methods.
\begin{lstlisting}
<<'More information...'>>
\end{lstlisting}
The function should accept an integer.
If the integer is 1, find the line using tag names and the \li{.string} method.
If the integer is 2, find the line by traversing through the children of the body tag with repeated calls to \li{.contents}.
If the integer is 3, find the line by using navigation between siblings and \li{.string}.
\end{problem}
\end{comment}

\subsection*{Searching for Tags} % --------------------------------------------

Navigating the HTML tree manually can be helpful for gathering data out of lists or tables, but these kinds of structures are usually buried deep in the tree.
The \li{find()} and \li{find_all()} methods of the \li{BeautifulSoup} class identify tags that have distinctive characteristics, making it much easier to jump straight to a desired location in the HTML code.
The \li{find()} method only returns the \textbf{first} tag that matches a given criteria, while \li{find_all()} returns a list of all matching tags.
Tags can be matched by name, attributes, and/or text.

\begin{lstlisting}
# Find the first <b> tag in the soup.
>>> pig_soup.find(name='b')
<<<b>The Three Little Pigs</b>>>

# Find all tags with a class attribute of 'pig'.
# Since 'class' is a Python keyword, use 'class_' as the argument.
>>> pig_soup.find_all(class_="pig")
<<[<a class="pig" href="http://example.com/larry" id="link1">Larry,</a>,
 <a class="pig" href="http://example.com/mo" id="link2">Mo</a>,
 <a class="pig" href="http://example.com/curly" id="link3">Curly.</a>]>>

# Find the first tag that matches several attributes.
>>> pig_soup.find(attrs={"class": "pig", "href": "http://example.com/mo"})
<<<a class="pig" href="http://example.com/mo" id="link2">Mo</a>>>

# Find the first tag whose text is 'Mo'.
>>> pig_soup.find(string='Mo')
<<'Mo'>>                                # The result is the actual string,
>>> soup.find(string='Mo').parent       # so go up one level to get the tag.
<<<a class="pig" href="http://example.com/mo" id="link2">Mo</a>>>
\end{lstlisting}

\begin{problem}
The file \texttt{san\_diego\_weather.html} contains the HTML source for an old page from Weather Underground.\footnote{See \url{http://www.wunderground.com/history/airport/KSAN/2015/1/1/DailyHistory.html?req_city=San+Diego&req_state=CA&req_statename=California&reqdb.zip=92101&reqdb.magic=1&reqdb.wmo=99999&MR=1}}.
Write a function that reads the file and loads it into BeautifulSoup.
Return a list of the following tags:
\begin{enumerate}
\item The tag containing the date ``Thursday, January 1, 2015''.
\item The tags which contain the \textbf{links} ``Previous Day'' and ``Next Day.''
\item The tag which contains the number associated with the Actual Max Temperature.
\end{enumerate}

This HTML tree is significantly larger than the previous examples.
To get started, consider opening the file in a web browser.
Find the element that you are searching for on the page, right click it, and select \li{Inspect}.
This opens the HTML source at the element that the mouse clicked on.
\end{problem}

\subsection*{Advanced Search Techniques} % ------------------------------------

Consider the problem of finding the tag that is a link the URL \url{http://example.com/curly}.

\begin{lstlisting}
>>> pig_soup.find(href="http://example.com/curly")
<<<a class="pig" href="http://example.com/curly" id="link3">Curly.</a>>>
\end{lstlisting}

This approach works, but it requires entering in the entire URL.
To perform generalized searches, the \li{find()} and \li{find_all()} method also accept compile regular expressions from the \li{re} module.
This way, the methods locate tags whose name, attributes, and/or string matches a pattern.

\begin{lstlisting}
>>> import re

# Find the first tag with an href attribute containing 'curly'.
>>> pig_soup.find(href=re.<<compile>>(r"curly"))
<<<a class="pig" href="http://example.com/curly" id="link3">Curly.</a>>

# Find the first tag with a string that starts with 'Cu'.
>>> pig_soup.find(string=re.<<compile>>(r"^Cu")).parent
<<<a class="pig" href="http://example.com/curly" id="link3">Curly.</a>>>

# Find all tags with text containing 'Three'.
>>> [tag.parent for tag in pig_soup.find_all(string=re.<<compile>>(r"Three"))]
<<[<title>Three Little Pigs</title>, <b>The Three Little Pigs</b>]>>
\end{lstlisting}

Finally, to find a tag that has a particular attribute, regardless of the actual value of the attribute, use \li{True} in place of search values.

\begin{lstlisting}
# Find all tags with an 'id' attribute.
>>> pig_soup.find_all(<<id>>=True)
<<[<a class="pig" href="http://example.com/larry" id="link1">Larry,</a>,
 <a class="pig" href="http://example.com/mo" id="link2">Mo</a>,
 <a class="pig" href="http://example.com/curly" id="link3">Curly.</a>]>>

# Final the names all tags WITHOUT an 'id' attribute.
>>> [tag.name for tag in pig_soup.find_all(<<id>>=False)]
<<['html', 'head', 'title', 'body', 'p', 'b', 'p', 'p', 'p']>>
\end{lstlisting}

\begin{problem} % Bank Data Index.
The file \texttt{large\_banks\_index.html} is an index of data about large banks, as recorded by the Federal Reserve.\footnote{See \url{https://www.federalreserve.gov/releases/lbr/}.}
Write a function that reads the file and loads the source into BeautifulSoup.
Return a list of the tags containing the links to bank data from September 30, 2003 to December 31, 2014, where the dates are in reverse chronological order.
\label{prob:bs-bank-index}
\end{problem}

\begin{problem} % Actual Bank Data.
The file \texttt{large\_banks\_data.html} is one of the pages from the index in Problem \ref{prob:bs-bank-index}.\footnote{See \url{http://www.federalreserve.gov/releases/lbr/20030930/default.htm}.}
Write a function that reads the file and loads the source into BeautifulSoup.
Create a single figure with two subplots:
\begin{enumerate}
    \item A sorted bar chart of the seven banks with the most domestic branches.
    \item A sorted bar chart of the seven banks with the most foreign branches.
\end{enumerate}
In the case of a tie, sort the banks alphabetically by name.
\end{problem}
