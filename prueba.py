import shlex 


#print(join(['echo', '-n', 'Multiple words']))


a = shlex.split('Multiple words')
print(a)

aa = ' pruebaFOUND '
if "FOUND" in aa.strip():
    print("Se ha encontrado la cadena")

