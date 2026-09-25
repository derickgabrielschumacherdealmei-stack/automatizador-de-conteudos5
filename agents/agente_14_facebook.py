# AGENTE 14 — PUBLICAÇÃO NO FACEBOOK REELS

import os


class AgenteFacebook:
    def __init__(self):
        self.nome = "Agente 14 - Facebook Reels"
        self.plataforma = "Facebook"

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
                "A história continua... 👀\n\n"
                "#Novelinha #Frutas #Reels #Historias"
            ),

            "configuracao": {
                "tipo": "REELS",
                "formato": "9:16",
                "idioma": "pt-BR"
            },

            "status": "PRONTO_PARA_PUBLICAR"
        }

    def publicar(self, dados):
        token = os.getenv("FACEBOOK_TOKEN")

        if not token:
            return {
                "publicado": False,
                "status": "AGUARDANDO_CONEXAO",
                "motivo": (
                    "A conta do Facebook precisa estar "
                    "conectada antes da publicação automática."
                )
            }

        # A integração autorizada será adicionada depois.

        return {
            "publicado": False,
            "status": "INTEGRACAO_PRONTA_PARA_IMPLEMENTAR"
        }


if __name__ == "__main__":
    agente = AgenteFacebook()

    dados = agente.preparar_publicacao(
        "output/episodio_001.mp4",
        1
    )

    print(dados)
