# 8_puzzle_bfs
Breadth first search for 8-puzzle problem to reach goal state


To run the visualization, clone the directory and run the following command in MATLAB shell
```
plotOutput_text('NodePath.txt')
```

This will output the given below visualization:

<p align="center">
  <img width="400" height="400" src="https://github.com/rishchou/8_puzzle_bfs/blob/master/gui.gif">
</p>

The three output files have been added to the folder. To run the code, follow the given command:

```
python3 project1.py
```

This will ask you to input the intial state, input the state in the given format - 3 elements in each row with space between each element


This will output the number of nodes traversed and the nodepath on the console, if a solution is found. If a solution is not found, the program will exit in approx 2 minutes.



Dependencies:

Install python3, numpy and collections(for queue) library as dependencies. 



The output files have been generated for the given sample intial node:

[1 8 2]
[0 4 3]
[7 6 5]

