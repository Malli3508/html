# print how many times reapeted 10,20,30
mylist=[10,20,10,20,30]
count1=0
count2=0
count3=0
for i in range(0,len(mylist)):
    if mylist[i]==10:
        count1=count1+1
    elif mylist[i]==20:
        count2=count2+1
    else:
        count3=count3+1
print('10 is ',count1,'times')
print('20 is',count2,'times')
print('30 is',count3,'times')