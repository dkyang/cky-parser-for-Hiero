def add_match_rules_to_chart(sentence, i, j):
    for i1 in xrange(i,j+1):
        key = ''
        if i < i1:
            key += ' '.join(sentence[i:i1])
        if i1 == j:
            print key
        else:
            for j1 in xrange(i1+1,j+1):
                key1 = key
                if i1 == i:
                    key1 += 'X'
                elif i1 < j:
                    key1 += ' X'

                if j1 == j:
                    print key1
                else:
                    for i2 in xrange(j1+1,j+1):
                        key2 = key1
                        key2 += ' '
                        key2 += ' '.join(sentence[j1:i2])
                        if i2 == j:
                            print key2
                        else: 
                            # j2 <= j
                            for j2 in xrange(i2+1,j+1):
                                key3 = key2
                                key3 += ' X'
                                if j2 == j:
                                    print key3
                                else:
                                    # j2 < j
                                    key3 += ' '
                                    key3 += ' '.join(sentence[j2:j])
                                    print key3
        
#sentence = ['dier', ',', 'zonghezhili', '.']
sentence = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

i = 0
j = len(sentence)
#for    
add_match_rules_to_chart(sentence, i, j) 