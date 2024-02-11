grid = [['_','_','_'],['_','_','_'],['_','_','_']]

def show_grid():
    for i in range(0,3):
        print(grid[i])
    return grid

def check_winner():
    for row in grid:
        if row[0] == row[1] == row[2] != '_':
            return True
    
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] != '_':
            return True
    
    if grid[0][0] == grid[1][1] == grid[2][2] != '_':
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] != '_':
        return True
    return False

def move(Player, InPlayer):
    global grid
    if len(InPlayer) != 2:
        print("Invalid")
        return False
    row =  int(InPlayer[0]) - 1
    col = int(InPlayer[1]) - 1

    if row<0 or col<0 or row >= len(grid) or col >= len(grid[0]):
        print('Invalid')
        return False
    if grid[row][col] != '_':
        print("Oh No")
        return False
    grid[row][col] == Player
    return True

def game():
    global grid
    show_grid()
    counter = 0
    while True:
        InPlayer1 = input("Player1 Move:(row,col)")
        while not move('O',InPlayer1):
            InPlayer1 = input("Player1 Move:(row,col)")
        counter += 1
        show_grid()
        if check_winner():
            print("Player1 wins")
            return
    
        if counter == 9:
            print("It is a draw")
            return
        
        InPlayer2 = input("Player2 Move:(row,col)")
        while not move('X', InPlayer2):
            InPlayer2 = input("Player2 Move:(row,col)")
        counter += 1
        if check_winner():
            print("Player2 Wins")
            return
        show_grid()


game()





    