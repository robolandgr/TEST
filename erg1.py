import random

def code(list1,list2):
    for i in range(0,len(list1)-1):
        list1[i]=list2[0]
        for j in range (1,i,1):
            list1[i]=list1[i]+list2[j]
    print(list2)



#Main Program
list2=[]
list1=list(range(1,10)) #dimiourgia listas me 100 stoixeia
#list1=random.sample(list1,k=10) #epilogi enos merous tis listas(10 stoixeia)
code(list1,list2)


