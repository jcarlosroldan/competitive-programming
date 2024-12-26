from xmlrpc.client import ServerProxy

sp = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(sp.system.listMethods())
print(sp.system.methodHelp('phone'))
print(sp.phone('Bert'))
print(sp.phone('555'))