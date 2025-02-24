#WAP to Find the Leader Elements. (Leader Element: An element is a leader if it is greater than all elements to its right.)

def leader(arr, n):
    for i in range(0,n):
        k=arr[i]
        isBreak=0
        for j in range(i+1,n):
            if arr[j]>=k:
                isBreak=1
                break
        if(isBreak==0):
            print(k,end=" ")

arr=[16, 17, 4, 3, 5, 2]
n=len(arr)
leader(arr,n)
