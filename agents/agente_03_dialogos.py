# AGENTE 03 — DIÁLOGOS

class AgenteDialogos:
    def __init__(self):
        self.nome = "Agente 03 - Diálogos"

    def criar_dialogos(self, roteiro, personagens):
        dialogos = []

        for personagem in personagens:
            dialogos.append({
                "personagem": personagem["nome"],
                "fala": "",
                "idioma": "pt-BR",
                "emocao": "neutra",
                "tom_de_voz": personagem.get(
                    "voz", "natural"
                ),
                "sincronizar_boca": True
            })

        resultado = {
            "episodio": roteiro.get("episodio"),
            "dialogos": dialogos,

            "instrucoes": [
                "Criar falas naturais em português brasileiro.",
                "Deixar explícito qual personagem diz cada fala.",
                "Respeitar a personalidade de cada personagem.",
                "Usar falas curtas para vídeos rápidos.",
                "Não trocar as falas entre personagens.",
                "Indicar a emoção de cada fala.",
                "Manter continuidade com o roteiro.",
                "Preparar as falas para sincronização labial."
            ]
        }

        return resultado


if __name__ == "__main__":
    agente = AgenteDialogos()

    personagens = [
        {
            "nome": "Morango",
            "voz": "jovem e expressiva"
        },
        {
            "nome": "Abacaxi",
            "voz": "confiante"
        },
        {
            "nome": "Limão",
            "voz": "jovem"
        },
        {
            "nome": "Coco",
            "voz": "séria"
        }
    ]

    teste = agente.criar_dialogos(
        {"episodio": 1},
        personagens
    )

    print(teste)
