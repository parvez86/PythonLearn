x = int(input("Enter a number for generating a table: "))

# for i in range(1,11):
#     print(x,'X',i,'=',i*x)
[print(i, 'x', j) for j in range(1, 11) for i in range(1, x+1)]