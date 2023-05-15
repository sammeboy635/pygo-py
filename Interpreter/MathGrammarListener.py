# Generated from MathGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MathGrammarParser import MathGrammarParser
else:
    from MathGrammarParser import MathGrammarParser

# This class defines a complete listener for a parse tree produced by MathGrammarParser.
class MathGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MathGrammarParser#prog.
    def enterProg(self, ctx:MathGrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by MathGrammarParser#prog.
    def exitProg(self, ctx:MathGrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by MathGrammarParser#stat.
    def enterStat(self, ctx:MathGrammarParser.StatContext):
        pass

    # Exit a parse tree produced by MathGrammarParser#stat.
    def exitStat(self, ctx:MathGrammarParser.StatContext):
        pass


    # Enter a parse tree produced by MathGrammarParser#function_call.
    def enterFunction_call(self, ctx:MathGrammarParser.Function_callContext):
        pass

    # Exit a parse tree produced by MathGrammarParser#function_call.
    def exitFunction_call(self, ctx:MathGrammarParser.Function_callContext):
        pass


    # Enter a parse tree produced by MathGrammarParser#arg_list.
    def enterArg_list(self, ctx:MathGrammarParser.Arg_listContext):
        pass

    # Exit a parse tree produced by MathGrammarParser#arg_list.
    def exitArg_list(self, ctx:MathGrammarParser.Arg_listContext):
        pass


    # Enter a parse tree produced by MathGrammarParser#function_def.
    def enterFunction_def(self, ctx:MathGrammarParser.Function_defContext):
        pass

    # Exit a parse tree produced by MathGrammarParser#function_def.
    def exitFunction_def(self, ctx:MathGrammarParser.Function_defContext):
        pass


    # Enter a parse tree produced by MathGrammarParser#arg_list_literal.
    def enterArg_list_literal(self, ctx:MathGrammarParser.Arg_list_literalContext):
        pass

    # Exit a parse tree produced by MathGrammarParser#arg_list_literal.
    def exitArg_list_literal(self, ctx:MathGrammarParser.Arg_list_literalContext):
        pass


    # Enter a parse tree produced by MathGrammarParser#suite.
    def enterSuite(self, ctx:MathGrammarParser.SuiteContext):
        pass

    # Exit a parse tree produced by MathGrammarParser#suite.
    def exitSuite(self, ctx:MathGrammarParser.SuiteContext):
        pass


    # Enter a parse tree produced by MathGrammarParser#expr.
    def enterExpr(self, ctx:MathGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by MathGrammarParser#expr.
    def exitExpr(self, ctx:MathGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by MathGrammarParser#term.
    def enterTerm(self, ctx:MathGrammarParser.TermContext):
        pass

    # Exit a parse tree produced by MathGrammarParser#term.
    def exitTerm(self, ctx:MathGrammarParser.TermContext):
        pass


    # Enter a parse tree produced by MathGrammarParser#factor.
    def enterFactor(self, ctx:MathGrammarParser.FactorContext):
        pass

    # Exit a parse tree produced by MathGrammarParser#factor.
    def exitFactor(self, ctx:MathGrammarParser.FactorContext):
        pass


    # Enter a parse tree produced by MathGrammarParser#number.
    def enterNumber(self, ctx:MathGrammarParser.NumberContext):
        pass

    # Exit a parse tree produced by MathGrammarParser#number.
    def exitNumber(self, ctx:MathGrammarParser.NumberContext):
        pass


