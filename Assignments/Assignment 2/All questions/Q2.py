'''Give a single command that computes the sum
   from Exercise R-1.6, relying on Python’s 
   comprehension syntax and the built-in sum 
   function.'''


oddSum = sum([x*x for x in range(int(input("Enter Value of n: "))) if x%2 != 0])
print(oddSum)
