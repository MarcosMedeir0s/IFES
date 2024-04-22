import json
import adm
import professor
import aluno

def main():
    while True:
        tipo_usuario = input('----- USUÁRIOS -----\n1- ADMINISTRADOR\n2- PROFESSOR\n3- ALUNO\n4- SAIR \nSELECIONE O PERFIL: ').lower()
        if tipo_usuario == '1':
            print()
            print('PERFIL DE ADMINISTRADOR')
            adm.adm_menu()
        elif tipo_usuario == '2':
            print()
            print('PAINEL DO PROFESSOR')
            professor.professor_menu()
        elif tipo_usuario == '3':
            print()
            print("PAINEL DO ALUNO")
            aluno.aluno_menu()
        elif tipo_usuario == '4':
            print("ENCERRANDO O PROCESSO")
            break
        else:
            print("Tipo de usuário inválido. Tente novamente.")

if __name__ == "__main__":
    main()
