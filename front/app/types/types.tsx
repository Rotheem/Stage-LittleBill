export type GetClient = {
    customers_id: string;
    last_name: string;
    first_name: string;
    email: string;
    company: string;
    loyalty_points: number;
};

export type GetClients = Array<GetClient>;

export type GetSale = {
    sale_id: number;
    completed_at: string;
    currency: string;
    total: string;
};

export type GetClientSales = Array<GetSale>;