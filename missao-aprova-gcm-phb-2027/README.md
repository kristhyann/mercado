# Missão Aprova GCM PHB 2027

Material de treino com questões, simulados, revisão e estratégia para a Guarda Civil Municipal de Parnaíba (PI).
É independente e não oficial. Todas as questões são originais.

- `Missao_Aprova_GCM_PHB_2027.pdf`: o PDF final (A4, 193 páginas, sumário clicável, folhas de respostas com bolhas clicáveis e páginas preenchíveis).
- 320 questões comentadas: Português 100, Informática 50, Matemática/RLM 50, Legislação 100, Parnaíba 20.
- 3 simulados inéditos de 40 questões cada, com gabarito separado.

## Código-fonte (`src/`)

| Arquivo | Conteúdo |
|---|---|
| `qbase.py` | Estrutura das questões; embaralhamento determinístico das alternativas |
| `q_port.py`, `q_info.py`, `q_mat.py`, `q_leg.py`, `q_local.py` | Bancos de questões, com fontes no cabeçalho de cada arquivo |
| `motor.py`, `layout.py` | Estilos, componentes, capa e folha de respostas |
| `gerar_pdf.py` | Monta os capítulos, os simulados e os gabaritos |

Para gerar de novo: `python3 src/gerar_pdf.py`. Requer `reportlab` e as fontes Carlito, Liberation e DejaVu.
