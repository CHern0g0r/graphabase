from tokenize import String
from pyformlang.regular_expression import Regex


def min_dfa_from_regex(r: Regex):
    return r.to_epsilon_nfa().to_deterministic().minimize()


def string_to_regex(s: String):
    return Regex(s)
