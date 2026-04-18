class Solution:
    def isValid(self, s: str) -> bool:

        stack = list()

        for c in s:

            if c in {'(', '[', '{'}:

                stack.append(c)

            else:
                
                try:
                    top_c = stack.pop(-1)

                    if c == ')' and top_c == '(':
                        continue
                    elif c == ']' and top_c == '[':
                        continue
                    elif c == '}' and top_c == '{':
                        continue

                    else:
                        # pattern does not match
                        return False

                except IndexError:
                    return False

        if len(stack) != 0:
            return False
            
        return True