class Solution:
    """
    @see https://leetcode.com/problems/text-justification/
    """
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        strings = []
        count = 0
        tmpwords = []
        width = 0
        for word in words:
            if width + len(word) + count > maxWidth:
                if count == 1:
                    strings.append(tmpwords[0].ljust(maxWidth))
                else:
                    divid = (maxWidth-width) // (count-1)
                    remain = maxWidth - width - (count-1)*divid
                    ins = ''.rjust(divid) 
                    string = ''
                    for s in tmpwords:
                        if string == '':
                            string = s
                        else:
                            if remain > 0:
                                string = string + ins + ' ' + s
                                remain -= 1
                            else:
                                string = string + ins + s
                    strings.append(string)
                count = 0
                width = 0
                tmpwords = []
            width += len(word)
            count += 1
            tmpwords.append(word)

        if count == 1:
            strings.append(tmpwords[0].ljust(maxWidth))
        else:
            string = ' '.join(tmpwords)
            strings.append(string.ljust(maxWidth))
        return strings

if __name__ == "__main__":
    solution = Solution()
    #print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(solution.fullJustify(["Give","me","my","Romeo;","and,","when","he","shall","die,","Take","him","and","cut","him","out","in","little","stars,","And","he","will","make","the","face","of","heaven","so","fine","That","all","the","world","will","be","in","love","with","night","And","pay","no","worship","to","the","garish","sun."], 25))

