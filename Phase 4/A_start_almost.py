import sys
import math
from typing import List, Dict

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

def path_length(path_points: List[int], euclid_distances:Dict[str, int]) -> int:
	if len(path_points) <= 1:
		return 0
	distance = 0
	for i in range(0, len(path_points) - 1):
		dist_name = create_heuristic_point_name(path_points[i], path_points[i+1])
		distance += euclid_distances[dist_name]
	return distance


def greedy_shortest_path(current_path: List[int], visited_points: List[int], M: any, current_point:int, goal: int, euclid_distances: Dict[str, int]) -> None:
	"""
	Uses the 'greedy heuristic' approach to find the
	next closest point to the goal along the available roads from the given current_point.
	Returns the value of the next point
	"""

	
	if current_point == goal:
		return

	visited_points.append(current_point)

	roads_from_point = M.roads[current_point]
	shortest_dist = sys.maxsize
	next_point: int = None

	current_path_length = path_length(current_path, euclid_distances)

	for intersection in roads_from_point:
		if intersection in visited_points:
			continue
		dist_point_to_intersect = euclid_distances[create_heuristic_point_name(current_point, intersection)]
		dist_intersect_to_goal = euclid_distances[create_heuristic_point_name(intersection, goal)]
		total_dist = current_path_length + dist_point_to_intersect + dist_intersect_to_goal
		if total_dist < shortest_dist:
			shortest_dist = total_dist
			next_point = intersection

	if next_point is not None:
		current_path.append(next_point)
		# print(current_path)
		if next_point != goal:
			greedy_shortest_path(current_path, visited_points, M, next_point, goal, euclid_distances)

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
	current_point = start
	visited_points: List[int] = []
	path = [current_point]
	greedy_shortest_path(path, visited_points, M, current_point, goal, euc_distances)
	return path