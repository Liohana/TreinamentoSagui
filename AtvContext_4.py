#1: Habituação:

habituacao = input("O animal está habituado?")

if habituacao == "sim":
    habitat = habituacao
else:
    print("O animal precisa se habituar ao ambiente.")

#2: Regime de aproximações sucessivas:

posicao = 30 #(cm)
if posicao < 30:
    print("Liberar 0,5 ml de rec.")

toques = input("Quantas vezes o animal tocou na barra?")
if toques >= 20:
    print("O animal está habituado para a proxima etapa.")

som = input("Qual som foi ativado?")
toque = input("Qual lado o animal tocou?")

if som == "som1" and toque == "esquerda":
    print("Liberar 0,5 ml de rec.")
else:
    print("Não liberar nada.")


if som == "som2" and toque == "direita":
    print("Liberar 0,5 ml de rec.")
else:
    print("Não liberar nada.")


tempo = input("Em quanto tempo o experimento foi realizado? (em min)")
n = input("Quantas vezes o experimento foi realizado?")

if tempo >= 30 and n >= 50:
    print("O seguimento seguira para próxima fase.")
else:
    print("O experimento segue na fase de regime de aproximações sucessivas")
