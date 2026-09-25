# AGENTE 04 — PERSONAGENS E CONSISTÊNCIA VISUAL

class AgentePersonagens:
    def __init__(self):
        self.nome = "Agente 04 - Personagens"

        self.estilo_visual = (
            "Animação 3D cinematográfica, personagens-frutas "
            "antropomórficos com corpos humanoides, expressões "
            "faciais fortes, cenários detalhados e formato 9:16."
        )

    def criar_ficha(self, nome, fruta, personalidade,
                    aparencia, roupa, voz):

        return {
            "nome": nome,
            "fruta": fruta,
            "personalidade": personalidade,
            "aparencia": aparencia,
            "roupa_padrao": roupa,
            "voz": voz,
            "estilo": self.estilo_visual,

            "bloqueios_de_consistencia": {
                "manter_rosto": True,
                "manter_fruta": True,
                "manter_cores": True,
                "manter_proporcoes": True,
                "manter_roupa": True,
                "manter_personalidade": True,
                "manter_voz": True
            }
        }

    def personagens_principais(self):

        return [
            self.criar_ficha(
                nome="Morango",
                fruta="morango",
                personalidade="gentil, determinada e emotiva",
                aparencia=(
                    "Morango 3D antropomórfico, rosto expressivo "
                    "e corpo humanoide."
                ),
                roupa="moletom rosa e roupa escolar",
                voz="jovem e expressiva"
            ),

            self.criar_ficha(
                nome="Abacaxi",
                fruta="abacaxi",
                personalidade="confiante, popular e provocadora",
                aparencia=(
                    "Abacaxi 3D antropomórfico, folhas verdes "
                    "no topo e corpo humanoide."
                ),
                roupa="roupa escolar elegante",
                voz="confiante"
            ),

            self.criar_ficha(
                nome="Limão",
                fruta="limão",
                personalidade="playboy e provocador",
                aparencia=(
                    "Limão 3D antropomórfico com corpo humanoide."
                ),
                roupa="jaqueta universitária vermelha",
                voz="jovem e descontraída"
            ),

            self.criar_ficha(
                nome="Coco",
                fruta="coco",
                personalidade="sério e popular",
                aparencia=(
                    "Coco 3D antropomórfico com corpo humanoide."
                ),
                roupa="jaqueta universitária preta",
                voz="séria"
            )
        ]

    def gerar_prompt(self, personagem):

        return f"""
PERSONAGEM FIXO DA SÉRIE

Nome: {personagem['nome']}
Fruta: {personagem['fruta']}
Personalidade: {personagem['personalidade']}
Aparência: {personagem['aparencia']}
Roupa: {personagem['roupa_padrao']}
Voz: {personagem['voz']}

ESTILO:
{personagem['estilo']}

REGRA DE CONTINUIDADE:
O personagem deve continuar reconhecível em todos os episódios.
Não alterar fruta, características principais, cores, proporções,
personalidade ou voz sem que o roteiro determine explicitamente
uma mudança.
"""


if __name__ == "__main__":
    agente = AgentePersonagens()

    personagens = agente.personagens_principais()

    for personagem in personagens:
        print(agente.gerar_prompt(personagem))
