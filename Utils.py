import Node as Node

class Utils:
    @staticmethod
    def is_goal(state):
        return int(state) == 12345678
    

    @staticmethod
    def get_children(state):
        # to get the indices we can switch with: right, left, up, down = current index of the 1: +1, -1, -3, +3

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
            pair = (int("".join(new_state)), "right")
            children.append(pair)
            
        if index % 3 != 0:
            new_state = list(s)
            new_state[index], new_state[left] = new_state[left], new_state[index]
            pair = (int("".join(new_state)), "left")
            children.append(pair)
            
        if up >= 0:
            new_state = list(s)
            new_state[index], new_state[up] = new_state[up], new_state[index]
            pair = (int("".join(new_state)), "up")
            children.append(pair)
            
        if down < 9:
            new_state = list(s)
            new_state[index], new_state[down] = new_state[down], new_state[index]
            pair = (int("".join(new_state)), "down")
            children.append(pair)
            
        return children
    

    @staticmethod
    def print_board(state):
        s = str(state)
        if len(s) != 9:
            s = "0" + s
        print(s[:3])
        print(s[3:6])
        print(s[6:])


    @staticmethod
    def get_path(node):
        path = []
        while node.parent != -1:
            path.append(node.direction)
            node = node.parent

        return path[::-1]