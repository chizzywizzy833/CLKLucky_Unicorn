# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print('**** How to Play ****')
    print()
    print("The rules of the game go here")
    print()
    return ""


def num_check(question, low, high):
    error = "please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here...
played_before = yes_no("Have you played the game before ")

if played_before == "no":
    instructions()

print()

print("Programs Continues")

# Ask user how much they want to play with...

how_much = num_check("how much would you like to play with? ", 0, 10)

print("you will be spending ${}".format(how_much))
