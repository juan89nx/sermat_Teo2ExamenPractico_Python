import ply_LexCup.yacc as yacc

# Get the token map from the lexer.
from Sermat_Implementation.SermatLexer import tokens

import Sermat_Implementation.SermatLexer as Lex

# Precedence rules for the arithmetic operators
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
             | TRUE
             | FALSE
             | NUM
             | NULL
             | STR
             | ID EQUALS value
             | ID
             | ID LEFT_PAR RIGHT_PAR
             | ID LEFT_PAR elements RIGHT_PAR
             | STR LEFT_PAR RIGHT_PAR
             | STR LEFT_PAR elements RIGHT_PAR'''
    if (v[1] == '{' and v[2] == '}') : v[0] = {}
    elif (v[1] == '{' and v[2] == 'members' and v[3]  == '}'): v[0] = v[2]
    elif (v[1] == '[' and v[2] == ']') : v[0] = []
    elif (v[1] == '[' and v[2] == 'elements' and v[3]  == ']'): v[0] = v[2]
    elif (v[1] == 'TRUE') : v[0] = v[1]
    elif (v[1] == 'FALSE') : v[0] = v[1]
    elif (v[1] == 'NUM') : v[0] = v[1]
    elif (v[1] == 'NULL') : v[0] = None
    elif (v[1] == 'STR') : v[0] = v[1]
    elif (v[1] == 'ID' and v[2]== 'EQUALS' and v[3]== 'value') :
        v[0] = v[3]
        membersVar[v[1]]=v[3]
    elif (v[1] == 'ID') :
        v[0]=v[1]
        membersVar[v[1]] = None
     #Preguntar-> Fruta!!!   
    elif (v[1] == 'ID' and v[2] == '(' and v[3]== ')') :
        v[0] = []
        membersVar[v[1]]=v[0]
    elif (v[1] == 'ID' and v[2] == '(' and v[3]== 'elements' and v[4]== ')') :
        v[0] = v[3]
        membersVar[v[1]]=v[0]
    elif (v[1] == 'STR' and v[2]== '(' and v[3]== ')') :
        v[0]=[]
        membersVar[v[1]]=v[0]
        #Materialize
    elif (v[1] == 'STR' and v[2]== '(' and v[3]== 'elements' and v[4]== ')') :
        v[0]=v[3]
        membersVar[v[1]]=v[3]

def p_members(m):
    '''members : members COMMA STR COLON value
               | members COMMA ID COLON value
               | STR COLON value
               | ID COLON value'''
    if (m[1] == 'members' and m[2] == 'COMMA' and m[3]=='STR' and m[4]=='COLON' and m[5]=='value') : 
            m[0] = m[1]
            membersVar[m[0]] = {m[3],m[5]}
    elif (m[1] == 'members' and m[2] == 'COMMA' and m[3]=='ID' and m[4]=='COLON' and m[5]=='value') : 
            m[0] = m[1]
            membersVar[m[0]] = {m[3],m[5]}
    elif (m[1] == 'STR' and m[2] == 'COLON' and m[3]=='value' ) : 
            m[0] = {}
            m[m[1]] = m[3]
    
def p_elements(e):
    '''elements : value
                | elements COMMA value'''
    if (e[1] == 'value' ) : 
        e[0]=[e[1]]
    elif (e[1] == 'elements' and e[2]=='COMMA' and e[3]=='value' ) :         
        e[0] = e[1]
        e[0] = e[0] + e[3]    

def p_error(p):
    print("Syntax error at '%s'" % p.value)

Lex.buildLexer()
parser = yacc.yacc()

while True:
    try:
        s = raw_input('entrada > ')   # use input() on Python 3
    except EOFError:
        break

    print(parser.parse(s))








