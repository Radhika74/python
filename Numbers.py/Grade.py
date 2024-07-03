print("Enter you marks")
marks1 = int(input())
marks2 = int(input())
marks3 = int(input())
marks4 = int(input())
marks5 = int(input())
Average=sum([marks1,marks2,marks3,marks4,marks5])/5
if Average>=90:
    print("grade A")
elif Average>=80 and Average<=89:
    print("grade B")
elif Average>=70 and Average<=79:
    print("grade C")
elif Average>=60 and Average<=69:
    print("grade D")
else:
    print("grade E")
