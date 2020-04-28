#!/usr/local/bin/python3

FULL_EXAMPLE_HEADER = '''\\documentclass[a4paper,12pt]{article}
\\pagestyle{empty}
\\usepackage{amsmath}
\\usepackage{tikz}
\\usepackage[siunitx,american]{circuitikz}
\\usetikzlibrary{bending}
\\usetikzlibrary{arrows}

\\begin{document}
'''

CIRCUIT_BEGINNING = '''\\ctikzset{tripoles/mos style/arrows}
\\begin{circuitikz}[transform shape,scale=1]
\\begin{center}
'''

CIRCUIT_END = '''
\\end{circuitikz}
\\end{center}\n'''

END_DOCUMENT = '''\n\\end{document}'''
