from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr_parser.GramLexer import GramLexer
from antlr_parser.GramParser import GramParser
from my_listener import CustomListener
from parse_errors import ParseErrorListener


def parse_from_file(input_file, output_file=None):
    istream = FileStream(input_file)
    lexer = GramLexer(istream)
    stream = CommonTokenStream(lexer)
    parser = GramParser(stream)
    parser.addErrorListener(ParseErrorListener)
    try:
        tree = parser.full_script()
        print("parse done")
        walker = ParseTreeWalker()
        listener = CustomListener()
        walker.walk(listener, tree)
        if output_file is None:
            print(listener.dot)
        else:
            with open(output_file, 'w') as f:
                print(listener.dot, file=f)
        return tree
    except Exception:
        print("parse exception")
        return None


if __name__ == '__main__':
    i_f = input()
    o_f = input()
    parse_from_file(i_f, o_f)
