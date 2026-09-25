# CONTROLADOR PRINCIPAL — NOVELINHA DAS FRUTAS

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


def iniciar():
    print("🍓 AUTOMATIZADOR DE NOVELINHAS")
    print("Iniciando os 14 agentes...\n")

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

    for numero, agente in enumerate(agentes, start=1):
        print(
            f"✅ Agente {numero:02}: "
            f"{agente.nome}"
        )

    print("\n✅ TODOS OS 14 AGENTES CARREGADOS")


if __name__ == "__main__":
    iniciar()
