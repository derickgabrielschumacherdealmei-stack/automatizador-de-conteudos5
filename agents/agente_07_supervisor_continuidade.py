# AGENTE 07 — SUPERVISOR DE CONTINUIDADE

class SupervisorContinuidade:
    def __init__(self):
        self.nome = "Agente 07 - Supervisor de Continuidade"

    def verificar(self, episodio, memoria):
        erros = []

        episodio_esperado = memoria.get("episodio_atual", 1)

        if episodio.get("episodio") != episodio_esperado:
            erros.append(
                f"Episódio incorreto. Esperado: {episodio_esperado}"
            )

        if memoria.get("novela_finalizada") is False:
            nova_novela = episodio.get("nova_novela", False)

            if nova_novela:
                erros.append(
                    "Não pode começar outra novela antes "
                    "da atual terminar."
                )

        personagens_oficiais = set(
            memoria.get("personagens", [])
        )

        personagens_do_episodio = set(
            episodio.get("personagens", [])
        )

        desconhecidos = (
            personagens_do_episodio - personagens_oficiais
        )

        if desconhecidos:
            erros.append(
                "Personagens não autorizados: "
                + ", ".join(desconhecidos)
            )

        resumo_anterior = memoria.get("resumo_anterior")

        if episodio_esperado > 1 and not resumo_anterior:
            erros.append(
                "Falta o resumo do episódio anterior."
            )

        aprovado = len(erros) == 0

        return {
            "agente": self.nome,
            "aprovado": aprovado,
            "erros": erros,
            "acao": (
                "ENVIAR PARA SUPERVISOR 3"
                if aprovado
                else "DEVOLVER PARA CORREÇÃO"
            )
        }


if __name__ == "__main__":
    memoria = {
        "episodio_atual": 1,
        "novela_finalizada": False,
        "resumo_anterior": None,
        "personagens": [
            "Morango",
            "Abacaxi",
            "Limão",
            "Coco"
        ]
    }

    episodio = {
        "episodio": 1,
        "nova_novela": False,
        "personagens": [
            "Morango",
            "Abacaxi"
        ]
    }

    supervisor = SupervisorContinuidade()

    print(
        supervisor.verificar(
            episodio,
            memoria
        )
    )
