import project_header as head

class Choices():
    def checkChoice(self):
        i = input()
        while i != "1" and i != "2" and i != "3":
            print("Unrecognized choice, please re-enter: ")
            i = input()
             
        return i
        
    def useChoice(self, file, i):
        line = file.readline()
        while line.strip() != "stop":
            if i == line.strip() :
                line = file.readline()
                print(line)
                line = file.readline()
            else:
                line = file.readline()
                line = file.readline()
            

    def addChoice(self, str):
        
        pass

    def readPrompt(self, file):
        line = file.readline()
        
        while line.strip() != "stop":
            print(line)
            line = file.readline()
        

    def openFile(self):
        
        file = open("C:/Users/danes/OneDrive/Documents/Python/Project_1/Story.md")
        
        return file
        
        

        

