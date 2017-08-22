from tkinter import *

class GroupItem:
    def __init__(self, row, column, parent, text):
        self.row = row
        self.column = column
        self.parent = parent
        self.text = text
        self.open = False
        self.widget = Label(parent, text=text)

    def set_pos(self, row, column):
        self.row = row
        self.column = column
        self.widget.grid(row=row, column=column)

    def set_pos_delta(self, d_row, d_column):
        self.row += d_row
        self.column += d_column
        self.widget.grid(row=self.row, column=self.column)

    def add_sub_item(self, sub_list):
        self.sub_list = sub_list


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
            label = GroupItem(i, 1, self.group, 'Item %s' % i)
            label.set_pos(i, 1)
            label.widget.bind("<Button-1>", self.add_subitem)
            self.label_dict[label.widget] = label
            self.label_list.append(label)
        mainloop()

    def add_subitem(self, event):
        p_label = self.label_dict[event.widget]
        p_num = self.label_list.index(p_label)
        if not p_label.open:
            if p_num < len(self.label_list):
                for p_item in self.label_list[p_num + 1:]:
                    p_item.set_pos_delta(len(self.sub_list),0)
            sub_label_list = []
            for item in self.sub_list:
                label = Label(self.group, text=item)
                label.grid(row=p_label.row + 1 + self.sub_list.index(item), column = p_label.column + 1)
                sub_label_list.append(label)
            p_label.add_sub_item(sub_label_list)
            p_label.open = True
        else:
            if p_num < len(self.label_list):
                for p_item in self.label_list[p_num + 1:]:
                    p_item.set_pos_delta(-len(self.sub_list),0)
            for item in p_label.sub_list:
                item.grid_remove()
            p_label.open = False


MoreItem()
