from my_gram_listener import MyRuleListener
from antlr_regex.RuleLexer import RuleLexer
from antlr_regex.RuleParser import RuleParser
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from weak_cfg import Weak_chom_cfg


def parse_rule(left, right, gram: Weak_chom_cfg):
    istream = InputStream(right)
    lexer = RuleLexer(istream)
    stream = CommonTokenStream(lexer)
    parser = RuleParser(stream)

    try:
        tree = parser.regex()
        walker = ParseTreeWalker()
        listener = MyRuleListener(left, gram)
        walker.walk(listener, tree)
        return listener.rules
    except Exception:
        print(str(Exception))
        return None


if __name__ == '__main__':
    c = Weak_chom_cfg()
    parse_rule('S', '(a a a)*', c)
