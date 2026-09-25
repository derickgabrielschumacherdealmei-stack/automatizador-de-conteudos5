class GeradorReserva:
    def __init__(self):
        self.nome = "Gerador Reserva"
        self.ativo = False
        self.permitir_gastos = False

    def disponivel(self):
        return self.ativo

    def gerar(self, prompt, arquivo_saida):
        if not self.ativo:
            return {
                "sucesso": False,
                "status": "INDISPONIVEL",
                "gerador": self.nome,
                "motivo": "Nenhum provedor gratuito configurado."
            }

        if not self.permitir_gastos:
            return {
                "sucesso": False,
                "status": "SOMENTE_GRATUITO",
                "gerador": self.nome
            }

        return {
            "sucesso": False,
            "status": "NAO_CONFIGURADO"
        }
