#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from disk_info import disk, create_node_tree, save_node_tree


class GroupItem:
    def __init__(self, text, level, node=None):
        self.text = text
        self.level = level
        self.node = node
        self.sub = []
        self.sign = ' > '
        self.open = False

    def get_sub_text_list_from_nodes(self):
        sub_nodes = self.node.get_children_dir()
        sub_text_list = []
        for node in sub_nodes:
            sub_text_list.append(node.name)
        return sub_text_list

    def get_children_dir(self):
        return self.node.get_children_dir()

    def get_text(self):
        return '        ' * self.level + self.sign + self.text

    def remove_sub(self, label_list):
        if len(self.sub) == 0:
            return
        else:
            for item in self.sub:
                label_list.remove(item)
                item.remove_sub(label_list)
            self.sub = []


class MoreItem:
    def __init__(self, root_nodes):
        # 初始化窗口
        self.master = Tk()
        self.master.geometry('840x500+500+200')
        self.master.resizable(False, False)
        # 初始化左边栏
        self.frame_left = LabelFrame(self.master, text="Group", padx=5, pady=5)
        scrollbar = Scrollbar(self.frame_left)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar_b = Scrollbar(self.frame_left, orient=HORIZONTAL)
        scrollbar_b.pack(side=BOTTOM, fill=X)
        self.group = Listbox(self.frame_left, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar_b.set, height=24)
        self.group.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=self.group.yview)
        scrollbar_b.config(command=self.group.xview)
        self.frame_left.grid(row=1, column=1, padx=15, pady=15)
        self.label_list = []
        self.text_list = []
        for root in root_nodes:
            label = GroupItem(root.name, 0, root)
            self.label_list.append(label)
            self.text_list.append(label.get_text())
        self.group.bind("<<ListboxSelect>>", self.show_sub)
        self.val = StringVar(value=self.text_list)
        self.group['listvariable'] = self.val
        self.refresh_left()
        # 初始化右边栏
        self.frame_right = LabelFrame(self.master, text="Explore", padx=5, pady=5)
        self.frame_right.grid(row=1, column=2, padx=15, pady=15, sticky='N')
        self.name_button = Button(self.frame_right, text='名称', width=25)
        self.size_button = Button(self.frame_right, text='大小', width=30)
        self.type_button = Button(self.frame_right, text='类型', width=25)
        self.name_button.grid(row=1, column=1)
        self.type_button.grid(row=1, column=2)
        self.size_button.grid(row=1, column=3)
        self.explore_frame = Frame(self.frame_right, padx=5, pady=5)
        self.explore_frame.grid(row=2, columnspan=4)
        explore_scroll = Scrollbar(self.explore_frame)
        explore_scroll.pack(side=RIGHT, fill=Y)
        self.explore = Listbox(self.explore_frame, yscrollcommand=explore_scroll, height=22, width=80)
        self.explore.pack(side=LEFT, fill=BOTH)
        explore_scroll.config(command=self.explore.yview)

        mainloop()

    def refresh_left(self):
        self.text_list = []
        for item in self.label_list:
            self.text_list.append(item.get_text())
        self.val.set(tuple(self.text_list))

    def show_sub(self, event):
        index = self.group.curselection()[0]
        p_label = self.label_list[index]
        if not p_label.open:
            for item in p_label.get_children_dir():
                label = GroupItem(item.name, p_label.level + 1, item)
                self.label_list.insert(index + 1, label)
                p_label.sub.append(label)
            p_label.open = True
            p_label.sign = ' ▼ '
        else:
            p_label.remove_sub(self.label_list)
            p_label.open = False
            p_label.sign = ' > '
        self.refresh_left()

        # p_label = self.label_dict[event.widget]
        # p_num = self.label_list.index(p_label)
        # if not p_label.open:
        #     for item in self.sub_list:
        #         label = GroupItem(p_label.level + 1, self.group, item)
        #         p_label.add_sub_item(label)
        #         self.label_list.insert(p_num + 1, label)
        #     p_label.open = True
        # else:
        #     for item in p_label.sub_list:
        #         item.widget.grid_remove()
        #         self.label_list.remove(item)
        #     p_label.remove_sub_list()
        #     p_label.open = False
        # self.refresh_left()