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

def deleterecords():
    file = open("Salaries.csv", "r")
    tmplist = []
    x = 0

    for row in file:
        tmplist.append(row)
    file.close()

    for row in tmplist:
        print(x, row)
        x += 1

    rowtodelete = int(input("Enter a row number to delete: "))
    tmplist.pop(rowtodelete)
    print("You delete a name!")

    file = open("Salaries.csv", "w")

    for row in tmplist:
        file.write(row)
    file.close()


def main():
    tryagain = True
    while tryagain:
        print("1) Add to file")
        print("2) View all records")
        print("3) Delete a record")
        print("4) Quit")
        print()

        selection = int(input("Please enter a number of your selection: "))

        if selection == 1:
            addtofile()

        elif selection == 2:
            viewrecords()

        elif selection == 3:
            deleterecords()

        elif selection == 4:
            tryagain = False

        else:
            print("Incorrect option")


main()
