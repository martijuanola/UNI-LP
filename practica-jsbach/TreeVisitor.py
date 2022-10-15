# ---------- IMPORTS ---------- #

if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
    from .jsbachVisitor import jsbachVisitor
else:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor

# ---------- EXCEPTIONS ---------- #


def UndefinedIdent(object, ident):
    a = "Ident"
    b = "ident"
    if object == "var":
        a = "Var"
        b = "variable"
    elif object == "proc":
        a = "Proc"
        b = "proceudre"

    return "[Undef " + a + "]: Use of " + b + " [" + ident + "] without previous definition."


def UndefinedMain(ident):
    return "[Undef Main Function]: Main function [" + ident + "] was not declared."


def RedefinedFunction(ident):
    return "[Redefined Procedure]: Procedure [" + ident + "] was already defined."


def DivisionByZero():
    return "[Division By 0]"


def ElementOutOfBounds(var, elem):
    return "[Index Out Of Bounds]: Index [" + elem + "] is out of bounds for array [" + var + "]."


def NonMatchingNumParameters(func):
    return "[Non Matching Number Of Parameters]: In the call of function [" + func + "] the wrong number of parameters were specified."


def RepeatedParameter(func, var):
    return "[Repeated Parameter]: The paramater [" + var + "] is used multiple times in the function [" + func + "]"


def NoteOutOfRange(noteText):
    return "[Note Out Of Range]: The note [" + noteText + "] is out of the specified range(A0 - C8)"

# ---------- USEFUL FUNCTIONS & CLASSES ---------- #


def note2Int(noteText):
    note2BaseValue = {
        'C': -9,
        'D': -7,
        'E': -5,
        'F': -4,
        'G': -2,
        'A': 0,
        'B': 2
    }
    alterations = ['#', 'b']

    note = noteText[0]
    octave = '4'
    alter = ''

    if len(noteText) == 2:
        if noteText[1] in alterations:
            alter = noteText[1]
        else:
            octave = noteText[1]
    elif len(noteText) == 3:
        octave = noteText[1]
        alter = noteText[2]

    result = note2BaseValue.get(note) + 12*int(octave)

    if alter == '#':
        result += 1
    elif alter == 'b':
        result -= 1

    if result < 0 or result > 87:
        raise Exception(NoteOutOfRange(noteText))

    return result


class FunctionContext():
    def __init__(self, ctx):
        self.context = ctx

        self.parameters = []
        for param in self.context.ident():
            paramName = param.getText()
            if paramName in self.parameters:
                raise Exception(RepeatedParameter(
                    function.FUNC().getText(), paramName))
            self.parameters.append(paramName)


# ---------- VISITORS ---------- #

class TreeVisitor(jsbachVisitor):

    def __init__(self, main):
        # Functionc Info & Contexts
        self.functions = {}  # name -> functionContext
        self.main = main

        # SymbolsTables
        self.STstack = []
        self.STstack.append({})

        # Returned TreeVisitor values
        self.tempo = 120
        self.notes = []

        def printStack(self):
            for st in self.STstack[::-1]:
                print(st)

# ----- ROOT ----- #

    def visitRoot(self, ctx):
        for function in ctx.function():
            name = function.FUNC().getText()

            if name in self.functions:
                raise Exception(RedefinedFunction(name))
            else:
                self.functions[name] = FunctionContext(function)

        if not self.main in self.functions:
            raise Exception(UndefinedMain(self.main))

        self.visit(self.functions[self.main].context)

        return self.tempo, self.notes


# ----- FUNCTION ----- #


    def visitFunction(self, ctx):
        self.visit(ctx.statements())

        self.STstack.pop()
        return

        # ----- STATEMENTS ----- #

    def visitStatements(self, ctx):
        self.visitChildren(ctx)


# ----- STATEMENT ----- #


    def visitAssign(self, ctx):
        var = self.visit(ctx.ident())

        if ctx.expr():
            value = self.visit(ctx.expr())
            self.STstack[-1][var] = value
        elif ctx.exprList():
            newList = self.visit(ctx.exprList())
            self.STstack[-1][var] = newList

    def visitProcedureCall(self, ctx):
        funcName = ctx.FUNC().getText()

        if not funcName in self.functions:
            raise Exception(UndefinedIdent("proc", funcName))

        func = self.functions[funcName]

        if len(func.parameters) != len(ctx.expr()):
            raise Exception(NonMatchingNumParameters(funcName))

        newST = {}
        i = 0
        for param in func.parameters:
            expr = self.visit(ctx.expr(i))
            newST[param] = expr
            i += 1

        self.STstack.append(newST)
        self.visit(func.context)
        return

    def visitIf(self, ctx):
        expr = self.visit(ctx.expr())
        if expr:
            self.visit(ctx.statements(0))
        elif ctx.ELSE():
            self.visit(ctx.statements(1))

    def visitWhile(self, ctx):
        while self.visit(ctx.expr()):
            self.visit(ctx.statements())

    def visitRead(self, ctx):
        var = self.visit(ctx.ident())
        value = int(input())
        self.STstack[-1][var] = value
        # EXEPCIONS!!!

    def visitWrite(self, ctx):
        for element in list(ctx.getChildren())[1:]:
            print(self.visit(element), end=" ")
        print("")

    def visitPlay(self, ctx):
        if ctx.expr():
            newNoteVal = self.visit(ctx.expr())
            self.notes.append(newNoteVal)
        elif ctx.exprList():
            newNotes = self.visit(ctx.exprList())
            self.notes.extend(newNotes)

    def visitTempo(self, ctx):
        self.tempo = self.visit(ctx.expr())

    def visitListAppend(self, ctx):
        var = self.visit(ctx.ident())
        newElem = self.visit(ctx.expr())

        if not var in self.STstack[-1]:
            raise Exception(UndefinedIdent("var", var))

        self.STstack[-1][var].append(newElem)

    def visitListRemove(self, ctx):
        var = self.visit(ctx.ident())
        elem = self.visit(ctx.expr()) - 1

        if not var in self.STstack[-1]:
            raise Exception(UndefinedIdent("var", var))

        if var in self.STstack[-1]:
            raise Exception(UndefinedIdent("var", var))

        del self.STstack[-1][var][elem]


# ----- EXPR ----- #

    def visitParenthesis(self, ctx):
        return self.visit(ctx.expr())

    def visitUnary(self, ctx):
        value = self.visit(ctx.expr())
        if ctx.SUM():
            return value
        elif ctx.SUB():
            return -value

    def visitArithmetic(self, ctx):
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        if ctx.SUM():
            return expr1 + expr2
        elif ctx.SUB():
            return expr1 - expr2
        elif ctx.MUL():
            return expr1 * expr2
        elif ctx.DIV():
            if expr2 == 0:
                raise Exception(DivisionByZero())
            return expr1 / expr2
        elif ctx.MOD():
            return expr1 % expr2

    def visitRelational(self, ctx):
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        if ctx.LT():
            return expr1 < expr2
        elif ctx.LE():
            return expr1 <= expr2
        elif ctx.GT():
            return expr1 > expr2
        elif ctx.GE():
            return expr1 >= expr2

    def visitEquality(self, ctx):
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        if ctx.EQ():
            return expr1 == expr2
        elif ctx.NEQ():
            return expr1 != expr2

    def visitArrayLength(self, ctx):
        var = self.visit(ctx.ident())
        if not var in self.STstack[-1]:
            raise Exception(UndefinedIdent("var", var))

        return len(self.STstack[-1][var])

    def visitArrayElement(self, ctx):
        var = self.visit(ctx.ident())
        elem = self.visit(ctx.expr()) - 1

        if not var in self.STstack[-1]:
            raise Exception(UndefinedIdent("var", var))

        if elem >= len(self.STstack[-1][var]):
            raise Exception(ElementOutOfBounds(var, elem))

        return self.STstack[-1][var][elem]

    def visitVariable(self, ctx):
        var = self.visit(ctx.ident())
        if not var in self.STstack[-1]:
            raise Exception(UndefinedIdent("var", var))

        return self.STstack[-1][var]

    def visitNote(self, ctx):
        text = ctx.NOTE().getText()
        return note2Int(text)

    def visitValue(self, ctx):
        return int(ctx.NUM().getText())

# ----- LIST ----- #

    def visitExprList(self, ctx):
        l = []
        for expr in ctx.expr():
            l.append(self.visit(expr))
        return l

# ----- STRING ----- #

    def visitString(self, ctx):
        return ctx.STRING().getText()[1:-1]

# ----- IDENT ----- #

    def visitIdent(self, ctx):
        return ctx.VAR().getText()
