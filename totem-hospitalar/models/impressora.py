#dev 2
class GeradorSenha:
    contador_geral = 0
    contador_prioridade = 0

    @classmethod
    def gerar_geral(cls):
        cls.contador_geral += 1
        return f"G-{cls.contador_geral:03d}"

    @classmethod
    def gerar_prioridade(cls):
        cls.contador_prioridade += 1
        return f"P-{cls.contador_prioridade:03d}"


# Teste rápido
if __name__ == "__main__":
    print(GeradorSenha.gerar_geral())        # G-001
    print(GeradorSenha.gerar_geral())        # G-002
    print(GeradorSenha.gerar_prioridade())   # P-001
