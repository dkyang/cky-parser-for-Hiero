from phrase_table import PhraseTable 
from cell import *

def add_match_item_to_cell(key, rules_table, cell, back_pointers):
    item = Item()
    target_grammar_list = rules_table.get_match_rules(key)
    if target_grammar_list is not None:
        item.source_grammar = key
        item.target_grammar_list = target_grammar_list
        item.back_pointers = back_pointers
        cell.add_item(item)
    

def add_inferable_items(sentence, i, j, rules_table, chart, cell):
    # debug
    #result = []
    #cell = Cell()
    cell.beg = i
    cell.end = j
    for i1 in xrange(i,j+1):
        key = ''
        if i < i1:
            key += ' '.join(sentence[i:i1])
        if i1 == j:
            print key
            back_pointers = []
            add_match_item_to_cell(key, rules_table, cell, back_pointers)
        else:
            for j1 in xrange(i1+1,j+1):
                # if no matched rules in this span, skip it
                if chart[i1][j1] is None:
                    continue

                key1 = key
                if i1 == i:
                    key1 += 'X'
                elif i1 < j:
                    key1 += ' X'

                if j1 == j:
                    print key1
                    back_pointers = []
                    # right? left close, right open
                    back_pointers.append(chart[i1][j1])
                    add_match_item_to_cell(key1, rules_table, 
                                           cell, back_pointers)
                else:
                    for i2 in xrange(j1+1,j+1):
                        key2 = key1
                        key2 += ' '
                        key2 += ' '.join(sentence[j1:i2])
                        if i2 == j:
                            print key2
                            back_pointers = []
                            back_pointers.append(chart[i1][j1])
                            add_match_item_to_cell(key2, rules_table,
                                                   cell, back_pointers)                           
                        else: 
                            # j2 <= j
                            for j2 in xrange(i2+1,j+1):
                                if chart[i2][j2] is None:
                                    continue 
                      
                                key3 = key2
                                key3 += ' X'
                                if j2 == j:
                                    print key3
                                    back_pointers = []
                                    back_pointers.append(chart[i1][j1])
                                    back_pointers.append(chart[i2][j2])
                                    add_match_item_to_cell(key3, rules_table,
                                                           cell, back_pointers)   
                                else:
                                    # j2 < j
                                    key3 += ' '
                                    key3 += ' '.join(sentence[j2:j])
                                    print key3
                                    back_pointers = []
                                    back_pointers.append(chart[i1][j1])
                                    back_pointers.append(chart[i2][j2])
                                    add_match_item_to_cell(key3, rules_table,
                                                           cell, back_pointers)
    #cell = []
    #return cell

def add_glued_items(sentence, i, j, chart, cell):
    cell.beg = i
    cell.end = j
    for mid in xrange(i+1,j):
        if chart[i][mid] is not None and chart[mid][j] is not None:
            key = 'S X'
            #back_pointers = []
            #back_pointers.append(chart[i][mid])
            #back_pointers.append(chart[mid][j])

            item = Item()
            item.source_grammar = key
            item.target_grammar_list = 'S X'
            item.back_pointers.append(chart[i][mid])
            item.back_pointers.append(chart[mid][j])
            cell.add_item(item)
        
    #return cell


#rule_file_name = 'rules.txt'
rule_file_name = 'rules_li.txt'
glue_rule_file_name = 'glue_rules.txt'
table = PhraseTable() 
table.load_rules(rule_file_name, glue_rule_file_name)
        
#sentence = ['dier', ',', 'zonghezhili', '.']
#sentence = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#sentence = ['a', 'b', 'c']
#sentence = ['Auzhou', 'shi', 'yu', 'Beihan', 'you', 'bangjiao', 'de', 'shaoshu', 'guojia', 'zhiyi']
sentence = ['']
#i = 0
#j = 1

#chart = [length][length+1]
length = len(sentence)
chart = [None] * length
for i in xrange(length):
    chart[i] = [None] * (length+1)

for l in xrange(1,length+1):
    for i in xrange(0,length-l+1):
        j = i + l
        cell = Cell()
        #cell = find_inferable_items(sentence, i, j, table, chart)
        add_inferable_items(sentence, i, j, table, chart, cell)
        #if cell.is_item_empty() == False:
        #    chart[i][j] = cell

        if i == 0:
            add_glued_items(sentence, i, j, chart, cell)
            #if cell.is_item_empty() == False:
            #    chart[i][j]

        if cell.is_item_empty() == False:
            chart[i][j] = cell
print "chart is :"
for i in xrange(length):
    for j in xrange(length+1):
        if chart[i][j] is not None:
            print 'Cell',
        else: 
            print '[  ]',
    print 
#add_match_rules_to_chart(sentence, i, j) 