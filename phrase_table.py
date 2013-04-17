class PhraseTable:
    def __init__(self):
        self.rules = dict()
        self.glue_rules = dict()

    def load_rules(self, rule_file_name, glue_rule_file_name):
        rule_file = open(rule_file_name, 'r')
        glue_rule_file = open(glue_rule_file_name, 'r')

        for line in rule_file:
            [lhs, rhs] = line.split(' ||| ')
            self.rules[lhs] = rhs

        for line in glue_rule_file:
            [lhs, rhs] = line.split(' ||| ')
            self.glue_rules[lhs] = rhs

        rule_file.close()
        glue_rule_file.close()

    def get_match_rules(self, key):
        return self.rules[key]

    def get_glue_rules(self, key):
        return self.glue_rules[key]
        