import { NavLink, redirect } from "react-router";
import type { GetClient } from "../../types/types";
import "./card.css";

export function ClientCard({ client }: { client: GetClient }) {
    return <NavLink to={`/client/${client.customers_id}`} className="ClientCard" >
        <div>
            <p>Nom Prénom :</p> <p>{client.last_name} {client.first_name}</p>
        </div>
        {client.company != "" ?
            <div>
                <p>Email :</p> <p>{client.email}</p>
            </div>
            : <div></div>}
        <div>
            <p>Ponts fidélité :</p> <p>{client.loyalty_points}</p>
        </div>
    </NavLink>;
}