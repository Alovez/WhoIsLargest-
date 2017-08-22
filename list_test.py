from tkinter import *

class GroupItem:
    def __init__(self, level, parent, text):
        self.level = level
        self.parent = parent
        self.text = text
        self.open = False
        # bm = PhotoImage(file='./img/Close_Folder.png')
        self.widget = Label(parent, text=text)
        self.sub_list = []

    def set_pos(self, row, column):
        self.widget.grid(row=row, column=column)

    def add_sub_item(self, sub_item):
        self.sub_list.append(sub_item)

    def remove_sub_list(self):
        self.sub_list = []


class MoreItem:
    def __init__(self):
        self.master = Tk()
        self.group = LabelFrame(self.master, text="Group", padx=20, pady=15)
        self.group.grid(row=1, column=1,padx=15, pady=15)
        self.explore = LabelFrame(self.master, text="Explore", padx=20, pady=15)
        self.explore.grid(row=1, column=2, padx=15, pady=15)
        self.label_dict = {}
        self.label_list = []
        self.sub_list = ['sub1', 'sub2']
        t_label = Label(self.explore, text='test')
        t_label.grid(row=1)
        for i in range(1,10):
            label = GroupItem(1, self.group, 'item %s' % i)
            label.widget.bind("<Button-1>", self.add_subitem)
            self.label_dict[label.widget] = label
            self.label_list.append(label)
        self.refresh()
        mainloop()

    def refresh(self):
        for item in self.label_list:
            item.set_pos(self.label_list.index(item) + 1, item.level)

    def add_subitem(self, event):
        p_label = self.label_dict[event.widget]
        p_num = self.label_list.index(p_label)
        if not p_label.open:
            for item in self.sub_list:
                label = GroupItem(p_label.level + 1, self.group, item)
                p_label.add_sub_item(label)
                self.label_list.insert(p_num + 1, label)
            p_label.open = True
        else:
            for item in p_label.sub_list:
                item.widget.grid_remove()
                self.label_list.remove(item)
            p_label.remove_sub_list()
            p_label.open = False
        self.refresh()

MoreItem()
