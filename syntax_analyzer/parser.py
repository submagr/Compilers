#!/usr/bin/python
import sys
sys.path.insert(0, '../lexical_analyzer/src')
sys.path.insert(0, '../')
from ply import yacc
from lexer import tokens, lexer

########################################
############# STATEMENTS ###############
########################################

def p_start(p):
	'''start : pkg_definition program'''

def p_program(p):
	'''program : ext_dec_lst program
				| func program 
				| e'''

def p_pkg_definition(p):
	'''pkg_definition : PACKAGE IDENTIFIER '''

def p_ext_dec_lst(p):
	'''ext_dec_lst : imports ext_dec_lst  
					| decs ext_dec_lst 
					| e'''

def p_imports(p):
	'''imports : IMPORT IDENTIFIER'''

def p_decs(p):
	'''decs : var_dec 
			| func_dec'''

def p_var_dec(p):
	'''var_dec : id_lst COLONEQ id_val_lst 
				| VAR temp1'''

def p_temp1(p):
	'''temp1 : id_lst temp2'''

def p_temp2(p):
	'''temp2 : EQUAL id_val_lst 
				| TYPE temp3'''

def p_temp3(p):
	'''temp3 : EQUAL id_val_lst
			| e '''

def p_id_lst(p):
	'''id_lst : IDENTIFIER COMMA id_lst 
			| IDENTIFIER'''

def p_id_val_lst(p):
	'''id_val_lst : num COMMA id_val_lst 
				| STRING id_val_lst 
				| num 
				| STRING   '''

def p_num(p):
	'''num : MINUS float_int 
			| PLUS float_int 
			| float_int '''

def p_float_int(p):
	'''float_int : FLOAT 
				| INTEGER'''

def p_func_dec(p):
	'''func_dec : FUNCTION IDENTIFIER LPAREN param_lst RPAREN ret_lst'''

def p_param_lst(p):
	'''param_lst : IDENTIFIER temp4'''

def p_temp4(p):
	'''temp4 : temp5 
			| temp6'''

def p_temp5(p):
	'''temp5 : TYPE temp7'''

def p_temp7(p):
	'''temp7 : COMMA IDENTIFIER temp7 
			| e'''

def p_temp6(p):
	'''temp6 : COMMA IDENTIFIER temp6 
			| TYPE '''

def p_ret_lst(p):
	'''ret_lst : TYPE
			| e
			| LPAREN temp8 RPAREN'''

def p_temp8(p):
	'''temp8 : temp9 
			| id_lst TYPE'''

def p_temp9(p):
	'''temp9 : TYPE COMMA temp9 
			| TYPE'''

def p_func(p):
	'''func : func_dec compound_stmt'''

def p_compound_stmt(p):
	'''compound_stmt : LPAREN stmt_lst RPAREN '''

def p_stmt_lst(p):
	'''stmt_lst : stmt stmt_lst 
				| stmt'''

def p_stmt(p):
	'''stmt : exp_stmt 
			| selection_stmt 
			| iteration_stmt 
			| return_stmt 
			| break_stmt 
			| continue_stmt'''

def p_exp_stmt(p):
	'''exp_stmt : mutable EQUAL sum_exp 
				| mutable PLUSEQ sum_exp 
				| mutable MINUSEQ sum_exp 
				| mutable TIMESEQ sum_exp 
				| mutable DIVIDEEQ sum_exp 
				| mutable PLUSPLUS 
				| mutable MINUSMIN 
				| simple_expression'''

def p_simple_expression(p):
	'''simple_expression :  simple_expression OROR and_expression 
						| and_expression'''

def p_and_expression(p):
	'''and_expression : and_expression AMPAMP unary_rel_expression 
					| unary_rel_expression'''

def p_unary_rel_expression(p):
	'''unary_rel_expression : NOT unary_rel_expression 
							| rel_expression'''

def p_rel_expression(p):
	'''rel_expression : factor relop factor 
					| factor'''

def p_relop(p):
	'''relop : LEQ 
			| GREAT 
			| LESS 
			| GEQ 
			| EQEQ 
			| NOTEQ '''


def p_sum_exp(p):
	'''sum_exp : sum_exp sumop term 
			| term'''

def p_sumop(p):
	'''sumop : PLUS 
			| MINUS 
			| OR 
			| CARET '''

def p_term(p):
	'''term : term mulop unary_expression 
			| unary_expression'''

def p_mulop(p):
	'''mulop : TIMES 
			| DIVIDE 
			| MOD 
			| GG 
			| LL 
			| AMPERS 
			| AMPCAR '''

def p_unary_expression(p):
	'''unary_expression : unaryop unary_expression 
						| factor'''

def p_unaryop(p):
	'''unaryop : MINUS 
				| TIMES 
				| PLUS '''


def p_factor(p):
	'''factor : immutable 
			| mutable'''

def p_mutable(p):
	'''mutable : TIMES mutable 
				| AMPERS mutable 
				| mutable LBRACE exp_stmt RBRACE 
				| LPAREN mutable RPAREN 
				| IDENTIFIER'''

def p_immutable(p):
	'''immutable : LPAREN exp_stmt RPAREN 
				| call 
				| num '''

def p_call(p):
	'''call : IDENTIFIER LPAREN args RPAREN'''

def p_args(p):
	'''args : arg_list 
			| e'''

def p_arg_list(p):
	'''arg_list : arg_list COMMA temp13 
				| temp13'''

def p_temp13(p):
	'''temp13 : simple_expression 
			| sum_exp '''

def p_selection_stmt(p):
	'''selection_stmt : IF simple_expression compound_stmt temp12'''

def p_temp12(p):
	'''temp12 : ELSE compound_stmt 
			| e'''

def p_iteration_stmt(p):
	'''iteration_stmt : FOR temp16 compound_stmt '''

def p_temp16(p):
	'''temp16 : simple_expression 
			| for_1 COLONEQ for_2 COLONEQ for_3     '''

def p_for_1(p):
	'''for_1 : IDENTIFIER temp14 sum_exp 
			| e'''

def p_temp14(p):
	'''temp14 : COLONEQ 
			| EQUAL '''

def p_for_2(p):
	'''for_2 : simple_expression 
			| e'''

def p_for_3(p):
	'''for_3 : exp_stmt 
			| e '''

def p_return_stmt(p):
	'''return_stmt : RETURN temp10 
					| e   '''

def p_temp10(p):
	'''temp10 : simple_expression 
			| sum_exp 
			| IDENTIFIER temp11 
			| float_int temp11'''

def p_temp11(p):
	'''temp11 : IDENTIFIER COMMA temp11 
			| float_int COMMA temp11 
			| e'''

def p_break_stmt(p):
	'''break_stmt : BREAK '''

def p_continue_stmt(p):
	'''continue_stmt : CONTINUE'''

########################################
def p_e(p):
	'''e :'''

########################################
############# ERROR ####################
########################################
def p_error(p):
	# Read ahead looking for a closing '''}'''
	tok = parser.token()
	if not tok:
		while 1:
			if not tok or tok.type in ['''SEP_SEMICOLON''', '''SEP_OPEN_BRACE''', '''SEP_CLOSE_BRACE''']:
				break
			tok = parser.token()             # Get the next token
		parser.restart()
		# parser.errok()

######################################################################################################
######## Required Globals ##############
parser = yacc.yacc()
########################################

def parseProgram(program):
	parser.parse(program, lexer=lexer)

# a function to test the parser
def testYacc(inputFile):
	program = open(inputFile).read()
	result = parser.parse(program, lexer=lexer)
	print result


if __name__ == "__main__":
	from sys import argv
	filename, inputFile = argv

	testYacc(inputFile)
