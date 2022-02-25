from set_of_stacks import SetOfStacks

set_of_stacks = SetOfStacks(2)

for i in range(10):
    set_of_stacks.push(i)

set_of_stacks.print()

for i in range(5):
    set_of_stacks.pop()

set_of_stacks.print()