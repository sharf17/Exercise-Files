# n = int(input())
# if(n%8 == 0):
#     print('side upper')
# elif(n%8==1 or n%8==4):
#     print('lower berth')
# elif(n%8==2 or n%8==5):
#     print('middle')
# elif(n%8==3 or n%8==6):
#     print('upper berth') 
# else:
#     print('side lower') 
a = int(input())
l = []
for i in range(a):
    b = int(input())
    l.append(i)
print(l)
for i in range(1,10):
    if i in a:
        pass
    else:
        print(i)