import math
from typing import List

'''

This is an implementation of the A* algorithm for path finding, using a given map
with road and intersection information available to work with.

For efficient and minimal path finding operation, the heuristic value 'h' for each point
is calculated as the pythagorean distance between that point and the goal.

NOTE:
	Typical heuristic distances include:
		
		Manhattan distance: 
			Best used on a grid where movements are limited to 4 directions up/down/left/right directions
			The available paths are straight or 'L' shaped
			See function manhattan_distance()
		
		Diagonal distance:
			Best used on a grid where movements are limited to 8 directions
			up / down / left / right / up-left / up-right / down-left / down-right
			See function diagonal_distance()

		Euclidean distance:
			The straight line distance between two points
			Best applied where any direction can be followed
			For the case of this assignment, the Euclidian distance has been chosen as a heuristic,
			because the path between points can take any direction.
			This is the most admissible heuristic because it can never over-estimate the path cost,
			it will always calculate a value that is equal to or lower than the total actual cost.
			(The other heuristics might in some cases over-estimate, since they do not provide straight line
			estimations)
			See function euclidian_distance()

It is interesting to note that all forms of heuristic distance work successfully
for this assignment.

During path traversal, the value 'g' is the current most efficient 
distance from the start point to the point currently being looked at.

Finally, each visited point is assigned a total value 'f' (= g + h) which represents the current
best estimate for the a complete path that goes via that point.

The aim is to efficiently find the path with the best 'f' value that starts at the start node
and traverses the map to the end node, using the heuristic 'h' to guide the algorithm
in the correct direction, so as to prevent the need to manually check every point 
on the map.

Complexity:

	Complexity depends highly on the arrangement of the given map, i.e. number
	of roads and intersections and how they are laid out.

	Generally, some research tells me the following:
	
	Time: O(b^d) 
		where b is the 'branching factor' - the average number of roads from each point,
		and d is the depth of the resulting path.
	
	Space: O(d)  - The algorithm only stores useful path node data

	Worst case：
		Time: O(n^n) for map with all nodes interconnected
		Space: O(n) as all nodes will be stored in the 'visited' set of nodes


'''

class Coordinate:
	def __init__(self, x:int, y:int) -> None:
		'''
		inits a co-ordinate object representing the (x,y) position
		of a map intersection
		Complexity:
			Time: O(1)
			Space: O(1)
		'''
		self.x = x
		self.y = y

def euclidian_distance(a: Coordinate, b: Coordinate) -> float:
	'''
	Finds the pythagorean distance between two coordinates
	Complexity:
		Time: O(1)
		Space: O(1)
	'''
	x_diff = math.pow(a.x - b.x, 2)
	y_diff = math.pow(a.y - b.y, 2)
	return math.sqrt(x_diff + y_diff)

def manhattan_distance(a: Coordinate, b: Coordinate) -> float:
	'''
	Finds the manhattan distance between two coordinates
	Complexity:
		Time: O(1)
		Space: O(1)
	'''
	x_diff = abs(a.x - b.x)
	y_diff = abs(a.y - b.y)
	return x_diff + y_diff

def diagonal_distance(a: Coordinate, b: Coordinate) -> float:
	'''
	Finds the diagonal distance between two coordinates
	Complexity:
		Time: O(1)
		Space: O(1)
	'''
	x_diff = abs(a.x - b.x)
	y_diff = abs(a.y - b.y)
	if x_diff > y_diff:
		return math.sqrt(2 * y_diff ** 2) + (x_diff - y_diff)
		# path moves straight left/right first, then diagonal to end point above or below
	elif x_diff < y_diff:
		# path moves straight up/down first, then diagonal to end point to left or right
		return math.sqrt(2 * x_diff ** 2) + (y_diff - x_diff)
	else:
		# 'perfect' diagonal
		return math.sqrt(2 * x_diff ** 2) # could also use y_diff here

class PathNode:
	def __init__(self, point: int, M: any) -> None:
		'''
		inits PathNode object with information about the node index (this is the intersection 'name'),
		the node co-ordinates, and point index values (the 'names') for the roads connected to this node. 
		The g, h and f path cost values are initialised as 0. These are calculated in-situ during 
		the shortest_path process
		Complexity:
			Time: O(1)
			Space: O(av(n)) the average number of roads across all map points
		'''
		self.point = point
		self.coords = Coordinate(M.intersections[point][0], M.intersections[point][1])
		
		self.parent: PathNode = None
		self.child: PathNode = None
		self.roads: List[int] = M.roads[point]
		
		self.g = 0 # path cost from start to here, should increment based on sum of path cost of parent nodes
		self.h = 0 # estimated distance to goal. In this case use pythagorean distance between node and goal
		self.f = 0 # g+h , current estimated path cost from start to goal, via this node


	def calculate_g_h_f(self, goal_coord: Coordinate) -> None:
		'''
		Determins the values of g, h and f of this node, based on data from
		its parent node and the goal node.
		Complexity:
			Time: O(1)
			Space: O(1)
		'''
		self.g = self.parent.g + euclidian_distance(self.coords, self.parent.coords)
		self.h = euclidian_distance(self.coords, goal_coord)
		self.f = self.g + self.h
		
	def path_from_start(self) -> List[int]:
		'''
		Generates an array of ints representing the current path that this
		takes from the start point.
		The returned array of values represents the index ('name') of each node
		Complexity:
			Time: O(d) where d is the depth of the node
			Space: O(d) for each value assigned while traversing from initial node
		'''
		path: List[int] = []
		node = self
		while node != None:
			path.append(node.point)
			if node.parent != None:
				node = node.parent
			else:
				node = None
		path.reverse()
		return path

	def __eq__(self, __o: object) -> bool:
		if isinstance(__o, PathNode):
			return self.point == __o.point
		else:
			return False

	def __str__(self) -> str:
		return f'{self.point}: {self.path_from_start()}'


def get_node_with_least_f(path_nodes: List[PathNode]):
	'''
	From the given list, the node with the lowest f value is returned
	Complexity:
		Time: O(n) where n is number of nodes on map (worst case)
		Space: O(1) 
	'''
	least_f = None
	for i in range(len(path_nodes)):
		if least_f == None:
			least_f = path_nodes[i]
		if path_nodes[i].f < least_f.f:
			least_f = path_nodes[i]
	path_nodes.remove(least_f)
	return least_f


def shortest_path(m: any, start: int, goal: int) -> List[int]:
	'''
	Calculates shortest path from start point to end point, in the given map 'm'

	Complexity:

		Complexity depends highly on the arrangement of the given map, i.e. number
		of roads and intersections and how they are laid out.

		Generally, some research tells me the following:
		
		Time: O(b^d) 
			where b is the 'branching factor' - the average number of roads from each point,
			and d is the depth of the resulting path.
		
		Space: O(d)  - The algorithm only stores useful path node data

		Worst case：
			Time: O(n^n) for map with all nodes interconnected
			Space: O(n) as all nodes will be stored in the 'visited' set of nodes
	'''
	visited: List[PathNode] = []
	frontier_set: List[PathNode] = []
	start_node = PathNode(start, m)
	goal_node = PathNode(goal, m)

	frontier_set.append(start_node)
	while len(frontier_set) > 0:
		# We want node with least total cost
		current_node = get_node_with_least_f(frontier_set)

		if current_node == goal_node:
			# Finished
			return current_node.path_from_start()

		if current_node not in visited:
			visited.append(current_node)

			for r in current_node.roads:
				r_node = PathNode(r, m)
				r_node.parent = current_node
				r_node.calculate_g_h_f(goal_node.coords)
				# Add each road to frontier set 
				# then on next loop of frontier_set we will check the least cost path first
				frontier_set.append(r_node)