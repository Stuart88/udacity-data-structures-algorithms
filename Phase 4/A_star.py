import networkx as nx
import pickle


class Map:
	def __init__(self, G: nx.classes.graph.Graph):
		if G is not None:
			self._graph: nx.classes.graph.Graph = G
			self.intersections: Dict[int, list[int]] = nx.get_node_attributes(G, "pos")
			# self.roads is a list[list[int]] !
			self.roads: list[list[int]] = [list(G[node]) for node in G.nodes()]
		else:
			self.intersections:Dict[int, list[int]] = {}
			self.roads: list[list[int]] = []

	def save(self, filename):
		with open(filename, 'wb') as f:
			pickle.dump(self._graph, f)

def load_map(name):
	with open(name, 'rb') as f:
		G = pickle.load(f)
	return Map(G)

### Important stuff below...

import sys
import math
from typing import List, Dict

class PathNode:
	def __init__(self, point: int, M: Map) -> None:
		self.point = point
		self.coords = Coordinate(M.intersections[point][0], M.intersections[point][1])
		
		self.parent: PathNode = None
		self.child: PathNode = None
		self.roads = M.roads[point]

		self.dist_from_start = 0
		
		
		self.g = 0 # path cost
		self.h = 0 # estimated distance to goal. In this case use pythagorean distance between node and goal
		self.f = 0 # g+h
		# aim is to find optimal f 
		
	def __eq__(self, __o: object) -> bool:
		if isinstance(__o, PathNode):
			return self.point == __o.point
		else:
			return False

	def __str__(self) -> str:
		return str(self.point)

	def __repr__(self) -> str:
		return str(self.point)


class Coordinate:
	def __init__(self, x:int, y:int) -> None:
		self.x = x
		self.y = y

def pythag_distance(a: Coordinate, b: Coordinate):
	'''
	Finds the pythagorean distance between two coordinates
	Complexity:
		Time: O(1)
		Space: O(1)
	'''
	x_diff = math.pow(a.x - b.x, 2)
	y_diff = math.pow(a.y - b.y, 2)
	return math.sqrt(x_diff + y_diff)

def create_heuristic_point_name(a_name: int, b_name: int):
	'''
	Creates a name for a heuristic measurement item representing
	distance between points with unique numeric names
	
	For example: 
		point 1 with point 7 will be named "1:7"
		point 7 with point 1 will be named "1:7" also.

	Complexity:
		Time: O(1)
		Space: O(1)
	'''
	if a_name < b_name:
		return f'{a_name}:{b_name}'
	else:
		return f'{b_name}:{a_name}'



def calculate_euclidian_distances(intersections: Dict[int, List[int]]):
	"""
	Creates a dictionary of pythagorean distances between each point
	in the map

	Complexity:
		Time: O(n^2)
		Space: O(nlogn) because reverse versions of the same distance are bypassed
	"""
	result: Dict[str, int] = {} 
	for i in intersections:
		for j in intersections:
			
			point_name = create_heuristic_point_name(i, j) 
			
			if point_name in result:
				# Will hit this if it's an existing but reversed direction
				# So we can skip it
				pass 
			else:
				if i == j:
					result[point_name] = 0
				else:
					a_coord = Coordinate(intersections[i][0], intersections[i][1])
					b_coord = Coordinate(intersections[j][0], intersections[j][1])
					result[point_name] = pythag_distance(a_coord, b_coord) 
	return result

def path_length(path_points: List[PathNode], euclid_distances:Dict[str, int]) -> int:
	if len(path_points) <= 1:
		return 0
	distance = 0
	for i in range(0, len(path_points) - 1):
		dist_name = create_heuristic_point_name(path_points[i].point, path_points[i+1].point)
		distance += euclid_distances[dist_name]
	return distance

def node_list_contains_point(node_list: List[PathNode], point: int):
	for n in node_list:
		if n.point == point:
			return True
	return False

def greedy_shortest_path(current_path: List[PathNode], visited_points: List[PathNode], M: any, current_point:PathNode, goal: PathNode, euclid_distances: Dict[str, int]) -> None:
	"""
	Uses the 'greedy heuristic' approach to find the
	next closest point to the goal along the available roads from the given current_point.
	Returns the value of the next point
	"""

	
	if current_point == goal:
		return

	visited_points.append(current_point)

	
	shortest_dist = sys.maxsize
	next_point: int = None

	current_path_length = path_length(current_path, euclid_distances)

	for intersection in current_point.roads:
		if node_list_contains_point(visited_points, intersection):
			continue
		dist_point_to_intersect = euclid_distances[create_heuristic_point_name(current_point.point, intersection)]
		dist_intersect_to_goal = euclid_distances[create_heuristic_point_name(intersection, goal.point)]
		total_dist = current_path_length + dist_point_to_intersect + dist_intersect_to_goal + current_point.dist_from_start
		if total_dist < shortest_dist:
			shortest_dist = total_dist
			next_point = intersection


	if next_point is not None:
		next_point_node = PathNode(next_point, M)
		current_point.child = next_point_node
		next_point_node.parent = current_point
		next_point_node.dist_from_start = current_point.dist_from_start + dist_point_to_intersect
		current_path.append(next_point_node)
		# print(current_path)
		if next_point_node != goal:
			greedy_shortest_path(current_path, visited_points, M, next_point_node, goal, euclid_distances)

	return


def shortest_path(M: any,start: int,goal: int):
	
	if start == None or goal == None:
		return None

	if isinstance(start, int) is False or isinstance(goal, int) is False:
		return None

	if start < 0 or goal < 0:
		return None
	
	if start == goal:
		return [goal]

	print("shortest path called")
	euc_distances = calculate_euclidian_distances(M.intersections)
	current_point = PathNode(start, M)
	goal_node = PathNode(goal, M)
	visited_points: List[PathNode] = []
	path: List[PathNode] = [current_point]
	greedy_shortest_path(path, visited_points, M, current_point, goal_node, euc_distances)

	result_path = []
	for i in path:
		result_path.append(i.point)

	return result_path


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

# result = shortest_path(map_test, 8, 24)
# expected = [8, 14, 16, 37, 12, 17, 10, 24]
# print(result)
# print(expected)
# if result == expected:
# 	print('YAY')
# else:
# 	print('NO')

### NEW


def generate_path_nodes(M: Map) -> List[PathNode]:
	"""
	Generates an array of path nodes with minimal data
	(no parents, all values set to 0)
	"""
	result = []
	for i in M.intersections:
		result.append(PathNode(i, M))
	return result

def get_node_with_least_f(path_nodes: List[PathNode]):
	least_f = None
	for i in range(len(path_nodes)):
		if least_f == None:
			least_f = path_nodes[i]
		if path_nodes[i].f < least_f.f:
			least_f = path_nodes[i]
	return least_f

def node_list_has_node(node_list: List[PathNode], node: PathNode):
	for i in node_list:
		if i.point == node.point:
			return True
	return False

def is_in_open_list_points(open_list: List[PathNode], node: PathNode) -> bool:
	for n in open_list:
		for i in n.roads:
			if i == node.point:
				return True
	return False 

def path_from_start(node: PathNode):
	path: List[int] = []
	while node != None:
		path.append(node.point)
		if node.parent != None:
			node = node.parent
		else:
			node = None
	path.reverse()
	return path

def shortest_path_new(m: Map, start: int, goal: int) -> List[int]:
	open_list: List[PathNode] = []
	closed_list: List[PathNode] = []

	start_node = PathNode(start, m)
	goal_node = PathNode(goal, m)
	open_list.append(start_node)
	while open_list:
		current_node = get_node_with_least_f(open_list)
		print(path_from_start(current_node))
		
		if current_node == None:
			return None # path does not exist
		open_list.remove(current_node)
		closed_list.append(current_node)
		
		if current_node == goal_node:
			# End reached
			# Generate path by traversing parent nodes back to start
			return path_from_start(current_node) 

		for r in [PathNode(n, m) for n in current_node.roads]:
			r.g = current_node.g + pythag_distance(current_node.coords, r.coords)
			r.h = pythag_distance(r.coords, goal_node.coords)
			r.f = r.g + r.h
			test_dist = r.f + current_node.h #pythag_distance(current_node.coords, r.coords) + pythag_distance(current_node.coords, goal_node.coords)
			if r not in open_list and r not in closed_list:
				r.parent = current_node
				current_node.child = r
				open_list.append(r)
			elif r in closed_list:
				if r.f > current_node.f + pythag_distance(current_node.coords, r.coords):
					if r in closed_list:
						closed_list.remove(r)
					if r not in open_list:
						open_list.append(r)
				else:
					r.parent = current_node
					current_node.child = r
				

		if current_node in open_list:
			open_list.remove(current_node)
		if current_node not in closed_list:
			closed_list.append(current_node)	
	
	return None

result = shortest_path_new(map_test, 8, 24)
expected = [8, 14, 16, 37, 12, 17, 10, 24]
print('DONE')
print('result: ' + str(result))
print('expected: ' + str(expected))
if result == expected:
	print('YAY')
else:
	print('NO')