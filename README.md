# Django-web-framework-software-metrics-measurement-using-Radon-and-Pylint

used radon and pylint to analyze the code and rank the code according to complexity

Django is a framework for web development using python and created for the quick development of database-driven sites 
Django was created at the Lawrence Journal-World newspaper

Maintainability Index is a software metric that evaluates how maintainable (simple to maintain and modify) the source code is. The maintainability index is measured as a factored formula comprising of Cyclomatic Complexity, Source Lines Of Code (SLOC), and Halstead volume. 

Radon is a Python tool that can measure various metrics from the source code. Radon can find out:raw metrics (Source lines of code or SLOC, blank lines, comment lines), all Halstead metrics, Cyclomatic Complexity such as McCabe's Complexity, and the Maintainability Index for a Visual Studio metric

Pylint is a Python instrument which verifies a module for coding standards

Cyclomatic complexity is a software metric used to indicate the complexity of a program. It is a quantitative measure of the number of linearly independent paths through a program's source code. It was developed by Thomas J. McCabe, Sr. in 1976

CC score        Rank        Risk
1-5             A           Low - simple block
6-10            B           Low = well structured and stable block
11-20           C           Moderate - slightly complex block
21-30           D           More than moderate - more complex block
31-40           E           High - complex block, alarming
41+             F           Very high - error prone, unstable block
