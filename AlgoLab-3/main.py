from reader_writer.writer import create_file
from help_method.helpers import duplicate
from help_method.helpers import female_amount
from help_method.helpers import male_amount
from reader_writer.reader import read_graph_from_file
from reader_writer.reader import read_len_of_graph_from_file
from help_method.brute_force import brute_force


def wedd(people, len_of_graph):
    print(people)

    families = brute_force(people, len_of_graph)

    male_in_family = [male_amount(family) for family in families]

    female_in_family = [female_amount(family) for family in families]
    print(families)
    print(male_in_family)
    print(female_in_family)

    all_pair = sum(male_in_family) * sum(female_in_family)

    duplicate_pair = sum(duplicate(male_in_family, female_in_family))

    create_file(all_pair - duplicate_pair)

    return all_pair - duplicate_pair


if __name__ == '__main__':
    graph = []
    graph = read_graph_from_file("test.in", graph)

    print("How much group: " + str(len(graph)) + " ;")
    res = wedd(graph, read_len_of_graph_from_file("test.in"))
    print(res)
