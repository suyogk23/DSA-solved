class Solution:
    # TC: O(n log nL)
    # space = nL
    # where L= average length of each word, n = len of logs list
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        # O(nL)
        for log in logs:
            log = log.split()
            if log[-1][-1].isdigit(): # str.isdigit() # return true if the string is a digit
                digit_logs.append(log)  
            else:
                letter_logs.append(log)
        # O(n log nL)
        letter_logs.sort(key = lambda x : (x[1:], x[0]))
        sorted_logs = letter_logs + digit_logs
        # O(nL)
        for i in range(len(sorted_logs)):
            sorted_logs[i] = ' '.join(sorted_logs[i])

        return sorted_logs

# sort:
'''
letter > digits

letter:
    content > id

digits:
    maintain original order

id: fixed

'''
