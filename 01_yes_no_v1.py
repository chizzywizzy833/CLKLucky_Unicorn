# Ask the user if they have played before
show_instructions = input("Have you played this game before?"). lower()


# If they say yes, output 'program continues'
# If they say no, output 'display instructions'
# If the answer is invalid, print an error
if show_instructions == "yes":
    print("program continues")

elif show_instructions == "y":
    print("program continues")

elif show_instructions == "no":
    print("display instruction")

elif show_instructions == "n":
    print("display instructions")

# If they say no, output "display instructions"
else:
    print("please answer yes / no")
