import { NavLink, useParams } from "react-router";
import { useClientSales } from "~/queries/useClientSales";
import { SaleCard } from "../components/sales_card";
import "./client_detail.css";
import { useClients } from "~/queries/useClients";

export function ClientDetailPage() {
    let params = useParams();
    const client_id = params.clientId ?? "";
    const { clients } = useClients();
    const client = clients.find((client) => client.customers_id == client_id);

    const { sales } = useClientSales(client_id);

    return (
        <main>
            <NavLink to="/">
                <button>Back</button>
            </NavLink>
            <div className="ClientDetail">
                <h1>Detail du client</h1>
                <div className="ClientInfo">
                    <span className="font-semibold">Nom : </span>{client?.first_name} {client?.last_name}<br />
                    <span className="font-semibold">Email : </span>{client?.email}<br />
                    {client?.company != "" && <p>  <span className="font-semibold">Entreprise : </span>{client?.company}</p>}
                    <span className="font-semibold">Ponts fidélité : </span>{client?.loyalty_points}
                </div>
                <h1>Ventes</h1>
                <div>
                    {sales.map((sale) => (
                        <SaleCard sale={sale} />
                    ))}
                </div>
            </div>
        </main >
    );
}
