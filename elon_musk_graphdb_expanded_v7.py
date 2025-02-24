import pandas as pd
import networkx as nx
import plotly.graph_objects as go

# Load dataset
dataset_path = "elon_musk_graphdb_dataset.csv"
df = pd.read_csv(dataset_path)

# Initialize a directed graph
G = nx.DiGraph()

# Add nodes and edges from dataset
for index, row in df.iterrows():
    G.add_node(row["Source"])
    G.add_node(row["Target"])
    G.add_edge(row["Source"], row["Target"], relation=row["Relation"])

# Define node categories for coloring
color_map = {
    'Elon Musk': 'blue',
    'Follower': 'lightblue',
    'Event': 'red',
    'Topic': 'yellow',
    'Tweet': 'green'
}

# Function to determine node color
def get_node_color(node):
    if node == "Elon Musk":
        return color_map["Elon Musk"]
    elif "Follower" in node:
        return color_map["Follower"]
    elif "Event" in node:
        return color_map["Event"]
    elif "Topic" in node:
        return color_map["Topic"]
    elif "Tweet" in node:
        return color_map["Tweet"]
    return 'gray'

node_colors_plotly = [get_node_color(node) for node in G.nodes]

# Get positions for all nodes
pos = nx.spring_layout(G, seed=42)

# Create edge traces
edge_x = []
edge_y = []
edge_texts = []

for edge in G.edges(data=True):
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
    edge_texts.append(f"{edge[0]} → {edge[1]} ({edge[2]['relation']})")

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=1, color='#888'),
    hoverinfo='text',
    text=edge_texts,
    mode='lines'
)

# Create node traces
node_x = []
node_y = []
node_texts = []

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_texts.append(node)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=node_texts,
    hoverinfo='text',
    marker=dict(
        size=10,
        color=node_colors_plotly,
        line=dict(width=2)
    )
)

# Create figure
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title="Expanded GraphDB Model of Elon Musk's Response to Controversy",
                    titlefont=dict(size=16),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=0, l=0, r=0, t=40),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                )
)

# Save the interactive graph as an HTML file for web deployment
html_path = "elon_musk_graphdb_expanded.html"
fig.write_html(html_path)

print(f"Graph visualization saved to {html_path}. Open this file in a web browser to interact with the graph.")
