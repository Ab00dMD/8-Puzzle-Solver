# the state will be stored as a number 125304678 to represent a board or 3*3
# board 125
#       304
#       678
# empty tile is 0

# goal state will be 012 345 678
# the leading 0 will not make a problem when comparing the state with the goal state
def is_goal(state):
    return state == 12345678

# to get the indices we can switch with: right, left, up, down = current index of the 1: +1, -1, -3, +3
def get_children(state):
    s = str(state)
    
    # to fix leading 0
    if len(s) != 9:
        s = "0" + s
    index = s.index("0")
    
    # get the indices of the tiles we can switch with
    right = index + 1
    left = index - 1
    up = index - 3
    down = index + 3
    children = []
    
    if index % 3 != 2:
        new_state = list(s)
        new_state[index], new_state[right] = new_state[right], new_state[index]
        children.append(int("".join(new_state)))
        
    if index % 3 != 0:
        new_state = list(s)
        new_state[index], new_state[left] = new_state[left], new_state[index]
        children.append(int("".join(new_state)))
        
    if up >= 0:
        new_state = list(s)
        new_state[index], new_state[up] = new_state[up], new_state[index]
        children.append(int("".join(new_state)))
        
    if down < 9:
        new_state = list(s)
        new_state[index], new_state[down] = new_state[down], new_state[index]
        children.append(int("".join(new_state)))
        
    return children

def print_board(state):
    s = str(state)
    if len(s) != 9:
        s = "0" + s
    print(s[:3])
    print(s[3:6])
    print(s[6:])

def main():
    print("Welcome to the 8-Puzzle Solver! please input the initial state of the board:")
    number = int(input())
    
    print_board(number)
    
    children = get_children(number)
    
    print("Children of the current state:")
    for child in children:
        print(child)
        # print_board(child)
        # print("\n")

if __name__ == "__main__":
    main()