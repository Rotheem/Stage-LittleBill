import { useState } from "react";
import { ClientCard } from "../components/client_card";
import "./main.css";
import { useClientsSearch } from "~/queries/useClientsSearch";


export function MainPage() {
  const [globalFilter, setGlobalFilter] = useState("");

  const { clients } = useClientsSearch(globalFilter);


  return (
    <main className="main">
      <h1>Recherche</h1>
      <input type="text" onChange={(e) => setGlobalFilter(e.target.value)} placeholder="Rechercher un client" />
      {globalFilter.length < 4 && <p>Entrez au moins 4 caractères</p>}
      {globalFilter.length >= 4 && <div className="sep"><h1>Résultat</h1>
        {clients.map((client) => (
          <ClientCard client={client} />
        ))}</div>}
    </main>
  );
}
