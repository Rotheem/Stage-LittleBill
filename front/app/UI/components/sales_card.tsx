import type { GetSale } from "~/types/types";
import "./card.css";

export function SaleCard({ sale }: { sale: GetSale }) {
    return (
        <div className="SalesCard">
            <div className="SalesCard-body">
                <h5 className="SalesCard-title">Sale {sale.sale_id}</h5>
                <p className="SalesCard-text">Date: {sale.completed_at}</p>
                <p className="SalesCard-text">Total: {sale.total} {sale.currency}</p>
            </div>
        </div>
    );
}