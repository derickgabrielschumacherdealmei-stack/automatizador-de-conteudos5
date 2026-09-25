import os


class WanVideo:
    def __init__(self):
        self.nome = "Wan Video"
        self.modelo = "Wan-AI/Wan2.2-T2V-A14B"
        self.permitir_gastos = False

    def disponivel(self):
        return bool(os.getenv("HF_TOKEN"))

    def gerar(self, prompt, arquivo_saida):
        if not self.disponivel():
            return {
                "sucesso": False,
                "status": "SEM_TOKEN",
                "gerador": self.nome
            }

        if not self.permitir_gastos:
            return {
                "sucesso": False,
                "status": "AGUARDANDO_PROVEDOR_GRATUITO",
                "gerador": self.nome,
                "prompt": prompt,
                "arquivo_saida": arquivo_saida
            }

        return {
            "sucesso": False,
            "status": "GASTOS_BLOQUEADOS"
        }
