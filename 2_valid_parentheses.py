class Solution:   
    p = {'(': ')', '{': '}', '[': ']'}
            
    def isValid(self, s: str) -> bool:   
        # odd length strings will never be valid
        if len(s) % 2:
            return False
           
        stack = []
        
        for ch in s:
            # push open parantheses to the stack
            if ch in self.p:
                stack.append(ch)
            
            else:
                # invalid if closing without any opened parantheses
                if not stack:
                    return False
                
                # invalid if the current closing parantheses
                # do not correspond with the latest open parantheses
                if self.p[stack.pop()] != ch:
                    return False
                
        # invalid if there is still open parantheses
        return len(stack) == 0
    
    
if __name__ == "__main__":
    solution = Solution()
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("(]") == False