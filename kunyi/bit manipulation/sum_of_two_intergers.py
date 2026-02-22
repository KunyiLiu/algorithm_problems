class Solution:
    def getSum(self, a: int, b: int) -> int:
        # In Python, left-shifting never truncates, 
        # so carry can grow without bound (or sign/bit-layout differs)
        # emulate the python integer to fixed-len 32 bit, as carry might never be 0
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        # a here represents the partial sum without carry, while b represents the carry that will be processed in the next step
        a &= mask
        b &= mask

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) 
            b = carry & mask     # must mask

        return a if a <= max_int else ~(a ^ mask)


# how about a - b, -b = ~b + 1 using two's complement

def getSubtraction(self, a, b):
    mask = 0xFFFFFFFF
    
    # Step 1: Get Two's Complement of b (-b = ~b + 1)
    # We use our bitwise adder logic to perform the "+ 1"
    negative_b = self.getSum(~b, 1)
    
    # Step 2: Perform a + (-b)
    return self.getSum(a, negative_b)

