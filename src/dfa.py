from tokenize import String
from pyformlang.regular_expression import Regex
from rdflib import Graph
from pygraphviz import AGraph
from pyformlang.finite_automaton import State
from pyformlang.finite_automaton import EpsilonNFA
from pyformlang.finite_automaton import Symbol
from pyformlang.finite_automaton import Epsilon
from pyformlang.finite_automaton import DeterministicFiniteAutomaton


def min_dfa_from_regex(r: Regex):
    return r.to_epsilon_nfa().to_deterministic().minimize()


def string_to_regex(s: String):
    return Regex(s)


def minimize_dfa(d: DeterministicFiniteAutomaton):
    return d.minimize()


def graph_to_dfa(g: Graph):
    nfa = EpsilonNFA()
    state_count = 0
    for tup in g:
        sub, pred, obj = map(str, tup)
        # nfa.add_transition(State(sub), Symbol(pred), State(obj))
        nfa.add_start_state(State(sub))
        nfa.add_start_state(State(obj))
        nfa.add_final_state(State(sub))
        nfa.add_final_state(State(obj))

        nfa.add_transition(State(sub), Epsilon(), State(state_count))
        for c in pred:
            nfa.add_transition(State(state_count),
                               Symbol(c),
                               State(state_count+1))
            state_count += 1
        nfa.add_transition(State(state_count),
                           Epsilon(),
                           State(obj))
    return nfa.to_deterministic()


def dfa_to_dot(graph: DeterministicFiniteAutomaton, path):
    g = AGraph(directed=True, strict=False)
    for s, p, o in graph:
        g.add_edge(str(s), str(o), str(p))
    with open(path, "w") as f:
        print(g, file=f)
