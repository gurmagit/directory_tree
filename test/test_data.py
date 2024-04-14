import pytest
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from data import update_dic, make_tree

Base = declarative_base()


class Node(Base):
    __tablename__ = "nodes"
    node_id = Column(Integer, primary_key=True)
    node_name = Column(String)


class Edge(Base):
    __tablename__ = "edges"
    edge_id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("nodes.node_id"))
    child_id = Column(Integer, ForeignKey("nodes.node_id"))


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    nodes_data = [
        {"node_id": 1, "node_name": "winterfell.westeros.got"},
        {"node_id": 2, "node_name": "computers"},
        {"node_id": 3, "node_name": "Domain Controllers"},
        {"node_id": 4, "node_name": "TheWall"},
        {"node_id": 5, "node_name": "Kylo-Ou"},
    ]
    session.bulk_insert_mappings(Node, nodes_data)

    edges_data = [
        {"parent_id": 1, "child_id": 2},
        {"parent_id": 1, "child_id": 3},
        {"parent_id": 1, "child_id": 4},
        {"parent_id": 4, "child_id": 5},
    ]
    session.bulk_insert_mappings(Edge, edges_data)

    session.commit()

    yield session

    session.rollback()
    session.close()


def test_update_dic_empty():
    dic = {}
    dic = update_dic(dic, "Parent")
    assert dic == {"text": "Parent", "nodes": []}


def test_update_dic_with_child():
    dic = {"text": "Parent", "nodes": []}
    dic = update_dic(dic, "Parent", "Child")
    assert dic == {"text": "Parent", "nodes": [{"text": "Child", "nodes": []}]}


def test_update_dic_with_existing_parent():
    dic = {"text": "Parent", "nodes": [{"text": "Child", "nodes": []}]}
    dic = update_dic(dic, "Parent", "Child 2")
    assert dic == {
        "text": "Parent",
        "nodes": [{"text": "Child", "nodes": []}, {"text": "Child 2", "nodes": []}],
    }


def test_make_tree():
    tree = make_tree()
    assert tree == [
        {
            "text": "winterfell.westeros.got",
            "nodes": [
                {"text": "computers", "nodes": []},
                {"text": "Domain Controllers", "nodes": []},
                {"text": "TheWall", "nodes": [{"text": "Kylo-Ou", "nodes": []}]},
            ],
        }
    ]
