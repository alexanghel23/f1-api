from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_driver_standings,
    retrieve_driver_standings_year

)
from server.models.driver_standings import (
    ErrorResponseModel,
    ResponseModel,
    DriverStandingsSchema,
)

router = APIRouter()

@router.get("/", response_description="Historical Driver standings retrieved")
async def get_driver_standings():
    driver_standings = await retrieve_driver_standings()
    if driver_standings:
        return ResponseModel(driver_standings, "Driver standings data retrieved successfully")
    return ResponseModel(driver_standings, "Empty list returned")


@router.get("/{year}", response_description = f"Historical Driver standings retrieved for year")
async def get_driver_standings_year(year):
    driver_standings = await retrieve_driver_standings_year(year)
    if driver_standings:
        return ResponseModel(driver_standings, "Driver standings data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")