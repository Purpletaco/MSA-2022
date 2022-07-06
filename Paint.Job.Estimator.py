import math

def get_float_value(prompt):
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

hourly_labor_cost = 62.25
unit_of_wall_area = 350
hours_labor_per_unit = 6

wall_area = get_float_value("What is the area of wall in sq/ft: ")
paint_price = get_float_value("What is the price of paint per gallon: ")

hours_of_labor = (wall_area / unit_of_wall_area) * hours_labor_per_unit
labor_cost = hours_of_labor * hourly_labor_cost
gallons_of_paint = math.ceil(wall_area / unit_of_wall_area)
paint_cost = gallons_of_paint * paint_price
total_cost = paint_cost + labor_cost

print("Report\n----------------------\n")
print(f"Hours of Labor: {hours_of_labor:.2f}")
print(f"Labor Cost: ${labor_cost:.2f}")
print(f"Gallons of Paint: {gallons_of_paint}")
print(f"Paint Cost: ${paint_cost:.2f}")
print(f"Total Job Cost: ${total_cost:.2f}")