# function which return reverse of a string
 
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "racecar"
ans = isPalindrome(s)
 
if ans:
    print(ans)
else:
    print("No")



#code from: https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/