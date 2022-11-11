def romanToInt(s):
    """
    convert roman to interger.
    """

    pairs_1 = {
                'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100,
                'D': 500, 'M': 1000
                }

    ans = []
    prev = None
    reversed_s = s[::-1]
    for i in reversed_s:
        if prev in ['V', 'X'] and i == 'I':
            ans.append(int(pairs_1.get(i) - 3))

        if prev in ['L', 'C'] and i == 'X':
            ans.append(int(pairs_1.get(i) - 30))

        if prev in ['D','M'] and i == 'C':
            ans.append(int(pairs_1.get(i) - 300))

        ans.append(int(pairs_1.get(i)))

        prev = i

    return sum(ans)