import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://root:example@localhost:27017/admin?authSource=admin&authMechanism=SCRAM-SHA-1"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.f1_raw

f1_driver_standings_collection = database.get_collection("f1_driver_standings")


# helpers 


def driver_standing_helper(driver_standing) -> dict:
    return {
        "Pos": driver_standing["Pos"],
        "Nationality": driver_standing["Nationality"],
        "Car": driver_standing["Car"],
        "PTS": driver_standing["PTS"],
        "FirstName": driver_standing["FirstName"],
        "LastName": driver_standing["LastName"],
        "ShortName": driver_standing["ShortName"],
        "Year": driver_standing["Year"],
    }


# Retrieve all driver_standings present in the database

async def retrieve_driver_standings():
    driver_standings = []
    async for driver_standing in f1_driver_standings_collection.find():
        driver_standings.append(driver_standing)
    return driver_standings