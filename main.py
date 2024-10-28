from utils import print_board, get_children
from algorithms.dfs import DFS
from algorithms.ids import IDS
from algorithms.bfs import BFS
from algorithms.a_star import AStar
import streamlit as st


def build():
    st.title("8 Puzzle Solver")
    st.write("This is a simple 8 puzzle solver using different algorithms")
    algorithm = render_sidebar()
    st.write("Algorithm: ", algorithm)
    board = st.text_area("Enter the board", "1 2 3\n4 5 6\n7 8 0")
    board = [[int(x) for x in row.split()] for row in board.split('\n')]
    print_board(board)
    if algorithm == "DFS":
        print("DFS")
    else:
        print("IDS")


def render_sidebar():
    st.sidebar.title("Algorithms")
    st.sidebar.subheader("Choose an algorithm")
    algorithm = st.sidebar.selectbox(
        "Algorithm",
        ["DFS", "IDS", "BFS", "A*-manhattan", "A*-euclidean"]
    )
    return algorithm









build()
    
        