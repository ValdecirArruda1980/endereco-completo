def address(rua, numero, complemento, bairro, cep, cidade, estado, pais):
    print("Seu endereço é:")
    print("Rua:", rua, numero, complemento)
    print("Bairro:", bairro)
    print("CEP:", cep)
    print("Cidade:", cidade)
    print("Estado:", estado)
    print("País:", pais)

# Coletando os dados do usuário
rua = input("Rua: ")
numero = input("Número: ")
complemento = input("Complemento: ")
bairro = input("Bairro: ")
cep = input("CEP: ")
cidade = input("Cidade: ")
estado = input("Estado: ")
pais = input("País: ")

# Chamando a função
address(rua, numero, complemento, bairro, cep, cidade, estado, pais)

