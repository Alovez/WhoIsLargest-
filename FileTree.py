# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 20:26
# @Author  : AloveZ
# @Email   : ruinand@live.com
# @File    : FileTree.py
# @Software: PyCharm Community Edition

import copy


class FileTreeNode:
    def __init__(self, name, file_type, is_dir, m_time, path, size=0):
        self.name = name
        self.type = file_type
        self.is_dir = is_dir
        self.m_time = m_time
        self.children = []
        self.path = path
        self.size = size
        if is_dir:
            self.is_init = False
        else:
            self.is_init = True

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_children(self):
        return self.children

    def get_children_dir(self):
        children_dir = []
        for child in self.get_children():
            if child.is_dir:
                children_dir.append(child)
        return children_dir

    def get_children_tree(self):
        child_save_tree = []
        for child in self.get_children():
            if child.is_dir:
                child_dict = child.get_save_dict()
            else:
                child_dict = {
                    'name': child.name,
                    'type': child.type,
                    'is_dir': child.is_dir,
                    'm_time': child.m_time,
                    'children_dict': None,
                    'path': child.path,
                    'size': child.get_size(),
                }
            child_save_tree.append(child_dict)
        return child_save_tree

    def get_save_dict(self):
        return {
            'name': self.name,
            'type': self.type,
            'is_dir': self.is_dir,
            'm_time': self.m_time,
            'children_dict': self.get_children_tree(),
            'path': self.path,
            'size':self.get_size()
        }

    def get_size(self):
        if self.is_init:
            return self.size
        else:
            size = 0
            for child in self.children:
                size += child.get_size()
            self.size = size
            self.is_init = True
        return self.size
