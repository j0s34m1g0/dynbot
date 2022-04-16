from os import system


def run():
    f = open ('master.txt','r')
    pares = f.readlines()
    f.close()
    for i in pares:
        name = i.replace("\n", "")
        f = open (name + '.py','w')
        f.write('while True:' + '\n' +
                '    ' + 'print("hola mundo")')        
        f.close()    
    f = open ('instancias.py','w')
    for i in pares:
        name = i.replace("\n", "")
        f.write('from os import system' + '\n' +
                'system("cd E:\JOSE_AMIGO\Desktop\dynbot")' + '\n' +
                'system("python ' +  name + '.py")' + '\n')     
    f.close()
    system("cd E:\JOSE_AMIGO\Desktop\dynbot")
    system("instancias.py")   
        
    

if __name__ == '__main__':
    run()