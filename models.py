from config import db, ma

class Node(db.Model):
  __tablename__ = "nodes"
  node_id = db.Column(db.Integer, primary_key=True)
  node_name = db.Column(db.String, nullable=False)

class Edge(db.Model):
  __tablename__ = "edges"
  parent_id = db.Column(db.Integer, primary_key=True)
  child_id = db.Column(db.Integer, primary_key=True)

class NodeSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Node
    load_instance = True
    sqla_session = db.session

class EdgeSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Edge
    load_instance = True
    sqla_session = db.session

node_schema = NodeSchema(many=True)
edge_schema = EdgeSchema(many=True)