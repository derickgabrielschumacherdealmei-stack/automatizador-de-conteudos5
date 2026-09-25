# AGENTE 01 — ANALISTA DE TENDÊNCIAS

from datetime import datetime


class AgenteTendencias:
    def __init__(self):
        self.nome = "Agente 01 - Analista de Tendências"

    def analisar(self):
        """
        Esta função será conectada depois a uma fonte de dados
        atualizada para analisar tendências reais.
        """

        resultado = {
            "data_analise": datetime.now().isoformat(),
            "tipo_conteudo": "novelinhas de frutas",
            "plataformas": [
                "TikTok",
                "YouTube Shorts",
                "Instagram Reels",
                "Facebook Reels"
            ],
            "procurar": [
                "temas com maior engajamento",
                "ganchos que prendem atenção",
                "duração dos vídeos",
                "estilos de personagens",
                "tipos de conflito",
                "reviravoltas",
                "formatos que incentivam continuação"
            ],
            "regras": [
                "não copiar histórias de outros criadores",
                "usar tendências apenas como inspiração",
                "manter personagens próprios",
                "priorizar histórias adequadas para público geral",
                "manter formato vertical 9:16"
            ]
        }

        return resultado


if __name__ == "__main__":
    agente = AgenteTendencias()
    print(agente.analisar())
