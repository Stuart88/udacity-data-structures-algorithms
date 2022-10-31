class Group(object):
    def __init__(self, _name: str):
        self.name:str = _name
        self.groups: list[Group] = []
        self.users: list[str] = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group: Group):
    """
    Checkes user names of the given group, then uses
    recursion to check user names of all child groups.
    Complexity: O(n), where n is the total number of users across all groups
    """
    if user is None:
        return False
    
    if len(user) == 0:
        return False

    if group is None:
        return False

    for u in group.get_users():
        if u == user:
            return True

    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True
    
    return False


def test_case(test_name: str, result, expected):
    if result == expected:
        print(f'{test_name} Passed')
    else:
        print(f'{test_name} Failed')

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

test_case('Test 1', is_user_in_group(sub_child_user, parent), True)
test_case('Test 2', is_user_in_group("King Albert", parent), False)
test_case('Test 3', is_user_in_group(None, parent), False)
test_case('Test 4', is_user_in_group(sub_child_user, child), True)
test_case('Test 5', is_user_in_group(sub_child_user, sub_child), True)
test_case('Test 6', is_user_in_group(sub_child_user, None), False)
test_case('Test 7', is_user_in_group(None, None), False)