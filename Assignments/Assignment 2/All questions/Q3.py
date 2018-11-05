'''Give a single command that computes the sum from Exercise 
   R-1.6, relying on Python’s comprehension syntax and the
   built-in sum function.'''
   
   
   
s = [1,2,3,4,5,6,7,8,9,10]
for n in s:              		#this loop prints in forward order
    print(s[n-1])
for m in range(-len(s),0):  	#this loop prints in reverse order
    print(s[m+len(s)])
