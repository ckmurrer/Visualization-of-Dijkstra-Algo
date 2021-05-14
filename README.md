# Visualization-of-Dijkstra-Algo

This program will implement a visualization of Dijkstra's Shortest Path Algorithm using Python3 and the Pygame module for the graphical interface.

*******************************************************

# Development Log #

05/09/2021 - Day One of Developing

This is my first time seriously using the Python language so the syntax is new to me but easy to understand. I had to research the Pygame module for the documentation on how to handle creating and populating a window. I had implemented the window screen that will be used for the visualization of the algorithm and populated it with a 31x31 grid using a 2D array on. This will be used in the future to allow the placements of nodes and barriers blocking the path of the algorithm to show how it is able to move around objects until it meets its desired node endpoint.

05/14/2021 - Day Two of Developing

The implementaion of being able to click on the screen twice to be able to place two different nodes to signify the start and end points of the algorithms pathfinding to and from the two points has been completed. I am currently working on the logic behind being able to click and drag barriers onto the screen to block the path of the algorithm so it will have to pathfind around it to find the node it is trying to reach. Once the barrier implementation has been completed I will transfer the array into an adjacency matrix with appropriate weights to begin implementation of Dijkstras Algorithm.