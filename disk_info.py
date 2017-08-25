import os
from FileTree import FileTreeNode
import json
import string
import sys
import platform
import time

BAN_LIST = ['$RECYCLE.BIN', 'System Volume Information', '$Recycle.Bin', '_Tree.json']

def disk():
    os.system("wmic VOLUME GET NAME > name")
    os.system("wmic VOLUME GET SystemVolume > SystemVolume")
    Volume_list = []
    with open('name','r',encoding= 'utf-16') as name_file:
        with open('SystemVolume', 'r',encoding= 'utf-16') as system_volume:
            names = name_file.readlines()
            bools = system_volume.readlines()
            for name in names:
                if bools[names.index(name)].strip() == 'FALSE':
                    Volume_list.append(name.strip())
    return Volume_list

def create_node_tree(p_node):
    try:
        path_list = os.listdir(p_node.path)
    except:
        path_list = []
    for file in path_list:
        f_path = os.path.join(p_node.path, file)
        # print('Searching: %s' % f_path)
        try:
            m_time = os.path.getmtime(f_path)
        except:
            continue
        if file in BAN_LIST:
            continue
        if os.path.isdir(f_path):
            sub_node = FileTreeNode(file, 'dir', True, m_time, f_path)
            create_node_tree(sub_node)
            p_node.add_child(sub_node)
        else:
            sub_node = FileTreeNode(file, 'file', False, m_time, f_path, os.path.getsize(f_path))
            p_node.add_child(sub_node)
    return

def save_node_tree(p_node):
    with open('./' + p_node.name[0] + '_Tree.json', 'w') as file:
        file.write(json.dumps(p_node.get_save_dict()))





v_list = disk()
trees = []

for v in v_list:
    tree_root = FileTreeNode(v, 'volume', os.path.isdir(v), None, path=v)
    create_node_tree(tree_root)
    print(tree_root.get_size())
    save_node_tree(tree_root)
# v = 'D:/'
# tree_root = FileTreeNode(v, 'volume', os.path.isdir(v), None, path=v)
# create_node_tree(tree_root)
# save_node_tree(tree_root)
