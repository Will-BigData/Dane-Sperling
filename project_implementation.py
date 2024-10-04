import project_header as head

class Choices():
    def checkChoice(self, str):
        print("works")
        if str == "Hi":
            print("Howdy")
        
    
    def addChoice(self, str):
        pass

    def openFile(self):
        
        file = open("C:/Users/danes/OneDrive/Documents/Python/Project_1/Story.md")
        print(file.read())
        """ with open("C:/Users/danes/OneDrive/Documents/Python/Project_1/Story.md") as file:
            
            string = file.__next__().strip()
            while string != "Stop":
                print(file.readline())
            file.close() """

