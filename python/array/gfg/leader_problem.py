import array as arr

leader = []

"""
#time limit extending error
#approaching from front
#Time Complexity: O(N * N)
#Auxiliary Space: O(1)
def leaders(arr,size): 
    for i in range(0,size):
        flag = True
        for j in range(i+1,size):
            if arr[i]<=arr[j]:
                flag = False
                
        if flag==True:
            print(j)
            leader.append(arr[i])
    return leader

"""

#brute force method
#Time Complexity: O(n)
#Auxiliary Space: O(1)
def leaders(arr,size):

    leader = []
    max = arr[size-1]
    leader.append(max)

    #iterating through array in reverse dirction
    for i in range(size-2, -1, -1):
    #for i in range(-2, -1*(size+1), -1): [another for loop method]
        if arr[i]>=max:
            leader.append(arr[i])
            max = arr[i]
    return leader[::-1]

arr=[16, 17, 4, 3, 5, 2]
print(leaders(arr, len(arr)))