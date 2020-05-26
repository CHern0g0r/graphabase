from hellings import Graph
from networkx import transitive_closure, tensor_product, \
    union, relabel_nodes, DiGraph
from pyformlang.regular_expression import Regex
from weak_cfg import Weak_chom_cfg
from my_gram_parser import parse_rule


def rules_to_nx(gram_rules):
    graph = DiGraph()
    rename = {}
    nonterms = set()
    from_nont = {}
    for left, right in gram_rules:
        nonterms.add(left)
        list(map(lambda y: nonterms.add(y),
             filter(lambda x: x.isupper(), right.split())))
    cnt = 0
    for left, right in gram_rules:
        nfa = Regex(right).to_epsilon_nfa().minimize()
        subgraph = nfa.to_networkx()
        for node in [n for n in subgraph.nodes
                     if not subgraph.nodes[n]['label']]:
            subgraph.remove_node(node)
        for v in sorted(subgraph.nodes):
            rename[v] = cnt
            cnt += 1
        subgraph = relabel_nodes(subgraph, rename)
        for edge in subgraph.edges:
            subgraph.edges[edge]['label'] = [subgraph.edges[edge]['label']]
        subgraph = DiGraph(subgraph)
        graph = union(graph, subgraph)
        for node in subgraph.nodes:
            from_nont[node] = left
    return graph, nonterms, from_nont


def tensor_prod(g1, g2):
    prod = tensor_product(g1, g2)
    remove = []
    for edge in prod.edges:
        v, u = prod.edges[edge]['label']
        intersect = set(v).intersection(set(u))
        if intersect:
            prod.edges[edge]['label'] = list(intersect)
        else:
            remove += [edge]
    list(map(lambda e: prod.remove_edge(e[0], e[1]), remove))
    return DiGraph(prod)


def eval_tensor_cfr(graph: Graph, gram_rules, gram: Weak_chom_cfg):
    m1, nonterms, from_nont = rules_to_nx(gram_rules)
    m2 = graph.to_digraph()
    # add loops
    eps_prod = list(gram.get_eps_gen_nonterm())
    if eps_prod:
        for i in range(len(m2.nodes)):
            m2.add_edge(i, i, label=[])
            for nont in nonterms:
                if nont in eps_prod:
                    m2[i][i]['label'] = m2[i][i]['label'] + [nont]

    flag = True
    while flag:
        flag = False
        m = tensor_prod(m1, m2)
        tcl = transitive_closure(m)
        for e in tcl.edges(data='label'):
            s = e[0][0]
            f = e[1][0]
            if m1.nodes[s]['is_start'] and m1.nodes[f]['is_final']:
                x = e[0][1]
                y = e[1][1]
                add = from_nont[s]
                if y not in m2[x].keys():
                    m2.add_edge(x, y, label=[add])
                    flag = True
                elif add not in m2[x][y]['label']:
                    m2[x][y]['label'].append(add)
                    flag = True

    return m2


def handle_res(res, resfile):
    with open(resfile, 'w') as f:
        for edge in res.edges(data='label'):
            if 'S' in edge[2]:
                f.write('{} {}\n'.format(edge[0], edge[1]))


if __name__ == '__main__':
    # gram_file = input()
    # graph_file = input()
    # res_file = input()
    gram_file = '/home/chernogor/Workspace/TFL/graphabase/test/res/gram8.txt'
    graph_file = '/home/chernogor/Workspace/TFL/graphabase/test/res/graph2.txt'
    res_file = 'res.txt'
    g = Graph()
    g.read_from_file(graph_file)
    c = Weak_chom_cfg()
    with open(gram_file) as f:
        lines = f.readlines()
    lines = [(i[0], ' '.join(i[1:])) for i in map(lambda x: x.split(), lines)]
    for left, right in lines:
        rules = parse_rule(left, right, c)
        for left, right in rules:
            c.new_rule(left, right)
    res = eval_tensor_cfr(g, lines, c)
    handle_res(res, res_file)
