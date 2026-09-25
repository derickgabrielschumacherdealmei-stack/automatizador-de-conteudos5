# AGENTE 09 — SINCRONIZAÇÃO

class AgenteSincronizacao:
    def __init__(self):
        self.nome = "Agente 09 - Sincronização"

    def verificar(self, dialogos, cenas):
        erros = []

        if not dialogos:
            erros.append("Nenhum diálogo encontrado.")

        if not cenas:
            erros.append("Nenhuma cena encontrada.")

        if isinstance(dialogos, dict):
            falas = dialogos.get("dialogos", [])

            for numero, fala in enumerate(falas, start=1):
                personagem = fala.get("personagem")
                texto = fala.get("fala")
                idioma = fala.get("idioma")

                if not personagem:
                    erros.append(
                        f"Fala {numero} sem personagem."
                    )

                if not texto:
                    erros.append(
                        f"{personagem or 'Personagem'} está sem fala."
                    )

                if idioma != "pt-BR":
                    erros.append(
                        f"Idioma incorreto na fala de "
                        f"{personagem or 'personagem desconhecido'}."
                    )

        aprovado = len(erros) == 0

        return {
            "agente": self.nome,
            "aprovado": aprovado,
            "erros": erros,

            "configuracao_video": {
                "idioma": "pt-BR",
                "sincronizacao_labial": True,
                "sincronizar_personagem_com_fala": True,
                "sincronizar_emocao": True,
                "sincronizar_cena": True,
                "formato": "9:16"
            },

            "resultado": (
                "PRONTO PARA GERAR O VÍDEO"
                if aprovado
                else "CORRIGIR ANTES DE GERAR"
            )
        }


if __name__ == "__main__":
    agente = AgenteSincronizacao()

    dialogos = {
        "dialogos": [
            {
                "personagem": "Morango",
                "fala": "Espera... o que está acontecendo aqui?",
                "idioma": "pt-BR",
                "emocao": "surpresa"
            }
        ]
    }

    cenas = [
        {
            "cena": 1,
            "personagens": ["Morango"]
        }
    ]

    print(
        agente.verificar(
            dialogos,
            cenas
        )
    )
