## Compiling antlr4
antlr4 MathGrammar.g4 -o Interpreter -Dlanguage=Python3 
antlr4 -Dlanguage=Cpp -no-listener -visitor -o libs MathGrammar.g4