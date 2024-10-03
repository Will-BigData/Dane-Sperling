import project_header as head
import csv
with open("C:/Users/danes/OneDrive/Documents/Python/Project_1/Story.md") as file:
    
    print(file.readline())
    string = file.__next__().strip()
    print(string)
    print(string == "Stop")
    if string == "Stop":
        print("Works")
    else:
        print(file.readline())

    """ for line in file:
        # Strip whitespace and check if the line is "Stop"
        if line.strip() == "Stop":
            break  # Stop reading if "Stop" is encountered
        print(line.strip())  # Process the line (e.g., print it) """

file.close()
class choices(head.choices):
    def checkChoice(str):
        pass
    
    def addChoice(str):
        pass

    def openFile():
        pass

