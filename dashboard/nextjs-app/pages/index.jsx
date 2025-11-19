import useSWR from "swr";
import GraficoPrecos from "../components/GraficoPrecos";
import Header from "../components/Header";

const fetcher = (url) => fetch(url).then((r) => r.json());

export default function Home() {
    const apiBase = "/api";
    const { data, error, isLoading } = useSWR(`${apiBase}/hoteis?limit=200`, fetcher, { refreshInterval: 60000 });

    return (
        <main style={{ padding: 20 }}>
            <Header title="Dashboard Turismo — Preços de Hotéis" />

            <section style={{ marginTop: 20 }}>
                <h2>Resumo</h2>
                {error && <div className="card error">Erro ao carregar dados: {String(error)}</div>}
                {isLoading && <div className="card">Carregando dados...</div>}
                {!data && !error && isLoading === false && <div className="card">Nenhum dado disponível.</div>}
            </section>

            <section style={{ marginTop: 20 }}>
                <h2>Gráfico de Preços</h2>
                <GraficoPrecos dados={data || []} />
            </section>

            <section style={{ marginTop: 20 }}>
                <h2>Últimos hotéis coletados</h2>
                <div className="grid">
                    {(data || []).slice(0, 12).map((h, i) => (
                        <div key={i} className="card">
                            <strong>{h.nome || h.hotel}</strong>
                            <div>Preço: {h.preco ?? h.price ?? "—"}</div>
                            <div>Avaliação: {h.avaliacao ?? h.score ?? "—"}</div>
                            <div style={{ fontSize: 12, marginTop: 6 }}>
                                Fonte: {h.fonte ?? "—"} • {new Date(h.scraped_at || h.scrapedAt || Date.now()).toLocaleString()}
                            </div>
                            {h.link && (
                                <a href={h.link} target="_blank" rel="noreferrer" style={{ display: "block", marginTop: 6 }}>
                                    Ver anúncio
                                </a>
                            )}
                        </div>
                    ))}
                </div>
            </section>
        </main>
    );
}
