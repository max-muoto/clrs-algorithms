def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        print(s[m])
        print(f[k])
        m += 1
    print("stop")
    print(m)
    if m <= n:
        print("here")
        return {m+1}.union(recursive_activity_selector(s, f, m, n))
    else:
        return set()


def main():
    # Example from CLRS page 15.1
    s = [1, 3, 0, 5, 3, 5, 6, 7, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    n = len(s) - 1
    # Our resulting set contains the index of each mutually compatiable activity.
    result = recursive_activity_selector(s, f, 0, n)
    print(result)


if __name__ == "__main__":
    main()
