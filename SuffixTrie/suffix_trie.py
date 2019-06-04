class SuffixTrie:
    def __init__(self, inp):
        self.rep = {}
        for i in range(len(inp)-1):
            c_dict = self.rep
            for c in inp[i:]:
                if c not in c_dict:
                    c_dict[c] = {}
                c_dict = c_dict[c]
            c_dict["*"] = True

    def __str__(self):
        str_val = str(self.rep)
        out = ""
        indent = 0
        indent_char = "  "
        for i in range(len(str_val)):
            if str_val[i:i+4] == "{'*'":
                out += str_val[i]
            elif str_val[i] == "{":
                indent += 1
                out += str_val[i] + "\n" + indent_char * indent
            elif str_val[i-1:i+1] == "},":
                out += str_val[i] + "\n" + indent_char * indent
            elif str_val[i-2:i+1] == "}, ":
                pass
            elif str_val[i-1:i+1] == "}}":
                indent -= 1
                out += "\n" + indent_char * indent + str_val[i]
            else:
                out += str_val[i]
        return out

    def contains(self, inp):
        c_dict = self.rep
        for c in inp:
            if c in c_dict:
                c_dict = c_dict[c]
            else:
                return False
        if "*" in c_dict:
            return True
        return False