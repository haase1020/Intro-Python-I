
import os
import platform
import sys

# for (let i = 0; i < nums.length; i++) in JS
# for n in range(10):
#     print(n)
# very last item not included, defaults at 0
# for a in range(2, 10):
#     print(a)

nums = [1, 2, 5, 4, 6]

for i in range(len(nums)):
    print(i, nums[i])

# can also do following:
# associated index
# this produces the index and then the value
# enumerate always produces index then value (in that order)
for i, v in enumerate(nums):
    print(i, v)


# great advice from stack overflow:
# Use os.name to check whether it's a posix-compliant system.
# sys.platform to check whether it's a linux, cygwin, darwin, atheos, etc.
# Use platform.system() if you don't believe the other sources.


# returns 'nt': 'nt' means you are running on windows, and 'posix' mac
print("os.name is: ", os.name)
print("sys.platform is: ", sys.platform)  # returns win32
print("platform.system()", platform.system())  # returns Windows
# print("python version using: ", sys.version)
# print("current process ID: ", os.getpid())
# print("current working directory: ", os.getcwd())
# print("machine's login name: ", os.getlogin())
