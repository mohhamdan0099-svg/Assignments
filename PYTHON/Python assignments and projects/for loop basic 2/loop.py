# Biggie Size

def big(nums):
    for i in range(0,len(nums)):
        if (nums[i]>0):
            nums[i]="big"
    return nums 

big([2,-2,0,7,4,2])
print(big([2,-2,0,7,4,2]))   

# Count Positives

def count_positive(num):
    count=0
    for i in range(0,len(num)):
        if (num[i]>0):
            count+=1
    num[len(num)-1] = count
    return num

count_positive([1,2,0,-6,8])
print(count_positive([1,2,0,-6,8]))    


# sum total

def sum_total(lis):
    summ=0
    for i in range(0,len(lis)):
        summ += lis[i]
    print(summ)    
    return summ

sum_total([1,2,-2,-5,8])

# average
def average(nums):
    avg=0
    sum=0
    for i in range(0,len(nums)):
        sum+=nums[i]
    avg=sum/len(nums)
    print(avg)
    return avg

average([2,2,4,4])

#length

def length(nums):
    leng=0
    for i in range(0,len(nums)):
        leng=len(nums)
    print(leng)
    return leng  
length([1,2,3,4,5,6])  

# Minimum
def Minimum(nums):
    
    if (len(nums)==0):
        print(False)
        return False
    min = nums[0]    
    for i in range(0,len(nums)):
        if (nums[i]<min):
            min=nums[i]
    print(min)
    return min

Minimum([0,1,2,-5,-8,22])


# Maximum

def Maximum(nums):
    if len(nums)==0:
        print(False)
        return False
    max= nums[0]
    for i in range(0,len(nums)):
        if nums[i]>max:
            max=nums[i]
    print(max)
    return max   
Maximum([0,2,-2,5,256,1451])


# Ultimate Analysis

def ultimate_analysis(nums):        #sumTotal, average, minimum, maximum and length
    if len(nums)==0:
        print ("please fill the list")
        return False
    else:    
        sumT=0
        avg=0
        min=nums[0]
        max=nums[0]
        for i in range(0,len(nums)):
            sumT+=nums[i]
            if nums[i]<min:
                min=nums[i]
            if nums[i]>max:
                max=nums[i]  
        avg=sumT/len(nums)

        print({'sumTotal': sumT , 'average':avg , 'minimum':min, 'maximum':max , 'length':len(nums)  } )
        return {'sumTotal': sumT , 'average':avg , 'minimum':min, 'maximum':max , 'length':len(nums)  }

ultimate_analysis([0,1,2,-2,5,6]) 

#Reverse List
def Reverse_List(nums):
    first=0
    last=len(nums)-1
    
    for i in range(0,len(nums)):
        if first<last:
            temp=nums[first]
            nums[i]=nums[last]
            nums[len(nums)-1-i]=temp
            first+=1
            last-=1
    print(nums)    
    return nums    
Reverse_List([1,2,4,5])



