length=int(input("Enter the length of your list: "))
list=[]
num=0
question=input("Which sheet do you need? (int,float,string): ")
if question=="Int" or question=="int":
    for i in range(length):
        string="Enter the element #"+str(num)+": "
        list.append(int(input(string)))
        num+=1
    print("List: ",list,sep="")
    list.sort()
    print("Sorted list: ",list,sep="")
elif question=="Float" or question=="float":
    for i in range(length):
        string="Enter the element #"+str(num)+": "
        list.append(float(input(string)))
        num+=1
    print("List: ",list,sep="")
    list.sort()
    print("Sorted list: ",list,sep="")
elif question=="String" or question=="string":
    for i in range(length):
        string="Enter the element#"+str(num)+": "
        list.append(input(string))
        num+=1
    print("List: ",list,sep="")
    list.sort()
    print("Sorted list: ",list,sep="")
else:
    print("Incorrect input")