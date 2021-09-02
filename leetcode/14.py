class Solution:
    def longestCommonPrefix(self, str: List[str]) -> str:

        # Solution 1

        if not in strs:
            return ""

        shortest = min(strs, key=len)

        for index, char in enumerate(shortest):
            for word in strs:
                if word[index] != char:
                    return shortest[:-1]
        return shortest


        # Solution 2

        shortest = len(min(strs))
        common = ''

        for i in range(0, shortest):
            common = common + strs[0][i]

            for word in strs:
                if common[i] == word[i]:
                    continue
                else:
                    return common[:-1]
        return common
