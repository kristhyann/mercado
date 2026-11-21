# -*- coding: utf-8 -*-
"""Estrutura de dados das questões.

Q(...)  -> alternativa correta é passada separada; a ordem é embaralhada de forma
           determinística (a explicação nunca cita letras, por isso o embaralhamento é seguro).
QF(...) -> alternativas em ordem fixa (ex.: valores numéricos crescentes); informa-se a letra.
T(...)  -> texto-base compartilhado por várias questões.
"""
import random
import zlib

LETRAS = 'ABCDE'
SAL = 's33'


class Questao:
    def __init__(self, assunto, enunciado, alts, resp, expl, erro='', tabela=None):
        assert len(alts) == 5, ('precisa de 5 alternativas', enunciado[:60])
        assert len(set(a.strip().lower() for a in alts)) == 5, ('alternativas repetidas', enunciado[:60])
        assert resp in LETRAS
        self.assunto = assunto
        self.enunciado = enunciado
        self.alts = alts
        self.resp = resp
        self.expl = expl
        self.erro = erro
        self.tabela = tabela
        self.num = None
        self.texto = None   # título do texto-base associado


class Texto:
    def __init__(self, titulo, corpo, fonte='Texto elaborado para este material.'):
        self.titulo = titulo
        self.corpo = corpo
        self.fonte = fonte


def Q(assunto, enunciado, certa, erradas, expl, erro='', tabela=None):
    assert len(erradas) == 4, ('precisa de 4 distratores', enunciado[:60])
    alts = [certa] + list(erradas)
    seed = zlib.crc32((SAL + enunciado + '|' + certa).encode('utf-8'))
    rnd = random.Random(seed)
    idx = list(range(5))
    rnd.shuffle(idx)
    novas = [alts[i] for i in idx]
    resp = LETRAS[novas.index(certa)]
    return Questao(assunto, enunciado, novas, resp, expl, erro, tabela)


def QF(assunto, enunciado, alts, resp, expl, erro='', tabela=None):
    return Questao(assunto, enunciado, list(alts), resp, expl, erro, tabela)


def T(titulo, corpo, fonte='Texto elaborado para este material.'):
    return Texto(titulo, corpo, fonte)


def numerar(itens, inicio=1):
    """Numera as questões de uma lista (que pode conter textos-base)."""
    n = inicio
    texto_atual = None
    qs = []
    for it in itens:
        if isinstance(it, Texto):
            texto_atual = it.titulo
            continue
        if it == 'FIM':
            texto_atual = None
            continue
        it.num = n
        it.texto = texto_atual
        n += 1
        qs.append(it)
    return qs


def _valor(s):
    import re
    t = s.replace('R$', '').replace('−', '-').replace('≈', '')
    m = re.search(r'(\d+)\s*h\s*(\d+)?', t)          # horários e durações: 8h10, 1 h 30 min
    if m and ('h' in t and (':' not in t)) and re.search(r'\d\s*h(\s|\d|$)', t):
        return int(m.group(1)) + (int(m.group(2)) / 60 if m.group(2) else 0)
    m = re.search(r'(-?\d+)\s*/\s*(\d+)', t)          # frações
    if m:
        return int(m.group(1)) / int(m.group(2))
    t = t.replace('.', '').replace(',', '.')
    m = re.search(r'-?\d+(?:\.\d+)?', t)
    return float(m.group()) if m else 0.0


def QN(assunto, enunciado, certa, erradas, expl, erro='', tabela=None):
    """Alternativas numéricas: ordenadas em ordem crescente automaticamente."""
    assert len(erradas) == 4, ('precisa de 4 distratores', enunciado[:60])
    alts = sorted([certa] + list(erradas), key=_valor)
    return Questao(assunto, enunciado, alts, LETRAS[alts.index(certa)], expl, erro, tabela)
