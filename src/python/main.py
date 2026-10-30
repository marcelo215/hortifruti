import json
import time
import numpy as np

try:
    from pyscript import document
    from pyodide.http import open_url
    NO_NAVEGADOR = True
except ImportError:
    NO_NAVEGADOR = False

LIMITE_POR_PEDIDO = 100
telemetria = []          



def carregar_frutas():
    if NO_NAVEGADOR:
        return json.loads(open_url("./src/python/dados.json").read())
    with open("dados.json", encoding="utf-8") as f:
        return json.load(f)


def registrar(evento, inicio):
    """Guarda o nome do evento e quanto tempo (ms) ele demorou."""
    ms = (time.perf_counter() - inicio) * 1000
    telemetria.append({"evento": evento, "ms": round(ms, 2)})


def moeda(v):
    return "R$ " + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")