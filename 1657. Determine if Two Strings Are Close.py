class Solution:
    # append the following to a hash map
    # check every character occuring
    # count the number of occurance of each character
    # check if the occurance is same numbers irrespective of the character that count is for
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)
        if n1 != n2:
            return False

        m1, m2 = {}, {}
        #O(n)
        for word in word1:
            if word not in m1:
                m1[word] = 1
            else:
                m1[word]+=1
        
        for word in word2:
            if word not in m2:
                m2[word] = 1
            else:
                m2[word]+=1
        
        k1 = set(m1.keys())
        k2 = set(m2.keys())
        if k1 != k2:
            return False
        v1 = list(m1.values())
        v2 = list(m2.values())
        v1.sort()
        v2.sort()

        print(v1, v2)
        if v1 != v2:
            return False

        return True


        



        
