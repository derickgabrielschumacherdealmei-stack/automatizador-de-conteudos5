# AGENTE 13 — PUBLICAÇÃO NO INSTAGRAM REELS

import os


class AgenteInstagram:
    def __init__(self):
        self.nome = "Agente 13 - Instagram Reels"
        self.plataforma = "Instagram"

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

            "legenda": (
                f"🍓 Novelinha das Frutas | Episódio {episodio}\n\n"
                "O que será que vai acontecer agora? 👀\n\n"
                "#novelinha #frutas #reels #historias"
            ),

            "configuracao": {
                "tipo": "REELS",
                "formato": "9:16",
                "idioma": "pt-BR"
            },

            "status": "PRONTO_PARA_PUBLICAR"
        }

    def publicar(self, dados):
        token = os.getenv("INSTAGRAM_TOKEN")

        if not token:
            return {
                "publicado": False,
                "status": "AGUARDANDO_CONEXAO",
                "motivo": (
                    "A conta do Instagram precisa estar "
                    "conectada antes da publicação automática."
                )
            }

        # A integração autorizada será adicionada depois.

        return {
            "publicado": False,
            "status": "INTEGRACAO_PRONTA_PARA_IMPLEMENTAR"
        }


if __name__ == "__main__":
    agente = AgenteInstagram()

    dados = agente.preparar_publicacao(
        "output/episodio_001.mp4",
        1
    )

    print(dados)
