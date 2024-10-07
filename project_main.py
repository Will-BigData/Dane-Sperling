from project_implementation import Choices


test = Choices()



file = test.openFile()

test.readPrompt(file)
print("Enter Choice: ")
i = test.checkChoice()
test.useChoice(file, i)
