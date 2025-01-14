from pymongo import MongoClient
import redis

# MongoDB setup
MONGO_URI = "mongodb+srv://user:123@atlascluster.pnicp6n.mongodb.net/"
mongo_client = MongoClient(MONGO_URI)
db = mongo_client["whatsapp_bot_db"]

# Redis setup (for temporary data storage if needed)
REDIS_URL = "rediss://:AX1rAAIjcDFlMGI5OTU0ZThlZDE0MmViODgxM2JjOTJjMDM3MzVjMXAxMA@mighty-starling-32107.upstash.io:6379" 
redis_client = redis.from_url(REDIS_URL)
