#print all integers from 0 to 150
for x in range (0, 151):
    print (x)

#print all the multiples of 5 from 5 to 1,000
#don't forget range is EXCLUSIVE of 2nd value
for x in range (5, 1001, 5):
    print(x)

#print integers from 100 to 100, if divisible by 5 print "Coding", if divisible by 10 print "Dojo"
for x in range (1, 101):
    if x % 10 == 0:
        print("Dojo")
    elif x % 5 == 0:
        print ("Coding")
    else:
        print (x)

#add odd integers from 0 to 5000000, and print final sum
#had to define sum outside function - ask why to clarify
sum = 0

for x in range (1, 500001):
    if (x % 2 != 0):
        sum += x

print (sum)

#print positive numbers starting at 2018, counting down by fours
for x in range (2018, 0, -4):
    print (x)

#set three variables: lowNum, highNum, mult; starting at lowNum and going thru highNum, print only the integers that are a multiple of mult
lowNum = 4
highNum = 7
mult = 84

for x in range (1, 85):
    if x % 4 == 0 and x % 7 == 0:
        print (x)