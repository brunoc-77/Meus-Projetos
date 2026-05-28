print("--------------------------------------------")
print("1 - Adicionar notas ")
print("2 - Ver Maior nota ")


notas = []

def addnotas():
    for i in range(1,11):
        nota = input(f"Digite a {i}° nota: ")
        notas.append(nota)

def maiornota():
    maiorn = max(notas)
    print(f"A maior nota é {maiorn}")

escolha = int(input("Escolha uma opção: "))

while True:
    if escolha == 1:
        addnotas()
    elif escolha == 2:
        maiornota()
        if not notas:
            print("Não há notas!!!")
            break

    