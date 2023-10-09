

Board = [
    [0, 0, 1, 7, 6, 0, 9, 0, 0],
    [8, 2, 0, 0, 0, 0, 0, 0, 3],
    [0, 4, 9, 0, 0, 1, 0, 0, 0],
    [2, 0, 0, 9, 3, 0, 7, 0, 0],
    [0, 0, 6, 0, 1, 7, 0, 3, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 8],
    [0, 0, 0, 6, 0, 0, 0, 0 ,0],
    [0, 7, 0, 0, 0, 0, 5, 0, 1]
]

def Board_vis(bo):
    #Print board with lines seperating each sudoku box

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print(" - - - - - - - - - - - - -")
    
        for j in range(len(bo)):
            if j % 3 == 0:
                print(' | ', end="")
        
            if j == 8:
                print(str(bo[i][j]) + " |")
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0 or bo[i][j] == None:
                return (i,j) #row, col
    
    return None

def isvalid(bo, num, pos):
    # check row
        for j in range(len(bo[0])):
            if bo[pos[0]][j] == num and pos[1] != j:
                return False
    # check col
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

    # check box
        
        """
        Divide the grid into 9 box indicated as (box_x,box_y)
        so the first box is (0,0) 
        the last box in the first row of boxs is (0,2)
        and the last box is (2,2)
        """
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3,(box_y+1) * 3):
            for j in range(box_x * 3,(box_x+1) * 3):
                if (i,j) != pos and bo[i][j] == num:
                    return False
                
        return True

def backtracking(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, len(bo[0])+1):
        if isvalid(bo, i, (row, col)):
            bo[row][col] = i    

            if backtracking(bo):
                return True
            
            bo[row][col] = 0
    
    return False


Board_vis(Board)
backtracking(Board)
print("Solution:")
Board_vis(Board)