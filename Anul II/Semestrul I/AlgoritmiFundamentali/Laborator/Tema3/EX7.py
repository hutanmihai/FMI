"""
Complexitatea algoritmului este: O(n*m)
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        ls = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    ls[i][j] = 1 + ls[i - 1][j - 1]
                else:
                    ls[i][j] = max(ls[i - 1][j], ls[i][j - 1])
        i, j = n, m
        res = ""
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res += str1[i - 1]
                i -= 1
                j -= 1
            else:
                if ls[i - 1][j] > ls[i][j - 1]:
                    res += str1[i - 1]
                    i -= 1
                else:
                    res += str2[j - 1]
                    j -= 1
        while i > 0:
            res += str1[i - 1]
            i -= 1
        while j > 0:
            res += str2[j - 1]
            j -= 1
        return res[::-1]


if __name__ == '__main__':
    print(Solution().shortestCommonSupersequence("abac", "cab"))
