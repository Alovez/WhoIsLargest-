from tkinter import *

class GroupItem:
    def __init__(self, text, level):
        self.text = text
        self.level = level
        self.sub = []
        self.sign = ' > '
        self.open = False

    def get_text(self):
        return '        ' * self.level + self.sign + self.text

    def remove_sub(self):
        self.sub = []

class MoreItem:
    def __init__(self):
        self.master = Tk()
        self.master.geometry('800x500+500+200')
        self.master.resizable(False, False)
        self.frame_left = LabelFrame(self.master, text="Group", padx=5, pady=5)
        scrollbar = Scrollbar(self.frame_left)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.group = Listbox(self.frame_left, yscrollcommand=scrollbar.set, height=24)
        self.group.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=self.group.yview)
        self.frame_left.grid(row=1, column=1,padx=15, pady=15)
        self.explore = LabelFrame(self.master, text="Explore", padx=20, pady=15)
        self.explore.grid(row=1, column=3, padx=15, pady=15)
        self.label_list = []
        self.text_list = []
        self.sub_list = ['sub1', 'sub2']
        t_label = Label(self.explore, text='test')
        t_label.grid(row=1)
        for i in range(1,10):
            label = GroupItem('item %s' % i, 0)
            self.label_list.append(label)
            self.text_list.append(label.get_text())
        self.group.bind("<<ListboxSelect>>", self.add_subitem)
        self.val = StringVar(value=self.text_list)
        self.group['listvariable'] = self.val
        self.refresh()
        mainloop()

    def refresh(self):
        self.text_list = []
        for item in self.label_list:
            self.text_list.append(item.get_text())
        self.val.set(tuple(self.text_list))

    def add_subitem(self, event):
        index = self.group.curselection()[0]
        p_label = self.label_list[index]
        if not p_label.open:
            for item in self.sub_list:
                label = GroupItem(item, p_label.level + 1)
                self.label_list.insert(index + 1, label)
                p_label.sub.append(label)
            p_label.open = True
            p_label.sign = ' ▼ '
        else:
            for label in p_label.sub:
                self.label_list.remove(label)
            p_label.remove_sub()
            p_label.open = False
            p_label.sign = ' > '
        self.refresh()

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
        # self.refresh()

MoreItem()
