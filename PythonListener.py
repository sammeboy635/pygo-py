from Interpreter.Python3Listener import Python3Listener
from Interpreter.Python3Parser import Python3Parser
_debug = True
import inspect

class PythonListener(Python3Listener):
	def __init__(self):
		self.stack = []
		self.module = {}
		self.var = {"x": 5 , "y":5}
		self.functions = {}

	def debug(self):
		if _debug:
			# Get the name of the function that called debug
			calling_function_name = inspect.stack()[1].function
			print(f"Debug: The function '{calling_function_name}' is being called.")




	# Exit a parse tree produced by Python3Parser#function_call.
	def exitFunction_call(self, ctx : Python3Parser.Function_callContext):
		self.debug()
		# Get the function name
		function_name = ctx.ID().getText()

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

    # Exit a parse tree produced by Python3Parser#function_def.
	def exitFunction_def(self, ctx : Python3Parser.Function_defContext):
		self.debug()
		# Get the function name
		function_name = ctx.ID().getText()
		# Get the number of arguments
		# Get the parameters
		params_ctx = ctx.params_id()
		if params_ctx is not None:
			params = [param.getText() for param in params_ctx.ID()]
		else:
			params = []
		
		print(f"Function call: {function_name}, Arguments: {params}, FBody: {ctx.suite().getText()}")

	def exitSuite(self, ctx:Python3Parser.SuiteContext):
		for stat in ctx.stat():
			print(stat.getText())
		self.debug()
	# Exit a parse tree produced by Python3Parser#prog.
	def exitProg(self, ctx : Python3Parser.ProgramContext):
		self.debug()
		return


	# Exit a parse tree produced by Python3Parser#stat.
	def exitStat(self, ctx : Python3Parser.StatContext):
		self.debug()
		return


	# Exit a parse tree produced by Python3Parser#expr.
	def exitExpr(self, ctx : Python3Parser.ExprContext):
		self.debug()
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

	# Exit a parse tree produced by Python3Parser#term.
	def exitTerm(self, ctx : Python3Parser.TermContext):
		self.debug()
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

	# Exit a parse tree produced by Python3Parser#factor.
	def exitFactor(self, ctx : Python3Parser.FactorContext):
		self.debug()
		if ctx.number():
			value = int(ctx.number().getText())
			print(value)
			self.stack.append(value)
		
		elif ctx.var():
			if ctx.var().getText() not in self.var:
				print("NO VAR")
				return 
			self.stack.append(self.var[ctx.var().getText()])

	# Exit a parse tree produced by Python3Parser#number.
	def exitNumber(self, ctx : Python3Parser.NumberContext):
		self.debug()
		if ctx.FLOAT():
			return float(ctx.FLOAT().getText())
			#self.stack.append(value)
		elif ctx.INTEGER():
			return int(ctx.INTEGER().getText())
			#self.stack.append(value)

	def exitAssignment(self, ctx : Python3Parser.AssignmentContext):
		self.debug()
		self.var[ctx.ID().getText()] = self.stack.pop()