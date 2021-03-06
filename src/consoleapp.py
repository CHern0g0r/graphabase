import rdf_utils
import dfa
# import src.rdf_utils as rdf_utils
# import src.dfa as dfa


class Control:
    is_running = True
    aut = None

    def __init__(self):
        self.is_loaded = False
        self.commands = {
            "load": self.load,
            "print": self.to_list,
            "request": self.request,
            "exit": self.exit,
            "help": self.help
        }

    def run(self):
        while self.is_running:
            user_input = list(map(str, input().split()))
            self.commands[user_input[0]](*(user_input[1:]))

    def load(self, *args):
        graph = rdf_utils.read_graph(args[0])
        self.is_loaded = True
        self.aut = dfa.graph_to_dfa(graph)

    def to_list(self, *args):
        for i in self.aut._input_symbols:
            print(i)

    def exit(self, *args):
        self.is_running = False

#   add honest checks and throwable
    def request(self, *args):
        if len(args) < 1:
            print("Enter request")
            return

        regex = ' '.join(list(args[0]))
        req = dfa.min_dfa_from_regex(
            dfa.string_to_regex(regex))
        inter = self.aut.get_intersection(req)

        if len(args) == 1:
            if inter.is_empty():
                print("Empty answer")
            else:
                print("Nonempty answer")
            return

        if len(args) == 2 and args[1] == "-ve":
            vertices = len(inter.states)
            edges = len(inter)
            print("Vertices: ", vertices)
            print("Edges: ", edges)
            return

        if len(args) == 3 and args[1] == "-dot":
            dfa.dfa_to_dot(inter, args[2])
            return

        print("Bad request")

    def help(self, *args):
        print("load <path> \t загрузить базу",
              "print \t вывести список ребер",
              "request <request> [-dot <path>, -ve] \t произвести запрос",
              sep='\n')


def main():
    control = Control()
    control.run()


if __name__ == "__main__":
    main()
