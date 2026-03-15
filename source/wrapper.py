import interpreter
casl = interpreter.casl([
    'print "Hello, world!"'
    ])
casl.mixin()
casl.parser()
casl.evaluator()
