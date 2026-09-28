# countdown
def countdown(num):
    output = []
    for i in range(num, -1, -1):
        output.append(i)
    return output
var=countdown(7)    
print(var)

# print and return
def print_and_return(nums):
    print(nums[0])
    return nums[1]

print_and_return([1,2])

# first plus length
def first_plus_length(arra):
    sum=arra[0]+len(arra)
    return sum
var=first_plus_length([7,4,5,4,2,1])
print(var)

# values greater than second
def valuesgt2(x):
    y=[]
    if len(x) < 2:
        print("False")
        return False
    else:    
        for i in range (0,len(x),1):
            if (x[i] > x[1]):
                y.append(x[i])
        print(len(y))  
        print(y)     
        return y
valuesgt2([4,2,1,4])

#this length,that value

def thisthat(size,value):
    n=[]
    for i in range(0,size,1):
        n.append(value)
    print(n)    
    return n

thisthat(8,2)
