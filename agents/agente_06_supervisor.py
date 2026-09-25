# AGENTE 06 — SUPERVISOR DE ROTEIRO

class AgenteSupervisor:
    def __init__(self):
        self.nome = "Agente 06 - Supervisor"

    def verificar(self, roteiro, dialogos, personagens, cenarios):
        erros = []

        if not roteiro:
            erros.append("Roteiro não foi criado.")

        if not dialogos:
            erros.append("Diálogos não foram criados.")

        if not personagens:
            erros.append("Personagens não foram definidos.")

        if not cenarios:
            erros.append("Cenários não foram definidos.")

        # Verifica idioma das falas
        if isinstance(dialogos, dict):
            for fala in dialogos.get("dialogos", []):
                if fala.get("idioma") != "pt-BR":
                    erros.append(
                        f"Idioma incorreto em {fala.get('personagem')}."
                    )

        # Verifica continuidade básica
        if isinstance(roteiro, dict):
            if not roteiro.get("continuidade"):
                erros.append("Roteiro sem informação de continuidade.")

        aprovado = len(erros) == 0

        return {
            "agente": self.nome,
            "aprovado": aprovado,
            "erros": erros,
            "acao": (
                "LIBERAR PARA O SUPERVISOR 2"
                if aprovado
                else "DEVOLVER PARA CORREÇÃO"
            )
        }


if __name__ == "__main__":
    supervisor = AgenteSupervisor()

    teste = supervisor.verificar(
        roteiro={
            "episodio": 1,
            "continuidade": "Início da história"
        },
        dialogos={
            "dialogos": [
                {
                    "personagem": "Morango",
                    "fala": "Oi!",
                    "idioma": "pt-BR"
                }
            ]
        },
        personagens=[{"nome": "Morango"}],
        cenarios=[{"cena": 1}]
    )

    print(teste)
