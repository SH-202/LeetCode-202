#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))]for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if(s[i] == s[j]):
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]
# @lc code=end
print(Solution().longestPalindromeSubseq("bbbab"))
