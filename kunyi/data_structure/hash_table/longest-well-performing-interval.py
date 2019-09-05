class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # [9,9,6,0,6,6,9] -> [1, 1, 0, 0, 0, 0, 1]
        # longest day count > 0 
        # {0:-1, 1:0, 2:1, 1:2, 0:3, -1:4, -2: 5, -1:6}
        # check if count < 0, count - 1 in count_dict
        # test [0,1,0]
        # .    -1 0 -1
        count = 0 
        count_dict = {0:-1}
        result = 0 
        for i, hour in enumerate(hours):
            if hour > 8:
                count += 1 
            else:
                count -= 1
            if count > 0:
                result = max(result, i + 1)
            elif count <= 0 and count - 1 in count_dict:
                result = max(result, i - count_dict[count - 1])
                
            if count not in count_dict:
                count_dict[count] = i 
                
        return result
