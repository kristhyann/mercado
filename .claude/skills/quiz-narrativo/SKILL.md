---
name: quiz-narrativo
description: Transforma questões de concursos públicos (foco GCM / Guarda Municipal) em quizzes narrativos para vídeo animado - uma situação visual com começo, meio e fim, narração que não entrega o conceito, pergunta, 4 alternativas, contagem regressiva de 5 s, revelação e explicação com fundamento legal. Só roteiro, nunca produz vídeo. Use quando o usuário escrever "CRIAR QUIZ", "CRIAR N QUIZZES", pedir quiz, questão narrativa, pergunta de concurso em forma de história, ou um quiz de uma das 19 disciplinas autorizadas.
argument-hint: "[N] — <disciplina> — <tema>"
---

# Quiz narrativo para concursos

Função: escrever a ESTRUTURA NARRATIVA do quiz. Não produzir vídeo, não alterar o estilo visual, os personagens, a skill `storytelling-ilustrado` nem o pipeline de produção. Quando um quiz for enviado para produção depois, ele usa o estilo visual já existente.

Fale em português do Brasil.

## Ativação

- "CRIAR QUIZ" sem disciplina/tema: pergunte apenas qual disciplina ou tema (dentre as 19 abaixo). Nada mais.
- "CRIAR QUIZ — <disciplina> — <tema>": crie imediatamente, sem perguntas.
- "CRIAR N QUIZZES — <disciplina>": crie N quizzes diferentes (situação, cenário, pergunta e personagens novos em cada um).
- Tema fora das 19 disciplinas: diga que está fora da lista e peça um tema dentro dela.

## Disciplinas autorizadas (somente estas)

1. Direito Constitucional · 2. Direitos e Garantias Fundamentais · 3. Administração Pública na Constituição · 4. Segurança Pública · 5. Direito Penal — Parte Geral · 6. Direito Penal — Parte Especial · 7. Crimes contra a Administração Pública · 8. Legislação Penal Especial · 9. Direito Administrativo — Fundamentos · 10. Poderes Administrativos · 11. Atos Administrativos · 12. Agentes Públicos · 13. Direito Processual Penal · 14. Direitos Humanos · 15. CTB · 16. Informática · 17. Língua Portuguesa · 18. Raciocínio Lógico · 19. Legislação das Guardas Municipais

## Sequência do vídeo

CENA ANIMADA → NARRAÇÃO → SITUAÇÃO → PERGUNTA → ALTERNATIVAS → TEMPO PARA RESPONDER → REVELAÇÃO → EXPLICAÇÃO

## Regras de construção

1. **História antes da pergunta.** Nunca pergunta seca ("O que é peculato?"). Mostre o fato acontecendo; a pergunta vem só depois, e a história precisa bastar para o espectador raciocinar.
2. **Gancho**: frase curta e variada (nunca o mesmo gancho em quizzes seguidos). Ex.: "Observe atentamente o que acontece." / "Um pequeno detalhe muda tudo." / "Imagine que você é o agente dessa ocorrência."
3. **Cena animada**: personagens, local, objetos importantes, ações, movimentos, interações, acontecimento principal e consequência. Simples, representável em poucos segundos, com no máximo 2 ou 3 personagens. O detalhe decisivo para a resposta (ex.: "o dinheiro estava sob a guarda dele em razão do cargo") precisa aparecer na imagem E na narração.
4. **Narração da situação**: natural, clara, objetiva, sem jargão excessivo, SEM o nome do conceito cobrado e sem palavras que entreguem a resposta. Curta: 30 a 60 palavras (~12 a 25 s de voz).
5. **Pergunta**: objetiva, ligada aos fatos, com formato variado (qual crime / qual princípio / qual medida / qual direito / qual procedimento / qual interpretação...).
6. **Alternativas**: sempre A, B, C e D; todas plausíveis e do mesmo tipo (quatro crimes, quatro princípios...); só UMA correta; nenhuma com palavra óbvia que denuncie a resposta; varie a letra da correta entre os quizzes.
7. **Tempo de resposta**: 5 segundos com contagem visual 5…4…3…2…1, sem narração e sem pista durante a contagem.
8. **Revelação**: "Resposta correta: alternativa X." Objetiva e visualmente clara.
9. **Explicação**: simples, dizendo por que a correta está certa e, em uma frase, por que a pegadinha principal está errada.
   - Disciplinas jurídicas: cite a lei e o artigo quando aplicável, com o conceito em linguagem simples.
   - Demais disciplinas: conceito + raciocínio passo a passo.

## Precisão jurídica (inegociável)

- Não inventar lei, artigo, súmula, tese ou jurisprudência. Citar só o que você tem certeza que existe e está vigente; se não tiver certeza do número do artigo, cite a lei sem o artigo e diga isso.
- Usar a redação atual (ex.: Lei de Abuso de Autoridade é a 13.869/2019; não a revogada 4.898/65). Desconfie de memória antiga em leis muito alteradas (CTB, Código Penal, Lei de Drogas, ECA).
- Situação juridicamente possível e sem ambiguidade: se um detalhe mudar a tipificação (ex.: violência → roubo, não furto; posse anterior → apropriação indébita, não furto), deixe esse detalhe explícito na cena.
- Não misturar dois conceitos numa mesma questão.

## Variedade

Antes de criar, leia `video-agent/quizzes/registro.md` e não repita cenário, situação nem pergunta já usados. Não abuse de furto, roubo e abordagem: use repartições, trânsito, escolas, praças, eventos, hospitais, internet, atendimento ao cidadão, ambiente de trabalho etc. Depois de criar, acrescente uma linha por quiz ao registro.

## Formato de saída (exatamente este)

```
QUIZ [NÚMERO]

DISCIPLINA:
TEMA:
NÍVEL: (fácil | médio | difícil)

GANCHO:

CENA ANIMADA:

NARRAÇÃO:

PERGUNTA:

A)
B)
C)
D)

TEMPO DE RESPOSTA: 5 segundos (contagem visual 5…4…3…2…1, sem narração)

RESPOSTA CORRETA:

EXPLICAÇÃO:

FUNDAMENTO LEGAL OU CONCEITO:
```

Numeração contínua: o próximo número vem do registro.

Salve cada quiz em `video-agent/quizzes/<disciplina-em-slug>/quiz-<NNN>.md` e mostre o texto completo na resposta.

## Verificação antes de apresentar (cada quiz)

- [ ] A situação descrita é plausível e juridicamente possível.
- [ ] A pergunta corresponde à situação.
- [ ] As 4 alternativas são plausíveis e do mesmo tipo.
- [ ] Só uma é correta (teste cada errada contra os fatos).
- [ ] A resposta e a explicação conferem.
- [ ] A legislação citada existe, está vigente e o artigo confere.
- [ ] A história e a narração não entregam a resposta antes do desafio.
- [ ] O cenário e a pergunta não repetem o registro.
