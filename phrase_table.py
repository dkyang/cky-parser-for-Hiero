class PhraseTable:
    def __init__(self):
        self.rules = dict()
        self.glue_rules = dict()

    # not robust enough
    def load_rules(self, rule_file_name, glue_rule_file_name):
        rule_file = open(rule_file_name, 'r')
        glue_rule_file = open(glue_rule_file_name, 'r')

        for line in rule_file:
            line = line[:len(line)-1]
            [lhs, rhs] = line.split(' ||| ')
            if self.rules.get(lhs) is None:
                self.rules[lhs] = []
                self.rules[lhs].append(rhs)
            else:
                self.rules[lhs].append(rhs)

        for line in glue_rule_file:
            line = line[:len(line)-1]
            [lhs, rhs] = line.split(' ||| ')
            if self.rules.get(lhs) is None:
                self.glue_rules[lhs] = []
                self.glue_rules[lhs].append(rhs)
            else:
                self.glue_rules[lhs].append(rhs)
                
        rule_file.close()
        glue_rule_file.close()

    def get_match_rules(self, key):
        #return self.rules[key]
        return self.rules.get(key)

    def get_glue_rules(self, key):
        #return self.glue_rules[key]
        return self.glue_rules.get(key)
        