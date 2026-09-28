# Basic
for x in range(0,151,1):
    print(x)
    
# Multiples of five
for y in range(5,1000,5):
    print(y)

# Counting, the dmjo way
for z in range(1,100):
    if(z%10==0):
        print(str(z)+" Coding Dojo")
    elif(z%5==0):
        print(str(z)+" Coding") 

#whoa.That Sucker's Huge
sum=0
for n in range(0,500000):
    if(n%2!=0):
        sum=sum+n
print(sum)

#Countdown by Fours
for c in range(2018,0,-4):
    print(c)

#Flexible Counter
lowNum=2
highNum=9
mult=3
for t in range(lowNum,highNum+1):
    if(t% mult==0):
        print(t)

