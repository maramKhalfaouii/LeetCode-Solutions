class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans=0
        left,right=0,len(height)-1
        maxLeft=height[left]
        maxRight=height[right]
        while right>left :
            if maxLeft<maxRight:
                left+=1
                maxLeft=max(maxLeft,height[left])
                ans+=maxLeft-height[left]
            else:
                right-=1
                maxRight=max(maxRight,height[right])
                ans+=maxRight-height[right]

        return ans 
