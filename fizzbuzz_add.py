import sys
i=1
if len(sys.argv)>0:
  try:
    x=int(sys.argv[1])
  except ValueError:
    x=int(raw_input("Please put upper range in integer format"))
else:
  try:
    x=int(raw_input("Please put upper range"))
  except ValueError:
    x=int(raw_input("Please put upper range in integer format"))
for i in range(1,x):
  if i%15==0:
    print "fizzbuzz"
  elif i%3==0:
    print "fizz"
  elif i%5==0:
    print "buzz"
  else:
    print i
  i+=1