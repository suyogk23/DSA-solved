class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        freq = defaultdict(int)
        users = defaultdict(list)

        for u, t, w in zip(username, timestamp, website):
            users[u].append([t, w])
        
        for patterns in users.values():
            patterns.sort(key = lambda x:x[0])
            #generate all subsequences
            n = len(patterns)
            vis = set()
            for i in range(n):
                for j in range(i+1, n):
                    for k in range(j+1, n):
                        subseq = (patterns[i][1], patterns[j][1], patterns[k][1])
                        if subseq not in vis:
                            freq[subseq] += 1
                            vis.add(subseq)
        
        maxf, ans = -1, None
        for subseq, count in freq.items():
            subseq = list(subseq)
            if count > maxf:
                maxf = count
                ans = subseq
            elif count == maxf:
                if subseq < ans:
                    ans = subseq
        return ans

