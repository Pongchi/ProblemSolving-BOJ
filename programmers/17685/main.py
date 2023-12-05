'''
def solution(words):
    result = [0] * len(words)
    words.sort()
    
    for i in range(len(words)-1):
        overlap = 0
        for length in range(min(len(words[i]), len(words[i+1]))):
            if words[i][length] != words[i+1][length]:
                overlap = length
                break
        else:
            overlap = min(len(words[i]), len(words[i+1]))

        result[i] = max(result[i], min(len(words[i]), overlap+1))
        result[i+1] = max(result[i+1], min(len(words[i+1]), overlap+1))

    return sum(result)
'''

def solution(words):
    Trie = dict()
    for word in words:
        current_trie = Trie
        for char in word:
            if char not in current_trie:
                current_trie[char] = {'count': 0}
            current_trie[char]['count'] += 1
            current_trie = current_trie[char]

    result = 0
    for word in words:
        current_trie = Trie
        for i, char in enumerate(word):
            current_trie = current_trie[char]
            if current_trie['count'] == 1:
                result += i+1
                break
        else:
            result += len(word)

    return result

print(solution(
    ["go", "gone", "guild"]
), 7)

print(solution(
    ["abc", "def", "ghi", "jklm"]
), 4)

print(solution(
    ["word", "war", "warrior", "world"]
), 15)