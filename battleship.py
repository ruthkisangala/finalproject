from random import randrange

def creating_grid(): #to create grid
    while True:
        try:
            length_of_grid = int(input("How big is the side of the grid? "))
            if length_of_grid <= 0:
                print("Grid size must be at least 1.")
            elif length_of_grid > 100:
                print("Maximal size of the grid is 100.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    grid = [["." for x in range(length_of_grid)] for y in range(length_of_grid)] #creates a list (y) with lists (x) in it
    return grid, length_of_grid

def printing_grid(grid):
    grid_for_printing = [list(row) for row in grid] #map which will be visible to the player
    #removes all the ships from the map so player can't see them
    for row, x in enumerate(grid_for_printing):
        for column, y in enumerate(x):
            if "O" in y: 
                grid_for_printing[row][column] = grid_for_printing[row][column].replace(y, ".")
    #printing grid
    print() #to print an emptry row, easier visibility afterwards
    for row in grid_for_printing:
        print(row)
    print() #to print an emptry row, easier visibility afterwards

def defining_size_number_ships(alphabet, length_of_grid):
    fleet_size = {}
    for size in range (1, length_of_grid + 1): #so ships cannot exceed size of grid
        while True:
            try: 
                ship_amount = int(input("How many ships with size " + str(size) + " do you want? "))
                if ship_amount > 5: 
                    print("Too many ships, limit is 5.")
                elif ship_amount > 0:
                    for ship in range(0, ship_amount):
                        fleet_size[str(size) + str(alphabet[ship])] = int(size) #creates dictionary of ships with their name as a string (eg. 3a) and their size as an integer (in given example = 3) 
                    break
                elif ship_amount == 0: #if no ships of a certain size needed
                    break
            except ValueError:
                "Invalid answer. Please write a number."
    return fleet_size

def player_ship_placing(fleet_size_local, grid, length_of_grid):
    for ship_name, ship_size in fleet_size_local.items():
        while True: #to determine whether ship should be placed vertically or horizontally
            try:
                orientation = input("\nDo you want to place the ship with size " + str(ship_name) + " vertically (v) or horizontally (h)? ")
                if orientation.lower() not in ["v", "h"]:
                    print("Invalid answer. Please choose \"v\" or \"h\".")
            except ValueError:
                print("No string. Please choose \"v\" or \"h\".")
            #to get x and y coordinates
            try:
                x_coordinate_ship = int(input("In which column (x) should the ship with size " + str(ship_name) + " start? "))
                y_coordinate_ship = int(input("In which row (y) should the ship with size " + str(ship_name) + " start? "))
            except ValueError:
                print("Invalid input")
                continue 
            
            #checks if coordinates lie on grid
            if x_coordinate_ship < 1 or x_coordinate_ship > length_of_grid or y_coordinate_ship < 1 or y_coordinate_ship > length_of_grid: 
                print("Coordinate has to be between 1 and " + str(length_of_grid) + ".")
            #checks if ship can fit on grid with given coordinates
            elif (x_coordinate_ship -1 + int(ship_size)) > length_of_grid and orientation == "h":
                print("Ship cannot fit on grit. Choose another starting point.")
            elif (y_coordinate_ship -1 + int(ship_size)) > length_of_grid and orientation == "v":
                print("Ship cannot fit on grit. Choose another starting point.")
            else:
                valid_placement = True
                # checks if space is still empty, for vertical placement
                if orientation == "v":
                    for i in range(ship_size):
                        if grid[y_coordinate_ship - 1 + i][x_coordinate_ship - 1] != ".":
                            print("One of the spaces is already taken. Choose another starting point.")
                            valid_placement = False
                            break
                    # places ship if coordinates are still empty
                    if valid_placement: 
                        for i in range(ship_size):
                            grid[y_coordinate_ship - 1 + i][x_coordinate_ship - 1] = "X" + str(ship_name)
                        printing_grid(grid)
                        break
                # checks if space is still empty, for horizontal placement
                elif orientation == "h":
                    for i in range(ship_size):
                        if grid[y_coordinate_ship - 1][x_coordinate_ship - 1 + i] != ".":
                            print("One of the spaces is already taken. Choose another starting point.")
                            valid_placement = False
                            break
                    # places ship if coordinates are still empty
                    if valid_placement:
                        for i in range(ship_size):
                            grid[y_coordinate_ship - 1][x_coordinate_ship - 1 + i] = "X" + str(ship_name)
                        break

    return grid

def computer_ship_placing(fleet_size_local, grid, length_of_grid):
    for ship_name, ship_size in fleet_size_local.items():
        while True:
            #to determine whether ship should be placed vertically or horizontally
            orientation_random_number = randrange(0, 2) 
            if orientation_random_number == 0:
                orientation = "v"
            elif orientation_random_number == 1:
                orientation = "h"

            #to get x and y coordinates
            x_coordinate_ship = randrange(0, length_of_grid)
            y_coordinate_ship = randrange(0, length_of_grid)

            #checks if ship can fit on grid with given coordinates
            if (x_coordinate_ship + int(ship_size)) > length_of_grid and orientation == "h":
                continue
            elif (y_coordinate_ship + int(ship_size)) > length_of_grid and orientation == "v":
                continue
            else:
                valid_placement = True

                # checks if space is still empty, for vertical placement
                if orientation == "v":
                    for i in range(ship_size):
                        if grid[y_coordinate_ship + i][x_coordinate_ship] != ".":
                            valid_placement = False
                            break
                    # places ship if coordinates are still empty
                    if valid_placement:
                        for i in range(ship_size):
                            grid[y_coordinate_ship + i][x_coordinate_ship] = "O" + str(ship_name)
                        break
                # checks if space is still empty, for horizontal placement
                elif orientation == "h":
                    for i in range(ship_size):
                        if grid[y_coordinate_ship][x_coordinate_ship + i] != ".":
                            valid_placement = False
                            break
                    # places ship if coordinates are still empty
                    if valid_placement:
                        for i in range(ship_size):
                            grid[y_coordinate_ship][x_coordinate_ship + i] = "O" + str(ship_name)
                        break
    return grid

def player_move(grid, length_of_grid):
    while True:
        #to get coordinates for move
        try:
            player_move_x = int(input(f"Please enter the x coordinate for your move: "))
            player_move_y = int(input(f"Please enter the y coordinate for your move: "))
        except ValueError:
            print("Please enter an integer.")
            continue
        
        #checking if coordinates don't lie on the grid
        if player_move_x < 1 or player_move_y < 1 or player_move_x > length_of_grid or player_move_y > length_of_grid:
            print(f"One of the coordinates is out of range. The coordinate has to be between 0 and {length_of_grid}.")
        
        else:
            # checking status of coordinate
            if grid[player_move_y -1][player_move_x - 1] == ".": #empty space
                grid[player_move_y - 1][player_move_x - 1] = "x"
                return grid
            elif grid[player_move_y -1][player_move_x - 1][0] == "O": #ship of computer
                name_of_hit_ship = grid[player_move_y -1][player_move_x - 1] 
                grid[player_move_y - 1][player_move_x - 1] = "Ø" + grid[player_move_y - 1][player_move_x - 1][1:]
                #to determine if ship was destroyed or only hit
                found_ship_parts = False
                for row, x in enumerate(grid):
                    for column, y in enumerate(x):
                        if y == name_of_hit_ship:
                            found_ship_parts = True
                            print(f"You hit a ship of size {str(name_of_hit_ship[1])}, bud you didn't completely destroy it.")
                            return grid
                        elif y != name_of_hit_ship:
                            found_ship_parts = False #no found ship parts until some are found
                if not found_ship_parts: #searched the whole grid, but no ship parts found
                    print(f"You destroyed a ship of size {str(name_of_hit_ship[1])}.")
                    return grid
            elif grid[player_move_y -1][player_move_x - 1][0] == "X": #own ship
                print("This space is occupied by your own ship!")
                continue
            else: #already occupied space
                print("Someone already played here.")
                continue

def computer_move(grid, length_of_grid, damaged_ship):
    valid_move = False

    if damaged_ship: #computer tries to move close to a damaged ship to destroy it completely
        while not valid_move:
            for i in range(1, length_of_grid):
                for move in [(i,0), (-i,0), (0,i),(0,-i)]:
                    possible_computer_move_x = damaged_ship[0] -1 + move[0]
                    possible_computer_move_y = damaged_ship[1] -1 + move[1]
                    valid_move = computer_checking_move(grid, possible_computer_move_x, possible_computer_move_y)
                    if valid_move:
                        break
                if valid_move:
                    break

    # gets coordinates if no damaged ship
    while not valid_move:
        possible_computer_move_x = randrange(0, length_of_grid)
        possible_computer_move_y = randrange(0, length_of_grid)
        valid_move = computer_checking_move(grid, possible_computer_move_x, possible_computer_move_y)

    # computer moves
    computer_move_x = possible_computer_move_x
    computer_move_y = possible_computer_move_y
    if grid[computer_move_y][computer_move_x] == ".": #empty space
        grid[computer_move_y][computer_move_x] = "o"
        return grid, damaged_ship
    elif grid[computer_move_y][computer_move_x][0] == "X": #ship of player
        name_of_hit_ship = grid[computer_move_y][computer_move_x]
        grid[computer_move_y][computer_move_x] = "*" + grid[computer_move_y][computer_move_x][1:]
        #to determine if ship was destroyed or only hit
        found_ship_parts = False
        for row, x in enumerate(grid):
            for column, y in enumerate(x):
                if y == name_of_hit_ship:
                    found_ship_parts = True
                    print(f"Computer hit a ship of size {str(name_of_hit_ship[1])}, but didn't completely destroy it.")
                    damaged_ship = (computer_move_x + 1, computer_move_y + 1) #saves the coordinates of the damaged ship so the computer can try to move close to it in the next round
                    return grid, damaged_ship
                elif y != name_of_hit_ship:
                    found_ship_parts = False #no found ship parts until some are found
        if not found_ship_parts: #searched the whole grid, but no ship parts found
                damaged_ship = None
                print(f"Computer destroyed a ship of size {str(name_of_hit_ship[1])}.")
                return grid, damaged_ship
            
def computer_checking_move(grid, possible_computer_move_x, possible_computer_move_y):
    if not (0 <= possible_computer_move_x < length_of_grid and 0 <= possible_computer_move_y < length_of_grid):
        valid_move = False
        return valid_move
    if grid[possible_computer_move_y][possible_computer_move_x] in [".", "X"]:
        valid_move = True
    else:
        valid_move = False
    return valid_move

def evaluate_all_ships_destroyed(grid, not_destroyed_ship_sign, destroyed_ship_sign):
    for row, x in enumerate(grid):
        for column, y in enumerate(x):
            if not_destroyed_ship_sign in y:
                return True, None
    return False, destroyed_ship_sign

def preparation():
    #creating grid
    grid, length_of_grid = creating_grid() 
    # determining how many ships in which sizes
    fleet_size = defining_size_number_ships(alphabet, length_of_grid)
    # player places ships
    player_ship_placing(fleet_size, grid, length_of_grid)
    printing_grid(grid)
    #computer places ships
    computer_ship_placing(fleet_size, grid, length_of_grid)
    return grid, length_of_grid

def game(grid, length_of_grid, damaged_ship):
    game_continues = True
    while game_continues:
        #player plays
        print("Your turn.")
        grid = player_move(grid, length_of_grid)
        printing_grid(grid)
        #evaluates if player won
        game_continues, loser_sign = evaluate_all_ships_destroyed(grid, "O", "Ø")
        if not game_continues: #exits loop if player won
            break
        #computer plays
        print("Computer's turn.")
        grid, damaged_ship = computer_move(grid, length_of_grid, damaged_ship)
        printing_grid(grid)
        #evaluates if computer won
        game_continues, loser_sign = evaluate_all_ships_destroyed(grid, "X", "*")
        
    # determines who won
    if loser_sign == "Ø":
        print("Player won.")
    elif loser_sign == "*":
        print("Computer won.")


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
damaged_ship = ()

grid, length_of_grid = preparation()
game(grid, length_of_grid, damaged_ship)


