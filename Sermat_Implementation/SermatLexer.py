import ply_LexCup.lex as lex
from test.test_cmath import NAN

tokens = (
    'EQUALS',
    'COMMA',
    'COLON',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'LEFT_BRACK',
    'RIGHT_BRACK',
    'LEFT_PAR',
    'RIGHT_PAR',
    'NULL',
    'TRUE',
    'FALSE',
    'NUM',
    'ID',
    'STR'
)

# Tokens
t_EQUALS = r'='
t_COMMA = r','
t_COLON = r':'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_LEFT_BRACK = r'\['
t_RIGHT_BRACK = r'\]'
t_LEFT_PAR = r'\('
t_RIGHT_PAR = r'\)'
t_NULL = r'null'
t_TRUE = r'true'
t_FALSE = r'\false'
t_ID = r'[\$A-Z_a-z][\$\-\.A-Z_a-z0-9]*'
t_STR = r'\"([^\\\"]|\\[\0-\uFFFF])*\"'
#t_ignore_IGNORAR = r'[ \t\r\n\f]+|\/\*+([^\*]|\*+[^\/])*\*+\/'

def t_NUM(t):
    r'NaN|[+-]?Infinity|[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?'
    t.value = int(t.value)
    return t

def t_ignore_IGNORAR(t):
    r'[ \t\r\n\f]+|\/\*+([^\*]|\*+[^\/])*\*+\/'
    pass
    # No return value. Token discarded

# Para fixear error de 't_ID'
#def t_ID(t):
#    r'[\$A-Z_a-z][\$\-\.A-Z_a-z0-9]*'
#    return t


#def t_STR(t):
#    r'\"([^\\\"]|\\[\0-\uFFFF])*\"'
#    return t


# Ignored characters
t_ignore = ' \t\r\n\f'#|/\*+([^\*]|\*+[^\/])*\*+/'


# t_ignore = "\/\*+([^\*]|\*+[^\/])*\*+\/"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Unexpected input < '%s' >" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
def buildLexer():
    myLexer = lex.lex()
    return myLexer


# Fruta para probar los tokens
# tokenize()
# Utility function. Given a string of text, tokenize into a list of tokens
def tokenize2(text):
    tokens2 = []
    lexer = buildLexer()
    lexer.input(text)
    while True:
        tok = lexer.token()
        if not tok: break
        tokens2.append(tok)
    return tokens2
