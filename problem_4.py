class Group:
    def __init__(self, _name: str) -> None:
        self.name: str = _name
        self.groups: list[Group] = []
        self.users: list[str] = []

    def add_group(self, group: 'Group') -> None:
        self.groups.append(group)

    def add_user(self, user: str) -> None:
        self.users.append(user)

    def get_groups(self) -> list['Group']:
        return self.groups

    def get_users(self) -> list[str]:
        return self.users

    def get_name(self) -> str:
        return self.name


def is_user_in_group(user: str, group: Group) -> bool:

    if user is None:
        return False

    # Use a stack to implement an iterative depth-first search
    stack = [group]

    while stack:
        current_group = stack.pop()
        # Check if the user is directly in this group
        if user in current_group.get_users():
            return True

        # Add all subgroups to the stack for further exploration
        stack.extend(current_group.get_groups())

    return False

if __name__ == "__main__":
    # Testing the implementation

    # Creating groups and users
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # Test Case 1: User is in a nested subgroup
    print("Test Case 1")
    print(is_user_in_group("sub_child_user", parent))  # Expected output: True

    # Test Case 2: empty gropu and user
    empty_group = Group("")
    empty_user = empty_group.add_user("")
    print(is_user_in_group("empty_user", empty_group))

    # Test Case 3: user in multiple groups
    print("Test Case 4")
    # Adding the same user to multiple subgroups
    child.add_user("user_in_child")
    sub_child.add_user("user_in_sub_child")

    print(is_user_in_group("user_in_child", parent))  # Expected output: True
    print(is_user_in_group("user_in_sub_child", parent))  # Expected output: True
    print(is_user_in_group("user_in_child", sub_child))  # Expected output: False

