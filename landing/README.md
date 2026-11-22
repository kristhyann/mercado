# Landing page — Projeto GCM PHB 2027

Página de vendas estática em HTML, CSS e JS puro. Não tem build nem dependências e funciona em qualquer hospedagem estática (Netlify, Vercel, GitHub Pages, Hostinger etc.).

## Estrutura

```
landing/
├── index.html            ← página (copy, seções, SEO, dados estruturados)
├── assets/css/style.css  ← identidade visual e responsividade (mobile first)
├── assets/js/config.js   ← CONFIGURAÇÃO: link do checkout, rodapé, vendedor
├── assets/js/main.js     ← checkout, animações, barra fixa no mobile
└── assets/img/           ← capas (WebP), kit, og-image e favicon
```

## Configurar o checkout (obrigatório antes de publicar)

Abra `assets/js/config.js` e cole o link de pagamento:

```js
checkoutUrl: 'https://pay.sua-plataforma.com/SEU-PRODUTO',
```

- Checkout atual: **https://payment.ticto.app/OCD9E1D6F** (Ticto).
- Levam ao checkout os botões do hero, da oferta, do CTA final e da barra fixa no celular. Só o botão “Ver oferta”, no topo, rola até a seção de oferta.
- O link também está escrito diretamente no `index.html`, então os botões funcionam mesmo se o JavaScript falhar. Se mudar o link, troque no `config.js` e faça buscar e substituir no `index.html`.
- Os parâmetros de campanha da URL (`utm_*`, `src`, `sck`, `fbclid`, `gclid`) são repassados ao checkout automaticamente. Para desativar, use `forwardUtm: false`.
- Enquanto `checkoutUrl` estiver vazio, os botões de compra mostram o aviso “O link de pagamento ainda não foi configurado”.

Na mesma configuração ficam os links do rodapé (privacidade, termos, contato) e a identificação do vendedor.

## Testar localmente

```bash
cd landing
python3 -m http.server 8000
# abra http://localhost:8000
```

## Trocar imagens

Substitua os arquivos em `assets/img/` mantendo os mesmos nomes. Prefira o formato WebP, com no máximo cerca de 600 px de largura para as capas.
Ao publicar, troque o `og:image` relativo em `index.html` pela URL absoluta do seu domínio. Algumas redes sociais exigem isso para mostrar a prévia.
