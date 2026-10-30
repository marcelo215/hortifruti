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



def validar_pedido(fruta, texto_qtd):
    """Devolve (ok, mensagem, quantidade)."""
    if fruta is None:
        return False, "Fruta inválida.", 0
    texto = str(texto_qtd).strip()
    if texto == "":
        return False, "Informe a quantidade.", 0
    if not texto.isdigit():
        return False, "A quantidade deve ser um número inteiro positivo.", 0
    qtd = int(texto)
    if qtd <= 0:
        return False, "A quantidade deve ser maior que zero.", 0
    if qtd > LIMITE_POR_PEDIDO:
        return False, f"Máximo de {LIMITE_POR_PEDIDO} unidades por pedido.", 0
    if qtd > fruta["estoque"]:
        return False, f"Estoque insuficiente (disponível: {fruta['estoque']}).", 0
    return True, "Pedido válido.", qtd



def norma(vetor):
    """Comprimento do vetor: raiz(a² + b² + c²)."""
    return float(np.linalg.norm(np.array(vetor)))


def fruta_mais_parecida(fruta, frutas):
    """Fruta com menor distância euclidiana entre os embeddings."""
    a = np.array(fruta["embedding"])
    melhor, menor = None, None
    for outra in frutas:
        if outra["id"] == fruta["id"]:
            continue
        d = float(np.linalg.norm(a - np.array(outra["embedding"])))
        if menor is None or d < menor:
            melhor, menor = outra, d
    return melhor, menor


FRUTAS = carregar_frutas()


def desenhar_catalogo():
    html = ""
    for f in FRUTAS:
        html += (f'<article class="fruta"><img src="{f["imagem"]}" alt="{f["nome"]}">'
                 f'<h3>{f["nome"]}</h3><p>{moeda(f["preco"])} / un.</p>'
                 f'<small>Estoque: {f["estoque"]}</small></article>')
    document.querySelector("#catalogo").innerHTML = html
    opcoes = "".join(f'<option value="{f["id"]}">{f["nome"]}</option>' for f in FRUTAS)
    document.querySelector("#fruta").innerHTML = opcoes


def desenhar_telemetria():
    linhas = "".join(f'<li>{t["evento"]} — {t["ms"]} ms</li>' for t in telemetria[-8:])
    document.querySelector("#telemetria").innerHTML = linhas


def calcular(event=None):
    inicio = time.perf_counter()
    id_fruta = document.querySelector("#fruta").value
    texto = document.querySelector("#qtd").value
    fruta = next((f for f in FRUTAS if f["id"] == id_fruta), None)

    ok, msg, qtd = validar_pedido(fruta, texto)
    saida = document.querySelector("#resultado")
    if not ok:
        saida.className = "erro"
        saida.innerText = "⚠ " + msg
        registrar("pedido_bloqueado", inicio)
    else:
        total = fruta["preco"] * qtd
        parecida, dist = fruta_mais_parecida(fruta, FRUTAS)
        saida.className = "ok"
        saida.innerHTML = (f"{qtd} × {fruta['nome']} = <b>{moeda(total)}</b><br>"
                           f"Norma do embedding: {norma(fruta['embedding']):.3f}<br>"
                           f"Mais parecida: {parecida['nome']} (distância {dist:.3f})")
        registrar("pedido_ok", inicio)
    desenhar_telemetria()


if NO_NAVEGADOR:
    desenhar_catalogo()
    registrar("pagina_carregada", time.perf_counter())
    desenhar_telemetria()
