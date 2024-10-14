from project_implementation import Choices


test = Choices()

i = 'Y'
while i == 'Y':
    file = test.openFile()
    lines = file.readlines()
    file.close()

    file = test.openFile()
    check = test.readPrompt(file)

    i = test.checkChoice()
    if i == "Quit" or i == "quit":
        exit(0)

    while not check:
        test.nextPrompt(file, lines, i)
        check = test.readPrompt(file)
        if not check:
            i = test.checkChoice()
        
            if i == "Quit" or i == "quit":
                exit(0)

    print("Your journey has ended, want to play again? Y/N")
    i = test.endChoice()
    file.close()
    test.outFile()

    
""" test.nextPrompt(file, lines, i)
check = test.readPrompt(file)
i = test.checkChoice()
if i == "Quit" or i == "quit":
    exit(0)
test.nextPrompt(file, lines, i)
check = test.readPrompt(file) """