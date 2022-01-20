#!/usr/bin/env python
Result:
         
. . O O . O O . . 
. O O O O O O O . 
. O O O O O O O . 
. . O O O O O . . 
. . . O O O . . . 
. . . . O . . . . 

# Method 1: Using Zip
grid = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']] 
    
for i in zip(*grid):
 print(*i)
  
# Method 2: Using Loops

for i in range(6):
    for j in range(9):
        print(grid[j][i], end = " ")
    print()

