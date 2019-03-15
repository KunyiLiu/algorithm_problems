class Solution(object):
    def isStrobogrammatic(self, num):
        symm = {'8':'8', '1':'1', '6':'9', '9':'6', '0':'0'}
        i, j = 0, len(num)-1
        while i < j:
            if num[i] not in symm or num[j] not in symm:
                return False
            if symm[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        if len(num)%2 ==0:
            return True
        else:
            mid_char = num[len(num)/2]
            if mid_char != '8' and mid_char != '0' and mid_char != '1':
                return False
            else:
                return True

s = Solution()
print s.isStrobogrammatic('609')


