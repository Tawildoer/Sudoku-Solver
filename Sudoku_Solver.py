import tkinter as tk
import numpy as np
from tkinter import messagebox

def vertical(grid, col, val):
    for i in range(0, 8):
        if grid[i, col] == val:
            return True
    return False

def horizontal(grid, row, val):
    for i in range(0, 8):
        if grid[row, i] == val:
            return True
    return False

def group(grid, row, col, val):
    row_box = row % 3
    col_box = col % 3
    for i in range(0, 2):
        for j in range(0, 2):
            if grid[3*row_box + i, 3*col_box + j] == val:
                return True
    return False

def solve_sudoku(grid):
    grid = np.array(grid)
    for row in range(0, 8):
        for col in range(0, 8):
            if grid[row, col] == 0:
                count = 0
                val = 0
                for i in range(0, 8):
                    if horizontal(grid, row, i) == False and vertical(grid, col, i) == False and group(grid, row, col, i) == False:
                        count += 1
                        val = i
                if count == 1:
                    grid[row, col] = val
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

        if solution:
            # Display the solution in the GUI
            for row in range(9):
                for col in range(9):
                    entries[row][col].delete(0, tk.END)
                    entries[row][col].insert(0, solution[row][col])
        else:
            messagebox.showerror("Error", "No solution found!")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
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