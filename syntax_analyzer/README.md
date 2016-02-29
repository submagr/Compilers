Syntax Analyzer and Parse Tree Generator
=======================================
Things to be handled in go
1. var declarations too many formats
2. function declarations
3.


Grammer for Go Language:

1.  start → pkg-def program
2.  program → ext-dec | func
3.  pkg-def → PACKAGE IDENTIFIER 
-----------------------------------------------------------------------
4.  ext-dec → imports | decs
5.  imports → IMPORT IDENTIFIER
6.  decs → var-dec | func-dec
-----------------------------------------------------------------------
7.  var-dec → id-lst COLONEQ id-val-lst | VAR temp1
8.  temp1 → id-lst temp2				                      |	#TODO : handle 1 
9.  temp2 → EQUAL id-val-lst | TYPE temp3
10. temp3 → EQUAL id-val-lst | e 
11. id-lst → IDENTIFIER COMMA id-lst | IDENTIFIER
12. id-val-lst → num | STRING   
13. num → MINUS float-int | float-int 
14. float-int → FLOAT | INT
-----------------------------------------------------------------------
15. func-dec => FUNCTION IDENTIFIER LPAREN param-lst RPAREN ret-lst
16. param-lst => IDENTIFIER temp4
17. temp4 => temp5 | temp6
18. temp5 => TYPE temp7
19. temp7 => COMMA IDENTIFIER temp7 | e
20. temp6 => COMMA IDENTIFIER temp6 | TYPE 
21. ret-lst => TYPE | e | LPAREN temp8 RPAREN
22. temp8 => temp9 | id-lst TYPE
23. temp9 => TYPE COMMA temp9 | TYPE
-----------------------------------------------------------------------
24. func => func-dec compound-stmt
25. compound-stmt => LPAREN stmt-lst RPAREN 
26. stmt-lst => stmt stmt-lst | stmt
27. stmt => exp-stmt | selection-stmt | iteration-stmt | return-stmt | break-stmt 
-----------------------------------------------------------------------
29. exp-stmt => mutable EQUAL exp-stmt | mutable PLUSEQ exp-stmt | mutable MINUSEQ exp-stmt | mutable TIMESEQ exp-stmt | mutable DIVIDEEQ exp-stmt | mutable PLUSPLUS | mutable MINUSMIN | simple-expression
27. simple-expression → simple-expression OR and-expression | and-expression
28. and-expression → and-expression & unary-rel-expression | unary-rel-expression
29. unary-rel-expression → ! unary-rel-expression | rel-expression
30. rel-expression → sum-expression relop sum-expression | sum-expression
31. relop → <= | < | > | >= | == | ! =
32. sum-expression → sum-expression sumop term | term
33. sumop → + | −
34. term → term mulop unary-expression | unary-expression
35. mulop → ∗ | / | %
36. unary-expression → unaryop unary-expression | factor
37. unaryop → − | ∗ 
38. factor → immutable | mutable
39. mutable → TIMES mutable | AMPERS mutable | mutable LBRACK expr-stmt RBRACK | IDENTIFIER
40. immutable → ( expr-stmt ) | call | constant
41. call → ID ( args )
42. args → arg-list | e
43. arg-list → arg-list , expr-stmt | exp-stmt
44. constant → CONSTANT| true | false


**Comments**:
1. mutable means a, b[exp-stmt], something to which we can assign something
2. exp-stmt means anything that evaluates to a value
3. 

**Things not handled** :
1. 
    var (
    	ToBe   bool       = false
    	MaxInt uint64     = 1<<64 - 1
    	z      complex128 = cmplx.Sqrt(-5 + 12i)
    	k int
    )
2.


**Example Grammar of C- Language**

1. program → declaration-list
2. declaration-list → declaration-list declaration | declaration
3. declaration → var-declaration | fun-declaration
4. var-declaration → type-specifier var-decl-list ;
5. scoped-var-declaration → scoped-type-specifier var-decl-list ;
6. var-decl-list → var-decl-list , var-decl-initialize | var-decl-initialize
7. var-decl-initialize → var-decl-id | var-decl-id : simple-expression
8. var-decl-id → ID | ID [ NUMCONST ]
9. scoped-type-specifier → static type-specifier | type-specifier
10. type-specifier → int | bool | char
11. fun-declaration → type-specifier ID ( params ) statement | ID ( params ) statement
12. params → param-list | e
13. param-list → param-list ; param-type-list | param-type-list
14. param-type-list → type-specifier param-id-list
15. param-id-list → param-id-list , param-id | param-id
16. param-id → ID | ID [ ]
17. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt| break-stmt
18. compound-stmt → { local-declarations statement-list }
19. local-declarations → local-declarations scoped-var-declaration | e
20. statement-list → statement-list statement | e
21. expression-stmt → expression ; | ;
22. selection-stmt → if ( simple-expression ) statement | if ( simple-expression ) statement else statement
23. iteration-stmt → while ( simple-expression ) statement | foreach ( mutable in simple-expression ) statement 
24. return-stmt → return ; | return expression ;
25. break-stmt → break ;
26. expression → mutable = expression | mutable += expression | mutable −= expression | mutable ∗= expression | mutable /= expression | mutable ++ | mutable −− | simple- expression
27. simple-expression → simple-expression and-expression | and-expression
28. and-expression → and-expression & unary-rel-expression | unary-rel-expression
29. unary-rel-expression → ! unary-rel-expression | rel-expression
30. rel-expression → sum-expression relop sum-expression | sum-expression
31. relop → <= | < | > | >= | == | ! =
32. sum-expression → sum-expression sumop term | term
33. sumop → + | −
34. term → term mulop unary-expression | unary-expression
35. mulop → ∗ | / | %
36. unary-expression → unaryop unary-expression | factor
37. unaryop → − | ∗ | ?
38. factor → immutable | mutable
39. mutable → ID | ID [ expression ]
40. immutable → ( expression ) | call | constant
41. call → ID ( args )
42. args → arg-list | e
43. arg-list → arg-list , expression | expression
44. constant → NUMCONST | CHARCONST | STRINGCONST | true | false


References 
==========

- https://gobyexample.com/variables
- https://github.com/luciotato/golang-notes/blob/master/OOP.md
