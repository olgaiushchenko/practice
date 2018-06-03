# You are tasked with determining whether a string of parenthesis is correctly balanced. Write a function that takes as input a single string 
#that may contain any ASCII character and determines at that moment whether or not the associated parenthesis ([, ], (, ),{,}) are correctly closed. 
#Return true or false accordingly.

# All open parenthesis should be closed in the same order that they were opened

def check_parens(str):
	o = ['(', '[', '{']
	c = [')', ']', '}']
	stack = []
	for element in str:
		if element in o:
			stack.append(element)
		elif len(stack) == 0:
			return False
		elif element in c and c.index(element) == o.index(stack[0]):
			stack.pop()

	if len(stack) == 0:
		return True
	else:
		return False
