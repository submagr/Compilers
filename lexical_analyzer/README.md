

Lexer for tokenizing GO Lang programmes - An implementation in python

The lexer requires  a execuatble instance of python2.7 in /usr/bin 


Building
=========
run make to build the bin directory

	make

to run the program set the working directory to assgn1 and execute lexer

	./bin/lexer ./test/test3.go

This will generate tabulated output to STDOUT
The table contains 3 columns (TOKEN.name | OCCURANCES | TOKEN.Value)


+ Identical tokens of same kind will be clubbed together


Project group
=============
 + Akash Waghela        (13064)
 + Manikanta Reddy D    (13265)
 + Parag Bansal         (13464)
 + Shubham Agrawal      (13674)

Reading
========

 + https://golang.org/ref/spec#Lexical_elements