"""
In the 5 by 5 matrix below, the minimal path sum from the top
left to the bottom right, by moving left, right, up, and down,
is indicated in bold red and is equal to 2297.

\begin{pmatrix}
\color{red}{131} & 673 & \color{red}{234} & \color{red}{103} & \color{red}{18}\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & \color{red}{150}\\
630 & 803 & 746 & \color{red}{422} & \color{red}{111}\\
537 & 699 & 497 & \color{red}{121} & 956\\
805 & 732 & 524 & \color{red}{37} & \color{red}{331}
\end{pmatrix}

Find the minimal path sum from the top left to the bottom
right by moving left, right, up, and down in matrix.txt (right
click and "Save Link/Target As..."), a 31K text file
containing an 80 by 80 matrix.
"""

import heapq


def parse(matfile):
    return [[int(n) for n in row.split(',')] for row in matfile]


def distance(a, b):
    return sum(abs(a[i] - b[i]) for i in range(len(a)))


def astar(matrix, targets, sources):
    def neighbors(position):
        (x, y) = position
        candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [(x, y) for (x, y) in candidates if x >= 0 and x < len(matrix)
                and y >= 0 and y < len(matrix[0])]

    def evaluate(path):
        f = sum(matrix[y][x] for (x, y) in path)
        h = min(distance(path[-1], target) for target in targets)
        return f + h

    targets = set(targets)
    frontier = set(sources)
    explored = set()
    frontier_queue = []
    for source in sources:
        path = [source]
        heapq.heappush(frontier_queue, (evaluate(path), path))

    while frontier:
        (_, path) = heapq.heappop(frontier_queue)
        frontier.remove(path[-1])
        explored.add(path[-1])
        if path[-1] in targets:
            return path
        for neighbor in neighbors(path[-1]):
            if neighbor not in frontier | explored:
                frontier.add(neighbor)
                new_path = path + [neighbor]
                heapq.heappush(frontier_queue, (evaluate(new_path), new_path))


with open("p083_matrix.txt") as matfile:
    matrix = parse(matfile)
targets = [(len(matrix) - 1, len(matrix[0]) - 1)]
sources = [(0, 0)]
print(sum(matrix[y][x] for (x, y) in astar(matrix, targets, sources)))
