
'''
    "r" --> read the file
    "w" --> create a file and writes on it
    "a" --> opens existing file if file exists 
'''

try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print("no file found")

file = f.read()