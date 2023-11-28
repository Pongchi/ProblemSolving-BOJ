# https://school.programmers.co.kr/learn/courses/30/lessons/72416

def solution(sales, links):
    graph = [ [] for i in range(len(sales)+1) ]
    for a, b in links:
        graph[a].append(b)

    teams = []
    in_team = [ [] for _ in range(len(sales)+1) ]
    for i in range(len(sales)+1):
        if len(graph[i]) > 0:
            teams.append([i]+graph[i])
            for member in teams[-1]:
                in_team[member].append(len(teams)-1)

    min_member_of_teams = []
    for team in teams:
        member = min(team, key=lambda x : sales[x-1])
        min_member_of_teams.append(member)
    
    min_overlap_member = []
    for i in range(1, len(sales)+1):
        if len(in_team[i]) == 2 and (i in min_member_of_teams):
            A, B = in_team[i]
            min_member_of_teams[A] = i
            min_member_of_teams[B] = i
            
    
    result = 0
    for i in set(min_member_of_teams):
        result += sales[i-1]

    return result

print(solution(
    [14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
    [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
), 44)

print(solution(
    [5, 6, 5, 3, 4],
    [[2,3], [1,4], [2,5], [1,2]]    
), 6)

print(solution(
    [5, 6, 5, 1, 4],
    [[2,3], [1,4], [2,5], [1,2]]
), 5)

print(solution(
    [10, 10, 1, 1],
    [[3,2], [4,3], [1,4]]
), 2)