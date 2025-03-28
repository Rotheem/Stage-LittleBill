import { useQuery } from '@tanstack/react-query'
import type { GetClients } from '../types/types'
import { useBackendUrl } from './useBackendUrl';

export const useClients = () => {
    const backendUrl = useBackendUrl();
    const { data, isLoading, refetch } = useQuery<GetClients>({
        queryKey: ['clients'],
        queryFn: async () => {
            const response = await fetch(backendUrl + '/clients');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        },
        retry: 0,
        enabled: true,
    }
    );

    return {
        clients: data ?? [],
        isLoading,
        refetch,
    };
}