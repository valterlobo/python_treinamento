# Human teste teste de include ou import 
from modelo.Human import Human

 # Instantiate a class
humano = Human(name="Ian")

print (humano.say("hi") ) # prints out "Ian: hi"
humano.age = 28

print ('Nome: ' + str(humano.name) )
print ('Age: ' +  str(humano.age) )

print ('Especie:' + Human.species) 

print ('Grunt:' + Human.grunt()) 