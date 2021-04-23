import os
path = os.getcwd()
print(f"Current working Directory: {path}")

for file in os.listdir(path):
    print(file)
