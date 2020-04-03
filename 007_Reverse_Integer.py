class Solution:
    def reverse(self, x: int):
        # 不断把低位提取做高位
        result = 0
        sign = 1 # 默认正
        while x != 0:
            if x < 0:
                sign = -1
                x = x*(-1) 
            result = result*10 + x%10 # 每次提取个位
            x //= 10 # x删除个位，十位变成个位 注意//整除
          
            if result > 2**31 -1:
                return 0 
        return result*sign
if __name__ == "__main__":
    X = Solution()
    X.reverse(321)