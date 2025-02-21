########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
class Q2:
	def store_original_ids(self):
		pass

	def check(self):
		pass

q2 = Q2()
q2.store_original_ids()
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.

temp = a
a = b
b = temp
 
# << a, b = b, a --> do the same thing as above 

print(a, b)
######################################################################

# Check your answer
q2.check()