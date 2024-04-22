import json

class Aluno:
    def __init__(self, id_aluno, nome):
        self._id_aluno = id_aluno
        self._nome = nome

    @property
    def id_aluno(self):
        return self._id_aluno

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def to_dict(self):
        return {"id_aluno": self._id_aluno, "nome": self._nome}

class Administrador:
    def __init__(self):
        self.alunos = []

    def carregar_alunos(self):
        try:
            with open('alunos.json', 'r') as file:
                alunos_data = json.load(file)
                self.alunos = [Aluno(**dados) for dados in alunos_data]
        except FileNotFoundError:
            self.alunos = []

    def salvar_alunos(self):
        with open('alunos.json', 'w') as file:
            json.dump([aluno.to_dict() for aluno in self.alunos], file, indent=4)

    def adicionar_aluno(self, id_aluno, nome):
        novo_aluno = Aluno(id_aluno, nome)
        self.alunos.append(novo_aluno)
        self.salvar_alunos()
        return f"Aluno {nome} adicionado com sucesso!"

    def excluir_aluno(self, id_aluno):
        aluno = next((a for a in self.alunos if a.id_aluno == id_aluno), None)
        if aluno:
            self.alunos.remove(aluno)
            self.salvar_alunos()
            return f"Aluno excluído com sucesso!"
        return "Aluno não encontrado."

    def buscar_aluno(self, id_aluno):
        aluno = next((a for a in self.alunos if a.id_aluno == id_aluno), None)
        if aluno:
            return aluno
        return f"Aluno {id_aluno} não encontrado."

def adm_menu():
    admin = Administrador()
    admin.carregar_alunos()
    while True:
        opcao = input("1- ADICIONAR ALUNO\n2- EXCLUIR ALUNO\n3- BUSCAR ALUNO\n4- SAIR\nSELECIONE A OPÇÃO: ")
        if opcao == '1':
            print()
            id_aluno = input("Digite o ID do aluno: ")
            nome = input("Digite o nome do aluno: ")
            print(admin.adicionar_aluno(id_aluno, nome))
        elif opcao == '2':
            print()
            id_aluno = input("Digite o ID do aluno para excluir: ")
            print(admin.excluir_aluno(id_aluno))
        elif opcao == '3':
            print()
            id_aluno = input("Digite o ID do aluno para pesquisar: ")
            aluno = admin.buscar_aluno(id_aluno)
            if isinstance(aluno, Aluno):
                print(f"ID: {aluno.id_aluno}, Nome: {aluno.nome}")
            else:
                print(aluno)
        elif opcao == '4':
            break
