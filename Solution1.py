def SumProduct(num1,num2): 
  """
  the function returns the product if the result is < or = 1000 and the sum otherwise
  """
    if (num1 * num2) <= 1000 : 
        return num1 * num2 #if true return the product
    else:
        return num1 + num2 #if not return the sum
      
#Calling the function
result = SumProduct(20,30)
print(f'The result is {result}')
result = SumProduct(20,70)
print(f'The result is {result}')

#Note : 
#I didn't assign the equation to a variable because the function was pretty easy and no need to occupy so much space (memory).
#However when we face a situation where the output is used many times or when the function gets more "complicated" (nothing is complicated)
#it will be best to name variables to refer to later on.

