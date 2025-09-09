class Solution:
    # solution by @suyogk23 GITHUB
    # maintain a cur_pos ptr
    # while cur group, move ptr forward
    # after group end: cur_pos = current char and cur_pos += 1
    # cur_pos = group len
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        cur_ptr = 0
        while i < n:
            char = chars[i]
            j = i+1
            # find the length of current group
            while j < n and chars[j] == char:
                j += 1
            # update the char
            count = j-i
            chars[cur_ptr] = char
            cur_ptr+=1
            # update the char length
            if count > 1:
                count = str(count)
                for c in count:
                    chars[cur_ptr] = c
                    cur_ptr+=1
            # jump to next group
            i = j
            
        return cur_ptr
