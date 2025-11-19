import dynamic from "next/dynamic";
import { useMemo } from "react";

const Chart = dynamic(() => import("react-apexcharts"), { ssr: false });

export default function GraficoPrecos({ dados }) {
  // prepara séries (assume que dados tem campos preco e scraped_at)
    const series = useMemo(() => {
    if (!dados || dados.length === 0) return [{ name: "Preço (R$)", data: [] }];
    // ordena por scraped_at crescente e agrupa por dia (média)
    const map = {};
    dados.forEach((d) => {
        const ts = d.scraped_at || d.scrapedAt || d.scrapedAt || d.scraped_at;
        const date = ts ? new Date(ts).toLocaleDateString() : "N/D";
        const preco = parseFloat(String(d.preco ?? d.price ?? NaN).replace(",", "."));
        if (!isNaN(preco)) {
        map[date] = map[date] || { sum: 0, count: 0 };
        map[date].sum += preco;
        map[date].count += 1;
        }
    });
    const labels = Object.keys(map).sort((a,b)=> new Date(a)- new Date(b));
    const dataSerie = labels.map((label) => +(map[label].sum / map[label].count).toFixed(2));
    return [{ name: "Preço médio diário (R$)", data: dataSerie, labels }];
    }, [dados]);

    const labels = series[0]?.labels ?? [];

    const options = {
    chart: { toolbar: { show: true }, zoom: { enabled: true } },
    xaxis: { categories: labels },
    stroke: { curve: "smooth" },
    dataLabels: { enabled: false },
    tooltip: { theme: "dark" },
    };

    return (
    <div style={{ width: "100%", maxWidth: 1100 }}>
        <Chart options={options} series={series} type="line" height={380} />
    </div>
    );
}
