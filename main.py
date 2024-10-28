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
    board = st.markdown(render_state(board_state), unsafe_allow_html=True)


def render_sidebar():
    st.sidebar.title("Algorithms")
    st.sidebar.subheader("Choose an algorithm")
    algorithm = st.sidebar.selectbox(
        "Algorithm",
        ["DFS", "IDS", "BFS", "A*-manhattan", "A*-euclidean"]
    )
    st.sidebar.text_input("Board State")

    if st.sidebar.button("Render State"):
      pass

    if st.sidebar.button("Solve"):
      pass

    return algorithm

def render_state(state: str):
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

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)








build()
    
        