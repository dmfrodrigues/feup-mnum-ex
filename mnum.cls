\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{mnum}
\LoadClass[a4paper]{book}
% Margins
\usepackage[top=35mm,bottom=35mm,left=25mm,right=25mm]{geometry}
% Tables with colored cells
\usepackage[table,dvipsnames]{xcolor}%
% Graphics and images
\usepackage{graphicx}
% Encodings (to render letters with diacritics and special characters)
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
% Hyperreferences
\usepackage{hyperref}
% Source code
\usepackage{listings}
\renewcommand{\lstlistingname}{File}
\lstset{
    basicstyle=\ttfamily,
    frame=tb, % draw frame at top and bottom of the code
    tabsize=4, % tab space width
    numbers=left, % display line numbers on the left
	% showstringspaces=false, % don't mark spaces in strings    
    commentstyle=\color{green}, % comment color
    keywordstyle=\color{blue}, % keyword color
    stringstyle=\color{red} % string color
}
\lstdefinelanguage{Maxima}{
	keywords={exp, sqrt, diff, log, abs, plot2d, jacobian, matrix, determinant, ratsimp, subst, sin, cos},
	sensitive=true,
	comment=[n][\itshape]{/*}{*/}
}
% Tables with bold rows
\usepackage{tabularx}
\newcommand\setrow[1]{\gdef\rowmac{#1}#1\ignorespaces}
\newcommand\clearrow{\global\let\rowmac\relax}
\clearrow
% Math stuff
\usepackage[mathscr]{euscript}
\usepackage{amsmath,amssymb}
\usepackage{mathtools}
\usepackage[inline]{enumitem}
\usepackage[binary-units=true,retain-explicit-plus,retain-zero-exponent]{siunitx} %SI units
\newcommand\comb[2]{^{#1}C_{#2}}
\usepackage{mathtools} %dcases
\newcommand\realset{\mathbb{R}}
% Copyright page
\newenvironment{secondpage}{
    \clearpage\null\vfill
    \thispagestyle{empty}
    \begin{minipage}[b]{0.9\textwidth}
        \footnotesize\raggedright
        \setlength{\parskip}{0.5\baselineskip}
}{
    \end{minipage}
    \vspace*{2\baselineskip}
}
% Some work
\def\title#1{\gdef\@title{#1}\gdef\@@title{#1}}
\def\author#1{\gdef\@author{#1}\gdef\@@author{#1}}
\let\@@title\@empty
\let\@@author\@empty
% Headers and footers
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\fancyhead[RE, LO]{\textit{\leftmark}}
\fancyhead[LE, RO]{\thepage}
\fancyfoot[LE, RO]{\ifx\@@author\@empty\else\@@author\fi}
% Sections
\makeatletter
\renewcommand\thesection{\thechapter\ifnum\c@section>\z@ -P\arabic{section}\fi}
\renewcommand\thesubsection{\thesection-\arabic{subsection}}
\renewcommand\thesubsubsection{\thesubsection\alph{subsubsection}}
\makeatother
% Alias
\setcounter{secnumdepth}{-2}
\newcommand\exam[1]{\chapter{#1}}
\newcommand\exampart[1]{\section{#1}}
\newcommand\question[1]{\subsection{#1}}
\newcommand\questionitem[1]{\subsubsection{#1}}
