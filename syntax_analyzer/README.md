Syntax Analyzer and Parse Tree Generator
=======================================

Grammer of Go Language

- program → declaration-list
- declaration-list → declaration-list declaration | declaration
- declaration → var-declaration | fun-declaration
- var-declaration → type-specifier var-decl-list ;
- scoped-var-declaration → scoped-type-specifier var-decl-list ;
- var-decl-list → var-decl-list , var-decl-initialize | var-decl-initialize
- var-decl-initialize → var-decl-id | var-decl-id : simple-expression
- var-decl-id → ID | ID [ NUMCONST ]
- scoped-type-specifier → static type-specifier | type-specifier
- type-specifier → int | bool | char
- fun-declaration → type-specifier ID ( params ) statement | ID ( params ) statement
- params → param-list | e
- param-list → param-list ; param-type-list | param-type-list
- param-type-list → type-specifier param-id-list
- param-id-list → param-id-list , param-id | param-id
- param-id → ID | ID [ ]
- statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt| break-stmt
- compound-stmt → { local-declarations statement-list }
- local-declarations → local-declarations scoped-var-declaration | e
- statement-list → statement-list statement | e
- expression-stmt → expression ; | ;
- selection-stmt → if ( simple-expression ) statement | if ( simple-expression ) statement else statement
- iteration-stmt → while ( simple-expression ) statement  | foreach ( mutable in simple-expression ) statement
- return-stmt → return ; | return expression ;
- break-stmt → break ;
- expression → mutable = expression | mutable += expression | mutable −= expression| mutable ∗= expression | mutable /= expression | mutable ++ | mutable −− | simple-expression
- simple-expression → simple-expression and-expression | and-expression
- and-expression → and-expression & unary-rel-expression | unary-rel-expression
- unary-rel-expression → ! unary-rel-expression | rel-expression
- rel-expression → sum-expression relop sum-expression | sum-expression 
- relop → <= | < | > | >= | == | ! =
- sum-expression → sum-expression sumop term | term
- sumop → + | −
- term → term mulop unary-expression | unary-expression
- mulop → ∗ | / | %
- unary-expression → unaryop unary-expression | factor
- unaryop → − | ∗ | ?
- factor → immutable | mutable
- mutable → ID | ID [ expression ]
- immutable → ( expression ) | call | constant
- call → ID ( args )
- args → arg-list | e
- arg-list → arg-list , expression | expression
- constant → NUMCONST | CHARCONST | STRINGCONST | true | false
