import redis
import os

print("--- Starting Redis Connection Test ---")

# --- Connection Parameters ---
# Use the credentials we confirmed are correct
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 1
REDIS_PASSWORD = "infini_rag_flow"

try:
    print(f"Attempting to connect to Redis at {REDIS_HOST}:{REDIS_PORT}...")
    
    # Create a Redis client
    r = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PASSWORD,
        decode_responses=True  # Important for getting string responses
    )
    
    # Ping the server
    r.ping()
    
    print("✅ Connection SUCCESSFUL!")

except redis.exceptions.AuthenticationError as e:
    print(f"❌ Connection FAILED: AuthenticationError - {e}")
    print("   This means the password is wrong.")

except redis.exceptions.ConnectionError as e:
    print(f"❌ Connection FAILED: ConnectionError - {e}")
    print("   This means the script could not reach the Redis server at the specified host/port.")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

finally:
    print("--- Test Complete ---")
