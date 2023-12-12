# https://school.programmers.co.kr/learn/courses/30/lessons/42892

import sys
sys.setrecursionlimit(10**4+1)

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key=lambda x : -x[1])

    # ROOT, LEFT, RIGHT
    def preorder(nodes):
        if len(nodes) <= 1:
            return [ node[2] for node in nodes ]

        left = []
        right = []
        pivot = nodes[0]
        for node in nodes:
            if node[2] == pivot[2]: continue
            if node[0] < pivot[0]:
                left.append(node)
            else:
                right.append(node)

        result = [pivot[2]]
        result += preorder(left)
        result += preorder(right)
        return result

    # LEFT, RIGHT, ROOT
    def postorder(nodes):
        if len(nodes) < 1:
            return []

        left = []
        right = []
        pivot = nodes[0]
        for node in nodes:
            if node[2] == pivot[2]: continue
            if node[0] < pivot[0]:
                left.append(node)
            else:
                right.append(node)

        result = postorder(left)
        result += postorder(right)
        result += [pivot[2]]
        return result
    

    return [preorder(nodeinfo), postorder(nodeinfo)]

print(solution(
    [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
), '\n', [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]])