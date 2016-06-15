import ply_LexCup.yacc as yacc

# Get the token map from the lexer.
from Sermat_Implementation.SermatLexer import tokens

import Sermat_Implementation.SermatLexer as Lex

# Precedence rules
precedence = (
    ('ID', 'EQUALS', 'STR'),
    ('LEFT_BRACE', 'RIGHT_BRACE'),
    ('RIGHT_BRACK', 'COMMA'),
    )

# for storing variables
membersVar = {}
elementsVar = []
valueVar = type(object)
# non terminal Map<String, Object> members; 
# non terminal List<Object> elements; 
# non terminal Object value; 


def p_value(v):
    '''value : LEFT_BRACE RIGHT_BRACE
             | LEFT_BRACE members RIGHT_BRACE
             | LEFT_BRACK RIGHT_BRACK
             | LEFT_BRACK elements RIGHT_BRACK
             | ID EQUALS value
             | ID LEFT_PAR RIGHT_PAR
             | ID LEFT_PAR elements RIGHT_PAR'''
    if (v[1] == '{' and v[2] == '}') :
        v[0] = {}
        print (len(v))
        print("Soy value rule 1")
    elif (v[1] == '{' and v[3]  == '}'):
        v[0] = v[2]
        print("Soy value rule 2")
    elif (v[1] == '[' and v[2] == ']') :
        v[0] = []
        print("Soy value rule 3")
    elif (v[1] == '[' and v[3]  == ']'):
        v[0] = v[2]
        print("Soy value rule 4")
    elif (v[2] == '=') :
        v[0] = v[3]
        membersVar[v[1]] = v[3]
        # Preguntar, deberia guardar en un map.
        '''Podria ser:
            v[0]={}
        if v[0].has_key(v[1]) == False:
            v[0][v[1]]=v[3]
        '''
        print("Soy value rule 5, igual")
    elif (v[2] == '(' and v[3]== ')') :
        v[0] = []
        membersVar[v[1]]=v[0]
        print("Soy value rule 6")
    elif (v[2] == '(' and v[4]== ')') :
        v[0] = v[3]
        membersVar[v[1]]=v[0]
        print("Soy value rule 7")

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
    membersVar[v[1]] = None
    print("Soy value ID")


def p_value_str_rules(v):
    '''value : STR LEFT_PAR  RIGHT_PAR
             | STR LEFT_PAR elements RIGHT_PAR'''
    if (v[2]=="(" and v[3]==")"):
        v[0] = []
        membersVar[v[1]] = v[0]
        print("Soy value STR rule 1")
    elif (len(v)==5):
        v[0] = v[3]
        membersVar[v[1]] = v[3]
        print("Soy value STR rule 2")



def p_members_mem_str_val(m):
        'members : members COMMA STR COLON value'
        m[0] = m[1]
        membersVar[m[0]] = {m[3], m[5]}
        print("Soy member rule 1")

def p_members_mem_id_val(m):
        'members : members COMMA ID COLON value'
        m[0] = m[1]
        membersVar[m[0]] = {m[3], m[5]}
        print("Soy member rule 2")

def p_members_str_val(m):
        'members : STR COLON value'
        if(m[2]==':'):
            print ("entra :")
            m[0] = {}
            m[m[1]] = m[3]
            print("Soy member rule 3")

def p_members_id_val(m):
        'members : ID COLON value'
        m[0] = {}
        m[m[1]] = m[3]
        print("Soy member rule 4")


def p_elements(e):
    '''elements : value
                | elements COMMA value'''
    global elementsVar
    if (len(e)==4) :
        e[0] = e[1]
        e[0] = e[0] + e[3]
        elementsVar = [e[1]]
        elementsVar.__add__(e[3])
        print("Soy element rule 2")
    else:
        e[0] = [e[1]]
        elementsVar.__add__(e[1])
        print("Soy element rule 1")

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








