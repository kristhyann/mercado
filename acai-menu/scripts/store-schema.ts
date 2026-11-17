/** Gera stores/store.schema.json (autocompletar e validação no VS Code). */
import fs from "node:fs";
import path from "node:path";
import { z } from "zod";
import { storeConfigSchema } from "../src/lib/schema";
import { STORES, c } from "./_shared";

const schema = z.toJSONSchema(storeConfigSchema, { io: "input", unrepresentable: "any" });
fs.writeFileSync(path.join(STORES, "store.schema.json"), JSON.stringify(schema, null, 2) + "\n");
c.ok("stores/store.schema.json gerado");
