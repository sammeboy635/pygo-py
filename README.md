## Compiling antlr4
antlr4 Python3.g4 -o Interpreter -Dlanguage=Python3 
antlr4 -Dlanguage=Cpp -no-listener -visitor -o libs Python3.g4

antlr4-parse Python3.g4 prog -tokens -trace
antlr4-parse Python3.g4 prog -gui