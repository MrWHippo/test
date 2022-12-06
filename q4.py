
question = ["how","what","why","when","who","where"]

exit = False
while exit == False:
    line = input()
    answer = 0
    line = line.split()
    for x in range(6):
        if line[0] == question[x]:
            print("not sure really")
            answer = 1
            
    if line[-1] == "goodbye":
        print("see you!")
        answer = 1
        exit = True
    elif line[-1] == "?":
        print("not sure really")
        answer = 1
    
    if answer == 0:
        print("but why?")
    
    