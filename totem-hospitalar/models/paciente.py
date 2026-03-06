#dev 1
class Classificador:
    
    IDADE_PRIORIDADE = 60
    PCD_SIM = "S"

    def classificar(self, paciente):
       

        if self._eh_prioritario(paciente):
            return "PRIORITARIO"

        return "GERAL"

    def _eh_prioritario(self, paciente):
       

        idade_prioritaria = paciente.idade >= self.IDADE_PRIORIDADE
        possui_deficiencia = paciente.pcd.upper() == self.PCD_SIM

        return idade_prioritaria or possui_deficiencia