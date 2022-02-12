import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://root:example@localhost:27017/admin?authSource=admin&authMechanism=SCRAM-SHA-1"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.f1_raw

f1_driver_standings_collection = database.get_collection("f1_driver_standings")


# helpers 


def driver_standing_helper(driver_standing) -> dict:

    return {

        "id": str(driver_standing["_id"]),
        "Pos": int(driver_standing["Pos"]),
        "Nationality": str(driver_standing["Nationality"]),
        "Car": str(driver_standing["Car"]),
        "PTS": int(driver_standing["PTS"]),
        "FirstName": str(driver_standing["FirstName"]),
        "LastName": str(driver_standing["LastName"]),
        "ShortName": str(driver_standing["ShortName"]),
        "Year": int(driver_standing["Year"]),
    }


# Retrieve all driver standings present in the database

async def retrieve_driver_standings():
    driver_standings = []
    async for driver_standing in f1_driver_standings_collection.find():
        driver_standings.append(driver_standing_helper(driver_standing))
    return driver_standings

# Retrieve driver standings with a matching Year

async def retrieve_driver_standings_year(Year: int) -> dict:
    driver_standings = []
    cursor = f1_driver_standings_collection.find({"Year": Year})
    for document in await cursor.to_list(length=100):
        driver_standings.append(driver_standing_helper(document))
    return driver_standings