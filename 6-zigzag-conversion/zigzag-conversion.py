class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        row = 0
        goingDown = True

        for ch in s:
            rows[row] += ch

            if row == 0:
                goingDown = True
            elif row == numRows - 1:
                goingDown = False

            if goingDown:
                row += 1
            else:
                row -= 1

        return "".join(rows)