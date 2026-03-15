# casl: a programming language.
# current version: alpha-2.0
# update name: misty mountains (doesnt mean anything just copying ubuntu's style lol)
# Cool And Simple Language. pronounced: castle
import json
class casl:

    def __init__(self, program):
        self.program = program # where your probably crappy code goes
        self.abstract_syntax_tree = [
            #{"function": "print", "arguments": [{"value": "Hello world!", "datatype": "string"}]} structure of an ast, here for reference

        ] # the program but in an ast
        self.inside_delimiters = False
        self.parser_buffer = ""
        self.object_space = {} # where all the variables get stored
        self.line = None # self explanatory
        self.col = None # also self explanatory
        self.standard_library_config = { # all the functions configuration!
            "print": [
                "any" # the structure of every function: the name of the function and a list of all the arguments with its datatype.
            ]
        }
        self.standard_library_functions = {
            """
            you may be wondering where the code of the actual functions are. those are in a seperate file named
            standard_library_functions.json. 
            """
        }

    def mixin(self): # loads the aforementioned std function code. dont ask why its not part of __init__. readability...?
        with open('standard_library_functions.json', 'r') as file:
            self.standard_library_functions = json.load(file)

    def parser(self):
        self.line = None
        for self.line in self.program:
            # below is code that resets and initilazes everutjong
            function = self.line.split()[0]
            arguments = []
            arguments_formatted = []
            self.parser_buffer = ""
            length = len(self.line.replace(function, ""))
            i = 0
            for self.col in self.line.replace(function, ""):
                self.parser_buffer += self.col
                if self.col == '"':
                    self.inside_delimiters = not self.inside_delimiters
                if self.col == "," and not self.inside_delimiters:
                    arguments.append((self.parser_buffer).replace(",", ""))
                    self.parser_buffer = ""
                if self.parser_buffer != "" and i == length - 1:
                    arguments.append(self.parser_buffer)
                    self.parser_buffer = ""
                # the above if statement is some very much patch-up work to fix the issue of the last argument not being parsed

                i += 1
            # turn our raw arguments into a suitable format for the ast
            for argument in arguments:
                arguments_formatted.append(
                    {"value": argument, "datatype": None} # none is the placeholder for the datatype. read the Known Issues section in CHANGELOG.md for more info
                )
            # now we push our output into the ast
            self.abstract_syntax_tree.append(
                {"function": function, "arguments": arguments_formatted}
            )
                
    def evaluator(self):
        self.line = None
        for self.line in self.abstract_syntax_tree:
            exec(self.standard_library_functions[self.line["function"]], {"self": self}) # ugliest line in the entire program

