class Solution(object):
    def numJewelsInStones(self, J, S):
        cnt = 0
        for j in J:
            cnt += S.count(j)
        return cnt
