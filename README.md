# PancakeSortingWorstStackNeuralNet 
# Introduction 
For background on the pancake sorting problem, check out the wikipedia page: https://en.wikipedia.org/wiki/Pancake_sorting
The goal of this repo is to help visualize the pancake graph. It is not easy to find pancake graphs for n>4 online. This is likely because the graph, with n! vertices, becomes messy and confusing with larger n.
We use the recursive property of the pancake graph to accomplish this. We also do not display all edges, instead once a vertex is selected, the path from that vertex to the sorted stack is displayed.

# How to Run 
The main function can be run with 
```
python -m main
```
with optional parameters:

"-n", "--n" -  length of pancake stacks (default = 5)  
Once run, click the IP displayed and open in your browser. The graph will be displayed (edges will not be displayed as this would be far too messy).

# Images
The pancake graphs for n = 5 to 7 are generated. The n>7 graphs can be generated but run slowly and are not useful.
The vertices are color coded by distance from the sorted stack, with the sorted stack being green and a gradient from green to blue, with the darkest blue indicating largest distance from the sorted stack. We highlight the vertices with largest distance for a particular n red.
n=5:
![image](https://github.com/user-attachments/assets/665f27c9-bdd2-4555-ac44-a2a2e00c49e7)
n=6:
![image](https://github.com/user-attachments/assets/f8cebce9-73d1-4f6e-ba9c-3467ea928977)
n=7:
![image](https://github.com/user-attachments/assets/5a26213d-d7b4-402d-adda-6739b121f4c8)

And an example of a path generated for one of the max distance stacks for n=6:
![image](https://github.com/user-attachments/assets/afe0d8eb-fc00-4d85-b31d-bc4075473922)

# Conclusion
The hope is that this visualizer will be useful in finding patterns in the pancake graphs that will help in solving the pancake sorting problem.

