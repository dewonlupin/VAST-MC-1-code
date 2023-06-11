import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from pyvis.network import Network

# ----------------------- Importing dataframes -----------------------
nodes = pd.read_csv('Helpers/Dataset/Nodes.csv')
links = pd.read_csv('Helpers/Dataset/Links.csv')
# ---------------------------------------------------------------------

HEIGHT = 700
WIDTH = 700

st.header("VAST Challenge MC-1")
st.write("---")

st.subheader("Nodes Dataframe")
n = st.data_editor(nodes, width=WIDTH, height=HEIGHT)
st.write("---")
st.subheader("Links Dataframe")
l = st.data_editor(links, width=WIDTH, height=HEIGHT)


# ---------------------------------------- Test Purpose ----------------------------------------
st.write("---")
st.subheader("Pyvis Tutorial")
nodes = [1, 2, 3, 4]
labels = ['a', 'b', 'c', 'd']

# first create a network
net = Network(notebook=True, height="750px", width="100%", bgcolor="#20202b", font_color="white")

# add_nodes() is used to add multiple nodes and labels from dataset
net.add_nodes(nodes, label=labels)
net.add_edge(1,2)
net.add_edge(2,3)
net.add_edge(3,4)
net.add_edge(2,4)
# net.add_edge(1,4)

# allows for more fluid graph interactions
#net.toggle_physics(True)
# exporting the graph in .html
net.show("hello.html")


# Save and read graph as HTML file (on Streamlit Sharing)
try:
   html_path = 'Helpers'
   net.save_graph(f'{html_path}/pyvis_graph.html')
   HtmlFile = open(f'{html_path}/pyvis_graph.html','r',encoding='utf-8').read()
# Save and read graph as HTML file (locally)
except:
    path = '/html_files'
    net.save_graph(f'{html_path}/pyvis_graph.html')
    HtmlFile = open(f'{html_path}/pyvis_graph.html','r',encoding='utf-8').read()

# Load HTML into HTML component for display on Streamlit
components.html(HtmlFile, height=HEIGHT, width=WIDTH)

# ---------------------------------------- Test Purpose (end) ----------------------------------------
