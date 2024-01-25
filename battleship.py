player_ships = []

def creating_grid():
    while True:
        length_of_grid_input = input("How big is the side of the grid? ")
        try:
            length_of_grid_local = int(length_of_grid_input)
            if length_of_grid_local <= 0:
                print("Grid size must be at least 1.")
            elif length_of_grid_local > 100:
                print("Maximal size of the grid is 100.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return [["." for x in range(length_of_grid_local)] for y in range(length_of_grid_local)]
        
def defining_number_ships():
    max_ships = int((len(grid)**2)/2)
    print(max_ships)
    while True:
        number_ships_input = (input("Enter the number of ships: "))
        try:
            number_ships_local = int(number_ships_input)
            if number_ships_local <= 0 or number_ships_local > max_ships:
                print("The number of ships must be at least 1, but cannot be more than " + str(max_ships) + ". ")
            else:
                return number_ships_local
        except ValueError:
            print("Invalid input. Please enter an integer.")

grid = creating_grid()
print(grid)
number_ships = defining_number_ships()

def ship_placing_function():
    for i in range(1, number_ships + 1):
        player_ship = input(f"Please enter the coordinates for your ship {i} in a (x/y) format: ")
        player_ships.append(player_ship)
    return player_ships
