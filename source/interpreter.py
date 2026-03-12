# casl: a programming language.
# current version: alpha-1.0
# Cool And Simple Language. pronounced: castle
import json
class casl:

    def __init__(self, program):
        self.program = program # where your probably crappy code goes
        self.abstract_syntax_tree = [
            {"function": "print", "printArgument": "Hello World"} # for now this is hardcoded for testing purposes
        ] # the program but in an ast
        self.tokenized_program = [] # the program but tokenized
        self.object_space = {} # where all the variables get stored
        self.line = 1 # self explanatory
        self.standard_library_config = { # all the functions configuration!
            "print": [
                {"datatype": "any", "name": "printArgument"} # the structure of every function
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
        pass

    def evaluator(self):
        for self.line in self.abstract_syntax_tree:
            exec(self.standard_library_functions[self.line["function"]], {"self": self}) # ugliest line in the entire program

