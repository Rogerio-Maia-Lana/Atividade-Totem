class Paciente:
    
    def __init__(self, nome, idade, pcd):
        self.nome = nome
        self.idade = idade
        self.pcd = pcd

    def exibir_dados(self):
        print("\n[CADASTRO DE PACIENTE]")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Possui deficiência: {self.pcd}")