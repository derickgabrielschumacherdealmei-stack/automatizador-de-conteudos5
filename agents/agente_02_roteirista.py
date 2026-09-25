# AGENTE 02 — ROTEIRISTA

class AgenteRoteirista:
    def __init__(self):
        self.nome = "Agente 02 - Roteirista"

    def criar_roteiro(self, tendencias, memoria):
        episodio = memoria.get("episodio_atual", 1)
        resumo_anterior = memoria.get(
            "resumo_anterior",
            "Primeiro episódio da novela."
        )

        roteiro = {
            "episodio": episodio,
            "idioma": "pt-BR",
            "formato": "vertical 9:16",

            "continuidade": resumo_anterior,

            "estrutura": {
                "inicio": "Gancho forte nos primeiros segundos.",
                "desenvolvimento": (
                    "Conflito claro entre os personagens."
                ),
                "reviravolta": (
                    "Adicionar uma surpresa que faça sentido."
                ),
                "final": (
                    "Terminar com suspense para o próximo episódio."
                )
            },

            "regras": [
                "Continuar exatamente a novela atual.",
                "Não começar outra história antes desta terminar.",
                "Manter personalidade e aparência dos personagens.",
                "Todas as falas devem ser em português brasileiro.",
                "Evitar cenas desconectadas.",
                "Não copiar histórias de outros criadores.",
                "Criar uma história original inspirada nas tendências."
            ],

            "tendencias_recebidas": tendencias
        }

        return roteiro


if __name__ == "__main__":
    agente = AgenteRoteirista()

    teste = agente.criar_roteiro(
        tendencias={"tema": "novelinha de frutas"},
        memoria={
            "episodio_atual": 1,
            "resumo_anterior": "Início da história."
        }
    )

    print(teste)
