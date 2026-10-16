import os
from dotenv import load_dotenv
from pymongo import AsyncMongoClient

load_dotenv()

client = AsyncMongoClient(os.getenv("mongo_token"))
print("Connected with mongo")


db = client["hand_cricket"]
users = db["users"]


async def create_user(user_id, user_name):
    await users.update_one(
        {"_id": user_id},
        {
            "$setOnInsert": {
                "username": user_name,
                "matches": 0,
                "wins": 0,
                "losses": 0,
                "total_run": 0,
                "highst_run": 0,
                "wickets_taken": 0
            }
        },
        upsert=True
    )

async def update_stats(user_id, result=None, runs=0, wickets=0):
    inc = {"matches": 1, "total_run": runs, "wickets_taken": wickets}
    if result:
        inc[result] = 1

    await users.update_one(
        {"_id": user_id},
        {"$inc": inc, "$max": {"highst_run": runs}}
    )




async def get_stats(user_id):

    return await users.find_one({"_id": user_id})