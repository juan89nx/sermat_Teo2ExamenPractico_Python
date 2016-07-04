import ply_LexCup.yacc as yacc

# Get the token map from the lexer.
from Sermat_Implementation.SermatLexer import tokens
import Sermat_Implementation.SermatLexer as Lex
from Construcciones import construirEnBaseAFuncion


# Precedence rules
precedence = (
    ('ID', 'EQUALS', 'STR'),
    ('LEFT_BRACE', 'RIGHT_BRACE'),
    ('RIGHT_BRACK', 'COMMA'),
    )

# for storing variables
membersMap = {}
elementsList = []
valueVar = type(object)

bindings = {}


def p_value(v):
    '''value : LEFT_BRACE RIGHT_BRACE
             | LEFT_BRACE members RIGHT_BRACE
             | LEFT_BRACK RIGHT_BRACK
             | LEFT_BRACK elements RIGHT_BRACK
             | ID EQUALS value
             | ID LEFT_PAR RIGHT_PAR
             | ID LEFT_PAR elements RIGHT_PAR'''
    global membersMap
    global bindings
    if (v[1] == '{' and v[2] == '}') :
        v[0] = {}
        print("Soy value rule 1")
    elif (v[1] == '{' and v[3]  == '}'):
        v[0] = v[2]
        print("Soy value rule 2")
    elif (v[1] == '[' and v[2] == ']') :
        v[0] = []
        print("Soy value rule 3")
    elif (v[1] == '[' and v[3]  == ']'):
        v[0] = v[2]
        print("Soy value rule 4 - [elements]")
    elif (v[2] == '=') :
        v[0] = v[3]
        #membersMap[v[1]] = v[3]
        bindings[v[1]] = v[3]
        print("Soy value rule 5, id=valor")
    elif (v[2] == '(' and v[3]== ')') :
        v[0] = []
        membersMap[v[1]]=v[0]
        valor = construirEnBaseAFuncion(v[1],[])
        print("Soy value rule 6 - id()")
        print "Retorno de Funcion: %s" % valor
    elif (v[2] == '(' and v[4]== ')') :
        v[0] = v[3]
        print("Soy value rule 7 - id(elem)")
        valor = construirEnBaseAFuncion(v[1],v[3])
        print "Retorno de Funcion: %s" % (valor,)

def p_value_num(v):
    'value : NUM'
    if(len(v)==2):
        v[0] = v[1]
    print("Soy value NUM")

def p_value_true(v):
    'value : TRUE'
    v[0] = v[1]
    print("Soy value true")

def p_value_false(v):
    'value : FALSE'
    v[0] = v[1]
    print("Soy value false")

def p_value_string(v):
    'value : STR'
    v[0] = v[1]
    print("Soy value Str")

def p_value_null(v):
    'value : NULL'
    v[0] = None
print("Soy value NULL")

def p_value_id(v):
    'value : ID'
    v[0] = v[1]
    membersMap[v[1]] = None
    print("Soy value ID")


def p_value_str_rules(v):
    '''value : STR LEFT_PAR  RIGHT_PAR
             | STR LEFT_PAR elements RIGHT_PAR'''
    if (v[2]=="(" and v[3]==")"):
        v[0] = []
        valor = construirEnBaseAFuncion(v[1],[])
        print("Soy value STR rule 1")
        print "Retorno de Funcion: %s" % valor
    elif (len(v)==5):
        v[0] = v[3]
        valor = construirEnBaseAFuncion(v[1],v[3])
        print("Soy value STR rule 2")
        print "Retorno de Funcion: %s" % valor



def p_members_mem_str_val(m):
        'members : members COMMA STR COLON value'
        global membersMap
        m[0] = m[1]
        membersMap[m[3]] = m[5]
        print("Soy member rule 1")

def p_members_mem_id_val(m):
        'members : members COMMA ID COLON value'
        if(m[2]=="," and m[4]== ":"):
            global membersMap
            m[0] = m[1]
            membersMap[m[3]] = m[5]
            print("Soy member rule 2")

def p_members_str_val(m):
        'members : STR COLON value'
        global membersMap
        if(m[2]==':' and type(m[1]) == type(" ")):
            print type(m[1])
            m[0] = {}
            m[0][m[1]] = m[3]
            membersMap[m[1]] = m[3]
            print membersMap
            print("Soy member rule 3")

def p_members_id_val(m):
        'members : ID COLON value'
        global membersMap
        m[0] = {}
        print "Valor m[1]: "+str(m[1])
        m[0][m[1]] = m[3]
        membersMap[m[1]] = m[3]
        print("Soy member rule 4")


def p_elements(e):
    '''elements : value
                | elements COMMA value'''
    global elementsVar
    if (len(e)==4) :
        e[0] = e[1]
        e[0].append(e[3])
        elementsVar.append(e[3])
        print("Soy element rule 2")
    else:
        e[0] = [e[1]]
        print("Soy element rule 1")
        elementsVar = []
        elementsVar.append(e[1])

def p_error(p):
    print("Syntax error at '%s'" % p.value)

Lex.buildLexer()
parser = yacc.yacc()


while True:
    try:
        s = raw_input('entrada > ')   # use input() on Python 3
    except EOFError:
        break
    result = parser.parse(s)
    print(result)
    print "memberVar:"
    print membersMap
    print "elementsList:"
    print elementsList
    print "bindings:"
    print bindings





