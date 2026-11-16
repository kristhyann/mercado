/** npm run store:validate -- <slug>   |   npm run store:validate -- --all */
import { listSlugs, positional, validate, die } from "./_shared";

const slugs = positional().length ? positional() : listSlugs();
if (!slugs.length) die("Nenhuma loja encontrada em /stores.");
const bad = slugs.filter((s) => !validate(s));
process.exit(bad.length ? 1 : 0);
