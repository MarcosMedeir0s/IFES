import json

class Professor:
    def __init__(self):
        self.notas = {}

    def carregar_notas(self):
        try:
            with open('notas.json', 'r') as file:
                self.notas = json.load(file)
        except FileNotFoundError:
            self.notas = {}

    def salvar_notas(self):
        with open('notas.json', 'w') as file:
            json.dump(self.notas, file, indent=4)

    def adicionar_nota(self, id_aluno, nota):
        if nota > 100:
            return "Nota não pode ser maior que 100."
        self.notas[id_aluno] = nota
        self.salvar_notas()
        return "Nota adicionada com sucesso!"

    def excluir_nota(self, id_aluno):
        if id_aluno in self.notas:
            del self.notas[id_aluno]
            self.salvar_notas()
            return "Nota excluída com sucesso!"
        return "Aluno não encontrado."

    def buscar_notas(self, id_aluno):
        if id_aluno in self.notas:
            return f"Nota do aluno {id_aluno}: {self.notas[id_aluno]}"
        return "Aluno não encontrado."

def professor_menu():
    prof = Professor()
    prof.carregar_notas()
    while True:
        opcao = input("1- ADICIONAR NOTA\n2- EXCLUIR NOTA\n3- BUSCAR NOTA\n4- SAIR\nSELECIONE A OPÇÃO: ")
        if opcao == '1':
            print()
            id_aluno = input("Digite o ID do aluno: ")
            nota = float(input("Digite a nota do aluno: "))
            print(prof.adicionar_nota(id_aluno, nota))
        elif opcao == '2':
            print()
            id_aluno = input("Digite o ID do aluno para excluir a nota: ")
            print(prof.excluir_nota(id_aluno))
        elif opcao == '3':
            print()
            id_aluno = input("Digite o ID do aluno para buscar a nota: ")
            print(prof.buscar_notas(id_aluno))
        elif opcao == '4':
            break
