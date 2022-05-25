class Solution:       
    def isValid(self, s: str) -> bool:
        l = {'(': 0, '{': 1, '[': 2}
        r = {')': 0, '}': 1, ']': 2}
        
        stack = []
        
        for ch in s:
            if ch in l:
                stack.append(ch)
            
            else:
                if not stack:
                    return False
                
                top = stack[-1]
                
                if l[top] == r[ch]:
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0
    
    
if __name__ == "__main__":
    solution = Solution()
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("(]") == False