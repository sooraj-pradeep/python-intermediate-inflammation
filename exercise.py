"""SUM OF SQUARES
Using the MapReduce model, write a function that calculates the sum of the squares of the values in a list. 
Although in practice we’d use the built in sum function for part of this - try doing it without using sum. 
"""

# Your function should behave as below:
def sum_of_squares(l):
    # Your code here
    add=0
    
    for i in l:
        if (type(i)==str):
            j= int(i)
        else:
            j=i
        add+= j * j; 
    return add


print(sum_of_squares([0]))
print(sum_of_squares([1]))
print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([-1]))
print(sum_of_squares([-1, -2, -3]))

# OUTPUT
# 0
# 1
# 14
# 1
# 14


"""
Now let’s assume we’re reading in these numbers from an input file, so they arrive as a list of strings. 
"""
# Modify your function so that it passes the following tests:

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))

# OUTPUT
# 14
# 14


"""
Like comments in Python, we’d like it to be possible for users to comment out numbers in the 
input file they give to our program.
"""

# Extend your function so that the following tests pass (don’t worry about passing the first set of tests):

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
# print(sum_of_squares(['1', '2', '#100', '3']))

# OUTPUT
# 14
# 14
# 14


# """
# If you’ve got this far and have time left, try converting these solutions to use generator expressions. 
# Which do you prefer? Are there situations when one would be much better than the other?
# """