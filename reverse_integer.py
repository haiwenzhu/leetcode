class Solution:
    """
    @see https://oj.leetcode.com/problems/reverse-integer/
    """
    # @return an integer
    def reverse(self, x):
        numbers = []
        sign = 1 if x >= 0 else -1
        x *= sign
        while x != 0:
            numbers = [i*10 for i in numbers]
            numbers.append(x % 10)
            x = x // 10

        res = sum(numbers) * sign
        return res if res >= -2**31 and res < 2**31 else 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(1534236469))
    print(solution.reverse(-120))

