# Task 2.2
# Write a program that lists all the files and directories in the current directory.
import os

def list_files_and_directories(path='.'):
    for root, dirs, files in os.walk(path):
        print("Current directory:", root)
        for name in dirs:
            print("Directory:", name)
        for name in files:
            print("File:", name)

# Example usage
list_files_and_directories()
