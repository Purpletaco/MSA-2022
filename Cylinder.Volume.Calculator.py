import math
def get_value(prompt):
    run_again = True
    while (run_again):
        try:
            user_input = float(input(prompt))
            if(user_input <= 0):
                print("ERROR: Value must be greater than 0.\n")
                continue
        except:
            print("ERROR: Input must be a number.\n")
        else:
            run_again = False
    
    return user_input
           
rerun = True
while(rerun):
    radius = get_value("What is the radius of the cylinder in inches: ")
    height = get_value("What is the height of the cylinder in inches: ")
    volume = radius * height * math.pi * 2
    print(f"The volume of the cylinder is {volume:.2f} inches cubed.")
    do_again  = input("Would you like to perform another caclulation?\n Press 'n' to quit or any key to continue")
    if do_again == "n":
        print("Goodbye")
        rerun = False