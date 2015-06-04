class Solution:
    """
    @see https://oj.leetcode.com/problems/simplify-path/
    """
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        path = path.split('/') 
        dirs = []
        for d in path:
            if d == '' or d == '.':
                continue
            elif d == '..':
                if len(dirs) > 0:
                    dirs.pop()
            else:
                dirs.extend([d])
        return '/' + '/'.join(dirs)

if __name__ == "__main__":
    solution = Solution()
    print(solution.simplifyPath("/home//foo/"))
    print(solution.simplifyPath("/a/./b/../../c/"))
    print(solution.simplifyPath("/../"))

