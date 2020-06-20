\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{mnumstyle}
\LoadClass[a4paper]{book}
\RequirePackage[top=25mm,bottom=25mm,left=25mm,right=25mm]{geometry}
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{graphicx}
% Listings
\usepackage{xcolor}
\usepackage{listings}
\renewcommand{\lstlistingname}{File}
\lstset{
    frame=tb, % draw frame at top and bottom of the code
    tabsize=4, % tab space width
    numbers=left, % display line numbers on the left
	showstringspaces=false, % don't mark spaces in strings    
    commentstyle=\color{green}, % comment color
    keywordstyle=\color{blue}, % keyword color
    stringstyle=\color{red} % string color
}
\lstdefinelanguage{Maxima}{
    keywords = {
        exp,
        sqrt,
        diff,
        log,
        abs,
        plot2d
    }
}
