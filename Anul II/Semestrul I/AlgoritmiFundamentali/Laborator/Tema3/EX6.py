"""
Complexitatea algoritmului este: O(n*m)
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        ls = [[0 for i in range(m + 1)] for j in range(n + 1)]
        res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    ls[i][j] = 1 + ls[i - 1][j - 1]
                else:
                    ls[i][j] = max((ls[i][j - 1]), ls[i - 1][j])
                res = max(res, ls[i][j])
        return res


if __name__ == '__main__':
    print(Solution().longestCommonSubsequence("abcde", "ace"))
