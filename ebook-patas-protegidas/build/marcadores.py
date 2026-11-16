"""Substitui os marcadores (bookmarks) do PDF por uma estrutura limpa:
capa, sumário, apresentação, capítulos com suas seções e referências."""
import json, sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter

pdf = Path(sys.argv[1])
estrutura = json.loads((Path(__file__).parent / "estrutura.json").read_text(encoding="utf-8"))
r = PdfReader(pdf)
w = PdfWriter(clone_from=r)
nd = r.named_destinations

def pagina(nome):
    d = nd.get("/" + nome) or nd.get(nome)
    return r.get_destination_page_number(d) if d else None

w.add_outline_item("Capa", 0)
for nome, titulo in [("sumario", "Sumário"), ("apresentacao", "Como usar este guia")]:
    if pagina(nome) is not None:
        w.add_outline_item(titulo, pagina(nome))
for cap in estrutura:
    pg = pagina(f"cap-{cap['num']}")
    if pg is None:
        continue
    pai = w.add_outline_item(f"{cap['num']}. {cap['titulo']}", pg)
    for sid, titulo in cap["secoes"]:
        p = pagina(sid)
        if p is not None:
            w.add_outline_item(titulo, p, parent=pai)
if pagina("referencias") is not None:
    w.add_outline_item("Referências", pagina("referencias"))
w.add_metadata({"/Title": "Patas Protegidas — Meu cachorro, minha responsabilidade",
                "/Author": "Projeto Patas Protegidas",
                "/Subject": "O guia completo de cuidados, saúde, proteção e bem-estar canino",
                "/Keywords": "cães, cachorro, tutor, cuidados, saúde, vacinas, primeiros socorros, adoção, abandono"})
w.page_mode = "/UseOutlines"
w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
with open(pdf, "wb") as f:
    w.write(f)
print("Marcadores reconstruídos:", pdf)
