export default function Header({ title }) {
    return (
    <header style={{ display: "flex", alignItems: "center", gap: 16 }}>
        <div style={{ width: 54, height: 54, background: "#0ea5a8", borderRadius: 8 }} />
        <div>
        <h1 style={{ margin: 0 }}>{title}</h1>
        <small style={{ color: "#555" }}>Dados extraídos automaticamente — atualizado periodicamente</small>
        </div>
    </header>
    );
}
