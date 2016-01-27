# Source: https://docs.python.org/2/tutorial/introduction.html#first-steps-towards-programming
#
print "\nGenerate Fibonacci series below 10...\n"
print "Result with python's 'multiple assignment' feature:"
a, b = 0, 1
while b<10:
	print b
	# For multiple assignment, right hand side expressions are 
	# evaluated from left to right.
	# Multiple assignment occurs for each variables simultaneously
	# So "b, a = a+b, b" will produce the same result.
	a, b = b, a+b

print "\nResult with traditional temporary variable:"
a, b = 0, 1
while b<10:
	print b
	t = a+b
	a = b
	b = t
