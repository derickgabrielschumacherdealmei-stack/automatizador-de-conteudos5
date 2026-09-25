# AGENTE 12 — PUBLICAÇÃO NO YOUTUBE SHORTS

import os


class AgenteYouTube:
    def __init__(self):
        self.nome = "Agente 12 - YouTube Shorts"
        self.plataforma = "YouTube"

    def preparar_publicacao(self, video, episodio):
        if not video:
            return {
                "aprovado": False,
                "erro": "Vídeo não encontrado."
            }

        return {
            "agente": self.nome,
            "plataforma": self.plataforma,
            "video": video,
            "episodio": episodio,

            "titulo": (
                f"Novelinha das Frutas 🍓 | "
                f"Episódio {episodio} #Shorts"
            ),

            "descricao": (
                "🍓 Mais um episódio da Novelinha das Frutas!\n\n"
                "#Shorts #Novelinha #Frutas #Historia"
            ),

            "configuracao": {
                "formato": "9:16",
                "tipo": "Shorts",
                "idioma": "pt-BR"
            },

            "status": "PRONTO_PARA_PUBLICAR"
        }

    def publicar(self, dados):
        token = os.getenv("YOUTUBE_TOKEN")

        if not token:
            return {
                "publicado": False,
                "status": "AGUARDANDO_CONEXAO",
                "motivo": (
                    "A conta do YouTube precisa estar "
                    "conectada antes da publicação."
                )
            }

        # A integração oficial será conectada depois.

        return {
            "publicado": False,
            "status": "INTEGRACAO_PRONTA_PARA_IMPLEMENTAR"
        }


if __name__ == "__main__":
    agente = AgenteYouTube()

    dados = agente.preparar_publicacao(
        "output/episodio_001.mp4",
        1
    )

    print(dados)
