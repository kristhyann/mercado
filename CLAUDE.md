# Canal olhaso_3D — regras dos vídeos

- **Marca d'água obrigatória:** todo vídeo (e capa) leva `@olhaso_3D` visível, discreto, sem cobrir o objeto nem a legenda.
- A pessoa gera a voz em outra plataforma (ElevenLabs). Entregar só o roteiro em texto (`roteiro_voz.txt`) e esperar o mp3; depois montar o vídeo em cima do áudio dela.
- Formato padrão: vertical 1080x1920, 3D low-poly colorido, legenda palavra por palavra (Poppins), estilo "construa do zero" (skill `construa-do-zero`).
- Kit reutilizável em `videos/_kit/` (render.js, kit.js, pessoas.js, scripts/).
- Estratégia de conteúdo e séries: ver `estrategia/README.md` (pilares, séries de 3 partes, formato de entrega).
- Antes de renderizar o vídeo completo, SEMPRE gerar quadros de teste de todas as cenas e conferir falhas de imagem (objetos cortados, câmera dentro de objetos, textos sobrepostos, peças sumindo, telas escuras). Só renderizar depois de corrigir.
