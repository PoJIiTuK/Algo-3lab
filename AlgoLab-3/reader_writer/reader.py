def read_graph_from_file(file_name, families):
    with open(file_name, "r", encoding='utf-8') as file:
        test_len = 1
        for line in file:
            if test_len == 1:
                a = line
                for line in file:
                    a, b = line.split(" ")
                    a = int(a)
                    b = int(b)
                    families.append((a, b))
                return families


def read_len_of_graph_from_file(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        test_len = 1
        for line in file:
            if test_len == 1:
                a = (line.split(" "))
                a = int(a[0])
                return a
