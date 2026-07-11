import os

# Specify the directory path
path = input("Enter the directory path: ")

# Check if the directory exists
if os.path.exists(path):
    print("\nContents of the directory:")
    for item in os.listdir(path):
        print(item)
else:
    print("Directory does not exist.")