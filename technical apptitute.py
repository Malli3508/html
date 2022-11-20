# Take a string 'aaabbcdaee' and count the string numbers,print 4a,2b,1c,1d,2e
x = 'aaabbcdaee'
count_a=0
count_b=0
count_c=0
count_d=0
count_e=0
for i in range(0,len(x)):
    if x[i]=='a':
        count_a+=1
    elif x[i]=='b':
        count_b+=1
    elif x[i]=='c':
        count_c+=1
    elif x[i]=='d':
        count_d+=1
    elif x[i]=='e':
        count_e+=1
print(count_a,'a',count_b,'b',count_c,'c',count_d,'d',count_e,'e')
