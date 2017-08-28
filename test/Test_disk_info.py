from FileTree import FileTreeNode
from disk_info import disk, create_node_tree, save_node_tree, load_node_tree
from Label_boxs import MoreItem
import os
import json

v_list = disk()
trees = []

for v in v_list:
    with open(v[0] + '_Tree.json') as file:
        tree_json = json.load(file)
        tree_root = load_node_tree(tree_json)
    # tree_root = FileTreeNode(v, 'volume', os.path.isdir(v), None, path=v)
    # create_node_tree(tree_root)
    print(tree_root.get_size())
    # save_node_tree(tree_root)
    trees.append(tree_root)

MoreItem(trees)

