import random

def creating_grid():
    while True:    
        try:
            length_of_grid_input = int(input("How big is the side of the grid? "))
            if length_of_grid_input <= 0:
                print("Grid size must be at least 1.")
            elif length_of_grid_input > 100:
                print("Maximal size of the grid is 100.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    grid_local = [["." for x in range(length_of_grid_input)] for y in range(length_of_grid_input)]
    return grid_local, length_of_grid_input

def printing_grid(grid_local):
    for i in grid_local:
            print(i)
    return grid_local

def defining_number_ships():
    max_ships = int((len(grid)**2)/2)
    while True:
        try:
            number_ships_input = int(input("Enter the number of ships: "))
            if number_ships_input <= 0 or number_ships_input > max_ships:
                print("The number of ships must be at least 1, but cannot be more than " + str(max_ships) + ". ")
            else:
                return number_ships_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

def ship_placing_function(grid, number_ships, length_of_grid):
    grid_local = grid
    player_ships = []
    for i in range(1, number_ships + 1):
        while True:
            try:
                player_ship_x_input = int(input(f"Please enter the x coordinate for your ship {i}: "))
                player_ship_y_input = int(input(f"Please enter the y coordinate for your ship {i}: "))
            except ValueError:
                print("Please enter an integer.")
            if player_ship_x_input < 1 or player_ship_y_input < 1 or player_ship_x_input > length_of_grid or player_ship_y_input > length_of_grid:
                print(f"One of the coordinates for ship {i} is out of range. The coordinate has to be between 0 and " + str(length_of_grid) + ".")
            else:
                print(grid_local[player_ship_x_input - 1][player_ship_y_input -1 ])
                if grid_local[player_ship_x_input - 1][player_ship_y_input -1 ] == ".":
                    grid_local[player_ship_x_input - 1][player_ship_y_input - 1] = "x"
                    break
                else:
                    print("Field already occupied.") 
            
        player_ships.append([player_ship_x_input - 1,player_ship_y_input - 1])
    return player_ships, grid_local



grid, length_of_grid = creating_grid()
printing_grid(grid)
number_ships = defining_number_ships()
position_player_ships, grid_with_player_ships = ship_placing_function(grid, number_ships, length_of_grid)
print(position_player_ships)
printing_grid(grid_with_player_ships)
