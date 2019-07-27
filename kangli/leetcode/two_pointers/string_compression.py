class Solution:
    def compress(self, chars):
        write_pointer, cur_count = 0, 1
        if len(chars) <= 1:
            return 1
        for i in range(1, len(chars)+1):
            if i < len(chars) and chars[i] == chars[i-1]:
                cur_count += 1
            else:
                chars[write_pointer] = chars[i-1]
                write_pointer += 1
                if cur_count > 1:
                    for c in str(cur_count):
                        chars[write_pointer] = c
                        write_pointer +=1
                    cur_count = 1
        chars = chars[:write_pointer]
        return write_pointer


'''
Success
Details
Runtime: 68 ms, faster than 65.22% of Python3 online submissions for String Compression.
Memory Usage: 13.9 MB, less than 6.57% of Python3 online submissions for String Compression.
Next challenges: Count and Say, Encode and Decode Strings, Design Compressed String Iterator
'''
