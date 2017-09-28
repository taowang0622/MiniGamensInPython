#a list comphrehension
#passing one whole list
print "max in list: ", max([num * 2 - 3 for num in range(7)])

#a genearator expression
#passing a generator
print "max in gen: ", max(num * 2 -3 for num in range(7))

#a generator function
# It's similar to Iterator in Java 
def genfunc(limit):
    num = 0
    while num < limit:
        yield num
        num = num + 1

gen = genfunc(7)
print gen.next()
print gen.next()

#Iteration using a generator function
print "Iterate over generator"
for num in genfunc(7):
    print num

#pass to the function expecting a sequence
print "max in gen func: ", max(genfunc(7))

#use return to end a generator
def genfunc2(endfunc):
    num = 0
    while True:
        if(endfunc(num)):
            return
        yield num
        num = num + 1

def endfunc(num):
    if num == 7:
        return True
    return False

print "Iterate over the second generator"
for num in genfunc2(endfunc):
    print num