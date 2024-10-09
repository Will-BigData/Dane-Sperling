from project_implementation import Choices


test = Choices()



file = test.openFile()
lines = file.readlines()
file.close()

file = test.openFile()
test.readPrompt(file)

i = test.checkChoice()
if i == "Quit" or i == "quit":
    exit(0)

test.nextPrompt(file, lines, i)
test.readPrompt(file)