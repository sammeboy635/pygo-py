from Interpreter.MathGrammarListener import MathGrammarListener
from Interpreter.MathGrammarParser import MathGrammarParser

class MathListener(MathGrammarListener):
	def __init__(self):
		self.stack = []
		self.module = {}


	# Enter a parse tree produced by MathGrammarParser#function_call.
	def enterFunction_call(self, ctx:MathGrammarParser.Function_callContext):
		pass

	# Exit a parse tree produced by MathGrammarParser#function_call.
	def exitFunction_call(self, ctx : MathGrammarParser.Function_callContext):
		# Get the function name
		function_name = ctx.LITERAL().getText()

		# Get the number of arguments
		num_arguments = len(ctx.arg_list().expr())

		# Pop the evaluated arguments off the stack
		arguments = [self.stack.pop() for _ in range(num_arguments)]
		arguments.reverse()
		# Print the function name and arguments
		print(f"Function call: {function_name}, Arguments: {arguments}")

		# Make a makeshift function call
		if function_name == "print":
			print(*arguments)

    # Exit a parse tree produced by MathGrammarParser#function_def.
	def exitFunction_def(self, ctx : MathGrammarParser.Function_defContext):
		print(ctx.getText())


	# # Enter a parse tree produced by MathGrammarParser#arg_list.
	# def enterArg_list(self, ctx:MathGrammarParser.Arg_listContext):
	# 	pass

	# # Exit a parse tree produced by MathGrammarParser#arg_list.
	# def exitArg_list(self, ctx : MathGrammarParser.Arg_listContext):
	# 	print("Arguments: ", ctx.getText())

	# Enter a parse tree produced by MathGrammarParser#prog.
	# def enterProg(self, ctx : MathGrammarParser.ProgContext):
	# 	return

	# Exit a parse tree produced by MathGrammarParser#prog.
	def exitProg(self, ctx : MathGrammarParser.ProgContext):
		return


	# Enter a parse tree produced by MathGrammarParser#stat.
	# def enterStat(self, ctx : MathGrammarParser.StatContext):
	# 	return

	# Exit a parse tree produced by MathGrammarParser#stat.
	def exitStat(self, ctx : MathGrammarParser.StatContext):
		return


	# Enter a parse tree produced by MathGrammarParser#expr.
	# def enterExpr(self, ctx : MathGrammarParser.ExprContext):
	# 	return

	# Exit a parse tree produced by MathGrammarParser#expr.
	def exitExpr(self, ctx : MathGrammarParser.ExprContext):
		if ctx.ADDITION():
			right = self.stack.pop()
			left = self.stack.pop()
			self.stack.append(left + right)
			print(f"{left}+{right}")
		if ctx.SUBTRACTION():
			right = self.stack.pop()
			left = self.stack.pop()
			self.stack.append(left - right)
			print(f"{left}-{right}")



	# Enter a parse tree produced by MathGrammarParser#term.
	# def enterTerm(self, ctx : MathGrammarParser.TermContext):
	# 	return

	# Exit a parse tree produced by MathGrammarParser#term.
	def exitTerm(self, ctx : MathGrammarParser.TermContext):
		if ctx.MULTIPLICATION():
			right = self.stack.pop()
			left = self.stack.pop()
			self.stack.append(left * right)
			print(f"{left}*{right}")
		elif ctx.DIVISION():
			right = self.stack.pop()
			left = self.stack.pop()
			self.stack.append(left / right)
			print(f"{left}/{right}")



	# Enter a parse tree produced by MathGrammarParser#factor.
	# def enterFactor(self, ctx : MathGrammarParser.FactorContext):
	# 	pass

	# Exit a parse tree produced by MathGrammarParser#factor.
	def exitFactor(self, ctx : MathGrammarParser.FactorContext):
		if ctx.number():
			value = int(ctx.number().getText())
			print(value)
			self.stack.append(value)


	# Enter a parse tree produced by MathGrammarParser#number.
	# def enterNumber(self, ctx : MathGrammarParser.NumberContext):
	# 	pass

	# Exit a parse tree produced by MathGrammarParser#number.
	def exitNumber(self, ctx : MathGrammarParser.NumberContext):
		if ctx.FLOAT():
			return float(ctx.FLOAT().getText())
			#self.stack.append(value)
		elif ctx.INTEGER():
			return int(ctx.INTEGER().getText())
			#self.stack.append(value)


