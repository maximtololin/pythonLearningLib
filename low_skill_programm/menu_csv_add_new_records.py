import csv


def addtofile():
    file = open("Salaries.csv", "a")
    name = input("Enter a name: ")
    salary = int(input("Enter a salary: "))
    newrecord = name + "," + str(salary) + "\n"
    file.write(str(newrecord))
    file.close()
    return


def viewrecords():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()
    return


def main():
    tryagain = True
    while tryagain:
        print("1) Add to file")
        print("2) View all records")
        print("3) Quit")
        print()

        selection = int(input("Please enter a number of your selection: "))

        if selection == 1:
            addtofile()

        elif selection == 2:
            viewrecords()

        elif selection == 3:
            tryagain = False

        else:
            print("Incorrect option")


main()
