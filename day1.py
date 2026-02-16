class Solution:

    def printValues(self, a, b, c):
        print(a)
        # print(b)
        print(c)

# a,b,c = map(int, input("input three number : ").split(" "))

a = input("Enter something: ")
a = int(a) if a.isdigit() else 0
b = input("Enter another number: ")
b = int(b) if b.isdigit() else 0
c = input("Enter a third number: ")
c = int(c) if c.isdigit() else 0

sol = Solution()
sol.printValues(a,b,c)
