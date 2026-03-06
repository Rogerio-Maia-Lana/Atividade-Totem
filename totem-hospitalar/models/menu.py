class Menu:

    def exibir_menu(self):
        print("==========================================")
        print("HOSPITAL VIVER BEM - AUTOATENDIMENTO")
        print("==========================================\n")

        # Cadastro do paciente
        print("[CADASTRO DE PACIENTE]")
        nome = input("Nome: ")
        idade = input("Idade: ")
        deficiencia = input("Possui deficiência? (S/N): ").upper()

        # Menu de serviços
        print("\n[MENU DE SERVIÇOS]")
        print("1. Consulta")
        print("2. Exame")
        print("3. Emergência")

        opcao = input("Escolha a opção: ")

        # Apenas retorna os dados coletados
        return {
            "nome": nome,
            "idade": int(idade),
            "deficiencia": deficiencia,
            "opcao": opcao
        }
if __name__ == "__main__":
    menu = Menu()
    
    