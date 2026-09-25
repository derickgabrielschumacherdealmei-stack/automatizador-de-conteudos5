
       class AgenteVideo:
    def __init__(self):
        self.nome = "Agente 10 - Gerenciador de Vídeo"

        # Ordem de tentativa dos geradores
        self.geradores = [
            {
                "nome": "Wan 2.2",
                "tipo": "gratuito",
                "ativo": True
            },
            {
                "nome": "Gerador Reserva 1",
                "tipo": "gratuito",
                "ativo": False
            },
            {
                "nome": "Gerador Reserva 2",
                "tipo": "gratuito",
                "ativo": False
            },
            {
                "nome": "Google Flow",
                "tipo": "ultimo_recurso",
                "ativo": False
            }
        ]

        # Nunca permitir gasto automático
        self.permitir_gastos = False

    def preparar(self, episodio, aprovacao_sincronizacao):
        if not aprovacao_sincronizacao:
            return {
                "aprovado": False,
                "status": "BLOQUEADO",
                "motivo": "Sincronização não aprovada."
            }

        numero = episodio.get("numero", 1)

        return {
            "aprovado": True,
            "status": "PRONTO_PARA_GERAR",
            "episodio": numero,
            "arquivo_final": f"output/episodio_{numero:03d}.mp4",

            "configuracao": {
                "formato": "mp4",
                "proporcao": "9:16",
                "resolucao": "1080x1920",
                "fps": 30,
                "idioma": "pt-BR",
                "duracao_minima_segundos": 60,
                "legendas": True,
                "sincronizacao_labial": True
            },

            "estrategia": {
                "usar_varios_clipes": True,
                "juntar_clipes": True,
                "manter_personagens": True,
                "manter_vozes": True,
                "manter_continuidade": True
            },

            "geradores": self.geradores,

            "seguranca": {
                "permitir_gastos": self.permitir_gastos,
                "se_todos_falharem": "SALVAR_COMO_PENDENTE"
            }
        }

    def escolher_proximo_gerador(self):
        for gerador in self.geradores:
            if gerador["ativo"]:
                return gerador

        return None
