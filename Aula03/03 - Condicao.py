# Esse codigo apesar de rodar corretamente
# nao deveria ser incentivado ao uso
# pois aumenta a complexidade de gestao dos "TAB"
idade =  66

if idade < 16:
    print("nao pode votar")
else:
    if idade < 18:
        print("Pode votar - opcional")
    else:
        if idade < 65:
            print("Deve votar - obrigatorio")
        else:
           print("Pode votar - opcional")
        print("asasd")