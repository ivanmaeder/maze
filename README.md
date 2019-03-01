## Approach

My experience with Python is limited to writing a small number of scripts which are all on GitHub ([1](https://github.com/ivanmaeder/vimv), [2](https://github.com/ivanmaeder/NLP), [3](https://github.com/ivanmaeder/little-z)). So please excuse any language blunders.

I have implemented the A* algorithm in the past so I'm going to try dead-end filling, without using a graph. It looks interesting.

Also, I recently implemented a variation of Dijkstra's algorithm using a graph [here](https://github.com/ivanmaeder/little-z/blob/master/teleport/)), so I wanted to try something different (this other problem searches for a path within 3D space, and instead of finding the shortest path it finds a path in which the largest distance between any two adjacent nodes is lowest—e.g., the path with the edge weights `[5, 5, 5]` is preferrable to `[1, 1, 6]` because the weighiest edge in the first path, `5`, is smaller than the weightiest edge in the second path, `6`).

My assumptions for the maze problem are:

- The algorithm has knowledge of whole the maze (not a limited view from inside the maze)
- There is only one exit
- Movement is up, down, left or right
- A wall surrounds the maze (there will never be a path on the edge of the maze except the exit square)
- All paths are connected

I'm using:

- Python 3.7.2
- pytest 4.3.0

## Further Questions

- Shortest path in a maze with multiple solutions: breadth-first traversal
- All paths: depth-first traversal plus a list to keep track of all the paths as they're found
- Any path as fast as possible: I'd say breadth-first traversal, possibly Dijkstra's algorithm but I'm not sure of the benefit with equal weights on the edges. Or possibly something a little more innovative like running bread-first from each end (start and finish) at the same time, and waiting for the paths to meet at some point ideally quite quickly (?)
- For a 3D maze the additional complexity is in either working directly with the different geometry (detecting connected cubes, dead ends, etc), or working with the different geometry to convert the structure to a node graph first, and then treating the node graph just like any other node graph