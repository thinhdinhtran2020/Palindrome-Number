class Solution:
    def isPalindrome(self, x: int) -> bool:
        xlist = []
        ylist = []
        boolList = []
        x = str(x)
        for i in x:
            xlist.append(i)
        for i in reversed(x):
            ylist.append(i)
        for i in range(len(xlist)):
            if xlist[i] == ylist[i]:
                boolList.append(True)
            else:
                boolList.append(False)
        for i in boolList:
            if i == False:
                return False
            else:
                pass
        return True
    
def main():
    solution = Solution()
    print(solution.isPalindrome(1000021))
    
main()
