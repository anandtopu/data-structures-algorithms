# cook your dish here


def max_weight_difference(test_cases):
    results = []

    for case in test_cases:
        N, K, weights = case
        weights.sort()
        total_sum = sum(weights)

        # choose the smaller of K and N-K
        K = min(K, N - K)

        # sum of K smallest items
        sum_light = sum(weights[:K])

        # calculate the difference

        diff = abs((total_sum - sum_light) - sum_light)

        # max difference
        results.append(diff)
    return results


# input handling

if __name__ == "__main__":
    T = int(input().strip())
    test_cases = []

    for _ in range(T):
        N, K = map(int, input().strip().split())
        weights = list(map(int, input().strip().split()))
        test_cases.append((N, K, weights))

    for result in max_weight_difference(test_cases):
        print(result)