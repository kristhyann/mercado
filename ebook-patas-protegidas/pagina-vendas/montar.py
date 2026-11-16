"""Monta a página de vendas: python3 montar.py
O vídeo, a capa do vídeo e os PDFs ficam em arquivos/ e são publicados junto com a página."""
import json, sys, base64
from pathlib import Path
aqui = Path(__file__).parent
fotos = json.load(open(sys.argv[2] if len(sys.argv) > 2 else aqui / "fotos64.json"))
html = (aqui / "modelo.html").read_text(encoding="utf-8")
for k, v in fotos.items():
    html = html.replace("{{" + k + "}}", v)
html = html.replace("{{LINK}}", "https://apoia.se/patasprotegidas")
html = html.replace("{{VIDEO}}", '<video controls playsinline preload="metadata" poster="arquivos/capa-video.jpg" src="arquivos/video-patas-protegidas.mp4">Seu navegador não reproduz este vídeo.</video>')
(aqui / "patas-protegidas.html").write_text(html, encoding="utf-8")
print("ok", len(html) // 1024, "KB")
