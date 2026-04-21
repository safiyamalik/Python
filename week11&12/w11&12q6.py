import sys

def matrix_chain_multiplication(p):
    n = len(p)
    
    # Create DP table
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # l = chain length
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            dp[i][j] = sys.maxsize
            
            for k in range(i, j):
                cost = (dp[i][k] +
                        dp[k+1][j] +
                        p[i-1] * p[k] * p[j])
                
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    return dp[1][n-1]


# Example usage
p = [10, 20, 30, 40, 30]

result = matrix_chain_multiplication(p)
print("Minimum number of multiplications:", result)