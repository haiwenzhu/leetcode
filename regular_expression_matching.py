class Solution:
    """
    @see https://oj.leetcode.com/problems/regular-expression-matching/
    """
    # @return a boolean
    def isMatch(self, s, p):
        stat = self.parse(p, 0, len(p))
        return self._isMatch(s, 0, len(s), stat)
    def _isMatch(self, s, i, n, stat):
        if i == n:
            return stat.isFinish()
        stats = stat.trans(s[i])
        for stat in stats:
            if self._isMatch(s, i+1, n, stat):
                return True
        return False


    def parse(self, s, i, n):
        stat = RegStat()
        if i < n:
            if s[i] == '.':
                if i+1 < n and s[i+1] == '*':
                    stat.addRule('*', stat)
                    i += 2
                    while i+2 < n and s[i:i+2] == s[i-2:i]:
                        i += 2
                    stat.addRule('', self.parse(s, i, n))
                else:
                    stat.addRule('*', self.parse(s, i+1, n))
            elif s[i] == '*':
                stat =  self.parse(s, i+1, n)
            else:
                if i+1 < n and s[i+1] == '*':
                    stat.addRule(s[i], stat)
                    i += 2
                    while i+2 < n and s[i:i+2] == s[i-2:i]:
                        i += 2
                    stat.addRule('', self.parse(s, i, n))
                else:
                    stat.addRule(s[i], self.parse(s, i+1, n))
        else:
            stat.setFinish()
        return stat
        
class RegStat:
    def __init__(self):
        self.rules = {}
        self.finish = False
    def addRule(self, input, output):
        self.rules[input] = output
    def trans(self, input):
        stats = []
        if input != '':
            if input in self.rules:
                stats.append(self.rules[input])
            elif '*' in self.rules:
                stats.append(self.rules['*'])
            if '' in self.rules:
                stat = self.rules['']
                stats.extend(stat.trans(input))
        else:
            if '' in self.rules:
                stats.append(self.rules[''])
        return stats
    def setFinish(self):
        self.finish = True
    def isFinish(self):
        if self.finish:
            return True
        else:
            stats = self.trans('')
            while stats:
                next_stats = []
                for stat in stats:
                    if stat.isFinish():
                        return True
                    else:
                        next_stats.extend(stat.trans(''))
                stats = next_stats
            return False
    def __str__(self):
        str = ''
        for k, v in self.rules:
            str += k + ',' 
        return str

if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b"))
