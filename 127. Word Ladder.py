class Solution:
    # create patters with 1 letter edit distance
    # eg: hot : *ot, h*t, ho*
    # use these patterns as key for adj list, the adj list will have words matching that pattern
    # example traversal:
    # cog - dog, log
    # dog - cog, log, dot
    # log - dog, cog, lot 
    # this creates a undirected graph between nodes with edit distance 1
    # we can do bfs while tracking levels of bfs and return the level which reaches endWord
    # if unable to reach we can return 0
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n, m = len(wordList), len(wordList[0])
        adj = defaultdict(list)

        for word in wordList:
            for i in range(m):
                pattern = word[:i] + '*' + word[i+1:]
                adj[pattern].append(word)

        # bfs
        q = deque([beginWord])
        vis = set([beginWord])
        level = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return level
                for i in range(m):
                    pattern = word[:i] + '*' + word[i+1:]
                    for neighbour in adj[pattern]:
                        if neighbour not in vis:
                            vis.add(neighbour)
                            q.append(neighbour)
            level += 1
        return 0

# hot 
# *ot, h*t, ho*
# *ot : [hot, dot , lot]
# *ot : 

'''
cog - dog, log
dog - cog, log, dot
log - dog, cog, lot 

hot - hit

n: wl
m: wrd
n * m * v
'''
