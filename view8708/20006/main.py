import sys

input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for i in range(p):
    player_level, player_name = input().split()
    player_level = int(player_level)
    find_room = False
    for room_number in range(len(rooms)):
        if len(rooms[room_number])+1 <= m and abs(rooms[room_number][0][0] - player_level) <= 10:
            find_room = True
            rooms[room_number].append((player_level, player_name))
            break

    if not find_room:
        rooms.append([(player_level, player_name)])

for room in rooms:
    if (len(room) == m):
        print("Started!")
    else:
        print("Waiting!")
    
    for player in sorted(room, key=lambda x : x[1]):
        print(player[0], player[1])