class Solution(object):
    def generateParenthesis(self, n):
        def generate(p):
            if len(p) == 2 * n:
                if valid(p):
                    res.append("".join(p))
            else:
                p.append('(')
                generate(p)
                p.pop()
                p.append(')')
                generate(p)
                p.pop()

        def valid(p):
            bal = 0
            for c in p:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0

        res = []
        generate([])
        return res
