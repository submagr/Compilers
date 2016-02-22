import sys
sys.path.insert(0,'./ply')
import ply.lex as lex
from regexes import *

Toks={}
for a in tokens:
    Toks[a]=[a,0]

#Scanning the file name
if (len(sys.argv) == 1):
    file_name =raw_input( "Give a GO file to lexer: ")
else:
    file_name = sys.argv[1]

try:
    lexer = lex.lex()
    with open(file_name) as fp:
        data = fp.read()
        data += '\n'
        lexer.input(data)
        print "Tokens \t\t Occurances\t\tLexemes"
        for tok in lexer:
            Toks[tok.type][1]=Toks[tok.type][1]+1
            if tok.value in Toks[tok.type]: continue
            Toks[tok.type].append(tok.value)

       	for x in Toks:
            if Toks[x][1]!=0 :
                print "-"*64
                print Toks[x][0],"\n\t\t\t",Toks[x][1],"\t\t",Toks[x][2]
                for i in range(3,len(Toks[x])):
                    print "\t\t\t\t\t",Toks[x][i]

        print "-"*64,'\nIllegal list'
        for i in range(0,len(ERROR_LIST)):
            print ERROR_LIST[i]+"\t",
        print "\n","-"*64

except IOError as e:
    print "I/O error({0}): "+ "We are not able to open " + file_name + " . Does it Exists? Check permissionsi!"
