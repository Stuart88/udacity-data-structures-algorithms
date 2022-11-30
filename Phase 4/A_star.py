import networkx as nx
import pickle
import math
from typing import List, Dict


"""

RUN THIS ONE TO VIEW THE RESULT

"""

class Map:
	def __init__(self, G: nx.classes.graph.Graph):
		if G is not None:
			self._graph: nx.classes.graph.Graph = G
			self.intersections: Dict[int, List[int]] = nx.get_node_attributes(G, "pos")
			# self.roads is a list[list[int]] !
			self.roads: list[list[int]] = [list(G[node]) for node in G.nodes()]
		else:
			self.intersections:Dict[int, List[int]] = {}
			self.roads: list[list[int]] = []

	def save(self, filename):
		with open(filename, 'wb') as f:
			pickle.dump(self._graph, f)

def load_map(name):
	with open(name, 'rb') as f:
		G = pickle.load(f)
	return Map(G)

### Important stuff below...


map_test = Map(None)
map_test.intersections = {0: [0.7801603911549438, 0.49474860768712914],
 1: [0.5249831588690298, 0.14953665513987202],
 2: [0.8085335344099086, 0.7696330846542071],
 3: [0.2599134798656856, 0.14485659826020547],
 4: [0.7353838928272886, 0.8089961609345658],
 5: [0.09088671576431506, 0.7222846879290787],
 6: [0.313999018186756, 0.01876171413125327],
 7: [0.6824813442515916, 0.8016111783687677],
 8: [0.20128789391122526, 0.43196344222361227],
 9: [0.8551947714242674, 0.9011339078096633],
 10: [0.7581736589784409, 0.24026772497187532],
 11: [0.25311953895059136, 0.10321622277398101],
 12: [0.4813859169876731, 0.5006237737207431],
 13: [0.9112422509614865, 0.1839028760606296],
 14: [0.04580558670435442, 0.5886703168399895],
 15: [0.4582523173083307, 0.1735506267461867],
 16: [0.12939557977525573, 0.690016328140396],
 17: [0.607698913404794, 0.362322730884702],
 18: [0.719569201584275, 0.13985272363426526],
 19: [0.8860336256842246, 0.891868301175821],
 20: [0.4238357358399233, 0.026771817842421997],
 21: [0.8252497121120052, 0.9532681441921305],
 22: [0.47415009287034726, 0.7353428557575755],
 23: [0.26253385360950576, 0.9768234503830939],
 24: [0.9363713903322148, 0.13022993020357043],
 25: [0.6243437191127235, 0.21665962402659544],
 26: [0.5572917679006295, 0.2083567880838434],
 27: [0.7482655725962591, 0.12631654071213483],
 28: [0.6435799740880603, 0.5488515965193208],
 29: [0.34509802713919313, 0.8800306496459869],
 30: [0.021423673670808885, 0.4666482714834408],
 31: [0.640952694324525, 0.3232711412508066],
 32: [0.17440205342790494, 0.9528527425842739],
 33: [0.1332965908314021, 0.3996510641743197],
 34: [0.583993110207876, 0.42704536740474663],
 35: [0.3073865727705063, 0.09186645974288632],
 36: [0.740625863119245, 0.68128520136847],
 37: [0.3345284735051981, 0.6569436279895382],
 38: [0.17972981733780147, 0.999395685828547],
 39: [0.6315322816286787, 0.7311657634689946]}
map_test.roads = [[36, 34, 31, 28, 17],
 [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
 [39, 36, 21, 19, 9, 7, 4],
 [35, 20, 15, 11, 6],
 [39, 36, 21, 19, 9, 7, 2],
 [32, 16, 14],
 [35, 20, 15, 11, 1, 3],
 [39, 36, 22, 21, 19, 9, 2, 4],
 [33, 30, 14],
 [36, 21, 19, 2, 4, 7],
 [31, 27, 26, 25, 24, 18, 17, 13],
 [35, 20, 15, 3, 6],
 [37, 34, 31, 28, 22, 17],
 [27, 24, 18, 10],
 [33, 30, 16, 5, 8],
 [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
 [37, 30, 5, 14],
 [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
 [31, 27, 26, 25, 24, 1, 10, 13, 17],
 [21, 2, 4, 7, 9],
 [35, 26, 1, 3, 6, 11, 15],
 [2, 4, 7, 9, 19],
 [39, 37, 29, 7, 12],
 [38, 32, 29],
 [27, 10, 13, 18],
 [34, 31, 27, 26, 1, 10, 15, 17, 18],
 [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
 [31, 1, 10, 13, 18, 24, 25, 26],
 [39, 36, 34, 31, 0, 12, 17],
 [38, 37, 32, 22, 23],
 [33, 8, 14, 16],
 [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
 [38, 5, 23, 29],
 [8, 14, 30],
 [0, 12, 17, 25, 26, 28, 31],
 [1, 3, 6, 11, 15, 20],
 [39, 0, 2, 4, 7, 9, 28],
 [12, 16, 22, 29],
 [23, 29, 32],
 [2, 4, 7, 22, 28, 36]]


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
		
		Diagonal distance:
			Best used on a grid where movements are limited to 8 directions
			up / down / left / right / up-left / up-right / down-left / down-right
		
		Euclidean distance:
			The straight line distance between two points
			Best applied where any direction can be followed
			For the case of this assignment, the Euclidian distance has been chosen as a heuristic,
			because the path between points can take any direction


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

result = shortest_path(map_test, 8, 24)
expected = [8, 14, 16, 37, 12, 17, 10, 24]
print('DONE')
print('result: ' + str(result))
print('expected: ' + str(expected))
if result == expected:
	print('YAY')
else:
	print('NO')
