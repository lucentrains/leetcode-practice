class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rev = 0
        n = x
        while x != 0:
            rev = rev * 10 + x % 10
            x = x // 10
        if rev == n:
            return True
        return False

        # Special cases:
        # As discussed above, when x < 0, x is not a palindrome.
        # Also if the last digit of the number is 0, in order to be a palindrome,
        # the first digit of the number also needs to be 0.
        # Only 0 satisfy this property.
        # if x < 0 or (x % 10 == 0 and x != 0):
        #     return False

        # revertedNumber = 0
        # while x > revertedNumber:
        #     revertedNumber = revertedNumber * 10 + x % 10
        #     x //= 10

        # When the length is an odd number, we can get rid of the middle digit by revertedNumber//10
        # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
        return x == revertedNumber or x == revertedNumber // 10