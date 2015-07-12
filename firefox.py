
from dragonfly import (Grammar, AppContext, MappingRule, Key)
from dragonfly.actions.action_mouse import Mouse

#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

grammar_context = AppContext(executable="firefox")
grammar = Grammar("firefox_example", context=grammar_context)


#---------------------------------------------------------------------------
# Create a mapping rule which maps things you can say to actions.
#
# Note the relationship between the *mapping* and *extras* keyword
#  arguments.  The extras is a list of Dragonfly elements which are
#  available to be used in the specs of the mapping.  In this example
#  the Dictation("text")* extra makes it possible to use "<text>"
#  within a mapping spec and "%(text)s" within the associated action.

example_rule = MappingRule(
    name="example",    # The name of the rule.
    mapping={          # The mapping dict: spec -> action.
             "save [file]":            Key("c-s"),
             "save [file] as":         Key("a-f, a"),
             #"save [file] as <text>":  Key("a-f, a/20") + Text("%(text)s"),
             #"find <text>":            Key("c-f/20") + Text("%(text)s\n"),
             "start is":               Key("c-a"),
             "start now":                  Key("c-o"),
             "a":             Key("a"),
             "b":             Key("b"),
             "c":             Key("c"),
             "dog":           Key("d"),
             "e":             Key("e"),
             "f":             Key("f"),
             "g":             Key("g"),
             "h":             Key("h"),
             "i":             Key("i"),
             "j":             Key("j"),
             "kite":          Key("k"),
             "lion":          Key("l"),
             "m":             Key("m"),
             "n":             Key("n"),
             "o":             Key("o"),
             "principle":     Key("p"),
             "q":             Key("q"),
             "rocket":        Key("r"),
             "s":             Key("s"),
             "tiger":         Key("t"),
             "umbrela":       Key("u"),
             "vita":          Key("v"),
             "w":             Key("w"),
             "x-mas":         Key("x"),
             "y":             Key("y"),
             "z":             Key("z"),
             "Full stop":           Key("dot"),
             "at":            Key("at"),
             "send mail section":        Key("home") + Key("space") + Key("space") + Key("space"),
             "Listen mail section":      Key("home") + Key("space") + Key("space"),
             "Listen mail":              Mouse("(0.2, 0.4), left"),
             "Help Section":     Key("end"),
             "send mail":        Mouse("(0.4, 0.17), left"),
             "Play":             Mouse("(0.05, 0.4), left"),
             "Go to top":             Key("end") + Mouse("(0.95, 0.89), left"),
             "Go back":          Mouse("(0.4, 0.4), left"),
             "Back to website":  Mouse("(0.5, 0.67), left"),
            },
    extras=[           # Special elements in the specs of the mapping.
          #Dictation("text"),
           ],
    )

# Add the action rule to the grammar instance.
grammar.add_rule(example_rule)


#---------------------------------------------------------------------------
# Load the grammar instance and define how to unload it.

grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None