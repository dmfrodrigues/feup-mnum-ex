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
