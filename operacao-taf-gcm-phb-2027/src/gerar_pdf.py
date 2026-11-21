# -*- coding: utf-8 -*-
"""Gera Operacao_TAF_GCM_PHB_2027.pdf.  Uso: python3 gerar_pdf.py"""
import os
from motor import *
import visuais  # registra a capa
import conteudo as C

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(os.path.dirname(AQUI), 'Operacao_TAF_GCM_PHB_2027.pdf')


def montar():
    story = [NextPageTemplate('normal'), PageBreak()]
    for f in (C.ficha, C.sumario, C.apresentacao, C.cap_taf, C.cap_avaliacao, C.cap_fundamentos, C.cap_corrida,
              C.cap_fortalecimento, C.cap_plano8, C.cap_plano12, C.cap_acompanhamento, C.cap_erros, C.cap_disciplina,
              C.cap_checklist, C.cap_diario, C.cap_recursos, C.conclusao):
        story += f()
    return story


def main():
    doc = Doc(SAIDA, title='Operação TAF GCM PHB 2027', author='Projeto Operação TAF GCM PHB',
              subject='Preparação física progressiva para candidatos à Guarda Municipal',
              keywords='TAF, preparação física, guarda municipal, corrida, fortalecimento, iniciantes',
              creator='Operação TAF GCM PHB', lang='pt-BR')
    doc.multiBuild(montar())
    print('PDF gerado:', SAIDA)


if __name__ == '__main__':
    main()
