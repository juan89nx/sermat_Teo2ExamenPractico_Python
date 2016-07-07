import ply_LexCup.yacc as yacc

# Get the token map from the lexer.
from Sermat_Implementation.SermatLexer import tokens
import Sermat_Implementation.SermatLexer as Lex
from Construcciones import construirEnBaseAFuncion


# Precedence rules
precedence = (
    ('BINDINGS', 'ID', 'EQUALS', 'STR'),
    ('LEFT_BRACE', 'RIGHT_BRACE'),
    ('RIGHT_BRACK', 'COMMA'),
    )

# for storing variables
bindingsList = {}


def p_value(v):
    '''value : LEFT_BRACE RIGHT_BRACE
             | LEFT_BRACE members RIGHT_BRACE
             | LEFT_BRACK RIGHT_BRACK
             | LEFT_BRACK elements RIGHT_BRACK
             | BINDINGS EQUALS value
             | BINDINGS
             | ID LEFT_PAR RIGHT_PAR
             | ID LEFT_PAR elements RIGHT_PAR'''
    global bindingsList
    if (v[1] == '{' and v[2] == '}') :
        v[0] = {}
    elif (v[1] == '{' and v[3]  == '}'):
        v[0] = v[2]
    elif (v[1] == '[' and v[2] == ']') :
        v[0] = []
    elif (v[1] == '[' and v[3]  == ']'):
        v[0] = v[2]
    elif (len(v) == 2):
        v[0] = bindingsList[v[1]]
    elif (v[2] == '=' and len(v)==4) :
        v[0] = v[3]
        bindingsList[v[1]] = v[3]
    elif (v[2] == '(' and v[3]== ')') :
        v[0] = construirEnBaseAFuncion(v[1],[])
    elif (v[2] == '(' and v[4]== ')') :
        v[0] = construirEnBaseAFuncion(v[1],v[3])


def p_value_boolNumStrNull(v):
    '''value : TRUE
             | FALSE
             | NUM
             | STR
             | NULL'''
    v[0] = v[1]


#def p_value_id(v):
#    'value : ID'
#    v[0] = v[1]
#    membersMap[v[1]] = None
#    print("Soy value ID")


def p_value_str_rules(v):
    '''value : STR LEFT_PAR  RIGHT_PAR
             | STR LEFT_PAR elements RIGHT_PAR'''
    if (v[2]=="(" and v[3]==")"):
        v[0] = []
        v[0] = construirEnBaseAFuncion(v[1],[])
    elif (len(v)==5):
        v[0] = construirEnBaseAFuncion(v[1],v[3])


def p_members_mem_str_val(m):
        'members : members COMMA STR COLON value'
        m[0] = m[1]
        m[0][m[3]] = m[5]

def p_members_mem_id_val(m):
        'members : members COMMA ID COLON value'
        if(m[2]=="," and m[4]== ":"):
            m[0] = m[1]
            m[0][m[3]] = m[5]

def p_members_str_val(m):
        'members : STR COLON value'
        if(m[2]==':' and type(m[1]) == type(" ")):
            m[0] = {}
            m[0][m[1]] = m[3]

def p_members_id_val(m):
        'members : ID COLON value'
        m[0] = {}
        m[0][m[1]] = m[3]


def p_elements(e):
    '''elements : value
                | elements COMMA value'''
    if (len(e)==4) :
        e[0] = e[1]
        e[0].append(e[3])
    else:
        e[0] = [e[1]]

def p_error(p):
    print("Syntax error at '%s'" % p.value)

Lex.buildLexer()
parser = yacc.yacc()


while True:
    try:
        s = raw_input('entrada > ') # use input() on Python 3
        result = parser.parse(s)
        print "Parser Result:"
        print(result)
        print "bindingsList:"
        print bindingsList
     #   bindingsList = {}
    #except Exception:
    #    print "You need to type a valid enter!"
    except EOFError:
        break
