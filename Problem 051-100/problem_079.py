# Project Euler

# Problem 79: Passcode derivation

# A common security method used for online banking is to ask the user for three random characters from a passcode.
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
# the expected reply would be: 317.
# The next list of numbers, contains fifty successful login attempts.
# 319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716
# Given that the three characters are always asked for in order,
# analyse the file so as to determine the shortest possible secret passcode of unknown length.

import time


def main():
    start_time = time.time()

    with open('problem_079_keylog.txt', 'r') as f:
        attempts = [line.strip() for line in f]
    characters = set(''.join(attempts))
    graph = {c: [] for c in characters}

    for attempt in attempts:
        for i, c in enumerate(attempt):
            if i == 0:
                graph[c] = list(set(graph[c]))
            elif c not in graph[attempt[i-1]]:
                graph[attempt[i-1]].append(c)
                graph[c] = list(set(graph[c]))

    order = []
    while len(graph) > 0:
        nodes = [node for node in graph if len(graph[node]) == 0]
        if len(nodes) == 0:
            print("The graph contains a cycle.")
            break
        for node in nodes:
            order.insert(0, node)
            del graph[node]
        for node in graph:
            graph[node] = [c for c in graph[node] if c not in nodes]

    ans_problem_079 = ''.join(order)

    print('Problem 79:', ans_problem_079)
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
