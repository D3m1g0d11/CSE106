def fileWriter():

    punish = input("What sentence would you like to repeat? ")
    num = input("How many times? ")


    path = "/Users/John Biton/College Code/CSE S23/CSE 106/Lab 1/"
    with open(path + "CompletedPunishment.txt", "r+") as file:
        for i in range(int(num)):
            file.write(punish + '\n')

        file.close()

fileWriter()