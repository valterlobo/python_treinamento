from Contato import Contato
import json
from collections import namedtuple

contato =  Contato(nome="Ana" , email="ana@mail.com")




contatoValter =  Contato(nome="Valter" , email="ana@mail.com")


print ( contato.nome )

print ( contatoValter.nome )



data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
print x.name, x.hometown.name, x.hometown.id

data_contato = '{ "email":"ana@mail.com", "nome":"Valter Lobo" }'
contato_json = json.loads(data_contato, object_hook=lambda d: namedtuple('Contato', d.keys())(*d.values()))

print ( contato_json.nome )



