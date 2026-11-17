/**
 * Cria (ou promove) o administrador do painel. Execute no seu computador:
 *   npm run admin:create -- voce@email.com "uma-senha-forte"
 * Usa a SUPABASE_SERVICE_ROLE_KEY do .env.local (nunca vai para a Vercel).
 * Para revogar:  npm run admin:create -- voce@email.com --remove
 */
import { admin, arg, c, die, positional } from "./_shared";

(async () => {
  const [email, password] = positional();
  if (!email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) die('Uso: npm run admin:create -- <email> "<senha>"   |   <email> --remove');
  const sb = admin();

  // Procura o usuário existente.
  let userId: string | null = null;
  for (let page = 1; page < 50 && !userId; page++) {
    const { data, error } = await sb.auth.admin.listUsers({ page, perPage: 200 });
    if (error) die(error.message);
    userId = data.users.find((u) => u.email?.toLowerCase() === email.toLowerCase())?.id ?? null;
    if (data.users.length < 200) break;
  }

  if (arg("--remove")) {
    if (!userId) die("Usuário não encontrado.");
    const { error } = await sb.from("platform_admins").delete().eq("user_id", userId);
    if (error) die(error.message);
    return c.ok(`${email} não é mais administrador.`);
  }

  if (!userId) {
    if (!password || password.length < 10) die("Informe uma senha com pelo menos 10 caracteres.");
    const { data, error } = await sb.auth.admin.createUser({ email, password, email_confirm: true });
    if (error) die(error.message);
    userId = data.user.id;
    c.ok(`Usuário criado: ${email}`);
  } else if (password) {
    if (password.length < 10) die("A senha precisa ter pelo menos 10 caracteres.");
    const { error } = await sb.auth.admin.updateUserById(userId, { password });
    if (error) die(error.message);
    c.ok("Senha atualizada.");
  }

  const { error } = await sb.from("platform_admins").upsert({ user_id: userId, email });
  if (error) die(`${error.message}\nVocê executou supabase/migrations/0003_admin_panel.sql?`);
  c.ok(`${email} agora é administrador do painel. Acesse /admin/login`);
})();
