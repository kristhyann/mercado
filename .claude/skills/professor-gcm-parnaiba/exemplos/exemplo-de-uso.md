# Exemplo de uso da Skill

## Como ativar
- **Automaticamente:** basta pedir algo sobre a GCM de Parnaíba ("crie minha apostila de…", "faça 10 questões de…", "monte meu plano de estudos"). O Claude Code reconhece a Skill pela descrição.
- **Manualmente:** digite `/professor-gcm-parnaiba` seguido do pedido.

## Prompt para a primeira apostila
```
/professor-gcm-parnaiba Crie a Apostila 01 de CÓDIGO PENAL para a GCM de Parnaíba.
Sou iniciante: ensine do zero, nos 7 passos, com quadros Atenção, Não confunda, Exemplo,
Memorize e Possível pegadinha. Pesquise o edital (sinalize se não houver), confira os artigos
no Planalto e priorize: princípios, aplicação da lei penal, tempo e lugar do crime, teoria do
crime (fato típico, ilicitude, culpabilidade), dolo e culpa, consumação e tentativa, desistência
voluntária, arrependimento eficaz e posterior, excludentes de ilicitude, imputabilidade, concurso
de pessoas, crimes contra a pessoa, contra o patrimônio e contra a Administração Pública.
Inclua 30 questões autorais (A–E) com gabarito comentado em seção separada, resumo estratégico,
mapa mental textual, flashcards, 20 perguntas rápidas, lista do que memorizar, checklist, caderno
de erros e revisões D+1/D+7/D+30. Arquivo: 01_Codigo_Penal_GCM_Parnaiba.pdf
```

## O que a Skill fará
1. Lerá `references/edital-e-status.md` e avisará que o edital não está confirmado (se for o caso).
2. Pesquisará a legislação vigente e anotará as verificações em `GCM-PARNAIBA/fontes/notas-de-verificacao.md`.
3. Copiará o kit para `GCM-PARNAIBA/apostilas/fonte/01-codigo-penal/`, escreverá o `gerar.py` e o `config.json` e gerará o PDF.
4. Revisará: checagem automática, QC de páginas, revisão visual, gabarito e integridade.
5. Salvará em `GCM-PARNAIBA/apostilas/01_Codigo_Penal_GCM_Parnaiba.pdf` e atualizará o catálogo.

## Exemplo mínimo pronto
`exemplos/exemplo-minimo/` contém `gerar.py`, `config.json` e o PDF gerado (`00_Exemplo_Minimo_GCM_Parnaiba.pdf`, 11 páginas). O PDF demonstra um tópico nos 7 passos, os quadros, 3 questões com gabarito e os blocos de revisão. Para reproduzir:
```bash
T=$(mktemp -d); cp .claude/skills/professor-gcm-parnaiba/assets/kit/* $T/
cp .claude/skills/professor-gcm-parnaiba/exemplos/exemplo-minimo/{gerar.py,config.json} $T/
cd $T && node build.js
```

## Outros pedidos que a Skill atende
- "Explique legítima defesa como se eu tivesse 12 anos." (aula curta no chat, 7 passos)
- "Faça um simulado de 15 questões de Código Penal." (salvo em `GCM-PARNAIBA/questoes/`)
- "Monte flashcards da Lei 13.022/2014." (salvo em `GCM-PARNAIBA/revisoes/`)
- "Chegou o edital, atualize tudo." (Skill atualiza o status e lista as apostilas a ajustar)
