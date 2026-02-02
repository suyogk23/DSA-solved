class Solution:
    # divide the number into 3 segments each, eg: 123456 -> 123 456
    # for each 3 segment: fidn the word for first 2 segment then append unit_word_digit in 3rd place + Hundred + the 2 segment answer
    # for each 2 segment in 3 segment, handle cases when num < 20, else add tens_word_digit in 2nd place + unit_word_digit in 1st place
    # in the final loop, according to segment if three_segment_word>0 add three_segment_word + Thousand, Million or Billion, else just add Thousand, Million or Billion
    def numberToWords(self, num: int) -> str:
        if num * 1 == 0:
            return "Zero"

        ones = ['_', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        sp_tens = ['Ten','Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['_', '_', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        hundred = 'Hundred'
        thousand = 'Thousand'
        million = 'Million'
        billion = 'Billion'

        def getTwoSegmentWord(num):
            if num == 0:
                return None
            if num < 10:
                return ones[num]
            if num < 20:
                return sp_tens[num%10]
            ans = ''
            for i in range (2):
                dig = num %10
                num = num //10
                if i == 0 and dig > 0:
                    word_dig = ones[dig]
                    ans = ' ' + word_dig
                if i == 1: # digit will alwaus be >= 2
                    word_dig = tens[dig]
                    ans = word_dig + ans
            return ans

        def getThreeSegmentWord(num):
            if num == 0:
                return None
            ans = getTwoSegmentWord(num%100)
            dig = num // 100
            if ans:
                if dig == 0:
                    return ans
                ans = ones[dig] + ' ' + hundred + ' ' + ans
            else:
                ans = ones[dig] + ' ' + hundred
            return ans
        
        ans = ''
        place = 0
        while num > 0:
            three_segment_word = getThreeSegmentWord(num%1000)
            num = num // 1000
            if three_segment_word:
                if place == 0:
                    ans = three_segment_word
                elif place == 1:
                    ans = three_segment_word + " " + thousand + " " + ans
                elif place == 2:
                    ans = three_segment_word + " " + million + " " + ans
                elif place == 3:
                    ans = three_segment_word + " " + billion + " " + ans
                else:
                    return f"Does not support numbers larger than 999 Billion, ans so far {ans}"
            place += 1
        
        return ans.strip()
                

"""
000.000.000

2.123.456.890 :Two billion one hundred twenty-three million four hundred fifty-six thousand eight hundred ninety
X:
Tens pl:
20: 0 in 1s place, Twenty #edge } 
22: 2 in 1s place, Twenty two
Hundred pl:
any digit + hundred

in next segment (thousand) X + thousand


"""
        
