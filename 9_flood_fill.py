from typing import List


class Solution:   
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:        
        oldColor = image[sr][sc]
        
        # no change
        if oldColor == newColor:
            return image
        
        mr, mc = len(image), len(image[0])
        
        queue = [(sr, sc)]
        
        while queue:
            r, c = queue.pop(0)
            
            if image[r][c] == oldColor:
                image[r][c] = newColor
                
                if r + 1 < mr: 
                    queue.append((r + 1, c))
                    
                if r >= 1:
                    queue.append((r - 1, c))
                    
                if c + 1 < mc:
                    queue.append((r, c + 1))
                    
                if c >= 1:
                    queue.append((r, c - 1))
            
        return image