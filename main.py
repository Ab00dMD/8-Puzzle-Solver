from utils import print_board, get_children
from algorithms.dfs import DFS
from algorithms.ids import IDS
from algorithms.bfs import BFS
from algorithms.a_star import AStar
import streamlit as st

board_state="012345678"

def build():
    local_css("style.css")
    st.title("8 Puzzle Solver")
    algorithm = render_sidebar()
    answer = {}
    # board = st.markdown(render_state(board_state), unsafe_allow_html=True)


def render_sidebar():
    st.sidebar.title("Algorithms")
    st.sidebar.subheader("Choose an algorithm")
    algorithm = st.sidebar.selectbox(
        "Algorithm",
        ["DFS", "IDS", "BFS", "A*-manhattan", "A*-euclidean"]
    )
    board_state_input = st.sidebar.text_input("Board State")
    board_state = board_state_input

    if st.sidebar.button("Render State"):
      board = st.markdown(render_state(board_state), unsafe_allow_html=True)

    if st.sidebar.button("Solve"):
      with st.spinner('Solving...'):
          answer = solve_board(board_state, algorithm)
      display_answer(answer)

    return algorithm

def render_state(state: str):
    #check if the state is valid
    if len(state) != 9 or not state.isdigit() or len(set(state)) != 9:
        return "Invalid state"
    
    ##delete prev board
    st.markdown('<div></div>', unsafe_allow_html=True)
    
    return f"""
    <div class="table">
      <div class="row">
        <div class="cell">
          {state[0]}
        </div>
        <div class="cell">
          {state[1]}
        </div>
        <div class="cell">
          {state[2]}
        </div>
      </div>
      <div class="row">
        <div class="cell">
          {state[3]}
        </div>
        <div class="cell">
          {state[4]}
        </div>
        <div class="cell">
          {state[5]}
        </div>
      </div>
      <div class="row">
        <div class="cell">
          {state[6]}
        </div>
        <div class="cell">
          {state[7]}
        </div>
        <div class="cell">
          {state[8]}
        </div>
      </div>
    </div>
    """

def solve_board(board_state, algorithm):
    if algorithm == "DFS":
        answer = DFS(board_state).search()
    elif algorithm == "IDS":
        answer = IDS(board_state).search()
    elif algorithm == "BFS":
        answer = BFS(board_state).search()
    elif algorithm == "A*-manhattan":
        answer = AStar(board_state, "manhattan").search()
    elif algorithm == "A*-euclidean":
        answer = AStar(board_state, "euclidean").search()
    else:
        answer = {}
    return answer
  
def display_answer(answer):
    if not answer:
        st.write("No solution found")
        return
    print(answer)
    paths = answer["path"][0]
    directions = answer["path"][1]
    st.write(f"Cost: {answer['cost']}")
    st.write(f"Nodes expanded: {answer['nodes_expanded']}")
    st.write(f"Max search depth: {answer['max_search_depth']}")
    st.write(f"Running time: {answer['running_time']}")
    for i in range(len(paths)):
        st.write(f"Move {i+1}: {directions[i]}")
        st.markdown(render_state(paths[i][0]), unsafe_allow_html=True)
        st.write("")
    
    

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)



build()
    
        