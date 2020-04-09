from min_stack import MinStack

stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(-5)

stack.print()
print(stack.min())
stack.pop()
print(stack.min())

# min can be defined as an instance variable of the Stack