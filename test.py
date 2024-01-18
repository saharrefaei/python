N = float(input('Number ? : '))

while True:
   M = float(input("do you want more number ?"))
   if N < M :
     N = M 
   s = input("do you wanna continue ?")
   if s.lower() == "no" :
       break

print('the lower is ' , M)