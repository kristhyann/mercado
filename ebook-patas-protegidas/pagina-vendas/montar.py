"""Monta a página de vendas: python3 montar.py [arquivo_de_video.mp4]
Sem vídeo, mostra um espaço reservado com a foto de capa."""
import json, sys, base64
from pathlib import Path
aqui = Path(__file__).parent
fotos = json.load(open(sys.argv[2] if len(sys.argv) > 2 else aqui / "fotos64.json"))
html = (aqui / "modelo.html").read_text(encoding="utf-8")
for k, v in fotos.items():
    html = html.replace("{{" + k + "}}", v)
html = html.replace("{{LINK}}", "https://apoia.se/patasprotegidas")
video = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != "-" else None
if video:
    html = html.replace("{{VIDEO}}", f'<video controls playsinline preload="metadata" poster="{fotos["agua"]}" src="{Path(video).name}"></video>')
else:
    html = html.replace("{{VIDEO}}", f'''<img src="{fotos["agua"]}" alt="" style="object-position:50% 30%">
      <div class="aguardando"><div class="play"><svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M6 4l14 8-14 8z"/></svg></div><p>Vídeo da campanha em breve</p></div>''')
(aqui / "patas-protegidas.html").write_text(html, encoding="utf-8")
print("ok", len(html) // 1024, "KB")
