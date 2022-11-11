

"""
Implementation of basic web router using tries
"""

class RouteTrieNode:
    def __init__(self, handler: str):
        self.children = {}
        self.handler = handler

    def insert(self, path_segment):
        """
        Inserts a route trie node for the given path segment
        """
        self.children[path_segment] = RouteTrieNode()


class RouteTrie:
    def __init__(self, handler: str):
        self.root = RouteTrieNode(handler)

    def insert(self, path_parts: list[str], handler: str): 
        """
        Inserts and hanlder for the given path
        """ 
        current_node = self.root

        for p in path_parts:
            if p not in current_node.children:
                current_node.children[p] = RouteTrieNode(None)
            current_node = current_node.children[p]

        current_node.handler = handler

    def find(self, split_path: list[str]):
        """
        Finds the handler for the given path.
        Returns None if no handler found.
        """
        current_node = self.root

        for p in split_path:
            if p not in current_node.children:
                return None
            current_node = current_node.children[p]

        return current_node.handler

class Router:
    def __init__(self, root_handler: str, not_found_handler: str):
        self.root = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        """
        Adds a handler to the given path
        """
        split_path = self.split_path(path)
        self.root.insert(split_path, handler)

    def lookup(self, path: str):
        """
        Finds the handler for any given path.
        Returns no_found_handler if lookup does not find anything
        """
        if path is None:
            return self.not_found_handler

        split_path = self.split_path(path)
        handler = self.root.find(split_path)
        if handler == None:
            return self.not_found_handler
        return handler

    def split_path(self, path:str) -> list[str]:
        """
        Splits the given path into an array of path segments, 
        e.g. '/home/about/me' --> [home, about, me]
        """
        section = ''
        result = []
        for c in path:
            if c == '/':
                if len(section) > 0:
                    result.append(section)
                section = ''
            else:
                section += c

        if len(section) > 0:
            result.append(section)

        return result

        
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/projects", "projects handler")  # add another route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/projects")) # should print 'projects handler'
print(router.lookup(None)) # should print 'not found handler'