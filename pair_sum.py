"""
write a Python program to determine if it’s possible to obtain the pair 
(c, d) from the pair (a, b) using the given operations: (a+b, a) or (a, a+b).
"""


def move(a, b, c, d, dp):
    # Memoization: Initialize dp array with -1
    if dp[a][b] != -1:
        return dp[a][b]
    
    dp[a][b] = float('inf')  # Initialize to infinity
    
    if a == c and b == d:
        dp[a][b] = True
        return dp[a][b]
    elif a > c or b > d:
        dp[a][b] = False
        return dp[a][b]
    else:
        if a < c:
            if move(a + b, b, c, d, dp):
                dp[a][b] = True
                return dp[a][b]
        if b < d:
            if move(a, b + a, c, d, dp):
                dp[a][b] = True
                return dp[a][b]
    dp[a][b] = False
    return dp[a][b]

# Example usage
c, d = 2, 1000
dp = [[-1] * (d + 1) for _ in range(c + 1)]
result = move(2, 2, c, d, dp)
print("Yes" if result else "No")
