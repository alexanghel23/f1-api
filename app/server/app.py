from fastapi import FastAPI

from server.routes.driver_standings import router as DriverStandingsRouter

app = FastAPI()

app.include_router(DriverStandingsRouter, tags=["DriverStandings"], prefix="/DriverStandings")

app.include_router(DriverStandingsRouter, tags=["DriverStandings"], prefix="/DriverStandings")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
