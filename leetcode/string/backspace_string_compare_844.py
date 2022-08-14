def backspaceCompare(self, s, t) -> bool:
    return self.helper(s) == self.helper(t)

    def helper(string):
        lst = list()
        for ch in string:
            if not ch is '#':
                lst.append(ch)
            elif not len(lst) is 0:
                lst.pop()

        return lst
