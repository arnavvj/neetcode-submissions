class Solution:

    def recurNumDecodings(self, s):

        if s in self.ways_map:
            return self.ways_map[s]

        if len(s) == 0:
            return 1
        
        if len(s) == 1:
            if s[0] == '0':
                self.ways_map[s] = 0
                return 0
            else:
                self.ways_map[s] = 1
                return 1

        ways = 0

        if s[0] == '0':
            self.ways_map[s] = 0
            return ways

        if 10 <= int(s[0:2]) <= 26:

            ways += self.recurNumDecodings(s[2:])

        ways += self.recurNumDecodings(s[1:])

        self.ways_map[s] = ways

        return ways

    

    def numDecodings(self, s: str) -> int:
        
        ways = 0
        self.ways_map = dict()
        
        if s[0] == '0':
            return ways

        if 10 <= int(s[0:2]) <= 26:

            ways += self.recurNumDecodings(s[2:])

        ways += self.recurNumDecodings(s[1:])

        return ways
        

        
        



"""
1012

    1 012   X

    10 1 2  1

    10 12   2


12

    1 2     1

    12      2


01

    0 1     X

"""