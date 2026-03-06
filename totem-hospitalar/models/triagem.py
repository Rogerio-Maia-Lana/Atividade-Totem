#dev 1
class Triagem:
    OPCAO_EMERGENCIA = 3

    def verificar_emergencia(self, opcao_menu, paciente):
      return opcao_menu == self.OPCAO_EMERGENCIA


    def mostrar_alerta(self, paciente):
        print("\n------------------------------------------")
        print("ALERTA DE EMERGÊNCIA")
        print("------------------------------------------")
        print(f"PACIENTE: {paciente.nome}")
        print("STATUS: RISCO IMEDIATO")
        print(">>> ATENÇÃO: Encaminhe-se IMEDIATAMENTE")
        print("ao balcão de triagem médica.")
        print("Não é necessário aguardar senha.")
        print("------------------------------------------")