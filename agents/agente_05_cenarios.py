# AGENTE 05 — CENÁRIOS

class AgenteCenarios:
    def __init__(self):
        self.nome = "Agente 05 - Cenários"

        self.estilo = (
            "cenário 3D cinematográfico, detalhado, iluminação "
            "profissional, personagens-frutas antropomórficos, "
            "formato vertical 9:16"
        )

    def criar_cenario(self, roteiro, cena):
        return {
            "episodio": roteiro.get("episodio", 1),
            "cena": cena,

            "prompt": f"""
Crie o cenário da cena {cena}.

ESTILO:
{self.estilo}

REGRAS:
- manter continuidade com a cena anterior;
- manter o mesmo horário do dia quando necessário;
- preservar posição e aparência dos objetos importantes;
- deixar espaço adequado para os personagens;
- iluminação cinematográfica;
- cenário detalhado;
- não alterar personagens;
- formato vertical 9:16.
""",

            "continuidade": {
                "manter_local": True,
                "manter_iluminacao": True,
                "manter_objetos_importantes": True
            }
        }


if __name__ == "__main__":
    agente = AgenteCenarios()

    teste = agente.criar_cenario(
        {"episodio": 1},
        cena=1
    )

    print(teste)
