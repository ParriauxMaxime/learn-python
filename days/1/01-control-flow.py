# Hello lucas
# Python is an interpreted language, meaning that it will interpret instruction from bottom to end

print('This will appear first')
print('This will appear second')


# You can create branch instruction in your code with if else statement
if True:
  print('This will print third')
else:
  print('This will never print')

# Or like that
if False:
  print('This will never print')
elif True:
  print('This will print fourth')
else:
  print('This will never print')

if False:
  print('This will never print')
elif 1 + 1 == 0:
  print('This will never print')
else:
  print('This will print fifth')


# You can also create loop like this
i = 0
print ('should print "while" 3 times')
while i < 3:
  print ('while')
  i = i + 1
# Or like this
print ('should print "for" 3 times')
for i in range(0, 3):
  print('for')


# Last but not least you can read arguments (parameters) from the command line
# E.G, if you run `python 01-control-flow.py arg1 arg2 arg3`
# should produce :
# Number of arguments: 4 arguments.
# Argument List: ['01-control-flow.py', 'arg1', 'arg2', 'arg3']
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

# That's all folks