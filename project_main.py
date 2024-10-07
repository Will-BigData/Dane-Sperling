from project_implementation import Choices


test = Choices()



file = test.openFile()
lines = file.readlines()
file.close()
file = test.openFile()

test.readPrompt(file)
print("Enter Choice: ")
i = test.checkChoice()
test.useChoice(file, i)
test.nextPrompt(file, lines)