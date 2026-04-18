class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        s = s.lower()

        s_ = ""
        for c in s:
            if c.isalnum():
                s_ += c

        print(s_)
        s_len = len(s_)

        for i in range(0, s_len//2):

            print(s_[i], s_[s_len - i - 1])

            if s_[i] != s_[s_len - i - 1]:
                return False

        return True
