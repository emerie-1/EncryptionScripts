from encrypt import Cypher



message = "let there be light"

code_in = Cypher(4)

code = code_in.cypher(message)
print(code)
decode = code_in.decypher(code)
print(decode)