all:
	@echo "This is a sort of cheat. We couldn't figure out how to make executables of python scripts, so we just compied entire ./src to ./bin :P"
	@echo "It works. It should"
	mkdir bin
	cp -r ./src/ply ./bin/ply
	cp ./src/lexer.py ./bin/lexer.py
	cp ./src/regexes.py ./bin/regexes.py
	cp ./src/tokens.py ./bin/tokens.py
	cp ./src/lexer ./bin/lexer
	chmod +x ./bin/lexer
clean:
	rm -r bin
