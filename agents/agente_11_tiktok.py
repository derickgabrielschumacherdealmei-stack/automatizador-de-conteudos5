# AGENTE 11 — PUBLICAÇÃO NO TIKTOK

import os


class AgenteTikTok:
    def __init__(self):
        self.nome = "Agente 11 - TikTok"
        self.plataforma = "TikTok"

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
            "formato": "9:16",
            "privacidade": "PUBLIC_TO_EVERYONE",

            "legenda": (
                f"🍓 Novelinha das Frutas | Episódio {episodio} "
                "#novelinha #frutas #historias"
            ),

            "status": "PRONTO_PARA_PUBLICAR"
        }

    def publicar(self, dados):
        token = os.getenv("TIKTOK_TOKEN")

        if not token:
            return {
                "publicado": False,
                "status": "AGUARDANDO_CONEXAO",
                "motivo": (
                    "Configure a integração autorizada do TikTok "
                    "antes da publicação automática."
                )
            }

        # A chamada à API oficial será adicionada
        # quando a integração estiver configurada.

        return {
            "publicado": False,
            "status": "INTEGRACAO_PRONTA_PARA_IMPLEMENTAR"
        }


if __name__ == "__main__":
    agente = AgenteTikTok()

    dados = agente.preparar_publicacao(
        "output/episodio_001.mp4",
        1
    )

    print(dados)
