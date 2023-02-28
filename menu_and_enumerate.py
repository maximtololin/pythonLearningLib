import random
import enum

# def ask_value():
#     num = int(input("Enter a number: "))
#     return num
#
#
# def count(num):
#     n = 1
#     while n <= num:
#         print(n)
#         n = n + 1
#
#
# def main():
#     num = ask_value()
#     count(num)
#
#
# main()


# def pick_num():
#     low = int(input("Enter a small number: "))
#     big = int(input("Enter a big number: "))
#     comp_num = random.randint(low, big)
#     return comp_num
#
#
# def first_guess():
#     print("I'm thinking of a number...")
#     guess = int(input("What am I thinking of: "))
#     return guess
#
#
# def check_answer(comp_num, guess):
#     try_again = True
#     while try_again:
#         if comp_num == guess:
#             print("Correct, you win!")
#             try_again = False
#         elif comp_num > guess:
#             guess = int(input("Too low, try again: "))
#         elif comp_num < guess:
#             guess = int(input("Too high, try again: "))
#
#
# def main():
#     comp_num = pick_num()
#     guess = first_guess()
#     check_answer(comp_num, guess)


# main()


# def addition():
#     num1 = random.randint(5, 20)
#     num2 = random.randint(5, 20)
#     print(num1, "+", num2, "=")
#     user_answer = int(input("Your answer: "))
#     actual_answer = num1 + num2
#     answers = (user_answer, actual_answer)
#
#     return answers
#
#
# def subtraction():
#     num3 = random.randint(25, 50)
#     num4 = random.randint(1, 25)
#     print(num3, "-", num4, "=")
#     user_answer = int(input("Your answer: "))
#     actual_answer = num3 - num4
#     answers = (user_answer, actual_answer)
#
#     return answers
#
#
# def check_answer(user_answer, actual_answer):
#     if user_answer == actual_answer:
#         print("Congratulations, you got it right!")
#     else:
#         print("Sorry, incorrect, the answer is: ", actual_answer)
#
#
# def main():
#     print("1) Addition")
#     print("2 Subtraction")
#     selection = int(input("Enter 1 or 2: "))
#
#     if selection == 1:
#         user_answer, actual_answer = addition()
#         check_answer(user_answer, actual_answer)
#
#     elif selection == 2:
#         user_answer, actual_answer = subtraction()
#         check_answer(user_answer, actual_answer)
#
#     else:
#         print("You enter a wrong number!")
#
#
# main()


names = []
new_list = ["123", "222"]


def add_name():
    name = input("Enter a new name:")
    names.append(name)

    return names


def change_name():
    num = 0

    for name in names:
        print(num, ": ", name)
        num += 1

    select_num = int(input("Select a number of name: "))
    new_name = input("Enter a new name:")
    names[select_num] = new_name
    print("You changed a name!")
    return names


def delete_name():
    num = 0

    for name in names:
        print(num, ": ", name)
        num += 1

    select_num = int(input("Select a number of name: "))
    names.pop(select_num)
    print("You deleted a name!")
    return names


def view_name():
    # num = 0
    #
    # for name in names:
    #     print(num, ": ", name)
    #     num += 1
    for index, name in enumerate(names):
        print(f"{index}: {name}")


def main():
    again = 'y'
    while again == 'y':
        print("1 Add name ")
        print("2 Change name ")
        print("3 Delete name ")
        print("4 View names ")
        print("5 Quit program ")

        select_number = int(input("Select a number: "))

        if select_number == 1:
            print(add_name())

        elif select_number == 2:

            print(change_name())

        elif select_number == 3:

            print(delete_name())

        elif select_number == 4:

            view_name()

        elif select_number == 5:
            again = 'n'

        else:
            print("Wrong number!")
        data = (names, again)

    return


main()
