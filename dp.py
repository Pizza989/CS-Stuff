import time
# Fibonacci Sequence

# Top-down approach (Memoization)
memo = {
    0: 0,
    1: 1
}


def fibonacci_t_d(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_t_d(n - 1) + fibonacci_t_d(n - 2)
        return memo[n]


# Bottom-up approach (Tabulation)
def fibonacci_b_u(n):
    arr = [0, 1]

    for _ in range(2, n + 1):
        arr.append(arr[_ - 1] + arr[_ - 2])

    return arr[n]


if __name__ == '__main__':
    c = 1000
    start = time.time_ns()
    for i in range(c):
        fibonacci_t_d(i)

    print(f"Duration: {time.time_ns() - start}")

    start = time.time_ns()
    for i in range(c):
        fibonacci_b_u(i)

    print(f"Duration: {time.time_ns() - start}")
