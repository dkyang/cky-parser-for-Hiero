class Item:
    def __init__(self):
        self.source_grammar = ''
        self.target_grammar_list = []
        self.back_pointers = []

class Cell:
    def __init__(self):
        self.item_list = []
        beg = -1
        end = -1

    def add_item(self, item):
        self.item_list.append(item)

    def is_item_empty(self):
        return len(self.item_list) == 0
        

    
