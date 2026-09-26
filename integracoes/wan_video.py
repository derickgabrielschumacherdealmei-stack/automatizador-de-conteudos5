import os
import urllib.request
import urllib.error
import json


class WanVideo:
    def __init__(self):
        self.nome = "Wan Video"
        self.modelo = "Wan-AI/Wan2.2-T2V-A14B"
        self.permitir_gastos = False

    def disponivel(self):
        return bool(os.getenv("HF_TOKEN"))

    def testar_conexao(self):
        token = os.getenv("HF_TOKEN")

        if not token:
            return {
                "sucesso": False,
                "status": "SEM_TOKEN"
            }

        # Consulta somente os dados da conta.
        # Não solicita inferência e não gera vídeo.
        requisicao = urllib.request.Request(
            "https://huggingface.co/api/whoami-v2",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

        try:
            with urllib.request.urlopen(requisicao, timeout=20) as resposta:
                dados = json.loads(resposta.read().decode("utf-8"))

            return {
                "sucesso": True,
                "status": "HUGGINGFACE_CONECTADO",
                "gerador": self.nome,
                "modelo": self.modelo,
                "usuario_hf": dados.get("name", "desconhecido"),
                "gastos_permitidos": False
            }

        except urllib.error.HTTPError as erro:
            return {
                "sucesso": False,
                "status": "TOKEN_INVALIDO_OU_SEM_PERMISSAO",
                "codigo_http": erro.code
            }

        except Exception as erro:
            return {
                "sucesso": False,
                "status": "ERRO_DE_CONEXAO",
                "erro": str(erro)
            }

    def gerar(self, prompt, arquivo_saida):
        return {
            "sucesso": False,
            "status": "GERACAO_AINDA_BLOQUEADA",
            "gerador": self.nome,
            "arquivo_saida": arquivo_saida,
            "gastos_permitidos": False
        }
           
