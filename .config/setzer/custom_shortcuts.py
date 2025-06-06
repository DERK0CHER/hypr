# ~/.config/setzer/custom_shortcuts.py
# Define only the overrideable mappings for insert-before-after and insert-symbol
# comments with #, flaceholders are either a comma for "isnert_before_after" or this{ • } for symbols.
# expected syntax: (['ursnippet','ursnippet end'],['ur command']),
# trailing commas are expected for every line!!!

insert_before_after = [
    (['\\textbf{', '}'], ['<Control>b']),
    (['\\textit{', '}'], ['<Control>i']),
    (['\\underline{', '}'], ['<Control>u']),
    (['\\texttt{', '}'], ['<Control><Shift>t']),
    (['\\emph{', '}'], ['<Control><Shift>e']),
    (['$','$'], ['<Control>m']),
    (['\\begin{equation}\n\t', '•\n\\end{equation}'], ['<Control><Shift>n']),
    (['\\begin{•}\n\t', '\n\\end{•}'], ['<Control>e']),
    (['_{', '}'], ['<Control><Shift>d']),
    (['^{', '}'], ['<Control><Shift>u']),
]

insert_symbol = [
    (['\\frac{•}{•}•'], ['<Alt><Shift>f']),
    (['\\left •'], ['<Control><Shift>l']),
    (['\\right •'], ['<Control><Shift>r']),
    (['\\item •'], ['<Control><Shift>i']),
    (['\\\\\n'], ['<Control>Return']),
]

