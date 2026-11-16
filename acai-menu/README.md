# 🍇 AÇAÍ MENU

**Seu açaí favorito a poucos cliques.**

Plataforma multiloja de cardápios digitais para açaiterias: cada loja tem link próprio, identidade visual própria,
montagem de açaí com regras de preço, carrinho persistente e pedido enviado pronto para o WhatsApp da loja.

- **Um único sistema** atende dezenas ou centenas de lojas: `seudominio.com/acai-da-maria`, `seudominio.com/acai-do-joao`…
- **Sem painel para lojistas** nesta versão: você (proprietário da plataforma) cadastra cada loja em um arquivo JSON e publica com um comando.
- Stack: Next.js 16 (App Router) · React 19 · TypeScript · Tailwind CSS 4 · Supabase (Postgres + Storage + RLS) · Vercel · Lucide.

---

## Sumário

1. [Como funciona](#1-como-funciona)
2. [Rodar no seu computador](#2-rodar-no-seu-computador)
3. [Configurar o Supabase](#3-configurar-o-supabase)
4. [Cadastrar uma nova loja](#4-cadastrar-uma-nova-loja)
5. [Alterar produtos, preços e opções](#5-alterar-produtos-preços-e-opções)
6. [Configurar o WhatsApp](#6-configurar-o-whatsapp)
7. [Publicar na Vercel](#7-publicar-na-vercel)
8. [Referência do store.json](#8-referência-do-storejson)
9. [Arquitetura e segurança](#9-arquitetura-e-segurança)
10. [Testes](#10-testes)

---

## 1. Como funciona

```
stores/acai-do-joao/store.json  ──npm run store:sync──►  Supabase (tabelas + imagens)
                                                              │
seudominio.com/acai-do-joao  ◄── Next.js na Vercel lê ────────┘  (somente leitura, RLS)
        │
        └─ cliente monta o pedido → mensagem pronta → wa.me/<whatsapp-da-loja>
```

Fluxo do cliente: abre o link → vê produtos → personaliza o açaí (preço em tempo real) → carrinho →
entrega ou retirada → dados → pagamento (troco) → confere a mensagem → **Enviar pelo WhatsApp**.
O cliente ainda precisa tocar em **ENVIAR** no WhatsApp; o sistema nunca diz que a loja recebeu o pedido.

**Funcionalidades:** status aberto/fechado automático (fuso da loja, feriados, intervalos que passam da meia-noite,
status manual, pausa de pedidos, agendamento quando fechada) · busca · categorias com rolagem e destaque automático ·
destaques · selos (mais vendido, promoção, novo, zero açúcar…) · preço "de/por" · produtos indisponíveis e opções esgotadas ·
taxa fixa, por bairro ou grátis, grátis acima de um valor, pedido mínimo · CEP com preenchimento automático (ViaCEP) ·
dados do cliente lembrados no aparelho · carrinho salvo por loja (sobrevive a atualização da página) · editar itens do carrinho ·
compartilhar cardápio · voltar ao topo · botão voltar do Android fecha janelas · Open Graph com imagem gerada por loja ·
mensagem do WhatsApp com cabeçalho/rodapé personalizáveis.

## 2. Rodar no seu computador

Requisitos: Node.js 20.9+.

```bash
cd acai-menu
npm install
cp .env.example .env.local
npm run dev
```

Abra http://localhost:3000. Sem Supabase configurado, o site usa as **lojas de demonstração** da pasta `stores/`
(Açaí da Maria, Açaí Tropical, Açaí Premium) — com faixa "Loja de DEMONSTRAÇÃO", preços e endereços fictícios.

> Lojas de demonstração **nunca** enviam pedido para um número de terceiros: elas usam o número de
> `NEXT_PUBLIC_PLATFORM_WHATSAPP` (o seu). Sem ele, o botão de envio fica desativado e a mensagem é apenas exibida.

## 3. Configurar o Supabase

1. Crie um projeto em https://supabase.com (região São Paulo recomendada).
2. Abra **SQL Editor** e execute, em ordem, o conteúdo de:
   - `supabase/migrations/0001_schema.sql` (tabelas, índices, RLS e funções)
   - `supabase/migrations/0002_storage.sql` (bucket público `store-assets` para imagens)
3. Em **Project Settings → API** copie para o `.env.local`:

| Variável | Onde encontrar | Vai para a Vercel? |
|---|---|---|
| `SUPABASE_URL` | Project URL | ✅ sim |
| `SUPABASE_ANON_KEY` | chave `anon` / publishable | ✅ sim |
| `SUPABASE_SERVICE_ROLE_KEY` | chave `service_role` / secret | ❌ **não** — só no seu computador |
| `REVALIDATE_SECRET` | invente um texto longo e aleatório | ✅ sim (mesmo valor nos dois lugares) |
| `NEXT_PUBLIC_SITE_URL` | URL do site publicado | ✅ sim |

Gere um segredo com: `node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"`

4. Publique as lojas: `npm run store:sync -- --all` (as de demonstração também, se quiser exibi-las).
5. Confira: `npm run store:list`.

## 4. Cadastrar uma nova loja

```bash
npm run store:new -- acai-do-joao "Açaí do João" 5511987654321
```

Isso cria `stores/acai-do-joao/store.json` a partir do modelo (`stores/_modelo`). Depois:

1. Coloque as imagens em `stores/acai-do-joao/images/` (logo quadrado ~512px, capa ~1600×640, fotos dos produtos ~1200×900;
   JPG/WebP de até 5 MB). No JSON, use caminhos relativos: `"image": "images/acai-500.jpg"`.
2. Edite o `store.json` (nome, cores, endereço, horários, entrega, produtos). No VS Code há autocompletar e validação
   graças ao `store.schema.json`.
3. Valide: `npm run store:validate -- acai-do-joao`
4. Publique: `npm run store:sync -- acai-do-joao`
   - envia as imagens para o Supabase Storage,
   - grava tudo de uma vez (se algo der errado, nada é alterado),
   - atualiza o site na hora (ou em até 60 s).
5. Envie ao lojista o link `https://seudominio.com/acai-do-joao`.

**Atalho para clientes parecidos:** `npm run store:duplicate -- acai-da-maria acai-do-joao "Açaí do João"`
copia cardápio, opções e imagens de uma loja existente.

**Desativar uma loja:** `"active": false` no JSON e `npm run store:sync -- <slug>` (o link passa a mostrar "Cardápio não encontrado").
**Apagar de vez:** no SQL Editor, `select admin_delete_store('slug');`.

## 5. Alterar produtos, preços e opções

Edite o `store.json` da loja e rode `npm run store:sync -- <slug>`. Exemplos:

- **Mudar preço:** altere `"price"` do tamanho (`variants`) ou do produto.
- **Promoção:** `"compareAtPrice": 18` mostra o preço antigo riscado e o selo "Promoção".
- **Esgotou um produto:** `"available": false` (aparece como "Indisponível"). Para esconder: `"active": false`.
- **Esgotou um acompanhamento:** `"available": false` na opção (aparece "Esgotado").
- **Duplicar produto:** `"extends": "acai-tradicional"` copia tudo de outro produto; informe só o que muda.
- **Pausar pedidos (muito movimento):** `"hours": { "ordersPaused": true, "pausedMessage": "Voltamos às 20h!" }`.
- **Fechar manualmente:** `"hours": { "mode": "closed" }` (`"open"` força aberto, `"auto"` segue a grade).

Se alguém editar diretamente nas tabelas do Supabase, traga a versão atual com `npm run store:export -- <slug>`
(o arquivo anterior vira backup).

### Regras de personalização

Grupos de opções (`addonGroups`) são cadastrados uma vez e reaproveitados por vários produtos:

```json
{ "key": "acompanhamentos", "name": "Acompanhamentos",
  "min": 0, "max": 6, "free": 3, "extraPrice": 2,
  "addons": [ { "key": "granola", "name": "Granola" },
              { "key": "nutella", "name": "Nutella", "price": 4, "alwaysPaid": true } ] }
```

| Campo | Significado |
|---|---|
| `min` | mínimo de escolhas (1+ = obrigatório) |
| `max` | máximo de escolhas (`null` = sem limite) |
| `free` | quantas escolhas são grátis |
| `extraPrice` | valor de cada escolha além das grátis (quando a opção não tem preço próprio) |
| `maxPerOption` | quantas vezes a mesma opção pode ser escolhida (ex.: 3x Nutella extra) |
| `price` (opção) | preço da opção quando cobrada |
| `alwaysPaid` (opção) | sempre cobrada e não consome as grátis |

As escolhas grátis abatem primeiro as opções mais caras (sempre a favor do cliente).

As regras podem mudar **por produto** (`"addonGroups": [{ "group": "acompanhamentos", "free": 6 }]`)
e **por tamanho** (`"rules": { "acompanhamentos": { "free": 4, "max": 8 } }` dentro da variação).
Prioridade: tamanho > produto > grupo.

## 6. Configurar o WhatsApp

- No `store.json`: `"contact": { "whatsapp": "5511987654321" }` — **somente dígitos**: 55 + DDD + número (celular com o 9).
- O pedido abre `https://wa.me/5511987654321?text=<mensagem codificada>` (link oficial do WhatsApp, sem API paga).
- Personalize o início e o fim da mensagem:
  `"whatsappMessage": { "header": "🍇 *NOVO PEDIDO - AÇAÍ DO JOÃO*", "footer": "Obrigado pela preferência!" }`
- Chave Pix opcional: `"ordering": { "pixKey": "..." }` — é incluída na mensagem quando o cliente escolhe Pix.
- Teste: faça um pedido no próprio celular e confira se abre a conversa com o número da loja.

## 7. Publicar na Vercel

1. Envie o repositório para o GitHub.
2. Na Vercel: **Add New → Project →** importe o repositório.
3. **Root Directory: `acai-menu`** (o projeto fica nesta subpasta). Framework: Next.js (detectado).
4. Em **Environment Variables** cadastre: `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `REVALIDATE_SECRET`,
   `NEXT_PUBLIC_SITE_URL` e, opcionalmente, `NEXT_PUBLIC_PLATFORM_WHATSAPP`. Em produção use `DATA_SOURCE=supabase`.
   **Não** cadastre a `SUPABASE_SERVICE_ROLE_KEY`.
5. Deploy. Depois, em **Settings → Domains**, conecte seu domínio e atualize `NEXT_PUBLIC_SITE_URL` (e faça redeploy,
   pois variáveis `NEXT_PUBLIC_*` são fixadas no build).
6. Teste o compartilhamento colando um link de loja no WhatsApp (a prévia usa `/<slug>/opengraph-image`, ou
   `seo.image` se você definir uma imagem própria 1200×630).

## 8. Referência do store.json

Exemplos completos: `stores/acai-da-maria/store.json` (todas as funcionalidades) e `stores/_modelo/store.json` (ponto de partida).

| Bloco | Principais campos |
|---|---|
| raiz | `slug` (igual ao nome da pasta), `name`, `description`, `active`, `isDemo` |
| `branding` | `logo`, `cover`, `primaryColor`, `secondaryColor` (hex `#RRGGBB`) |
| `banner` | `enabled`, `image`, `title`, `subtitle` |
| `seo` | `title`, `description`, `image` (prévia de compartilhamento) |
| `contact` | `whatsapp`, `instagram`, `address`, `region`, `mapsUrl` |
| `hours` | `timezone`, `mode` (auto/open/closed), `whenClosed` (block/schedule), `ordersPaused`, `pausedMessage`, `weekly` (`sun`…`sat`: lista de `{open, close}`), `special` (`{date, closed, intervals, label}`) |
| `ordering` | `delivery`, `pickup`, `minOrder`, `deliveryTime`, `pickupTime`, `paymentMethods` (pix/cash/credit/debit), `pixKey` |
| `delivery` | `mode` (fixed/zones/free), `fixedFee`, `freeAbove`, `allowUnlistedNeighborhoods`, `zones` (`{neighborhood, fee}`) |
| `categories` | `{key, name, description, active}` — a ordem do arquivo é a ordem na tela |
| `addonGroups` | ver [Regras de personalização](#regras-de-personalização) |
| `products` | `key`, `category`, `name`, `description`, `image`, `price` **ou** `variants`, `compareAtPrice`, `variantLabel`, `addonGroups`, `badges`, `featured`, `available`, `active`, `extends` |

Bairros sem cadastro **não recebem taxa inventada**: o cliente vê "Ainda não entregamos neste bairro" ou, com
`allowUnlistedNeighborhoods: true`, "taxa a combinar" (e a mensagem informa isso à loja).

## 9. Arquitetura e segurança

```
src/app/page.tsx                    página da plataforma Açaí Menu
src/app/[slug]/layout.tsx           carrega a loja pelo endereço, aplica cores, provê carrinho
src/app/[slug]/page.tsx             cardápio (SEO/Open Graph por loja)
src/app/[slug]/checkout/page.tsx    finalização
src/app/[slug]/opengraph-image.tsx  imagem de compartilhamento automática
src/app/api/revalidate/route.ts     atualização imediata do cache (protegida por segredo)
src/lib/schema.ts                   formato do store.json (validação zod)
src/lib/menu.ts · pricing.ts        cardápio e regras de preço (centavos, sem erro de arredondamento)
src/lib/order.ts                    carrinho → totais → mensagem → link wa.me
src/lib/hours.ts                    aberto/fechado no fuso da loja
src/lib/data.ts                     leitura Supabase (ou arquivos locais) — somente servidor
supabase/migrations/                tabelas, RLS, funções get_store_menu / admin_sync_store
scripts/                            comandos store:* do proprietário
stores/                             uma pasta por loja (JSON + imagens)
```

- **Multi-tenant:** todas as tabelas têm `store_id`; chaves estrangeiras compostas `(id, store_id)` impedem que um produto
  aponte para categoria/grupo de outra loja; cada página consulta apenas o `slug` acessado; o carrinho é salvo por loja.
- **RLS:** visitantes só leem lojas ativas e itens ativos; nenhuma escrita pública (políticas + `revoke`).
  Escrita só pela função `admin_sync_store`, executável apenas com a `service_role`.
- **Chaves:** o navegador não recebe nenhuma chave do Supabase (leitura acontece no servidor). A `service_role` existe
  só no seu `.env.local` para os scripts.
- **Performance:** páginas em cache (ISR, 60 s) com revalidação imediata após `store:sync`; imagens otimizadas pelo
  `next/image` (AVIF/WebP, tamanhos responsivos); uma única consulta ao banco por loja; sem bibliotecas pesadas.

## 10. Testes

```bash
npm test            # 44 testes: preços, carrinho, entrega, horários, mensagem e banco (Postgres real em memória)
npm run typecheck
npm run build
```

`tests/db` executa as migrações em um Postgres real (PGlite) simulando os papéis do Supabase e confirma: cadastro atômico
de várias lojas, separação entre lojas, RLS (anon não escreve, não vê loja inativa), bloqueio de vínculo entre lojas
e que o banco devolve exatamente o mesmo cardápio do arquivo JSON.
