import re


class istack:
	def __init__(self):
		self.top = -1
		#stack
		self.array = []

	def isEmpty(self):
		return True if self.top == -1 else False

	# top of the stack
	def get_top(self):
		return self.array[-1]

	# stack pop
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"

	# stack push
	def push(self, op):
		self.top += 1
		self.array.append(op)

# token is operand
def isOperand(ch):
	return isinstance(ch, int)

#priority check
def notGreater(array, i):
	precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
	try:
		a = precedence[i]
		b = precedence[array.get_top()]
		return True if a <= b else False
	except KeyError:
		return False

	
def infixToPostfix(tokens):
	output = []
	array = istack()
	for i in tokens:
		
		if isOperand(i):
			output.append(i)

			
		elif i == '(':
			array.push(i)

			
		elif i == ')':
			while((not array.isEmpty()) and
				array.get_top() != '('):
				a = array.pop()
				output.append(a)
			if (not array.isEmpty() and array.get_top() != '('):
				print("Invalid Input")
				return -1
			else:
				array.pop()

			#means operator
		else:
			while(not array.isEmpty() and notGreater(array,i)):
				output.append(array.pop())
			array.push(i)

	while not array.isEmpty():
		output.append(array.pop())

	return output

def evaluatePostfix(tokens):
	array = istack()
		
	for i in tokens:
			
		#operand
		if isinstance(i, int):
				array.push(i)

		#operator
		else:
			val1 = array.pop()
			val2 = array.pop()
			if i=="*":
				array.push(val1 * val2)
			elif i=="/":
				array.push(val2 / val1)
			elif i=="+":
				array.push(val1 + val2)
			elif i=="-":
				array.push(val2 - val1)

	return int(array.pop())


def get_token(input):
	tokens = []
	i=0
	#these two for checking opening and ending parentheses
	n=0
	m=0
	while i < len(input):
		if input[i] == ' ':
			i += 1
			continue
		elif input[i] == '(':
			n +=1
			tokens.append(input[i])
		elif input[i].isdigit():
			val = 0
			
			while (i < len(input) and
				input[i].isdigit()):
			
				val = (val * 10) + int(input[i])
				i += 1
			
			tokens.append(val)
			i-=1
		elif input[i] == ')':
			m+=1
			tokens.append(input[i])
		else:
			tokens.append(input[i])
		i +=1
	if (n!=m):
		print("Invalid Input")
	else:
		return tokens

if __name__ == "__main__":
	while(True):
		expression = input("enter an arithmetic operation:")
		# checking valid input with regex 
		if not re.search("([-+]?[0-9]*\.?[0-9]+[\/\+\-\*])+([-+]?[0-9]*\.?[0-9]+)",expression):
			print("Invalid Input")
			continue
		else:
			#getting tokens
			tokens = get_token(expression)
			if not tokens: #not matching number of opening and ending parentheses
				continue
			print("Tokens: " + str(tokens))
			#conversing to postfix
			postfix = infixToPostfix(tokens)
			print("Postfix: " + str(postfix))
			result = evaluatePostfix(postfix)
			print ("final result: " + str(result))
			continue


