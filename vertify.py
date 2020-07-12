'''
@Author: your name
@Date: 2020-03-24 14:18:21
@LastEditTime: 2020-07-11 22:03:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/vertify.py
'''



class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # if(len(s) == 1):
        #     return s
        # else:
        #     return [s[-1]] + self.reverseString(s[0:-1])

        def recursive(s,start,end):
            if start==end:
                pass
            elif end - start == 1:
                s[start],s[end] = s[end],s[start]
            else:
                s[start],s[end] = s[end],s[start]
                recursive(s,start+1,end-1)
        recursive(s,0,len(s)-1)
if __name__ == "__main__":
    s = Solution()
    print(s.reverseString(["H","a","n","n","a","h"]))