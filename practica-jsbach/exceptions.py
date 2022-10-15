def UndefinedIdent(object,ident):
	a = "Ident"
	b = "ident"
	if object == "var":
		a = "Var"
		b = "variable"
	elif object == "proc":
		a = "Proc"
		b = "proceudre"
		
	return "[Undef " + a + "]: Use of " + b + " [" + ident +"] without previous definition."


def UndefinedMain(ident):
	return "[Undef Main Function]: Main function [" + ident +"] was not declared."

def RedefinedFunction(ident):
	return "[Redefined Procedure]: Procedure [" + ident +"] was already defined."

def DivisionByZero():
	return "[Division By 0]"

def ElementOutOfBounds(var,elem):
	return "[Index Out Of Bounds]: Index [" + elem +"] is out of bounds for array [" + var + "]."

def NonMatchingNumParameters(func):
	return "[Non Matching Number Of Parameters]: In the call of function [" + func + "] the wrong number of parameters were specified."

def RepeatedParameter(func,var):
	return "[Repeated Parameter]: The paramater [" + var + "] is used multiple times in the function [" + func +"]"

def	NoteOutOfRange(noteText):
	return "[Note Out Of Range]: The note [" + noteText +"] is out of the specified range(A0 - C8)"