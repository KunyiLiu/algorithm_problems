class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        # write your code here
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                break
        else:
            num.reverse()
            return num
        for j in range(len(num)-1, i, -1):
            if num[j] > num[i]:
                num[i], num[j] = num[j], num[i]
                break
        # nums i+1 ... nums[n-1] descending 
        # reverse 
        return num[:(i+1)] + sorted(num[i+1: len(num)])
        # for j in range(0, (len(num) - i)//2):
        #     num[i+j+1], num[len(num)-j-1] = num[len(num)-j-1], num[i+j+1]
        # return num
