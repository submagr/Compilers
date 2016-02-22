
from tokens import *
#These are a set of reserved tokens in GO, NOT to be used as keywords

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# How to ignore comments? Its done this way
t_ignore_COMMENT = r'(/\*([^*]|\n|(\*+([^*/]|\n])))*\*+/)|(//.*)'
#r'/\* [^(\*/)]* \*/ '  #
#This is just a list of all operators in GO! LOL too many
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD     = r'%'
t_AMPERS  = r'&'
t_OR 	  = r'\|'
t_CARET   = r'\^'
t_LL      = r'(<<)'
t_GG	  = r'(>>)'
t_AMPCAR  = r'&\^'
t_PLUSEQ  = r'(\+=)'
t_MINUSEQ = r'(-=)'
t_TIMESEQ = r'(\*=)'
t_DIVIDEEQ= r'/='
t_MODEQ   = r'(%=)'
t_AMPEQ   = r'(&=)'
t_OREQ    = r'(\|=)'
t_CAREQ   = r'(\^=)'
t_LLEQ    = r'(<<=)'
t_GGEQ    = r'(>>=)'
t_AMPCAREQ= r'(&\^=)'
t_AMPAMP  = r'(&&)'
t_OROR    = r'(\|\|)'
t_LMINUS  = r'(<-)'
t_PLUSPLUS= r'(\+\+)'
t_MINUSMIN= r'(--)'
t_EQEQ    = r'(==)'
t_LESS    = r'<'
t_GREAT   = r'>'
t_EQUAL   = r'='
t_NOT     = r'!'
t_NOTEQ   = r'(!=)'
t_LEQ     = r'(<=)'
t_GEQ     = r'(>=)'
t_COLONEQ = r'(:=)'
t_DDD	  = r'(\.\.\.)'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACK  = r'\['
t_RBRACK  = r'\]'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_COMMA   = r'\,'
t_DOT     = r'\.'
t_SEMICOL = r'\;'
t_COLON   = r'\:'
#The Other Stuff in GO  

# Strings in quotes
def t_STRING(t):
    r'(\"[^(\")]*\")|(\'[^(\')]*\') '
    #r'\'.*\' | \".*\"'
    t.value=t.value[1:-1].replace("\'","\"")
    return t

# This particular Keyword Screwed us a lot. So It so happens PLY doesn't 
# peform maximal match among definition functions, 
# it matches them sequentially
def t_INTERFACE(t):
    r'interface'
    return t

#those types :P
def t_TYPE(t):
    r'(((\*)|\ )*int|((\*)|\ )*float|((\*)|\ )*string)'
    t.value=t.value.replace(" ","")
    return t

#Identifier token for names and variables
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

# The almighty float
def t_FLOAT(t):
    r'(([0-9](_?[0-9]+)*(\.[0-9](_?[0-9]+)*)?)[eE]\-[0-9](_?[0-9]+)*)|([0-9](_?[0-9]+)*\.[0-9](_?[0-9]+)*)([eE][\+]?[0-9](_?[0-9]+)*)?'
    t.value = float(t.value.replace("_",""))
    return t

# -
def t_INTEGER(t):
    r'[0-9](_?[0-9]+)*([Ee](\+)?[0-9](_?[0-9]+)*)?'
    t.value = int(float(t.value.replace("_","")))   
    return t

# Define a rule so we can track line numbersg
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

ERROR_LIST=[]
# Error handling rule
def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    ERROR_LIST.append(t.value[0])
    t.lexer.skip(1)
