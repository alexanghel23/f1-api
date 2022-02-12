from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class DriverStandingsSchema(BaseModel):
    Pos: int = Field(...)
    Nationality: str = Field(...)
    Car: str = Field(...)
    PTS: int = Field(...)
    FirstName: str = Field(...)
    LastName: str = Field(...)
    ShortName: str = Field(...)
    Year: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "Pos": 1,
                "Nationality": "ROU",
                "Car": "Dacia",
                "PTS": 500,
                "FirstName": "Alex",
                "LastName": "Anghel",
                "ShortName": "ANG",
                "Year": 2022,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
