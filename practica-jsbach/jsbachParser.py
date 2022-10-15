# Generated from jsbach.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,5,1,27,
        8,1,10,1,12,1,30,9,1,1,1,1,1,1,1,1,1,1,2,5,2,37,8,2,10,2,12,2,40,
        9,2,1,3,1,3,1,3,1,3,3,3,46,8,3,1,3,1,3,5,3,50,8,3,10,3,12,3,53,9,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,65,8,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,78,8,3,10,3,12,3,81,9,3,1,3,
        1,3,1,3,3,3,86,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,3,3,100,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,3,4,119,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,5,4,133,8,4,10,4,12,4,136,9,4,1,5,1,5,5,5,140,8,5,
        10,5,12,5,143,9,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,0,1,8,8,0,2,4,6,8,
        10,12,14,0,4,1,0,13,14,1,0,10,12,1,0,15,18,1,0,19,20,171,0,19,1,
        0,0,0,2,24,1,0,0,0,4,38,1,0,0,0,6,99,1,0,0,0,8,118,1,0,0,0,10,137,
        1,0,0,0,12,146,1,0,0,0,14,148,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,
        0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,19,
        1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,28,5,33,0,0,25,27,3,14,7,0,
        26,25,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,31,1,
        0,0,0,30,28,1,0,0,0,31,32,5,1,0,0,32,33,3,4,2,0,33,34,5,2,0,0,34,
        3,1,0,0,0,35,37,3,6,3,0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,
        0,38,39,1,0,0,0,39,5,1,0,0,0,40,38,1,0,0,0,41,42,3,14,7,0,42,45,
        5,21,0,0,43,46,3,8,4,0,44,46,3,10,5,0,45,43,1,0,0,0,45,44,1,0,0,
        0,46,100,1,0,0,0,47,51,5,33,0,0,48,50,3,8,4,0,49,48,1,0,0,0,50,53,
        1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,100,1,0,0,0,53,51,1,0,0,0,
        54,55,5,22,0,0,55,56,3,8,4,0,56,57,5,1,0,0,57,58,3,4,2,0,58,64,5,
        2,0,0,59,60,5,23,0,0,60,61,5,1,0,0,61,62,3,4,2,0,62,63,5,2,0,0,63,
        65,1,0,0,0,64,59,1,0,0,0,64,65,1,0,0,0,65,100,1,0,0,0,66,67,5,24,
        0,0,67,68,3,8,4,0,68,69,5,1,0,0,69,70,3,4,2,0,70,71,5,2,0,0,71,100,
        1,0,0,0,72,73,5,25,0,0,73,100,3,14,7,0,74,79,5,26,0,0,75,78,3,12,
        6,0,76,78,3,8,4,0,77,75,1,0,0,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,
        1,0,0,0,79,80,1,0,0,0,80,100,1,0,0,0,81,79,1,0,0,0,82,85,5,27,0,
        0,83,86,3,8,4,0,84,86,3,10,5,0,85,83,1,0,0,0,85,84,1,0,0,0,86,100,
        1,0,0,0,87,88,5,28,0,0,88,100,3,8,4,0,89,90,3,14,7,0,90,91,5,29,
        0,0,91,92,3,8,4,0,92,100,1,0,0,0,93,94,5,30,0,0,94,95,3,14,7,0,95,
        96,5,3,0,0,96,97,3,8,4,0,97,98,5,4,0,0,98,100,1,0,0,0,99,41,1,0,
        0,0,99,47,1,0,0,0,99,54,1,0,0,0,99,66,1,0,0,0,99,72,1,0,0,0,99,74,
        1,0,0,0,99,82,1,0,0,0,99,87,1,0,0,0,99,89,1,0,0,0,99,93,1,0,0,0,
        100,7,1,0,0,0,101,102,6,4,-1,0,102,103,5,5,0,0,103,104,3,8,4,0,104,
        105,5,6,0,0,105,119,1,0,0,0,106,107,7,0,0,0,107,119,3,8,4,10,108,
        109,5,7,0,0,109,119,3,14,7,0,110,111,3,14,7,0,111,112,5,3,0,0,112,
        113,3,8,4,0,113,114,5,4,0,0,114,119,1,0,0,0,115,119,3,14,7,0,116,
        119,5,31,0,0,117,119,5,34,0,0,118,101,1,0,0,0,118,106,1,0,0,0,118,
        108,1,0,0,0,118,110,1,0,0,0,118,115,1,0,0,0,118,116,1,0,0,0,118,
        117,1,0,0,0,119,134,1,0,0,0,120,121,10,9,0,0,121,122,7,1,0,0,122,
        133,3,8,4,10,123,124,10,8,0,0,124,125,7,0,0,0,125,133,3,8,4,9,126,
        127,10,7,0,0,127,128,7,2,0,0,128,133,3,8,4,8,129,130,10,6,0,0,130,
        131,7,3,0,0,131,133,3,8,4,7,132,120,1,0,0,0,132,123,1,0,0,0,132,
        126,1,0,0,0,132,129,1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,
        135,1,0,0,0,135,9,1,0,0,0,136,134,1,0,0,0,137,141,5,8,0,0,138,140,
        3,8,4,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,
        1,0,0,0,142,144,1,0,0,0,143,141,1,0,0,0,144,145,5,9,0,0,145,11,1,
        0,0,0,146,147,5,35,0,0,147,13,1,0,0,0,148,149,5,32,0,0,149,15,1,
        0,0,0,14,19,28,38,45,51,64,77,79,85,99,118,132,134,141
    ]

class jsbachParser ( Parser ):

    grammarFileName = "jsbach.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|:'", "':|'", "'['", "']'", "'('", "')'", 
                     "'#'", "'{'", "'}'", "'*'", "'/'", "'%'", "'+'", "'-'", 
                     "'<'", "'<='", "'>'", "'>='", "'='", "'/='", "'<-'", 
                     "'if'", "'else'", "'while'", "'<?>'", "'<!>'", "'<:>'", 
                     "'<t>'", "'<<'", "'8<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "MUL", "DIV", "MOD", "SUM", 
                      "SUB", "LT", "LE", "GT", "GE", "EQ", "NEQ", "ASSIGN", 
                      "IF", "ELSE", "WHILE", "READ", "WRITE", "PLAY", "TEMPO", 
                      "APPEND", "REMOVE", "NOTE", "VAR", "FUNC", "NUM", 
                      "STRING", "ESC_SEQ", "COMMENT", "WS" ]

    RULE_root = 0
    RULE_function = 1
    RULE_statements = 2
    RULE_statement = 3
    RULE_expr = 4
    RULE_exprList = 5
    RULE_string = 6
    RULE_ident = 7

    ruleNames =  [ "root", "function", "statements", "statement", "expr", 
                   "exprList", "string", "ident" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    MUL=10
    DIV=11
    MOD=12
    SUM=13
    SUB=14
    LT=15
    LE=16
    GT=17
    GE=18
    EQ=19
    NEQ=20
    ASSIGN=21
    IF=22
    ELSE=23
    WHILE=24
    READ=25
    WRITE=26
    PLAY=27
    TEMPO=28
    APPEND=29
    REMOVE=30
    NOTE=31
    VAR=32
    FUNC=33
    NUM=34
    STRING=35
    ESC_SEQ=36
    COMMENT=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(jsbachParser.EOF, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.FunctionContext)
            else:
                return self.getTypedRuleContext(jsbachParser.FunctionContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = jsbachParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.FUNC:
                self.state = 16
                self.function()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(jsbachParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(jsbachParser.FUNC, 0)

        def statements(self):
            return self.getTypedRuleContext(jsbachParser.StatementsContext,0)


        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.IdentContext)
            else:
                return self.getTypedRuleContext(jsbachParser.IdentContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = jsbachParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(jsbachParser.FUNC)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.VAR:
                self.state = 25
                self.ident()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self.match(jsbachParser.T__0)
            self.state = 32
            self.statements()
            self.state = 33
            self.match(jsbachParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.StatementContext)
            else:
                return self.getTypedRuleContext(jsbachParser.StatementContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = jsbachParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.IF) | (1 << jsbachParser.WHILE) | (1 << jsbachParser.READ) | (1 << jsbachParser.WRITE) | (1 << jsbachParser.PLAY) | (1 << jsbachParser.TEMPO) | (1 << jsbachParser.REMOVE) | (1 << jsbachParser.VAR) | (1 << jsbachParser.FUNC))) != 0):
                self.state = 35
                self.statement()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return jsbachParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PlayContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLAY(self):
            return self.getToken(jsbachParser.PLAY, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)

        def exprList(self):
            return self.getTypedRuleContext(jsbachParser.ExprListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlay" ):
                return visitor.visitPlay(self)
            else:
                return visitor.visitChildren(self)


    class ReadContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(jsbachParser.READ, 0)
        def ident(self):
            return self.getTypedRuleContext(jsbachParser.IdentContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


    class ProcedureCallContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNC(self):
            return self.getToken(jsbachParser.FUNC, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedureCall" ):
                return visitor.visitProcedureCall(self)
            else:
                return visitor.visitChildren(self)


    class ListRemoveContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REMOVE(self):
            return self.getToken(jsbachParser.REMOVE, 0)
        def ident(self):
            return self.getTypedRuleContext(jsbachParser.IdentContext,0)

        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListRemove" ):
                return visitor.visitListRemove(self)
            else:
                return visitor.visitChildren(self)


    class ListAppendContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self):
            return self.getTypedRuleContext(jsbachParser.IdentContext,0)

        def APPEND(self):
            return self.getToken(jsbachParser.APPEND, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListAppend" ):
                return visitor.visitListAppend(self)
            else:
                return visitor.visitChildren(self)


    class TempoContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEMPO(self):
            return self.getToken(jsbachParser.TEMPO, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTempo" ):
                return visitor.visitTempo(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(jsbachParser.WHILE, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)

        def statements(self):
            return self.getTypedRuleContext(jsbachParser.StatementsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(jsbachParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.StatementsContext)
            else:
                return self.getTypedRuleContext(jsbachParser.StatementsContext,i)

        def ELSE(self):
            return self.getToken(jsbachParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class WriteContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(jsbachParser.WRITE, 0)
        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.StringContext)
            else:
                return self.getTypedRuleContext(jsbachParser.StringContext,i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self):
            return self.getTypedRuleContext(jsbachParser.IdentContext,0)

        def ASSIGN(self):
            return self.getToken(jsbachParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)

        def exprList(self):
            return self.getTypedRuleContext(jsbachParser.ExprListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = jsbachParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = jsbachParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.ident()
                self.state = 42
                self.match(jsbachParser.ASSIGN)
                self.state = 45
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [jsbachParser.T__4, jsbachParser.T__6, jsbachParser.SUM, jsbachParser.SUB, jsbachParser.NOTE, jsbachParser.VAR, jsbachParser.NUM]:
                    self.state = 43
                    self.expr(0)
                    pass
                elif token in [jsbachParser.T__7]:
                    self.state = 44
                    self.exprList()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                localctx = jsbachParser.ProcedureCallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(jsbachParser.FUNC)
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 48
                        self.expr(0) 
                    self.state = 53
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 3:
                localctx = jsbachParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(jsbachParser.IF)
                self.state = 55
                self.expr(0)
                self.state = 56
                self.match(jsbachParser.T__0)
                self.state = 57
                self.statements()
                self.state = 58
                self.match(jsbachParser.T__1)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==jsbachParser.ELSE:
                    self.state = 59
                    self.match(jsbachParser.ELSE)
                    self.state = 60
                    self.match(jsbachParser.T__0)
                    self.state = 61
                    self.statements()
                    self.state = 62
                    self.match(jsbachParser.T__1)


                pass

            elif la_ == 4:
                localctx = jsbachParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.match(jsbachParser.WHILE)
                self.state = 67
                self.expr(0)
                self.state = 68
                self.match(jsbachParser.T__0)
                self.state = 69
                self.statements()
                self.state = 70
                self.match(jsbachParser.T__1)
                pass

            elif la_ == 5:
                localctx = jsbachParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.match(jsbachParser.READ)
                self.state = 73
                self.ident()
                pass

            elif la_ == 6:
                localctx = jsbachParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                self.match(jsbachParser.WRITE)
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 77
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [jsbachParser.STRING]:
                            self.state = 75
                            self.string()
                            pass
                        elif token in [jsbachParser.T__4, jsbachParser.T__6, jsbachParser.SUM, jsbachParser.SUB, jsbachParser.NOTE, jsbachParser.VAR, jsbachParser.NUM]:
                            self.state = 76
                            self.expr(0)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 81
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass

            elif la_ == 7:
                localctx = jsbachParser.PlayContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.match(jsbachParser.PLAY)
                self.state = 85
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [jsbachParser.T__4, jsbachParser.T__6, jsbachParser.SUM, jsbachParser.SUB, jsbachParser.NOTE, jsbachParser.VAR, jsbachParser.NUM]:
                    self.state = 83
                    self.expr(0)
                    pass
                elif token in [jsbachParser.T__7]:
                    self.state = 84
                    self.exprList()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 8:
                localctx = jsbachParser.TempoContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 87
                self.match(jsbachParser.TEMPO)
                self.state = 88
                self.expr(0)
                pass

            elif la_ == 9:
                localctx = jsbachParser.ListAppendContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 89
                self.ident()
                self.state = 90
                self.match(jsbachParser.APPEND)
                self.state = 91
                self.expr(0)
                pass

            elif la_ == 10:
                localctx = jsbachParser.ListRemoveContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 93
                self.match(jsbachParser.REMOVE)
                self.state = 94
                self.ident()
                self.state = 95
                self.match(jsbachParser.T__2)
                self.state = 96
                self.expr(0)
                self.state = 97
                self.match(jsbachParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return jsbachParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ArrayElementContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self):
            return self.getTypedRuleContext(jsbachParser.IdentContext,0)

        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayElement" ):
                return visitor.visitArrayElement(self)
            else:
                return visitor.visitChildren(self)


    class NoteContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOTE(self):
            return self.getToken(jsbachParser.NOTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNote" ):
                return visitor.visitNote(self)
            else:
                return visitor.visitChildren(self)


    class ArrayLengthContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self):
            return self.getTypedRuleContext(jsbachParser.IdentContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLength" ):
                return visitor.visitArrayLength(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self):
            return self.getTypedRuleContext(jsbachParser.IdentContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def MUL(self):
            return self.getToken(jsbachParser.MUL, 0)
        def DIV(self):
            return self.getToken(jsbachParser.DIV, 0)
        def MOD(self):
            return self.getToken(jsbachParser.MOD, 0)
        def SUM(self):
            return self.getToken(jsbachParser.SUM, 0)
        def SUB(self):
            return self.getToken(jsbachParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
            else:
                return visitor.visitChildren(self)


    class RelationalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def LT(self):
            return self.getToken(jsbachParser.LT, 0)
        def LE(self):
            return self.getToken(jsbachParser.LE, 0)
        def GT(self):
            return self.getToken(jsbachParser.GT, 0)
        def GE(self):
            return self.getToken(jsbachParser.GE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)


    class UnaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)

        def SUM(self):
            return self.getToken(jsbachParser.SUM, 0)
        def SUB(self):
            return self.getToken(jsbachParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class ValueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(jsbachParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)


    class EqualityContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def EQ(self):
            return self.getToken(jsbachParser.EQ, 0)
        def NEQ(self):
            return self.getToken(jsbachParser.NEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = jsbachParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = jsbachParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 102
                self.match(jsbachParser.T__4)
                self.state = 103
                self.expr(0)
                self.state = 104
                self.match(jsbachParser.T__5)
                pass

            elif la_ == 2:
                localctx = jsbachParser.UnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                _la = self._input.LA(1)
                if not(_la==jsbachParser.SUM or _la==jsbachParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 107
                self.expr(10)
                pass

            elif la_ == 3:
                localctx = jsbachParser.ArrayLengthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(jsbachParser.T__6)
                self.state = 109
                self.ident()
                pass

            elif la_ == 4:
                localctx = jsbachParser.ArrayElementContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.ident()
                self.state = 111
                self.match(jsbachParser.T__2)
                self.state = 112
                self.expr(0)
                self.state = 113
                self.match(jsbachParser.T__3)
                pass

            elif la_ == 5:
                localctx = jsbachParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.ident()
                pass

            elif la_ == 6:
                localctx = jsbachParser.NoteContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.match(jsbachParser.NOTE)
                pass

            elif la_ == 7:
                localctx = jsbachParser.ValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 117
                self.match(jsbachParser.NUM)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 132
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = jsbachParser.ArithmeticContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 120
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 121
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MUL) | (1 << jsbachParser.DIV) | (1 << jsbachParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 122
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = jsbachParser.ArithmeticContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 123
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 124
                        _la = self._input.LA(1)
                        if not(_la==jsbachParser.SUM or _la==jsbachParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 125
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = jsbachParser.RelationalContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 126
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 127
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.LT) | (1 << jsbachParser.LE) | (1 << jsbachParser.GT) | (1 << jsbachParser.GE))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 128
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = jsbachParser.EqualityContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 129
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 130
                        _la = self._input.LA(1)
                        if not(_la==jsbachParser.EQ or _la==jsbachParser.NEQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 131
                        self.expr(7)
                        pass

             
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_exprList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = jsbachParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(jsbachParser.T__7)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.SUM) | (1 << jsbachParser.SUB) | (1 << jsbachParser.NOTE) | (1 << jsbachParser.VAR) | (1 << jsbachParser.NUM))) != 0):
                self.state = 138
                self.expr(0)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(jsbachParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(jsbachParser.STRING, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = jsbachParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(jsbachParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(jsbachParser.VAR, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_ident

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)




    def ident(self):

        localctx = jsbachParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ident)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(jsbachParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




