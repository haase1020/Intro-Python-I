import string

# # if you want to store all of the even nums in the range
# # 1-100 in a list
# # how can you do this?
# evens_1 = []
# # loop through the range
# for i in range(101):
#     # check if the current number is even
#     if i % 2 == 0:
#         evens_1.append(i)

# print(evens_1)

# # comprehensions allow us to write the above logic concisely:
# evens_2 = [i for i in range(101) if i % 2 == 0]

# print(evens_1 == evens_2)

# # print square values of numbers in range 1-10

# squares_1 = []
# for i in range(1, 11):  ## This includes start value doesn't include end value
#     squares_1.append(i**2)

# print(squares_1)

# squares_2 = [i**2 for i in range(1, 11)]
# print(squares_2)
# # don't need the append method because it is implied for list comprehension
# # great way to populate lists

# names = ["Mandi", "noel", "caleb", "timothy", "matt"]

# m_names = []
# for name in names:
#     # check if the name starts with `m`
#     # if name[0] == 'm' or 'M':
#     if name[0].lower() == 'm':
#         m_names.append(name.capitalize())

# print(m_names)

# if it does, add it to the m_names and capitalize

########Dictionaries#######################
# can use comprehension with dictionaries too!
# populate a dict with all letters of alphabet, with corresponding
# place in alphabet
letters = string.ascii_lowercase

alpha = {letter: i + 1 for i, letter in enumerate(letters)}

# traditional way of doing things
# for i, letter, in enumerate(letters):
# alpha[letter] = i +1
print(alpha)
