from random import randrange

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

def printing_grid(alphabet, grid_local):
    grid_for_printing = [list(row) for row in grid_local]
    for row, x in enumerate(grid_for_printing):
        for column, y in enumerate(x):
            for size in range(1,6):
                for letter in alphabet:
                    ship_code = ("O" + str(size) + (str(letter)))
                    grid_for_printing[row][column] = grid_for_printing[row][column].replace(ship_code, ".")
    for row in grid_for_printing:
        print(row)

def testing_printing_grid(grid_local):
    print("\nTesting if printing grid works:")
    for row in grid_local:
        print(row)

def defining_number_ships_one_size_ships(grid):
    max_ships = int(((len(grid)**2)/2)/2) #divided by two because two players and then again divided by two so half of the spaces remain empty to be able to make moves
    while True:
        try:
            number_ships_input = int(input("Enter the number of ships: "))
            if number_ships_input <= 0 or number_ships_input > max_ships:
                print("The number of ships must be at least 1, but cannot be more than " + str(max_ships) + ". ")
            else:
                return number_ships_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

def defining_size_number_ships_bigger_ships(alphabet, length_of_grid):
    fleet_size_local = {}
    for size in range (1, 6):
        while True:
            try: 
                ship_amount = int(input("How many ships with size " + str(size) + " do you want? "))
                if ship_amount > 24: 
                    print("Too many ships, limit is 24.")
                elif ship_amount > 0:
                    for _ in range(0, ship_amount):
                        fleet_size_local[str(size) + str(alphabet[_])] = int(size)
                    break
                elif ship_amount == 0:
                    break
            except ValueError:
                "Invalid answer. Please write a number."
    return fleet_size_local

def player_ship_placing_one_size_ships(grid_local, number_ships, length_of_grid):
    player_ships = []
    for i in range(1, number_ships + 1):
        while True:
            try:
                player_ship_x_input = int(input(f"Please enter the x coordinate for your ship {i}: "))
                player_ship_y_input = int(input(f"Please enter the y coordinate for your ship {i}: "))
            except ValueError:
                print("Please enter an integer.")
                continue
            if player_ship_x_input < 1 or player_ship_y_input < 1 or player_ship_x_input > length_of_grid or player_ship_y_input > length_of_grid:
                print(f"One of the coordinates for ship {i} is out of range. The coordinate has to be between 0 and " + str(length_of_grid) + ".")
            else:
                if grid_local[player_ship_x_input - 1][player_ship_y_input -1 ] == ".":
                    grid_local[player_ship_x_input - 1][player_ship_y_input - 1] = "X"
                    break
                else:
                    print("Field already occupied.")
        player_ships.append([player_ship_x_input, player_ship_y_input])
    return player_ships, grid_local

def player_ship_placing_bigger_ships(fleet_size_local, grid_local, length_of_grid):
    for ship_name, ship_size in fleet_size_local.items():
        while True:
            try:
                orientation = str(input("Do you want to place the ship with size " + str(ship_name) + " vertically (v) or horizontally (h)? "))
                if orientation == "v" or orientation == "h":
                    break
                else:
                    print("Invalid answer. Please choose \"v\" or \"h\".")
            except ValueError:
                print("Invalid answer. Please choose \"v\" or \"h\".")

        while True:
            try:
                x_coordinate_ship = int(input("In which column (x) should the ship with size " + str(ship_name) + " start? "))
                y_coordinate_ship = int(input("In which row (y) should the ship with size " + str(ship_name) + " start? "))
            except ValueError:
                print("Invalid input")
                continue 

            if x_coordinate_ship < 1 or x_coordinate_ship > length_of_grid or y_coordinate_ship < 1 or y_coordinate_ship > length_of_grid:
                print("Coordinate has to be between 1 and " + str(length_of_grid) + ".")
            elif (x_coordinate_ship -1 + int(ship_size)) > length_of_grid and orientation == "h":
                print("Ship cannot fit on grit. Choose another starting point.")
            elif (y_coordinate_ship -1 + int(ship_size)) > length_of_grid and orientation == "v":
                print("Ship cannot fit on grit. Choose another starting point.")
            else:
                valid_placement = True

                if orientation == "v":
                    for i in range(ship_size):
                        if grid_local[y_coordinate_ship - 1 + i][x_coordinate_ship - 1] != ".":
                            print("One of the spaces is already taken. Choose another starting point.")
                            valid_placement = False
                            break
                    if valid_placement:
                        for i in range(ship_size):
                            grid_local[y_coordinate_ship - 1 + i][x_coordinate_ship - 1] = "X" + str(ship_name)
                        printing_grid(alphabet, grid_local)
                        break
                elif orientation == "h":
                    for i in range(ship_size):
                        if grid_local[y_coordinate_ship - 1][x_coordinate_ship - 1 + i] != ".":
                            print("One of the spaces is already taken. Choose another starting point.")
                            valid_placement = False
                            break
                    if valid_placement:
                        for i in range(ship_size):
                            grid_local[y_coordinate_ship - 1][x_coordinate_ship - 1 + i] = "X" + str(ship_name)
                        printing_grid(alphabet, grid_local)
                        break
    return grid_local

def computer_ship_placing_bigger_ships(fleet_size_local, grid_local, length_of_grid):
    for ship_name, ship_size in fleet_size_local.items():
        while True:
            orientation_random_number = randrange(0, 2)
            if orientation_random_number == 0:
                orientation = "v"
            elif orientation_random_number == 1:
                orientation = "h"
            print(orientation)
        
            x_coordinate_ship = randrange(0, length_of_grid)
            y_coordinate_ship = randrange(0, length_of_grid)
            print(x_coordinate_ship, y_coordinate_ship)

            if (x_coordinate_ship + int(ship_size)) > length_of_grid and orientation == "h":
                print("Ship cannot fit on grit. Choose another starting point.")
            elif (y_coordinate_ship + int(ship_size)) > length_of_grid and orientation == "v":
                print("Ship cannot fit on grit. Choose another starting point.")
            else:
                valid_placement = True

                if orientation == "v":
                    for i in range(ship_size):
                        if grid_local[y_coordinate_ship + i][x_coordinate_ship] != ".":
                            print("One of the spaces is already taken. Choose another starting point.")
                            valid_placement = False
                            break
                    if valid_placement:
                        for i in range(ship_size):
                            grid_local[y_coordinate_ship + i][x_coordinate_ship] = "O" + str(ship_name)
                        printing_grid(alphabet, grid_local)
                        break
                elif orientation == "h":
                    for i in range(ship_size):
                        if grid_local[y_coordinate_ship][x_coordinate_ship + i] != ".":
                            print("One of the spaces is already taken. Choose another starting point.")
                            valid_placement = False
                            break
                    if valid_placement:
                        for i in range(ship_size):
                            grid_local[y_coordinate_ship][x_coordinate_ship + i] = "O" + str(ship_name)
                        printing_grid(alphabet, grid_local)
                        break
    return grid_local

def computer_ship_placing_one_size_ships(grid_local, number_ships, length_of_grid):
    computer_ships = []
    for i in range(0, number_ships):
        while True:
            computer_ship_x_random = randrange(0,length_of_grid)
            computer_ship_y_random = randrange(0,length_of_grid)
            #print("(" + str(computer_ship_x_random) + "/" + str(computer_ship_y_random) + ")")
            if grid_local[computer_ship_x_random][computer_ship_y_random] == ".":
                grid_local[computer_ship_x_random][computer_ship_y_random] = "O"
                break
        computer_ships.append([computer_ship_x_random,computer_ship_y_random])
    return computer_ships, grid_local

def player_move_one_size_ships(grid_local, length_of_grid):
    while True:
        try:
            player_move_x_input = int(input(f"Please enter the x coordinate for your move: "))
            player_move_y_input = int(input(f"Please enter the y coordinate for your move: "))
        except ValueError:
            print("Please enter an integer.")
            continue
        if player_move_x_input < 1 or player_move_y_input < 1 or player_move_x_input > length_of_grid or player_move_y_input > length_of_grid:
            print(f"One of the coordinates is out of range. The coordinate has to be between 0 and " + str(length_of_grid) + ".")
        else:
            if grid_local[player_move_x_input - 1][player_move_y_input -1 ] == ".":
                grid_local[player_move_x_input - 1][player_move_y_input - 1] = "x"
                return grid_local
            elif grid_local[player_move_x_input - 1][player_move_y_input -1 ] == "O":
                grid_local[player_move_x_input - 1][player_move_y_input - 1] = "Ø"
                print("You destroyed a ship.")
                return grid_local
            elif grid_local[player_move_x_input - 1][player_move_y_input -1 ] == "X":
                print("This space is occupied by your own boat!")
            else:
                print("Someone already played here.")

def player_move_bigger_ships(grid_local, length_of_grid):
    while True:
        try:
            player_move_x_input = int(input(f"Please enter the x coordinate for your move: "))
            player_move_y_input = int(input(f"Please enter the y coordinate for your move: "))
        except ValueError:
            print("Please enter an integer.")
            continue
        if player_move_x_input < 1 or player_move_y_input < 1 or player_move_x_input > length_of_grid or player_move_y_input > length_of_grid:
            print(f"One of the coordinates is out of range. The coordinate has to be between 0 and " + str(length_of_grid) + ".")
        else:
            if grid_local[player_move_x_input - 1][player_move_y_input -1] == ".":
                grid_local[player_move_x_input - 1][player_move_y_input - 1] = "x"
                return grid_local
            elif grid_local[player_move_x_input - 1][player_move_y_input -1][0] == "O":
                name_of_destroyed_boat = grid_local[player_move_x_input - 1][player_move_y_input -1]
                grid_local[player_move_x_input - 1][player_move_y_input - 1] = "Ø" + grid_local[player_move_x_input - 1][player_move_y_input - 1][1:]
                for row, x in enumerate(grid_local):
                    for column, y in enumerate(x):
                        if y == name_of_destroyed_boat:
                            print(f"Boat of size {str(name_of_destroyed_boat[1])} hit, but not completely destroyed.")
                        elif y != name_of_destroyed_boat:
                            print(f"You destroyed a ship of the sice {str(name_of_destroyed_boat[1])}.")
                return grid_local
            elif grid_local[player_move_x_input - 1][player_move_y_input -1][0] == "X":
                print("This space is occupied by your own boat!")
            else:
                print("Someone already played here.")
    
def computer_move_bigger_ships(grid_local, length_of_grid):
    while True:
        computer_move_x_input = randrange(0, length_of_grid)
        computer_move_y_input = randrange(0, length_of_grid)
        
        if grid_local[computer_move_x_input - 1][computer_move_y_input -1] == ".":
            grid_local[computer_move_x_input - 1][computer_move_y_input - 1] = "o"
            return grid_local
        elif grid_local[computer_move_x_input - 1][computer_move_y_input -1][0] == "X":
            name_of_destroyed_boat = grid_local[computer_move_x_input - 1][computer_move_y_input -1]
            grid_local[computer_move_x_input - 1][computer_move_y_input - 1] = "X̶" + grid_local[computer_move_x_input - 1][computer_move_y_input - 1][1:]
            for row, x in enumerate(grid_local):
                for column, y in enumerate(x):
                    if y == name_of_destroyed_boat:
                        print(f"Boat of size {str(name_of_destroyed_boat[1])} hit, but not completely destroyed.")
                        return
                    elif y != name_of_destroyed_boat:
                        print(f"You destroyed a ship of the sice {str(name_of_destroyed_boat[1])}.")
                        return
            return grid_local
        elif grid_local[computer_move_x_input - 1][computer_move_y_input -1][0] == "O":
            print("This space is occupied by your own boat!")
        else:
            print("Someone already played here.")

def computer_move_one_size_ships(grid_local, length_of_grid):
    while True:
        computer_ship_x_random = randrange(0,length_of_grid)
        computer_ship_y_random = randrange(0,length_of_grid)
        #print("(" + str(computer_ship_x_random) + "/" + str(computer_ship_y_random) + ")")
        if grid_local[computer_ship_x_random][computer_ship_y_random] == ".":
            grid_local[computer_ship_x_random][computer_ship_y_random] = "o"
            return grid_local
        elif grid_local[computer_ship_x_random][computer_ship_y_random] == "X":
            grid_local[computer_ship_x_random][computer_ship_y_random] = "X̶"
            print("Computer destroyed one of your ships.")
            return grid_local
        elif grid_local[computer_ship_x_random][computer_ship_y_random] == "O":
            print("Sorry Computer. This space is occupied by your own boat!")
        else:
            print("Someone already played here.")

def evaluate_X_bigger_ships(grid_local):
    for row, x in enumerate(grid_local):
        for column, y in enumerate(x):
            if y[0] == "X":
                print("Game continues.")
                return True, None
    return False, "X̶"

def evaluate_O_bigger_ships(grid_local):
    for row, x in enumerate(grid_local):
        for column, y in enumerate(x):
            if "0" in y:
                print(f"Game continues. Found 'O' in cell [{row+1}][{column+1}].")
                return True, None
    return False, "Ø"

def evaluate_X_one_size_ships(grid_local):
    for row, x in enumerate(grid_local):
        for column, y in enumerate(x):
            if y == "X":
                return True, None
    return False, "X̶"

def evaluate_O_one_size_ships(grid_local):
    for row, x in enumerate(grid_local):
        for column, y in enumerate(x):
            if y == "O":
                return True, None
    return False, "Ø"

def preparation_one_size_ships(): 
    grid, length_of_grid = creating_grid()
    printing_grid(grid)

    number_ships = defining_number_ships_one_size_ships(grid)
    position_player_ships, grid_with_player_ships = player_ship_placing_one_size_ships(grid, number_ships, length_of_grid)
    #print(position_player_ships)
    #printing_grid(grid_with_player_ships)
    position_computer_ships, grid_with_all_ships = computer_ship_placing_one_size_ships(grid_with_player_ships, number_ships, length_of_grid)
    printing_grid(grid_with_all_ships)
    return grid_with_all_ships, length_of_grid

def game_one_size_ships(grid_with_all_ships, length_of_grid):
    game_continues = True

    while game_continues:
        grid_with_all_ships = player_move_one_size_ships(grid_with_all_ships, length_of_grid)
        game_continues, loser_sign = evaluate_O_one_size_ships(grid_with_all_ships)
        if not game_continues:
            break
        grid_with_all_ships = computer_move_one_size_ships(grid_with_all_ships, length_of_grid)
        game_continues, loser_sign = evaluate_X_one_size_ships(grid_with_all_ships)

    if loser_sign == "Ø":
        print("Player won.")
    elif loser_sign == "X̶":
        print("Computer won.")


#grid_with_all_ships_global, length_of_grid_global = preparation_one_size_ships()
#game_one_size_ships(grid_with_all_ships_global, length_of_grid_global)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def preparation_bigger_ships():
    grid, length_of_grid = creating_grid()
    fleet_size = defining_size_number_ships_bigger_ships(alphabet, length_of_grid)
    print("Fleet size is:" + str(fleet_size))
    player_ship_placing_bigger_ships(fleet_size, grid, length_of_grid)
    computer_ship_placing_bigger_ships(fleet_size, grid, length_of_grid)
    return grid, length_of_grid

def game_bigger_ships(grid, length_of_grid):
    game_continues = True

    while game_continues:
        grid = player_move_bigger_ships(grid, length_of_grid)
       # printing_grid(alphabet, grid_with_all_ships)
        testing_printing_grid(grid)
        game_continues, loser_sign = evaluate_O_bigger_ships(grid)
        if not game_continues:
            break
        grid = computer_move_bigger_ships(grid, length_of_grid)
        testing_printing_grid(grid)
        game_continues, loser_sign = evaluate_X_bigger_ships(grid)
    
    if loser_sign == "Ø":
        print("Player won.")
    elif loser_sign == "X̶":
        print("Computer won.")

grid, length_of_grid = preparation_bigger_ships()

game_bigger_ships(grid, length_of_grid)




