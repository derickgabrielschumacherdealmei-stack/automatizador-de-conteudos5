# AGENTE 10 — PREPARAÇÃO E EXPORTAÇÃO DO VÍDEO

import os


class AgenteVideo:
    def __init__(self):
        self.nome = "Agente 10 - Vídeo"

    def preparar(self, episodio, aprovacao_sincronizacao):
        if not aprovacao_sincronizacao:
            return {
                "aprovado": False,
                "erro": "O Agente 09 não aprovou o conteúdo."
            }

        numero = episodio.get("episodio", 1)

        nome_arquivo = f"episodio_{numero:03}.mp4"
        caminho = os.path.join("output", nome_arquivo)

        configuracao = {
            "resolucao": "1080x1920",
            "proporcao": "9:16",
            "formato": "mp4",
            "idioma": "pt-BR",
            "legendas": True,
            "sincronizacao_labial": True,
            "qualidade": "alta",
            "fps": 30
        }

        return {
            "agente": self.nome,
            "aprovado": True,
            "episodio": numero,
            "arquivo_final": caminho,
            "configuracao": configuracao,

            "instrucoes": [
                "Gerar todas as cenas na ordem correta.",
                "Usar somente o roteiro aprovado.",
                "Manter os personagens consistentes.",
                "Usar as falas aprovadas.",
                "Sincronizar boca e voz.",
                "Adicionar legendas em português.",
                "Manter formato vertical 9:16.",
                "Exportar somente depois das verificações."
            ],

            "status": "PRONTO PARA GERADOR DE VÍDEO"
        }


if __name__ == "__main__":
    agente = AgenteVideo()

    episodio = {
        "episodio": 1
    }

    resultado = agente.preparar(
        episodio,
        aprovacao_sincronizacao=True
    )

    print(resultado)
