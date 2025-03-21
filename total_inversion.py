import math

#Simple approach 
def count_inversion_simple(a):
    inversion = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                inversion += 1
    return inversion

a = [3,2,1]
total_inversion = count_inversion_simple(a)
print('First approach:')
print('The total inversion of '+ str(a) +' is:', total_inversion)

#Using merge sort 
def merge(a, lp, mid, hp):
    left = lp
    right = mid + 1
    count = 0

    while(left <=mid and right<=hp):
        if (a[left] <= a [right]):
            left += 1
        else:
            count += mid - left + 1
            right +=1

    return count 

def merge_sort(a, lp, hp):
    inversion_count = 0
    if lp >= hp:
        return inversion_count
    mid = math.floor((lp+hp) /2)
    inversion_count += merge_sort(a,lp, mid)
    inversion_count += merge_sort(a, mid+1, hp)
    inversion_count += merge(a, lp, mid, hp)
    return inversion_count

def count_inversion_using_merge_sort(a):
    return merge_sort(a, 0, len(a)-1)

a = [3,2,1]
total_inversion = count_inversion_using_merge_sort(a)
print('Second approach:')
print('The total inversion of '+ str(a) +' is:', total_inversion)
