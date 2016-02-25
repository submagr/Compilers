Syntax Analyzer and Parse Tree Generator
=======================================

Grammer of Go Language

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
12. params → param-list |
13. param-list → param-list ; param-type-list | param-type-list
14. param-type-list → type-specifier param-id-list
15. param-id-list → param-id-list , param-id | param-id
16. param-id → ID | ID [ ]
17. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt| break-stmt
18. compound-stmt → { local-declarations statement-list }
19. local-declarations → local-declarations scoped-var-declaration |
20. statement-list → statement-list statement |
21. expression-stmt → expression ; | ;
22. selection-stmt → if ( simple-expression ) statement | if ( simple-expression ) statement else statement
23. iteration-stmt → while ( simple-expression ) statement expression ) statement | foreach ( mutable in simple-
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
42. args → arg-list |
43. arg-list → arg-list , expression | expression
44. constant → NUMCONST | CHARCONST | STRINGCONST | true | false
