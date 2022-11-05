
try:
    f = open('test.txt')
    print(f.read())
except Exception as e:
    print(e)
    print("File not found")
    with open('test.txt', 'w') as f:
        f.write("Hello I am a file!")