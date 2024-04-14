from db_methods import get_nodes, get_edges, get_node, get_parent, get_child
  
def get_id(id, col):
  if col == "parent":
    node_id = get_parent(id)
    return get_node(node_id)['node_name']
  elif col == "child":
    node_id = get_child(id)
    return get_node(node_id)['node_name']    

def update_dic(dic, parent, child=""):
  flag = False
  if not bool(dic):
    dic = {'text': parent, 'nodes': []}
  else:
    for key, val in dic.items():
      if key == 'text':
        if val == parent and child != "":
          dic['nodes'].append({'text': child, 'nodes': []})
        else:
          flag = True
      elif key == 'nodes' and val and flag:
        dic[key] = [update_dic(o, parent, child) for o in val]
  return dic

def make_tree():
  tree = {}
  nodes = get_nodes()
  edges = get_edges()
  parents = list(map(lambda x: x['parent_id'], edges))
  children = list(map(lambda x: x['child_id'], edges))

  for node in nodes:
    id = node['node_id']
    name = node['node_name']
    if parents.count(id) > 0:
      if children.count(id) > 0:
        parent_name = get_id(id, "parent")
        tree = update_dic(tree.copy(), parent_name, name)
      else:
        tree = update_dic(tree.copy(), name)
    else:
      parent_name = get_id(id, "parent")
      tree = update_dic(tree.copy(), parent_name, name)
  return [tree]