# -*- coding: utf-8 -*-
"""Gera Operacao_GCM_PHB_2027.pdf.  Uso: python3 gerar_pdf.py"""
import os
from motor import *
import parte1, parte2, parte3

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(os.path.dirname(AQUI), 'Operacao_GCM_PHB_2027.pdf')


def montar():
    story = [NextPageTemplate('normal'), PageBreak()]   # página 1 = capa
    story += parte1.ficha()
    story += parte1.sumario()
    story += parte1.apresentacao()
    for f in (parte1.cap1, parte1.cap2, parte1.cap3, parte1.cap4, parte1.cap5, parte1.cap6,
              parte2.cap7, parte2.cap8, parte2.cap9,
              parte3.cap10, parte3.cap11, parte3.cap12, parte3.cap13, parte3.cap14,
              parte3.cap15, parte3.cap16, parte3.cap17, parte3.conclusao):
        story += f()
    return story


def main():
    doc = Doc(SAIDA, title='Operação GCM PHB 2027',
              author='Projeto Operação GCM PHB',
              subject='Guia estratégico de preparação pré-edital para a Guarda Civil Municipal de Parnaíba (PI)',
              keywords='concurso, guarda civil municipal, Parnaíba, Piauí, GCM, preparação, estudos',
              creator='Operação GCM PHB', lang='pt-BR')
    doc.multiBuild(montar())
    print('PDF gerado:', SAIDA)


if __name__ == '__main__':
    main()
