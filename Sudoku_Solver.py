import tkinter as tk
import numpy as np
import time
from tkinter import messagebox


def vertical(grid, col, val):
    # Inputs: the Sudoku, the column to check and the value to check for
    # Outputs: True if the value exists in the column, False if the value does not
    for i in range(0, 9):
        if grid[i][col] == val:
            return True
    return False

def horizontal(grid, row, val):
    # Inputs: the Sudoku, the row to check and the value to check for
    # Outputs: True if the value exists in the row, False if the value does not
    for i in range(0, 9):
        if grid[row][i] == val:
            return True
    return False

def group(grid, row, col, val):
    # Inputs: the Sudoku, the square to check and the value to check for
    # Outputs: True if the value exists in the square, False if the value does not
    row_box = row//3
    col_box = col//3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[3*row_box + i][3*col_box + j] == val:
                return True
    return False

def solve_sudoku(grid):
    grid = np.array(grid)
    val_added = True
    while val_added:
        val_added = False
        for row in range(0, 9):
            for col in range(0, 9):
                if grid[row][col] == 0:
                    count = 0
                    val = 0
                    for i in range(1, 10):
                        if horizontal(grid, row, i) == False and vertical(grid, col, i) == False and group(grid, row, col, i) == False:
                            count += 1
                            val = i
                    if count == 1:
                        grid[row][col] = val
                        val_added = True
    return grid
    
        

# Function to get values from the GUI and solve the Sudoku
def solve_puzzle():
    try:
        # Collect input from the GUI into a 9x9 grid
        grid = []
        for row in range(9):
            current_row = []
            for col in range(9):
                value = entries[row][col].get()
                if value == "":
                    current_row.append(0)  # Treat empty cells as 0
                else:
                    current_row.append(int(value))
            grid.append(current_row)
        
        # Call your solving function here
        solution = solve_sudoku(grid)
        zeros_in = np.any(solution == 0)
        solution = solution.tolist()
        if not zeros_in:
            # Display the solution in the GUI
            for row in range(9):
                for col in range(9):
                    entries[row][col].delete(0, tk.END)
                    entries[row][col].insert(0, solution[row][col])
        else:
            messagebox.showerror("Error", "No solution found!")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

#Create the main window
root = tk.Tk()
root.title("Sudoku Solver")

# Create a 9x9 grid of entry boxes
entries = []
for row in range(9):
    current_row = []
    for col in range(9):
        entry = tk.Entry(root, width=2, font=("Arial", 18), justify='center')
        entry.grid(row=row, column=col, padx=5, pady=5)
        current_row.append(entry)
    entries.append(current_row)

# Add a button to solve the Sudoku
solve_button = tk.Button(root, text="Solve", command=solve_puzzle, font=("Arial", 18))
solve_button.grid(row=9, column=0, columnspan=9)

# Start the GUI loop
root.mainloop()

grid = np.array([[8, 0, 0, 0, 0, 5, 0, 0, 0],
                 [0, 7, 0, 9, 0, 0, 0, 4, 0],
                 [0, 0, 9, 0, 7, 8, 3, 2, 5], 
                 [3, 0, 1, 0, 9, 0, 0, 5, 0],
                 [0, 0, 6, 0, 0, 0, 1, 0, 0],
                 [0, 9, 0, 0, 3, 0, 6, 0, 2],
                 [2, 8, 3, 6, 5, 0, 7, 0, 0],
                 [0, 1, 0, 0, 0, 2, 0, 8, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 9]])
