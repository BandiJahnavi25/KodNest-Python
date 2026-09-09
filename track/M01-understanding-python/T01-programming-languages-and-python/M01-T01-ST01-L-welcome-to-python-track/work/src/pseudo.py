# TO print Hello world
# start
#      print "Hello world"
# stop
print("Hello world \nThank you for learning python")
print("Hello world" , end=" ")
print("Thank you for learning python")
name = "Jahnavi"
print("Name:\t", name)
# To find whether number (n) is even or odd
"""start
input n
if n%2 == 0
   print "even"
else
   print "odd"
end"""

n = 10
if n%2 == 0:
   print("even")
else:
   print("odd")
# To find the is pos , neg or zero
"""start
input n
if n > 0
    print "positive"
else if n < 0
    print "negitive"
else
    print"zero"
end"""
n = 2
if n > 0:
    print("positive")
elif n < 0:
    print("negitive")
else:
    print("zero")
# To find the largest among 3 numbers a, b , c
"""start
input a 
input b
input c
if a>= b and a >= c
   print "a is largest"
else if b >= a and b >= c
   print "b is largest"
else
    print "c is largest"
end"""
a = 10; b = 2; c = 0
if a >= b and a >= c:
    print("a is largest")
elif b >= a and b >= c:
    print("b is largest")
else:
    print("c is largest")