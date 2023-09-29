class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l1 = 0
        l2 = 0
        stack = []

        for ch in operations:
            if ch == "C":
                stack.pop()
            elif ch == "D":
                stack.append(stack[-1]*2)
            elif ch == "+":
                l1 = stack.pop() if stack else l1
                l2 = stack.pop() if stack else l2
                stack.append(l2)
                stack.append(l1)
                stack.append(l1 + l2)
            else:
                stack.append(int(ch))
            
        
        sumVal = 0
        while stack:
            sumVal += stack.pop()
        
        return sumVal








        