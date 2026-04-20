class Solution:
    def reverseBits(self, n: int) -> int:
        
        bit_str = f"{n:032b}"

        rev_bit_str = bit_str[::-1]

        return int(rev_bit_str, 2)