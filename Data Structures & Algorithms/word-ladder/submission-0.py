from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            w, d = q.popleft()
            if w == endWord:
                return d

            for i in range(len(w)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    x = w[:i] + c + w[i+1:]
                    if x in words:
                        words.remove(x)
                        q.append((x, d + 1))

        return 0