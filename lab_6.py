def fizzbuzz(n):
  result=[]
  for number in range(1,n):
      if number%3==0 and number%5==0:
        result.append('FizzBuzz')
      elif number%3==0:
        result.append('Fizz')
      elif number%5==0:
        result.append("Buzz")
      else:
        result.append(number)
        
  return(result)
x=fizzbuzz(9)
print(x)

