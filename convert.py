# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def cycle(self, numRows):
        return 2*(numRows -1)

    def cycleRow(self, numRows, row):
        cycle = self.cycle(numRows)
        return cycle - row*2, row*2

    def convert(self, s, numRows):
        if len(s) <= 2 or numRows == 1:
            return s
            
        jumbled = ""
        max_value = len(s)

        for i in range(numRows):
            cycle = self.cycleRow(numRows, i)
            seq = self.generate_sequence(cycle, i, max_value)
            for index in seq:
                jumbled += s[index]

        return jumbled
        
    def generate_sequence(self, tup, start, max_value):
        sequence = [start]

        while sequence[-1] < max_value:
            for value in tup:
                if value != 0:
                    sequence += [sequence[-1] + value]

        
        
        if len(sequence) > 0:
            if sequence[-1] >= max_value:
                sequence = sequence[:-1]

        if len(sequence) > 0:
            if sequence[-1] >= max_value:
                sequence = sequence[:-1]
        print(sequence)
        return sequence
             

if __name__ == "__main__":
    solution = Solution()

    s = "PAYPALISHIRING"
    numRows = 4
    print(solution.convert(s, numRows))

    s = "ABC"
    numRows = 2
    print(solution.convert(s, numRows))

    s = "ABC"
    numRows = 1
    print(solution.convert(s, numRows))