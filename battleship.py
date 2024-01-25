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

def printing_grid(grid_local):
    for i in grid_local:
            print(i)
    return grid_local

def defining_number_ships():
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

def player_ship_placing(grid_local, number_ships, length_of_grid):
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

def computer_ship_placing(grid_local, number_ships, length_of_grid):
    computer_ships = []
    for i in range(0, number_ships):
        while True:
            computer_ship_x_random = randrange(0,length_of_grid)
            computer_ship_y_random = randrange(0,length_of_grid)
            print("(" + str(computer_ship_x_random) + "/" + str(computer_ship_y_random) + ")")
            if grid_local[computer_ship_x_random][computer_ship_y_random] == ".":
                grid_local[computer_ship_x_random][computer_ship_y_random] = "O"
                break
        computer_ships.append([computer_ship_x_random,computer_ship_y_random])
    return computer_ships, grid_local

def player_move(grid_local, length_of_grid):
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

def computer_move(grid_local, length_of_grid):
    while True:
        computer_ship_x_random = randrange(0,length_of_grid)
        computer_ship_y_random = randrange(0,length_of_grid)
        print("(" + str(computer_ship_x_random) + "/" + str(computer_ship_y_random) + ")")
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

def evaluate_X(grid_local):
    for row, x in enumerate(grid_local):
        for column, y in enumerate(x):
            if y == "X":
                print("Game continues.")
                return True, None
    return False, "X̶"

def evaluate_O(grid_local):
    for row, x in enumerate(grid_local):
        for column, y in enumerate(x):
            if y == "O":
                return True, None
    return False, "Ø"

game_continues = True
grid, length_of_grid = creating_grid()
printing_grid(grid)
number_ships = defining_number_ships()
position_player_ships, grid_with_player_ships = player_ship_placing(grid, number_ships, length_of_grid)
print(position_player_ships)
printing_grid(grid_with_player_ships)
position_computer_ships, grid_with_all_ships = computer_ship_placing(grid_with_player_ships, number_ships, length_of_grid)
printing_grid(grid_with_all_ships)

while game_continues:
    grid_with_all_ships = player_move(grid_with_all_ships, length_of_grid)
    printing_grid(grid_with_all_ships)
    game_continues, loser = evaluate_O(grid_with_all_ships)
    if not game_continues:
        break
    grid_with_all_ships = computer_move(grid_with_all_ships, length_of_grid)
    printing_grid(grid_with_all_ships)
    game_continues, loser = evaluate_X(grid_with_all_ships)

if loser == "Ø":
    print("Player won.")
elif loser == "X̶":
    print("Computer won.")