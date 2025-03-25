import logging
from fastapi import APIRouter, Depends, Query
from app.hiboutik_api import HiboutikAPI, get_hiboutik_api


router = APIRouter(
    tags=["clients"],
)

logger = logging.getLogger("logger")


@router.get("/clients")
async def read_clients(
    hiboutik: HiboutikAPI = Depends(get_hiboutik_api),
):
    return hiboutik.get("customers")


@router.get("/clients/search")
async def read_clients_with_filter(
    name: str = Query(None),
    hiboutik: HiboutikAPI = Depends(get_hiboutik_api),
):
    return hiboutik.get("customers/search", params={"last_name": name})


@router.get("/clients/{client_id}")
async def read_client(
    client_id: str,
    hiboutik: HiboutikAPI = Depends(get_hiboutik_api),
):
    return hiboutik.get(f"customer/{client_id}")


@router.get("/clients/{client_id}/sales")
async def read_client_sales(
    client_id: str,
    page: int = Query(1),
    hiboutik: HiboutikAPI = Depends(get_hiboutik_api),
):
    sales = hiboutik.get(f"customer/{client_id}/sales")
    return sales[(page - 1) * 5 : min(page * 5, len(sales))]
