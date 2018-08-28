import random
import os


def branch_gen(random_edge, vertices_number, min_range, max_range, sign):
    """
    This function generate branch and weight vector of each vertex
    :param sign:
    :param random_edge: number of vertex edges
    :type random_edge:int
    :param vertices_number: number of vertices
    :type vertices_number:int
    :param min_range: weight min range
    :type min_range:int
    :param max_range: weight max range
    :type max_range:int
    :return: branch and weight list
    """
    index = 0
    branch_list = []
    weight_list = []

    while index < random_edge:
        random_tail = random.randint(sign + 1, vertices_number + 1)
        if sign == 2:
            random_weight = random.randint(min_range, max_range)
        else:
            random_weight = random.randint(min_range, max_range)
        if (random_tail not in branch_list) and (random_tail != sign):
            branch_list.append(random_tail)
            weight_list.append(random_weight)
            index += 1
    return [branch_list, weight_list]


def edge_gen(vertices_number, min_range, max_range, min_edge, max_edge, sign):
    """
    This function generate each vertex connection number
    :param vertices_number: number of vertices
    :type vertices_number:int
    :param min_range: weight min_range
    :type min_range:int
    :param max_range: weight max_range
    :type max_range:int
    :return: list of 2 dictionary
    """
    temp = 0
    vertices_id = list(range(1, vertices_number + 1))
    vertices_edge = []
    weight_list = []
    i = 0
    while i < len(vertices_id):
        i += 1
        random_edge = random.randint(min_edge, min(max_edge, vertices_number - i) + 1)
        temp_list = branch_gen(
            random_edge, vertices_number, min_range, max_range, i)
        vertices_edge.append(temp_list[0])
        weight_list.append(temp_list[1])
        temp = temp + random_edge
    return [dict(zip(vertices_id, vertices_edge)), dict(zip(vertices_id, weight_list)), temp]


""" a = []
N = 10000
for x in range(N):
    a.append(random.randint(1, 3))

# Open a file
fo = open("foo.txt", "w")

n = random.randint(6, 10)

fo.write(str(n) + "\n")

for i in range(n):
    l = random.randint(0, N - 100)
    r = random.randint(l + 1, min(l + 100, N))
    fo.write(str(r - l) + " ")
    fo.write(" ".join(str(x) for x in a[l:r]))
    fo.write("\n")


# Close opened file
fo.close()

os.system("./a.out") """
n = random.randint(2, 15)
a = edge_gen(n, 0, 1, 0, n - 1, 1)

edges = a[0]
edgeCount = a[2]
print(edgeCount)
# Open a file
fo = open("foo.txt", "w")

fo.write(str(n) + " " + str(edgeCount) + "\n")

for vertex in edges:
    for tail in edges[vertex]:
        fo.write(str(vertex) + " " + str(tail) + "\n")


# Close opened file
fo.close()
os.system("g++ problem.cpp")
os.system("./a.out")