from antlr4 import *
from Interpreter.Python3Lexer import Python3Lexer
from Interpreter.Python3Parser import Python3Parser
from PythonListener import PythonListener

def print_tokens(input_string):
	input_stream = FileStream("input.py")
	lexer = Python3Lexer(input_stream)
	token_stream = CommonTokenStream(lexer)
	
	token_stream.fill()
	for token in token_stream.tokens:
		if token.type != -1 and token.type < len(lexer.symbolicNames):
			print(f"Token type: {lexer.symbolicNames[token.type]}, Token text: {repr(token.text)}")
		else:
			print(f"Token text: {repr(token.text)}")

# Main script
def evaluate_expression(input_string):
	# Create an input stream from the input string
	#input_stream = InputStream(input_string)
	input_stream = FileStream("input.py")
	# Create a lexer that reads from the input stream
	lexer = Python3Lexer(input_stream)
	
	# Create a token stream based on the lexer
	token_stream = CommonTokenStream(lexer)
	
	# Create a parser that reads from the token stream
	parser = Python3Parser(token_stream)
	
	# Specify the entry point rule
	entry_point = parser.program()
	
	# Create a custom listener to perform calculations during parsing
	listener = PythonListener()
	
	# Walk the parse tree with the listener
	walker = ParseTreeWalker()
	walker.walk(listener, entry_point)
	print(listener.var)
	# Return the result from the listener's stack
	return listener.stack.pop() if len(listener.stack) == 1 else None

# Example usage
input_string = [#"3 + 4 * (2 - 1)\n", 
				#"print(1 + 2, 5)\n",
				"def test(x,y):\n\treturn x+y\n"
				"test(5,4)"
				]
for input in input_string:
	print_tokens(input)
	result = evaluate_expression(input)
	print("Expression:", input)
	print("Result:", result)
	print("\n")

