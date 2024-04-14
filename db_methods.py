from flask import abort
from models import Node, node_schema, Edge, edge_schema

def get_nodes():
  nodes = Node.query.all()
  return node_schema.dump(nodes)

def get_node(node_id):
  node = Node.query.filter(Node.node_id == node_id)
  if node is not None:
    return node_schema.dump(node)[0]
  else:
    abort(
      404, f"Node with ID {node_id} not found"
    )

def get_edges():
  edges = Edge.query.all()
  return edge_schema.dump(edges)

def get_parent(child_id):
  edge = Edge.query.filter(Edge.child_id == child_id)
  if edge is not None:
    return edge_schema.dump(edge)[0]['parent_id']
  else:
    abort(
      404, f"Edge with ID {child_id} not found"
    )

def get_child(parent_id):
  edge = Edge.query.filter(Edge.parent_id == parent_id)
  if edge is not None:
    return edge_schema.dump(edge)[0]['child_id']
  else:
    abort(
      404, f"Edge with ID {parent_id} not found"
    )