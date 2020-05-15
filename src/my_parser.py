from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr_parser.GramLexer import GramLexer
from antlr_parser.GramParser import GramParser
from my_listener import CustomListener
from parse_errors import ParseErrorListener
from script_listener import ScriptExecutor


def parse_from_file(input_file):
    istream = FileStream(input_file)
    lexer = GramLexer(istream)
    stream = CommonTokenStream(lexer)
    parser = GramParser(stream)
    parser.addErrorListener(ParseErrorListener)
    try:
        tree = parser.full_script()
        # print("parse done")
        return tree
    except Exception:
        # print("parse exception")
        return None


def print_tree(tree, output_file=None):
    walker = ParseTreeWalker()
    listener = CustomListener()
    walker.walk(listener, tree)
    if output_file is None:
        print(listener.dot)
    else:
        with open(output_file, 'w') as f:
            print(listener.dot, file=f)


def run_script(tree):
    walker = ParseTreeWalker()
    listener = ScriptExecutor()
    walker.walk(listener, tree)
    return listener


if __name__ == '__main__':
    i_f = input()
    # o_f = input()
    tree = parse_from_file(i_f)
    run_script(tree)
    # print_tree(tree, o_f)
