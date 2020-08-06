# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
# Print out "Even!" if the number is even. Otherwise print "Odd"
num = input('please enter number: ')


def is_even2(num):
    if int(num) % 2 == 0:
        print('even')
    else:
        print('odd')


is_even2(num)
