import math
from typing import List, Dict

class PathNode:
	def __init__(self, point: int, M: any) -> None:
		self.point = point
		self.coords = Coordinate(M.intersections[point][0], M.intersections[point][1])
		
		self.parent: PathNode = None
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


def get_node_with_least_f(path_nodes: List[PathNode]):
	least_f = None
	for i in range(len(path_nodes)):
		if least_f == None:
			least_f = path_nodes[i]
		if path_nodes[i].f < least_f.f:
			least_f = path_nodes[i]
	return least_f

def shortest_path(m: any, start: int, goal: int) -> List[int]:
	path: List[int] = []
	open_list: List[PathNode] = []
	closed_list: List[PathNode] = []

	start_node = PathNode(start, m)
	goal_node = PathNode(goal, m)
	open_list.append(start_node)
	while open_list:
		current_node = get_node_with_least_f(open_list)
		if current_node == None:
			return None # path does not exist
		open_list.remove(current_node)
		closed_list.append(current_node)
		
		if current_node == goal_node:
			# End reached
			# Generate path by traversing parent nodes back to start
			while current_node.parent != None:
				path.append(current_node.point)
				current_node = current_node.parent
			path.reverse()
			return path 

		for r in [PathNode(n, m) for n in current_node.roads]:
			if r not in open_list and r not in closed_list:
				r.parent = current_node
				r.g = current_node.g + pythag_distance(current_node.coords, r.coords)
				r.h = pythag_distance(r.coords, goal_node.coords)
				r.f = r.g + r.h
				open_list.append(r)
			else:
				if r.g > current_node.g:
					r.g = current_node.g + pythag_distance(current_node.coords, r.coords)
					r.h = pythag_distance(r.coords, goal_node.coords)
					r.f = r.g + r.h
					if r in closed_list:
						closed_list.remove(r)
						open_list.append(r)

		if current_node in open_list:
			open_list.remove(current_node)
		if current_node in closed_list:
			closed_list.append(current_node)	
	
	return None