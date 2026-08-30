class Solution:
    def findRelativeRanks(self, score):
        order = sorted(score, reverse=True)
        ans = [""] * len(score)

        for i, value in enumerate(order):
            if i == 0:
                rank = "Gold Medal"
            elif i == 1:
                rank = "Silver Medal"
            elif i == 2:
                rank = "Bronze Medal"
            else:
                rank = str(i + 1)

            ans[score.index(value)] = rank

        return ans