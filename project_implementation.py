import project_header as Choices

class Choices():
    choicesList = []


    def checkChoice(self):
        print("Enter Choice: ")
        i = input()
        while i != "1" and i != "2" and i != "3" and i != "Quit" and i != "quit":
            print("Unrecognized choice, please re-enter: ")
            i = input()
        self.addChoice(i)
        return i
        
    def endChoice(self):
        print("Enter Choice: ")
        i = input()
        while i != "Y" and i != "N":
            print("Unrecognized choice, please re-enter: ")
            i = input()
        self.addChoice(i)
        return i

    def addChoice(self, str):
        self.choicesList.append(str)
        pass

    def readPrompt(self, file)-> bool:
        
        line = file.readline()
        
        while line.strip() != "stop" and line.strip() != "finish":
            print(line)
            line = file.readline()
        if line.strip() == "finish":
            return True
        return False

    def nextPrompt(self, file, lines, i):
        l = file.readline()
        while l.strip() != i:
            l = file.readline()
            
        
        
        #After choice is found
        num_str = file.readline()
        num = int(num_str)
        
        l = file.readline()
        
        while l != lines[num - 1]:
            l = file.readline()

        print(l)
        pass
        

    def openFile(self):
        
        file = open("C:/Users/danes/OneDrive/Documents/Python/Project_1/Story.md")
        
        return file
        
    def outFile(self):
        file = open("C:/Users/danes/OneDrive/Documents/Python/Project_1/Choices.txt", "w")
        for i in self.choicesList:
            file.write(i)
            file.write("\n")
        file.close()
        pass
        

        

