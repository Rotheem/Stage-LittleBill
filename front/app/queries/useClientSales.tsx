import { useQuery } from '@tanstack/react-query'
import type { GetClientSales } from '../types/types'
import { useBackendUrl } from './useBackendUrl';

export const useClientSales = (clientId: string) => {
    const backendUrl = useBackendUrl();
    const { data, isLoading, refetch } = useQuery<GetClientSales>({
        queryKey: ['sales', clientId],
        queryFn: async () => {
            const response = await fetch(backendUrl + '/clients/' + clientId + '/sales');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        },
        retry: 3,
        enabled: !!clientId,
    }
    );

    return {
        sales: data ?? [],
        isLoading,
        refetch,
    };
}