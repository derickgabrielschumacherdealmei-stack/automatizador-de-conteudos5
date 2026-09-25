import json

from agents.agente_01_tendencias import AgenteTendencias
from agents.agente_02_roteirista import AgenteRoteirista
from agents.agente_03_dialogos import AgenteDialogos
from agents.agente_04_personagens import AgentePersonagens
from agents.agente_05_cenarios import AgenteCenarios
from agents.agente_06_supervisor import AgenteSupervisor
from agents.agente_07_supervisor_continuidade import SupervisorContinuidade
from agents.agente_08_supervisor_final import SupervisorFinal
from agents.agente_09_sincronizacao import AgenteSincronizacao
from agents.agente_10_video import AgenteVideo
from agents.agente_11_tiktok import AgenteTikTok
from agents.agente_12_youtube import AgenteYouTube
from agents.agente_13_instagram import AgenteInstagram
from agents.agente_14_facebook import AgenteFacebook


ARQUIVO_MEMORIA = "memoria.json"


def carregar_memoria():
    with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def executar():
    memoria = carregar_memoria()

    print("=" * 50)
    print("🍓 AUTOMATIZADOR DE CONTEÚDOS")
    print("=" * 50)

    agentes = [
        AgenteTendencias(),
        AgenteRoteirista(),
        AgenteDialogos(),
        AgentePersonagens(),
        AgenteCenarios(),
        AgenteSupervisor(),
        SupervisorContinuidade(),
        SupervisorFinal(),
        AgenteSincronizacao(),
        AgenteVideo(),
        AgenteTikTok(),
        AgenteYouTube(),
        AgenteInstagram(),
        AgenteFacebook()
    ]

    print("\n14 agentes carregados:\n")

    for numero, agente in enumerate(agentes, 1):
        print(f"✅ {numero:02} — {agente.nome}")

    novela = memoria["novela"]

    if novela["novela_finalizada"]:
        print("\n🏁 A novela atual foi finalizada.")
        print("Uma nova novela poderá ser iniciada.")
    else:
        print(
            f"\n🎬 Continuando: {novela['nome']}"
        )

        print(
            f"📺 Episódio: {novela['episodio_atual']}"
        )

    print("\n🕐 Horários programados:")

    for horario in memoria["publicacao"]["horarios"]:
        print(f"• {horario}")

    print("\n🚀 Sistema preparado para executar o pipeline.")


if __name__ == "__main__":
    executar()
