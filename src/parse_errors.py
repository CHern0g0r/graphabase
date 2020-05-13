from antlr4.error.ErrorListener import ErrorListener


class ParseErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("line " + str(line) + ":" + str(column) + " " + msg)
        raise ParseException


class ParseException(Exception):
    pass
