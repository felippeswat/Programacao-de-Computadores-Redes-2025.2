strTexto   =   input('Digite Algo:')

if ' ' in strTexto:
    palavras        =       strTexto.split()
    
for palavra in palavras:
    print(palavra)