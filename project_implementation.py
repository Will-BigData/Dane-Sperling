import project_header as head

class Choices():
    def checkChoice(self):
        print("Enter Choice: ")
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
                while line.strip() != "stop":
                    print(line)
                    line = file.readline()
            else:
                line = file.readline()
                while line.strip() != "stop":
                    line = file.readline()
                line = file.readline()
                line = file.readline()
            
            

    def addChoice(self, str):
        
        pass

    def readPrompt(self, file):
        
        line = file.readline()
        
        while line.strip() != "stop":
            print(line)
            line = file.readline()

    def nextPrompt(self, file, lines, i):
        l = file.readline()
        while l.strip() != i:
            l = file.readline()
            
        
        
        #After choice is found
        num_str = file.readline()
        num = int(num_str)
        
        l = file.readline()
        while l != lines[num - 2]:
            l = file.readline()

        
        pass
        

    def openFile(self):
        
        file = open("C:/Users/danes/OneDrive/Documents/Python/Project_1/Story.md")
        
        return file
        
        

        

