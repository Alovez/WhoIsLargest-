# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 20:26
# @Author  : AloveZ
# @Email   : ruinand@live.com
# @File    : FileTree.py
# @Software: PyCharm Community Edition

import copy


class FileTreeNode:
    def __init__(self, name, file_type, is_dir):
        self.name = name
        self.type = file_type
        self.is_dir = is_dir
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_children(self):
        return copy.copy(self.children)

    def get_size(self):
        size = 0
        if self.is_dir:
            for child in self.children:
                size += child.get_size()
        else:
            size = self.size
        return size
