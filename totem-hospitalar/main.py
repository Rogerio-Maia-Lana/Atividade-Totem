from models.menu import Menu
from models.paciente import Paciente
from models.classificador import Classificador
from models.triagem import Triagem
from models.gerador_senha import GeradorSenha
from models.impressora import Impressora


SERVICOS = {
    "1": "Consulta",
    "2": "Exame",
    "3": "Emergência",
}


def coletar_dados_do_menu():
    """Coleta os dados do menu e repete até receber valores válidos."""
    menu = Menu()

    while True:
        try:
            dados = menu.exibir_menu()

            nome = str(dados.get("nome", "")).strip()
            idade = int(dados.get("idade", 0))
            deficiencia = str(dados.get("deficiencia", "")).strip().upper()
            opcao = str(dados.get("opcao", "")).strip()

            if not nome:
                raise ValueError("O nome não pode ficar vazio.")

            if idade < 0:
                raise ValueError("A idade não pode ser negativa.")

            if deficiencia not in ("S", "N"):
                raise ValueError("Digite apenas S ou N para deficiência.")

            if opcao not in SERVICOS:
                raise ValueError("Escolha apenas 1, 2 ou 3 no menu.")

            return {
                "nome": nome,
                "idade": idade,
                "deficiencia": deficiencia,
                "opcao": opcao,
            }
        except ValueError as erro:
            print(f"[ERRO] {erro}")
            print("Por favor, tente novamente.")


def criar_paciente(dados):
    return Paciente(
        nome=dados["nome"],
        idade=dados["idade"],
        pcd=dados["deficiencia"],
    )


def processar_atendimento(paciente, opcao):
    triagem = Triagem()
    classificador = Classificador()
    impressora = Impressora()

    opcao_int = int(opcao)
    servico = SERVICOS[opcao]

    if triagem.verificar_emergencia(opcao_int, paciente):
        impressora.imprimir_ticket(
            nome=paciente.nome,
            tipo="Emergência",
            servico=servico,
        )
        return

    tipo_classificacao = classificador.classificar(paciente)

    if tipo_classificacao == "PRIORITARIO":
        tipo_ticket = "PRIORITÁRIO (Lei 10.048)"
        senha = GeradorSenha.gerar_prioridade()
    else:
        tipo_ticket = "Geral"
        senha = GeradorSenha.gerar_geral()

    impressora.imprimir_ticket(
        nome=paciente.nome,
        tipo=tipo_ticket,
        servico=servico,
        senha=senha,
    )


def perguntar_novo_atendimento():
    while True:
        resposta = input("Deseja iniciar um novo atendimento? (S/N): ").strip().upper()
        if resposta in ("S", "N"):
            return resposta == "S"
        print("Digite apenas S para sim ou N para não.")


def main():
    print("Iniciando sistema do Totem Hospitalar...")

    while True:
        dados = coletar_dados_do_menu()
        paciente = criar_paciente(dados)
        processar_atendimento(paciente, dados["opcao"])

        if not perguntar_novo_atendimento():
            print("Sistema encerrado. Obrigado por utilizar o Totem Hospitalar Viver Bem.")
            break

        print("" + "=" * 42 + "")


if __name__ == "__main__":
    main()