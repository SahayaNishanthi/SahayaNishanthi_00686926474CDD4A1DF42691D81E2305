def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return(n*fact(n-1))
print("enter the number")
x=int(input())
f=fact(x)
print("factorial of",x,"=",f)
