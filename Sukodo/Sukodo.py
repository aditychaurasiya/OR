import gurobipy as gp
from gurobipy import GRB

# Define the Sudoku puzzle (0 represents empty cells)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

#create model
model = gp.Model("Sukodo")

#DV
x = model.addVars(9,9,9,vtype=GRB.BINARY,name = "x")

# objective function ----> find the feasible solution

#Constraint

# each cell has exactly one number
for i in range(9):
    for j in range(9):
        model.addConstr(gp.quicksum(x[i, j, k] for k in range(9)) == 1)
# each number appears exactly once in each row
for i in range(9):
    for k in range(9):
        model.addConstr(gp.quicksum(x[i, j, k] for j in range(9)) == 1)
# each number appears exactly once in each column
for j in range(9):
    for k in range(9):
        model.addConstr(gp.quicksum(x[i, j, k] for i in range(9)) == 1)
# each number appears exactly once in each 3*3 block
for k in range(9):
    for i in range(9):
        # Each number appears once per row
        model.addConstr(gp.quicksum(x[i, j, k] for j in range(9)) == 1)

    for j in range(9):
        # Each number appears once per column
        model.addConstr(gp.quicksum(x[i, j, k] for i in range(9)) == 1)

    for box_i in range(3):
        for box_j in range(3):
            # Each number appears once per 3x3 box
            model.addConstr(gp.quicksum(
                x[i, j, k]
                for i in range(box_i * 3, (box_i + 1) * 3)
                for j in range(box_j * 3, (box_j + 1) * 3)
            ) == 1)

# Apply pre-filled cells constraints
for i in range(9):
    for j in range(9):
        if puzzle[i][j] != 0:
            k = puzzle[i][j] - 1  # Adjust for 0-indexing
            model.addConstr(x[i, j, k] == 1)

# optimize
model.optimize()

# print the solution
if model.status == GRB.OPTIMAL:
    solution = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if x[i, j, k].x > 0.5:  # Check if the variable is set to 1
                    solution[i][j] = k + 1  # Convert back to 1-indexing

    print("Solved Sudoku:")
    for row in solution:
        print(row)
else:
    print("No solution found.")


