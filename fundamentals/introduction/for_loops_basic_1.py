#Basics
for i in range (151):
    print (i)
#Multiple of Fives
for i in range (5, 1001, 5):
    print(i)
#Counting, the Dojo way -- Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range (1, 101):
    print (i)
    if i % 5 == 0:
        print ("Coding")
    if i % 10 == 0:
        print ("Coding Dojo")
#Whoa. That sucker's huge -- Add odd integers from 0 to 500,000, and print the final sum.
for i in range (0, 500000 + 1):
    if i % 2 != 0:
        print (i)
#Countdown by fours -- Print positive numbers starting at 2018, counting down by fours.
for i in range (2018, 0, -4):
    print(i)
#Flexible counter -- Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 50
mult = 7
for i in range (lowNum, highNum, +1):
    if i % mult == 0:
        print (i)