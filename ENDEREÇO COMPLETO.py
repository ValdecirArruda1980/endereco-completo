def address(rua, numero, complemento, bairro, cep, cidade, estado, pais):
    print("Seu endereço é:","Rua",rua,numero,complemento,"\nBairro:",bairro,"\nCep:",cep,"\nCidade:",cidade,"\nEstado:",estado,"\nPais:",pais)
 
r=input("Rua:")
n=input("Número:")
cp=input("Complemento:")
b=input("Bairro:")
cep=input("Cep:")
c=input("Cidade:")
e=input("Estado:")
p=input("Pais:")
address(r,n,cp,b,cep,c,e,p)
