import node as node

DIRECTIONS = {
    "right": 1,
    "left": -1,
    "up": -3,
    "down": 3
}

def is_goal(state, goal="012345678"):
    return state == goal

def move_tile(state, direction):
    s = str(state)
    index = s.index("0")
    target = index + DIRECTIONS[direction]

    new_state = list(s)
    new_state[index], new_state[target] = new_state[target], new_state[index]
    return ("".join(new_state), direction)


def get_children(state):
    # to get the indices we can switch with: right, left, up, down = current index of the 1: +1, -1, -3, +3


    index = state.index("0")
    
    # get the indices of the tiles we can switch with

    up = index + DIRECTIONS["up"]
    down = index + DIRECTIONS["down"]
    children = []
    
    if index % 3 != 2:
        children.append(move_tile(state, "right"))
        
    if index % 3 != 0:
        children.append(move_tile(state, "left"))
        
    if up >= 0:
        children.append(move_tile(state, "up"))
        
    if down < 9:
        children.append(move_tile(state, "down"))
        
    return children


def print_board(state):
    print(state[:3])
    print(state[3:6])
    print(state[6:])


def get_path(node):
    path = []
    while node.parent != -1:
        path.append(node.direction)
        node = node.parent

    return path[::-1]