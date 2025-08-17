class Solution:
    '''
    Problem: Two parties (R, D) take turns banning each other until one remains. Output winner.
    Key Idea: Use queues to simulate turns.
    Approach:
    Push indices of R into one queue, D into another.
    Pop front from both → the smaller index acts first (bans the other).
    Winner (smaller index) gets re-added to its queue with +n (next round).
    Continue until one queue empty.
    Result: If R queue empty → "Dire"; else → "Radiant".

    solution by @suyogk23 GITHUB
    '''
    def predictPartyVictory(self, senate: str) -> str:
        dQ, rQ = [], []
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                rQ.append(i)
            else:
                dQ.append(i)
        
        while dQ and rQ:
            if dQ[0] < rQ[0]:
                dQ.append(dQ.pop(0) + n)
                rQ.pop(0)
            else:
                rQ.append(rQ.pop(0) + n)
                dQ.pop(0)

        if dQ:
            return "Dire"
        else:
            return "Radiant"



        
