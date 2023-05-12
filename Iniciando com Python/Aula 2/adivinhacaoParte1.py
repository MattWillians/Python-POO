#A ideia do nosso jogo é termos que acertar um número secreto. 
# Quando o programa estiver rodando, teremos que digitar um número e o programa dirá se acertamos ou erramos o número, com várias tentativas e níveis.

print("+----------------------------------------+")
print("| Bem vindo ao nosso jogo de adivinhação |")
print("+----------------------------------------+\n")

numero_para_adivinhar = 42
chute = int(input("Digite o seu numero: "))

if (numero_para_adivinhar == chute):
    print("Acertou o numero!\n")
else:
    print("Este numero esta errado.\n")

print("Fim de jogo!")