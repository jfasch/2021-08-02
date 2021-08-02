import sys

num1str = sys.argv[1]
num2str = sys.argv[2]

num1 = int(num1str)
num2 = int(num2str)

print('Value1:', num1, 'Type1:', type(num1), 'Value2', num2, 'Type2:', type(num2))

if num1 < num2:
    max = num2
else:
    max = num1

print('The maximum value is:', max)
