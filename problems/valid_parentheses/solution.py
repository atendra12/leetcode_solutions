class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para_dict = {'(':')', '{':'}','[':']'}
        for char in s:
            if char in para_dict:
                stack.append(char)
            else:
                if stack:
                    top_char = stack.pop()
                    if para_dict[top_char] == char:
                        continue
                    else:
                        return False
                else:
                    return False

        if len(stack)==0:
            return True
        else:
            return False

