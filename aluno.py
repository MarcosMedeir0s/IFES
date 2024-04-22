import json

def carregar_notas():
    try:
        with open('notas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def aluno_menu():
    notas = carregar_notas()
    while True:
        opcao = input("1- CONSULTAR NOTA\n2- SAIR\nSELECIONE A OPÇÃO: ")
        if opcao == '1':
            print()
            id_aluno = input("Digite seu ID de aluno: ")
            if id_aluno in notas:
                print(f"Sua nota é: {notas[id_aluno]}")
            else:
                print("Nota não encontrada ou você ainda não possui notas.")
        elif opcao == '2':
            break
