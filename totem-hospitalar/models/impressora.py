from datetime import datetime
class Impressora:

    def imprimir_ticket(self, nome: str, tipo: str, servico: str, senha: str = None):
        print("\n------------------------------------------")
        if tipo == "Emergência":
            
            print("ALERTA DE EMERGÊNCIA")
            print("------------------------------------------")
            print(f"PACIENTE: {nome}")
            print("STATUS: RISCO IMEDIATO")
            print(">>> ATENÇÃO: Encaminhe-se IMEDIATAMENTE")
            print("ao balcão de triagem médica.")
            print("Não é necessário aguardar senha.")
        else:
            
            print("TICKET DE ATENDIMENTO")
            print("------------------------------------------")
            print(f"PACIENTE: {nome}")
            print(f"TIPO: {tipo}")
            print(f"SERVIÇO: {servico}")
            print(f"SENHA: {senha}")
            print("------------------------------------------")
            print("Aguarde ser chamado no painel central.")
        
        
        print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("------------------------------------------\n")



if __name__ == "__main__":
    impressora = Impressora()
    impressora.imprimir_ticket("Lorrany Marim", "Geral", "Consulta", "G-001")
    impressora.imprimir_ticket("João Guimarães", "PRIORITÁRIO (Lei 10.048)", "Exame", "P-001")
    impressora.imprimir_ticket("Woody Batista", "Emergência", "Exame")