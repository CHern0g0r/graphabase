from src import dfa as DFA
from pyformlang.finite_automaton import finite_automaton
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton
from pyformlang.regular_expression import Regex

symb_a = finite_automaton.Symbol("a")
symb_b = finite_automaton.Symbol("b")
symb_c = finite_automaton.Symbol("c")
epsilon = finite_automaton.Epsilon()


def test_regex_to_epsilon_nfa():
    regex = Regex("(a-|a a b)*")
    enfa = regex.to_epsilon_nfa()
    assert (len(enfa.states) == 12)
    assert (not enfa.accepts([symb_a]))
    assert (enfa.accepts([symb_a, symb_a, symb_b, epsilon]))
    assert (not enfa.accepts([symb_c]))
    assert (enfa.accepts([epsilon]))
    assert (not enfa.accepts([symb_b, symb_a]))


def test_regex_to_min_dfa():
    regex = Regex("((b|a) a b)*")
    dfa = DFA.min_dfa_from_regex(regex)
    assert (len(dfa.states) == 3)
    assert(dfa.accepts([symb_b, symb_a, symb_b]))
    assert(dfa.accepts([symb_a, symb_a, symb_b, symb_a, symb_a, symb_b]))
    assert(not dfa.accepts([symb_a, symb_a, symb_b, symb_b]))
    assert(not dfa.accepts([symb_a, symb_a, symb_b, epsilon]))
    assert(not dfa.accepts([symb_c]))
    assert(not dfa.accepts([epsilon]))
    assert(not dfa.accepts([symb_b, symb_a]))


def test_string_to_min_dfa():
    s = "((b|a) a b)*"
    r = DFA.string_to_regex(s)
    dfa = DFA.min_dfa_from_regex(r)
    assert (len(dfa.states) == 3)
    assert(dfa.accepts([symb_b, symb_a, symb_b]))
    assert(dfa.accepts([symb_a, symb_a, symb_b, symb_a, symb_a, symb_b]))
    assert(not dfa.accepts([symb_a, symb_a, symb_b, symb_b]))
    assert(not dfa.accepts([symb_a, symb_a, symb_b, epsilon]))
    assert(not dfa.accepts([symb_c]))
    assert(not dfa.accepts([epsilon]))
    assert(not dfa.accepts([symb_b, symb_a]))


def test_dfa_intersection():
    regex = Regex("(a |a b c)*")
    dfa1 = DFA.min_dfa_from_regex(regex)
    regex = Regex("(a* | (a | b)*) c")
    dfa2 = DFA.min_dfa_from_regex(regex)
    new_dfa = dfa1.get_intersection(dfa2)
    assert (new_dfa.accepts([symb_a, symb_b, symb_c]))
    assert (new_dfa.accepts([symb_a, symb_a, symb_b, symb_c]))
    assert (not new_dfa.accepts([symb_a, symb_b, symb_c,
                                 symb_a, symb_b, symb_c]))


def test_nfa_intersection():
    nfa1 = NondeterministicFiniteAutomaton()
    state0 = finite_automaton.State(0)
    state1 = finite_automaton.State(1)
    state2 = finite_automaton.State(2)
    state3 = finite_automaton.State(3)
    nfa1.add_transition(state0, symb_a, state1)
    nfa1.add_transition(state0, symb_c, state2)
    nfa1.add_transition(state1, symb_a, state1)
    nfa1.add_transition(state1, symb_b, state2)
    nfa1.add_transition(state2, symb_a, state0)
    nfa1.add_transition(state0, symb_c, state3)
    nfa1.add_transition(state3, symb_a, state1)
    nfa1.add_start_state(state0)
    nfa1.add_final_state(state1)

    nfa2 = NondeterministicFiniteAutomaton()
    nfa2.add_transition(state0, symb_a, state1)
    nfa2.add_transition(state0, symb_b, state2)
    nfa2.add_transition(state1, symb_b, state2)
    nfa2.add_transition(state2, symb_c, state1)
    nfa2.add_transition(state2, symb_a, state0)
    nfa2.add_transition(state0, symb_c, state3)
    nfa2.add_transition(state3, symb_a, state1)
    nfa2.add_start_state(state0)
    nfa2.add_final_state(state1)
    new_nfa = nfa1.get_intersection(nfa2)
    assert (new_nfa.accepts([symb_a]))
    assert (new_nfa.accepts([symb_c, symb_a]))
    assert (new_nfa.accepts([symb_a, symb_b, symb_a, symb_a]))
    assert (not new_nfa.accepts([symb_c, symb_b]))
    assert (not new_nfa.accepts([symb_a, symb_a]))
    assert (not new_nfa.accepts([symb_b]))
