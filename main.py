from antlr4 import *
from Interpreter.MathGrammarLexer import MathGrammarLexer
from Interpreter.MathGrammarParser import MathGrammarParser
from MathListener import MathListener

def print_tokens(input_string):
    input_stream = InputStream(input_string)
    lexer = MathGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    token_stream.fill()
    for token in token_stream.tokens:
        print(f"Token type: {lexer.symbolicNames[token.type]}, Token text: {repr(token.text)}")

# Main script
def evaluate_expression(input_string):
    # Create an input stream from the input string
    input_stream = InputStream(input_string)
    
    # Create a lexer that reads from the input stream
    lexer = MathGrammarLexer(input_stream)
    
    # Create a token stream based on the lexer
    token_stream = CommonTokenStream(lexer)
    
    # Create a parser that reads from the token stream
    parser = MathGrammarParser(token_stream)
    
    # Specify the entry point rule
    entry_point = parser.expr()
    
    # Create a custom listener to perform calculations during parsing
    listener = MathListener()
    
    # Walk the parse tree with the listener
    walker = ParseTreeWalker()
    walker.walk(listener, entry_point)
    
    # Return the result from the listener's stack
    return listener.stack.pop() if len(listener.stack) == 1 else None

# Example usage
input_string = ["3 + 4 * (2 - 1)\n", 
                "print(1 + 2, 5)\n",
                #"elif"
				]
for input in input_string:
	print_tokens(input)
	result = evaluate_expression(input)
	print("Expression:", input)
	print("Result:", result)
	print("\n")

