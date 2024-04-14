Simple python application to display directory tree using Flask, SQLAlchemy and SQLite
You need to pip install flask, connexion, SQLAlchemy and Marshmallow
Then run "python app.py".
There are 2 db tables: Nodes and Edges. The Nodes table contains id (node_id) and dir name (node_name). The Edges table contains the relation between every parent (parent_id) and child (child_id)
The server will use the db to traverse the directory structure which can be viewed with the following link: localhost:8765/tree.
For all APIs go to localhost:8765/api/ui
