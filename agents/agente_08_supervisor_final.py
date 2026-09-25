# AGENTE 08 — SUPERVISOR FINAL

class SupervisorFinal:
    def __init__(self):
        self.nome = "Agente 08 - Supervisor Final"

    def verificar(
        self,
        roteiro,
        dialogos,
        personagens,
        cenarios,
        aprovacao_supervisor_1,
        aprovacao_supervisor_2
    ):
        erros = []

        # Confere os supervisores anteriores
        if not aprovacao_supervisor_1:
            erros.append("Supervisor 1 não aprovou.")

        if not aprovacao_supervisor_2:
            erros.append("Supervisor 2 não aprovou.")

        # Confere componentes
        if not roteiro:
            erros.append("Roteiro ausente.")

        if not dialogos:
            erros.append("Diálogos ausentes.")

        if not personagens:
            erros.append("Personagens ausentes.")

        if not cenarios:
            erros.append("Cenários ausentes.")

        # Confere falas
        if isinstance(dialogos, dict):
            for fala in dialogos.get("dialogos", []):
                if not fala.get("personagem"):
                    erros.append("Existe uma fala sem personagem.")

                if not fala.get("fala"):
                    erros.append(
                        f"{fala.get('personagem', 'Personagem')} "
                        "está sem fala."
                    )

                if fala.get("idioma") != "pt-BR":
                    erros.append(
                        "Existe uma fala que não está em pt-BR."
                    )

        aprovado = len(erros) == 0

        return {
            "agente": self.nome,
            "aprovado": aprovado,
            "erros": erros,
            "resultado": (
                "APROVADO PARA PRODUÇÃO"
                if aprovado
                else "REPROVADO — CORRIGIR"
            )
        }


if __name__ == "__main__":
    supervisor = SupervisorFinal()

    resultado = supervisor.verificar(
        roteiro={"episodio": 1},
        dialogos={
            "dialogos": [
                {
                    "personagem": "Morango",
                    "fala": "Eu preciso descobrir a verdade!",
                    "idioma": "pt-BR"
                }
            ]
        },
        personagens=[{"nome": "Morango"}],
        cenarios=[{"cena": 1}],
        aprovacao_supervisor_1=True,
        aprovacao_supervisor_2=True
    )

    print(resultado)
