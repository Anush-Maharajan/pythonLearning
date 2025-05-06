st = "he12o_Python"
x = 9

# string Index
print(st[7])

# string slicing
print(st[1:6:2])
print(st[2:9:2])

# string slicing using variable
print(st[1:x:2])

# string slicing using negative index
print(st[-5:-11:-1])

# string finding
print(st.find("Python"))

# string stripping
print(st.strip())

print(st[:])

print(st[::-1])