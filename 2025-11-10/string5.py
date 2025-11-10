
from configparser import InterpolationSyntaxError


strtexto   =   input('Digite o seu nome:')

intpos   =   1

while intpos <= len (strtexto):
    
    print(strtexto[:intpos])
    intpos  +=1