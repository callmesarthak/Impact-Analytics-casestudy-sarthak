from functools import lru_cache


class SolutionClass:
    def __init__(self, days):
        self.days = days
        self.consecutive_days = 4 # 4 or more

    def using_memoization(self):

        @lru_cache(None)
        def rec(n, m):

            if self.consecutive_days == m:
                return 0
            if n == 0:
                return 1

            return rec(n- 1, 0) + rec(n-1, m+1)

        total = rec(self.days, 0)
        missed = rec(self.days-1, 1)

        return f"{missed}/{total}"

    def using_dynamic_programming(self):
        n, m = self.days, self.consecutive_days
        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(m):
            dp[0][i] = 1

        for i in range(1,n+1):
            for j in range(m-1,-1,-1):
                dp[i][j] = dp[i-1][0] + dp[i-1][j+1]

        total = dp[n][0]
        missed = dp[n-1][1]

        return f"{missed}/{total}"


    def using_dynamic_programming_with_spaceoptimization(self):
        n, m = self.days, self.consecutive_days
        dp = [1] * (m + 1)
        dp[m] = 0

        for i in range(1, n + 1):
            temp = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                temp[j] = dp[0] + dp[j + 1]

            temp, dp = dp, temp

        total = dp[0]
        missed = temp[1]
        return f"{missed}/{total}"
