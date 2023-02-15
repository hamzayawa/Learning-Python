# Check if num is divisible by 2 and 3

num = int(input("Enter Number: "))

if num % 2 == 0:
   if num % 3 == 0:
      print ("Divisible by 2 and 3")
   else:
      print ("Divisible by 2 not divisible by 3")
else:
   if num % 3 == 0:
      print ("Divisible by 3 not divisible by 2")
   else:
      print  ("Not Divisible by 2 not divisible by 3")
