# Operação GCM PHB 2027

Guia estratégico de preparação pré-edital para a Guarda Civil Municipal de Parnaíba (PI).
Material educacional independente, não oficial.

- `Operacao_GCM_PHB_2027.pdf`: o eBook final (A4, 67 páginas, sumário clicável, marcadores e campos preenchíveis).
- `src/`: código-fonte do PDF em Python com ReportLab.
  - `motor.py`: fontes, cores, estilos, componentes e template das páginas
  - `parte1.py`: apresentação e capítulos 1 a 6
  - `parte2.py`: planos de 30, 60 e 90 dias
  - `parte3.py`: capítulos 10 a 17 e conclusão

Para gerar de novo:

```bash
pip install reportlab
python3 src/gerar_pdf.py
```

Usa as fontes Carlito, Liberation Sans e DejaVu Sans (pacotes `fonts-crosextra-carlito`, `fonts-liberation` e `fonts-dejavu`).
