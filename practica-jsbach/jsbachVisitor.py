# Generated from jsbach.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
else:
    from jsbachParser import jsbachParser

# This class defines a complete generic visitor for a parse tree produced by jsbachParser.

class jsbachVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx:jsbachParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#function.
    def visitFunction(self, ctx:jsbachParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#statements.
    def visitStatements(self, ctx:jsbachParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#assign.
    def visitAssign(self, ctx:jsbachParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#procedureCall.
    def visitProcedureCall(self, ctx:jsbachParser.ProcedureCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#if.
    def visitIf(self, ctx:jsbachParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#while.
    def visitWhile(self, ctx:jsbachParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#read.
    def visitRead(self, ctx:jsbachParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#write.
    def visitWrite(self, ctx:jsbachParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#play.
    def visitPlay(self, ctx:jsbachParser.PlayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#tempo.
    def visitTempo(self, ctx:jsbachParser.TempoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#listAppend.
    def visitListAppend(self, ctx:jsbachParser.ListAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#listRemove.
    def visitListRemove(self, ctx:jsbachParser.ListRemoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#arrayElement.
    def visitArrayElement(self, ctx:jsbachParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#note.
    def visitNote(self, ctx:jsbachParser.NoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#arrayLength.
    def visitArrayLength(self, ctx:jsbachParser.ArrayLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#variable.
    def visitVariable(self, ctx:jsbachParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#arithmetic.
    def visitArithmetic(self, ctx:jsbachParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#relational.
    def visitRelational(self, ctx:jsbachParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#unary.
    def visitUnary(self, ctx:jsbachParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#parenthesis.
    def visitParenthesis(self, ctx:jsbachParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#value.
    def visitValue(self, ctx:jsbachParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#equality.
    def visitEquality(self, ctx:jsbachParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#exprList.
    def visitExprList(self, ctx:jsbachParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#string.
    def visitString(self, ctx:jsbachParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#ident.
    def visitIdent(self, ctx:jsbachParser.IdentContext):
        return self.visitChildren(ctx)



del jsbachParser