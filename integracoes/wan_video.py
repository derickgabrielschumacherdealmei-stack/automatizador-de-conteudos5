import os


class WanVideo:
    def __init__(self):
        self.nome = "Wan Video"
        self.modelo = "Wan-AI/Wan2.2-T2V-A14B"
        self.permitir_gastos = False

    def disponivel(self):
        return bool(os.getenv("HF_TOKEN"))

    def testar_conexao(self):
        if not self.disponivel():
            return {
                "sucesso": False,
                "status": "SEM_TOKEN"
            }

        return {
            "sucesso": True,
            "status": "HF_TOKEN_OK",
            "gerador": self.nome,
            "modelo": self.modelo,
            "gastos_permitidos": False
        }

    def gerar(self, prompt, arquivo_saida):
        # Segurança: ainda não chama nenhum serviço que possa cobrar.
        if not self.disponivel():
            return {
                "sucesso": False,
                "status": "SEM_TOKEN",
                "gerador": self.nome
            }

        return {
            "sucesso": False,
            "status": "GERACAO_BLOQUEADA_ATE_CONFIRMAR_PROVEDOR_GRATUITO",
            "gerador": self.nome,
            "prompt": prompt,
            "arquivo_saida": arquivo_saida,
            "gastos_permitidos": False
        }
