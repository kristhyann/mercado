import { requireAdminPage } from "@/lib/admin/auth";
import { AdminShell } from "@/components/admin/AdminShell";

export default async function PainelLayout({ children }: { children: React.ReactNode }) {
  const session = await requireAdminPage();
  return (
    <AdminShell email={session.email} mode={session.mode}>
      {children}
    </AdminShell>
  );
}
