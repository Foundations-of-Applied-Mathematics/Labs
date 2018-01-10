\lab{Regular Expressions}{Regular Expressions}
\objective{Cleaning and formatting data are fundamental problems in data science.
Regular expressions are an important tool for working with text carefully and efficiently, and are useful for both gathering and cleaning data.
This lab introduces regular expression syntax and common practices, including an application to a data cleaning problem.
}

% TODO: use fullmatch() instead of search() in the examples up to the end of the regex syntax section.

% TODO: Important links!
% \url{https://docs.python.org/3/howto/regex.html}
% \url{https://docs.python.org/3/library/re.html}

    % As an example, the following program will find and fill in missing colons after control statements in normally formatted python files:
    % % ^((def|if|elif|else|while|for|with).*):\s*$

A \emph{regular expression} or \emph{regex} is a string of characters that follows a certain syntax to specify a pattern.
Strings that follow the pattern are said to \emph{match} the expression (and vice versa).
A single regular expression can match a large set of strings, such as the set all valid email addresses.
% The idea is similar to using wildcards like \li{*} in the Unix shell: the command \li{ls *.py} displays \textbf{all} files that have a \texttt{.py} file extension.

\begin{warn}
There are some universal standards for regular expression syntax, but the exact syntax varies slightly depending on the program or language.
However, the syntax presented in this lab (for Python) is sufficiently similar to any other regex system.
Consider learning to use regular expressions in vim or your favorite text editor, keeping in mind that there are bound to be slight syntactic differences from what is presented here.
\end{warn}

\section*{Regular Expression Syntax in Python} % ==============================

The \li{re} module implements regular expressions in Python.
The function \li{re.<<compile>>()} takes in a regular expression string and returns a corresponding \emph{pattern} object, which has methods for determining if and how other strings match the pattern.
For example, the \li{search()} method returns \li{None} for a string that doesn't match, and a \emph{match} object for a string that does (more on these later).

\begin{lstlisting}
>>> import re
>>> pattern = re.<<compile>>("cat")     # Make a pattern for finding 'cat'.
>>> bool(pattern.search("cat"))     # 'cat' matches 'cat', of course.
<<True>>
>>> bool(pattern.search("catfish")) # 'catfish' also contains 'cat'.
<<True>>
>>> bool(pattern.search("hat"))     # 'hat' does not contain 'cat'.
<<False>>
\end{lstlisting}

\begin{warn} % re.match() only matches the beginning!
The poorly named \li{match()} method for pattern objects only matches strings that satisfy the pattern \textbf{at the beginning} of the string.
To answer the question ``does any part of my target string match this regular expression?'' always use the \li{search()} method.
\begin{lstlisting}
>>> pattern = re.<<compile>>("cat")
>>> bool(pattern.match("catfish"))
<<True>>
>>> bool(pattern.match("fishcat"))
<<False>>
>>> bool(pattern.search("fishcat"))
<<True>>
\end{lstlisting}
\end{warn}

\begin{info} % re.search() vs. re.compile().search()
Most of the functions in the \li{re} module are shortcuts for compiling a pattern object and calling one of its methods.
For example, the following lines of code are equivalent.
\begin{lstlisting}
>>> bool(re.<<compile>>("cat").search("catfish"))
<<True>>
>>> bool(re.search("cat", "catfish"))
<<True>>
\end{lstlisting}
Using \li{re.<<compile>>()} is good practice because the resulting object is reusable, while each call to \li{re.search()} compiles a new (but redundant) pattern object.
\end{info}

\begin{problem} % Easy regular expression, construct test cases.
Write a function that compiles and returns a regular expression pattern object with the pattern string \li{"python"}.

Construct positive and negative test cases to test your object.
Having good test cases will be important later, so be thorough.
Your verification process might start as follows.
\begin{lstlisting}
>>> pattern = re.<<compile>>("cat")
>>> positive = ["cat", "catfish", "fish cat", "your cat ran away"]
>>> assert all(pattern.search(p) for p in positive)
\end{lstlisting}
\label{prob:regex-superbasic}
\end{problem}

\subsection*{Literal Characters and Metacharacters} % -------------------------

The following string characters (separated by spaces) are \emph{metacharacters} in Python's regular expressions, meaning they have special significance in a pattern string:
\li{. ^ \$ * + ? \{ \} [ ] \\ | ( )}.

To construct a regular expression that matches strings with one or more metacharacters in them requires two things.
First, use \emph{raw strings} instead of regular Python strings by prefacing the string with an \li{r}, such as \li{r"cat"}.
The resulting string interprets backslashes as actual backslash characters, rather than the start of an escape sequence like \li{\\n} or \li{\\t}.
Second, preface any metacharacters with a backslash to indicate a literal character.
For example, the following code constructs a regular expression to match the string \li{"\$3.99? Thanks."}.

\begin{lstlisting}
>>> dollar = re.<<compile>>(r"\$3\.99\? Thanks\.")
>>> bool(dollar.search("$3.99? Thanks."))
<<True>>
>>> bool(dollar.search("$3\.99? Thanks."))
<<False>>
>>> bool(dollar.search("$3.99?"))   # Doesn't contain the entire pattern.
<<False>>
\end{lstlisting}

Without raw strings, every backslash in has to be written as a double backslash, which makes many regular expression patterns hard to read (\li{"\\\\\$3\\\\.99\\\\? Thanks\\\\."}).
Readability counts.

\begin{problem}
Write a function that compiles and returns a regular expression pattern object that matches the string \li{"^\{@\}(?)[\%]\{.\}(*)[_]\{&\}\$"}.
\label{prob:regex-metacharacter-literals}
\end{problem}

The regular expressions of Problems \ref{prob:regex-superbasic} and \ref{prob:regex-metacharacter-literals} only match strings that are or include the exact pattern.
The metacharacters allow regular expressions to have much more flexibility and control so that a single pattern could match a wide variety of strings, or a very specific set of strings.

To begin, the \emph{line anchor} metacharacters \li{^} and \li{\$} are used to match the \textbf{start} and the \textbf{end} of a line of text, respectively.
This shrinks the matching set, even when using the \li{search()} method instead of the \li{match()} method.
For example, the only single-line string that the expression \li{^x\$} matches is \li{'x'}, whereas the expression \li{x} can match any string with an \li{x} in it.

\begin{lstlisting}
>>> has_x, just_x = re.<<compile>>(r"x"), re.<<compile>>(r"^x$")
>>> for test in ["x", "xabc", "abcx"]:
...     print(test + ':', bool(has_x.search(test)), bool(just_x.search(test)))
...
<<x: True True
xabc: True False>>                    # Starts with 'x', but doesn't end with it.
<<abcx: True False>>                    # Ends with 'x', but doesn't start with it.
\end{lstlisting}

% TODO: put this back in later.
\begin{comment}
An added benefit of using \li{'^'} and \li{'\$'} is that they allow you to search across multiple lines.
For example, how would we match \li{"World"} in the string \mbox{\li{"Hello\\nWorld"}}?
Using \li{re.MULTILINE} in the \li{re.search} function will allow us to match at the beginning of each new line, instead of just the beginning of the string.
Since we have seen two ways to match strings with regex expressions, the following shows two ways to implement multiline searching:

\begin{lstlisting}
>>>bool(re.search("^W","Hello\nWorld"))
<<False>>
>>>bool(re.search("^W","Hello\nWorld", re.MULTILINE))
<<True>>
>>>pattern1 = re<<.compile>>("^W")
>>>pattern2 = re<<.compile>>("^W", re.MULTILINE)
>>>bool(pattern1.search("Hello\nWorld"))
<<False>>
>>>bool(pattern2.search("Hello\nWorld"))
<<True>>
\end{lstlisting}

For simplicity, the rest of the lab will focus on single line matching.
\end{comment}

The \emph{pipe} character \li{|} is like a logical \li{OR} in a regular expression: \li{A|B} matches \li{A} or \li{B}.
\begin{lstlisting}
>>> rb, rbg = re.<<compile>>(r"^red$|^blue$"), re.<<compile>>(r"^red$|^blue$|^green$")
>>> for test in ["red", "blue", "green", "redblue"]:
...     print(test + ":", bool(rb.search(test)), bool(rbg.search(test)))
<<red: True True
blue: True True
green: False True
redblue: False False>>                # The line anchors prevent matching here.
\end{lstlisting}

The parentheses \li{()} create a \emph{group} in a regular expression.
Among other things, a group establishes an order of operations in an expression, much like how parentheses work in an arithmetic expression such as $3\cdot(4+5)$.

\begin{lstlisting}
>>> fish = re.<<compile>>(r"^(one|two) fish$")
>>> for test in ["one fish", "two fish", "red fish", "one two fish"]:
...     print(test + ':', bool(fish.search(test)))
...
<<one fish: True
two fish: True
red fish: False
one two fish: False>>
\end{lstlisting}

% Parentheses help give regular expressions higher precedence.
% For example, \li{"^one|two fish\$"} gives precedence to the invisible string concatenation between \li{"two"} and \li{"fish"} while \li{"^(one|two) fish\$"} gives precedence to the \li{'\|'} metacharacter.

\begin{problem}
Write a function that compiles and returns a regular expression pattern object that matches the following strings (and no other strings, even with \li{re.search()}).

\centering
\begin{tabular}{lll}
\li{"Book store"} & \li{"Mattress store"} & \li{"Grocery store"} \\
\li{"Book supplier"} & \li{"Mattress supplier"} & \li{"Grocery supplier"} \\
\end{tabular}
\end{problem}

\subsection*{Character Classes} % ---------------------------------------------

The hard bracket metacharacters \li{[} and \li{]} are used to create \emph{character classes}, a part of a regular expression that can match a variety of characters.
For example, the pattern \li{[abc]} matches any of the characters \li{a}, \li{b}, or \li{c}.
This is different than a group delimited by parentheses: a group can match multiple characters, while a character class matches only one character.
For instance, \li{[abc]} does not match \li{ab} or \li{abc}, and \li{(abc)} matches \li{abc} but not \li{ab} or even \li{a}.

Within character classes, there are two additional metacharacters.
When \li{^} appears \textbf{as the first character} in a character class, right after the opening bracket \li{[}, the character class matches anything \textbf{not} specified instead.
In other words, \li{^} is the set complement operation on the character class.
Additionally, the dash \li{-} specifies a range of values.
For instance, \li{[0-9]} matches any digit, and \li{[a-z]} matches any lowercase letter.
Thus \li{[^0-9]} matches any character \textbf{except} for a digit, and \li{[^a-z]} matches any character \textbf{except} for a lowercase letters

\begin{lstlisting}
>>> p1, p2 = re.<<compile>>(r"^[a-z][^0-7]$"), re.<<compile>>(r"^[^abcA-C][0-27-9]$")
>>> for test in ["d8", "aa", "E9", "EE", "d88"]:
...     print(test + ':', bool(p1.search(test)), bool(p2.search(test)))
...
<<d8: True True>>
<<aa: True False>>                      # a is not in [^abcA-C] or [0-27-9].
<<E9: False True>>                      # E is not in [a-z].
<<EE: False False>>                     # E is not in [a-z] or [0-27-9].
<<d88: False False>>                    # Too many characters.
\end{lstlisting}

Note that \li{[0-27-9]} acts like \li{[(0-2)|(7-9)]}.

There are also a variety of shortcuts that represent common character classes, listed in Table \ref{table:regex-character-class-shortcuts}.
Familiarity with these shortcuts makes some regular expressions significantly more readable.

\begin{table}[H]
\begin{tabular}{c|l}
Character & Description \\ \hline
% \li{\\number} & Matches the contents of the group of the same number. \\
\li{\\b} & Matches the empty string, but only at the start or end of a word. \\
\li{\\d} & Matches any decimal digit; equivalent to \li{[0-9]}. \\
\li{\\D} & Matches any non-digit character; equivalent to \li{[^\\d]}. \\
\li{\\s} & Matches any whitespace character; equivalent to \li{[ \\t\\n\\r\\f\\v]}. \\
\li{\\S} & Matches any non-whitespace character; equivalent to \li{[^\\s]}. \\
\li{\\w} & Matches any alphanumeric character; equivalent to \li{[a-zA-Z0-9_]}. \\
\li{\\W} & Matches any non-alphanumeric character; equivalent to \li{[^\\w]}. \\
% \li{\\\\} & Matches a literal backslash. \\
\end{tabular}
\caption{Character class shortcuts.}
\label{table:regex-character-class-shortcuts}
\end{table}

Any of the character class shortcuts can be used within other custom character classes.
For example, \li{[\_A-Z\\s]} matches an underscore, capital letter, or whitespace character.

Finally, a period \li{.} matches \textbf{any} character except for a line break, and is therefore equivalent to \li{[\^\\n]} on UNIX machines and \li{[\^\\r\\n]} on Windows machines.
This is a very powerful metacharacter; be careful to only use it when part of the regular expression really should match \textbf{any} character.

\begin{lstlisting}
# Match any three-character string with a digit in the middle.
>>> pattern = re.<<compile>>(r"^.\d.$")
>>> for test in ["a0b", "888", "n2%", "abc", "cat"]:
...     print(test + ':', bool(pattern.search(test)))
...
<<a0b: True
888: True
n2%: True
abc: False
cat: False>>

# Match two letters followed by a number and two non-newline characters.
>>> pattern = re.<<compile>>(r"^[a-zA-Z][a-zA-Z]\d..$")
>>> for test in ["tk421", "bb8!?", "JB007", "Boba?"]:
...     print(test + ':', bool(pattern.search(test)))
..
<<tk421: True
bb8!?: True
JB007: True
Boba?: False>>
\end{lstlisting}

\begin{table}[H]
\begin{tabular}{c|l}
Character & Description \\ \hline
\li{.}    & Matches any character except a newline. \\
\li{^}    & Matches the start of the string. \\
\li{\$}   & Matches the end of the string or just before the newline at the end of the string. \\
% \li{\\\\}   & Either escapes special characters or signals a special sequence. \\
\li{|}    & \li{A|B} creates an regular expression that will match either \li{A} or \li{B}. \\
\li{[...]}     & Indicates a set of characters. A \li{^} as the first character indicates a complementing set. \\
\li{(...)}  & Matches the regular expression inside the parentheses.\\ & The contents can be retrieved or matched later in the string. \\
\end{tabular}
\caption{Standard regular expression metacharacters in Python.}
\label{table:regex-special-characters}
\end{table}

% TODO: shorten this section.

\subsection*{Repetition} % ----------------------------------------------------

The remaining metacharacters are for matching a specified number of characters.
This allows a single regular expression to match strings of varying lengths.

\begin{table}[H]
\begin{tabular}{c|l}
Character & Description \\ \hline
\li{*}    & Matches 0 or more repetitions of the preceding regular expression. \\
\li{+}    & Matches 1 or more repetitions of the preceding regular expression. \\
\li{?}    & Matches 0 or 1 of the preceding regular expression. \\
\li{\{m,n\}}  & Matches from m to n repetitions of the preceding regular expression. \\
\li{*?}, \li{+?}, \li{??}, \li{\{m,n\}?} & Non-greedy versions of the previous four special characters.
\end{tabular}
\caption{Repetition metacharacters for regular expressions in Python.}
\label{table:regex-special-characters2}
\end{table}


% The \li{'*'} metacharacter means ``Match zero or more times (\textbf{as many as possible})'' when it follows another regular expression.
% The \li{'+'} metacharacter means ``Match one or more times (as many as possible)'' when it follows another regular expression.
% The \li{'?'} metacharacter means ``Match one time (if possible) or do nothing (i.e. match zero times)'' when it follows another regular expression:
% The curly brace metacharacters are used to specify a more precise amount of repetition:

\begin{lstlisting}
# Match 0 or more 'a' characters, ending in a 'b'.
>>> pattern = re.<<compile>>(r"^a*b$")
>>> for test in ["b", "ab", "aaaaaaaaaab", "aba"]:
...     print(test + ':', bool(pattern.search(test)))
...
<<b: True>>                             # 0 'a' characters, then 1 'b'.
<<ab: True>>
<<aaaaaaaaaab: True>>                   # Several 'a' characters, then 1 'b'.
<<aba: False>>                          # 'b' must be the last character.

# Match an 'h' followed by at least one 'i' or 'a' characters.
>>> pattern = re.<<compile>>(r"^h[ia]+$")
>>> for test in ["ha", "hii", "hiaiaa", "h", "hah"]:
...     print(test + ':', bool(pattern.search(test)))
...
<<ha: True
hii: True>>
<<hiaiaa: True>>                        # [ia] matches 'i' or 'a'.
<<h: False>>                            # Need at least one 'i' or 'a'
<<hah: False>>                          # 'i' or 'a' must be the last character.

# Match an 'a' followed by 'b' followed by 0 or 1 'c' characters.
>>> pattern = re.<<compile>>(r"^abc?$")
>>> for test in ["ab", "abc", "abcc", "ac"]:
...     print(test + ':', bool(pattern.search(test)))
...
<<ab: True
abc: True>>
<<abcc: False>>                         # Only up to one 'c' is allowed.
<<ac: False>>                           # Missing the 'b'.
\end{lstlisting}

Each of the repetition operators acts on the expression immediately preceding it.
This could be a single character, a group, or a character class.
For instance, \li{(abc)+} matches \li{abc}, \li{abcabc}, \li{abcabcabc}, and so on, but not \li{aba} or \li{cba}.
On the other hand, \li{[abc]*} matches any sequence of \li{a}, \li{b}, and \li{c}, including \li{abcabc} and \li{aabbcc}.

The curly braces \li{\{\}} specify a custom number of repetitions allowed.
\li{\{,n\}} matches \textbf{up to} $n$ instances, \li{\{m,\}} matches \textbf{at least} $m$ instances, \li{\{k\}} matches \textbf{exactly} $k$ instances, and \li{\{m,n\}} matches from $m$ to $n$ instances.
Thus the \li{?} operator is equivalent to \li{\{,1\}} and \li{+} is equivalent to \li{\{1,\}}.

\begin{lstlisting}
# Match exactly 3 'a' characters.
>>> pattern = re.<<compile>>(r"^a{3}$")
>>> for test in ["aa", "aaa", "aaaa", "aba"]:
...     print(test + ':', bool(pattern.search(test)))
...
<<aa: False>>                           # Too few.
<<aaa: True
aaaa: False>>                         # Too many.
<<aba: False>>
\end{lstlisting}

\begin{warn} % Use line anchors with repetition operators.
Line anchors are especially important when using repetition operators.
Consider the following (bad) example and compare it to the previous example.

\begin{lstlisting}
# Match exactly 3 'a' characters, hopefully.
>>> pattern = re.<<compile>>(r"a{3}")
>>> for test in ["aaa", "aaaa", "aaaaa", "aaaab"]:
...     print(test + ':', bool(pattern.search(test)))
...
<<aaa: True
aaaa: True>>                          # Should be too many!
<<aaaaa: True>>                         # Should be too many!
<<aaaab: True>>                         # Too many, and even with the 'b'?
\end{lstlisting}
The unexpected matches occur because \li{"aaa"} is at the beginning of each of the test strings.
With the line anchors \li{^} and \li{\$}, the search truly only matches the exact string \li{"aaa"}.
\end{warn}

\begin{problem}
A \emph{valid Python identifier} (a valid variable name) is any string staring with an alphabetic character or an underscore, followed by any (possibly empty) sequence of alphanumeric characters and underscores.

Define a function that compiles and returns a regular expression pattern object that matches any valid Python identifier.
\\(Hint: Use the \li{\\w} character class shortcut to keep your regular expression clean.)

Check your regular expression against the following words.
These test cases are a good start, but are not exhaustive.

\centering
\begin{tabular}{c|lllll}
Matches: & \li{"Mouse"} & \li{"compile"} & \li{"_123456789"} & \li{"__x__"} & \li{"while"} \\ \hline
Non-matches: & \li{"3rats"} & \li{"err*r"} & \li{"sq(x)"} & \li{"sleep()"} & \li{"     x"}
\end{tabular}
% As you might have noticed, using this definition, \li{"while"} is considered a valid python identifier, even though it really is a reserved word. In the following problems, we will make a few other simplifying assumptions about the python language.
\end{problem}


\begin{comment} % Might be worth putting this in...
\begin{problem}
A \emph{valid python parameter definition} is defined as the concatenation of the following strings:
\begin{itemize}
    \item any valid python identifier
    \item any number of spaces
    \item (optional) an equals sign followed by any number of spaces and ending with one of the following: any real number, a single quote followed by any number of non-single-quote characters followed by a single quote, or any valid python identifier
\end{itemize}

Define a variable \li{parameter_pattern_string} that defines a regular expression that matches valid python parameter definitions.

For example, each element of \li{["max=4.2", "string= ''", "num_guesses", "msg ='\\\\'", "volume_fn=_CALC_VOLUME"]} is a valid python parameter definition, while each element of \li{["300", "no spaces", "is_4=(value==4)", "pattern = r'^one|two fish\$'", 'string="these last two are actually valid in python, but they should not be matched by your pattern"']} is not. % TODO add more negative examples maybe?
\end{problem}
\end{comment}


\begin{comment} % Might be worth putting this in...
\begin{problem}
A \emph{valid python function definition} is defined as the concatenation of the following strings:
\begin{itemize}
    \item \li{"def"}
    \item Any number of spaces
    \item any valid python identifier
    \item \li{"("}
    \item a sequence of any number of (possibly zero) valid python parameter definitions, separated by any number of spaces followed by a comma followed by any number of spaces
    \item \li{")"}
    \item \li{":"}
\end{itemize}
with any number of spaces between each element of the above list.

Define a variable \li{function_pattern_string} that defines a regular expression that matches valid python function definitions.

For example, the program should behave as follows:
\begin{lstlisting}
>>> run match_function_definition.py
Enter a string>>> def compile(pattern,string):
<<True>>
Enter a string>>> def  space  ( ) :
<<True>>
Enter a string>>> def func(_dir, file_path='\Desktop\files', val=_PI):
<<True>>
Enter a string>>> def func(num=3., num=.5, num=0.0):
<<True>>
Enter a string>>> def func(num=., error,):
<<False>>
Enter a string>>> def variable:
<<False>>
Enter a string>>> def not.allowed(, *args):
<<False>>
Enter a string>>> def err*r('no parameter name'):
<<False>>
Enter a string>>> def func(value=_MY_CONSTANT, msg='%s' % _DEFAULT_MSG):
<<False>>
Enter a string>>> def func(s1='', a little tricky, s2=''):
<<False>>
Enter a string>>> def func(): Remember your line anchors!
<<False>>
Enter a string>>> deffunc()
<<False>>
Enter a string>>> func():
<<False>>
Enter a string>>> exit

\end{lstlisting}

\begin{warn}
In the end, my variable \li{function_pattern_string} was \emph{215 characters long}. You WILL make a mistake while defining \li{function_pattern_string}; do you want to try to debug a 215-character regular expression? Do NOT try to define it all at once!

Instead, use your previously defined regular expressions to make this easier. For example, either of the two following idioms will work:
\begin{lstlisting}
>>> key_1 = "basic"
>>> print("This is a " + key_1 + " way to concatenate strings.")
This is a basic way to concatenate strings.
>>> format_dict = {"key_1": "basic", "key_2": "much more", "key_3": "advanced"}
>>> print("This is a {key_2} {key_3} way to concatenate strings. It's {key_2} flexible.".format(**format_dict))
This is a much more advanced way to concatenate strings. It's much more flexible.
\end{lstlisting}
Keep in mind that you'll have to remove the line anchors from your previously defined regular expressions.

For reference, I used about ten lines to define \li{function_pattern_string} and used statements of the form \li{intermediate_pattern_string = r"(my regular expression here)".format()} four times.
\end{warn}

\label{prob:match_function_definition}
\end{problem}
\end{comment}

\section*{Manipulating Text with Regular Expressions} % ======================

So far we have been solely concerned with whether or not a regular expression and a string match, but the power of regular expressions comes with what can be done with a match.
In addition to the \li{search()} method, regular expression pattern objects have the following useful methods.

\begin{table}[H]
\begin{tabular}{r|l}
Method & Description \\ \hline
\li{match()}     & Match a regular expression pattern to the beginning of a string. \\
\li{fullmatch()} & Match a regular expression pattern to all of a string. \\
\li{search()}    & Search a string for the presence of a pattern. \\
\li{sub()}       & Substitute occurrences of a pattern found in a string. \\
\li{subn()}      & Same as sub, but also return the number of substitutions made. \\
\li{split()}     & Split a string by the occurrences of a pattern. \\
\li{findall()}   & Find all occurrences of a pattern in a string. \\
\li{finditer()}  & Return an iterator yielding a match object for each match.
\end{tabular}
\caption{Methods of regular expression pattern objects.}
\end{table}

\begin{lstlisting}
# Find words that start with 'cat'.
>>> expr = re.<<compile>>(r"\bcat\w*")  # \b is the shortcut for a word boundary.

>>> target = "Let's catch some catfish for the cat"
>>> bool(expr.search(target))       # Check to see if there is a match.
<<True>>

>>> expr.findall(target)            # Get all matching substrings.
<<['catch' 'catfish', 'cat']>>

>>> expr.sub("DOG", target)         # Substitute 'DOG' for the matches.
<<"Let's DOG some DOG for the DOG">>

>>> expr.split(target)              # Split the target by the matches.
<<["Let's ", ' some ', ' for the ', '']>>
\end{lstlisting}

Some substitutions require remembering part of the text that the regular expression matches.
Groups are useful here: each group in the regular expression can be represented in the substitution string by \li{\\n}, where $n$ is an integer (starting at 1) specifying which group to use.

\begin{lstlisting}
# Find words that start with 'cat', remembering what comes after the 'cat'.
>>> pig_latin = re.compile(r"\bcat(\w*)")
>>> target = "Let's catch some catfish for the cat"

>>> pig_latin.sub(r"at\1clay", target)  # \1 = (\w*) from the expression.
<<"Let's atchclay some atfishclay for the atclay">>
\end{lstlisting}

\begin{info} % Greedy repetition, check with findall().
The repetition operators \li{?}, \li{+}, \li{*}, and \li{\{m,n\}} are \emph{greedy}, meaning that they match the largest string possible.
On the other hand, the operators \li{??}, \li{+?}, \li{*?}, and \li{\{m,n\}?} are \emph{non-greedy}, meaning they match the smallest strings possible.
This is very often the desired behavior for a regular expression.

\begin{lstlisting}
>>> target = "<abc> <def> <ghi>"

# Match angle brackets and anything in between.
>>> greedy = re.<<compile>>(r"^<.*>$")  # Greedy *
>>> greedy.findall(target)
<<['<abc> <def> <ghi>']>>               # The entire string matched!

# Try again, using the non-greedy version.
>>> nongreedy = re.<<compile>>(r"<.*?>")# Non-greedy *?
>>> nongreedy.findall(target)
<<['<abc>', '<def>', '<ghi>']>>         # Each <> set is an individual match.
\end{lstlisting}
\end{info}

Finally, there are a few customizations that make searching larger texts manageable.
Each of these \emph{flags} can be used as keyword arguments to \li{re.<<compile>>()}.

\begin{table}[H]
\begin{tabular}{c|l}
Flag & Description \\ \hline
\li{re.DOTALL}     & \li{.} matches any character at all, including the newline. \\
\li{re.IGNORECASE} & Perform case-insensitive matching. \\
\li{re.MULTILINE}  & \li{^} matches the beginning of lines (after a newline)
               as well as the string; \\ & \li{\$} matches the end of lines (before a newline) as well as the end of the string.
\end{tabular}
\caption{Regular expression flags.}
\end{table}

\begin{lstlisting}
# Match any line with 3 consecutive 'a' characters somewhere.
>>> pattern = re.<<compile>>("^.*a{3}.*$", re.MULTILINE)    # Search each line.
>>> pattern.findall("""
This is aaan example.
This is not an example.
Actually, it's an example, but it doesn't match.
This example does maaatch though.""")
<<['This is aaan example.', 'This example does maaatch though.']>>

# Match anything instance of 'cat', ignoring case.
>>> catfinder = re.compile("cat", re.IGNORECASE)
>>> catfinder.findall("cat CAT cAt TAC ctacATT")
<<['cat', 'CAT', 'cAt', 'cAT']>>
\end{lstlisting}

\begin{problem}
A Python \emph{block} is composed of several lines of code with the same indentation level.
Blocks are delimited by key words and expressions, followed by a colon.
Possible key words are \li{if}, \li{elif}, \li{else}, \li{for}, \li{while}, \li{try}, \li{except}, \li{finally}, \li{with}, \li{def}, and \li{class}.
Some of these keywords require an expression of some sort to follow before the colon (\li{if}, \li{elif}, \li{for}, etc.), some require no expressions to follow before the colon (\li{else}, \li{finally}), and \li{except} may or may not have an expression following before the colon.

Write a function that accepts a string of Python code and uses regular expressions to place colons in the appropriate spots.
You may assume that every colon is missing in the input string.
See the following for an example.

\begin{lstlisting}
"""
k, i, p = 999, 1, 0
while k > i
    i *= 2
    p += 1
    if k != 999
        print("k should not have changed")
    else
        pass
print(p)
"""

# The string given above should become this string.
"""
k, i, p = 999, 1, 0
while k > i:
    i *= 2
    p += 1
    if k != 999:
        print("k should not have changed")
    else:
        pass
print(p)
"""
\end{lstlisting}
\end{problem}

\begin{problem}
The file \texttt{fake\_contacts.txt} contains poorly formatted contact data for 2000 fictitious individuals.
Each line of the file contains data for one person, including their name and possibly their birthday, email address, and/or phone number.
The formatting of the data is not consistent, and much of it is missing.
For example, not everyone has their birthday listed, and those who do may have it listed in the form \li{1/1/11}, \li{1/01/2011}, or some other format.

Use regular expressions to parse the data and format it uniformly, writing birthdays as \li{mm/dd/yyyy} and phone numbers as \li{(xxx)xxx-xxxx}.
Return a dictionary where the key is the name of an individual and the value is another dictionary containing their information.
Each of these inner dictionaries should have the keys \li{"birthday"}, \li{"email"}, and \li{"phone"}.
In the case of missing data, map the key to \li{None}.
The first two entries of the completed dictionary are given below.

\begin{lstlisting}
{
    "John Doe": {
        "birthday": "01/01/1990",
        "email": "john_doe90@hopefullynotarealaddress.com",
        "phone": "(123)456-7890"
        },
    "Jane Smith": {
        "birthday": None,
        "email": None,
        "phone": "(222)111-3333"
        },
# ...
}
\end{lstlisting}
\end{problem}

\newpage

\section*{Additional Material} % ==============================================

\section*{Regular Expressions in the Unix Shell}
As we have seen thusfar, regular expressions are very useful when we want to match patterns. Regular expressions can be used when matching patterns in the Unix Shell. Though there are many Unix commands that take advantage of regular expressions, we will focus on \li{grep} and \li{awk}.

\subsection*{Regular Expressions and grep}
Recall from Lab 1 that \li{grep} is used to match patterns in files or output. It turns out we can use regular expressions to define the pattern we wish to match.

In general, we use the following syntax:
\begin{lstlisting}
$ grep 'regexp' filename
\end{lstlisting}
%$

We can also use regular expressions when piping output to \li{grep}.
\begin{lstlisting}
# List details of directories within current directory.
$ ls -l | grep ^d
\end{lstlisting}
%$

\subsection*{Regular Expressions and awk}
As in Lab 2, we will be using \li{awk} to format output. By incorporating regular expressions, \li{awk} becomes much more robust. Before GUI spreedsheet programs like Microsoft Excel, \li{awk} was commonly used to visualize and query data from a file.

Including \li{if} statements inside \li{awk} commands gives us the ability to perform actions on lines that match a given pattern. The following example prints the filenames of all files that are owned by \li{freddy}.
\begin{lstlisting}
$ ls -l | awk ' {if ($3 ~ /freddy/) print $9} '
\end{lstlisting}
%$

Because there is a lot going on in this command, we will break it down piece-by-piece. The output of \li{ls -l} is getting piped to \li{awk}. Then we have an \li{if} statement. The syntax here means if the condition inside the parenthesis holds, print field $9$ (the field with the filename). The condition is where we use regular expressions. The \li{\~} checks to see if the contents of field $3$ (the field with the username) matches the regular expression found inside the forward slashes. To clarify, \li{freddy} is the regular expression in this example and the expression must be surrounded by forward slashes.

Consider a similar example. In this example, we will list the names of the directories inside the current directory. (This replicates the behavior of the Unix command \li{ls -d */})

\begin{lstlisting}
$ ls -l | awk ' {if ($1 ~ /^d/) print $9} '
\end{lstlisting}
%$

Notice in this example, we printed the names of the directories, whereas in one of the example using \li{grep}, we printed all the details of the directories as well.

\begin{warn}
Some of the definitions for character classes we used earlier in this lab will not work in the Unix Shell. For example, \li{\\w} and \li{\\d} are not defined. Instead of \li{\\w}, use \li{[[:alnum:]]}. Instead of \li{\\d}, use \li{[[:digit:]]}. For a complete list of similar character classes, search the internet for \emph{POSIX Character Classes} or \emph{Bracket Character Classes.}
\end{warn}

\begin{problem}
You have been given a list of transactions from a fictional start-up company. In the \li{transactions.txt} file, each line represents a transaction. Transactions are represented as follows:
\begin{lstlisting}
# Notice the semicolons delimiting the fields. Also, notice that in between the last and first name, that is a comma, not a semicolon.
<ORDER_ID>;<YEAR><MONTH><DAY>;<LAST>,<FIRST>;<ITEM_ID>
\end{lstlisting}

Using this set of transactions, produce the following information using regular expressions and the given command:
\begin{itemize}
    \item Using \li{grep}, print all transactions by either Nicholas Ross or Zoey Ross.
    \item Using \li{awk}, print a sorted list of the names of individuls that bought item $3298$.
    \item Using \li{awk}, print a sorted list of items purchased between June 13 and June 15 of 2014 (inclusive).
\end{itemize}
These queries can be produced using one command each.
\end{problem}

We encourage the interested reader to research more about how regular expressions can be used with \li{sed}.

% TODO: deterministic finite state automata.
