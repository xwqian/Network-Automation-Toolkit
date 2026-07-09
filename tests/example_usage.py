from modules.resource_manager import managed_test_resource

def setup_db(): return "DB_CONNECTION_HANDLE"
def cleanup_db(handle): print(f"Closing {handle}")

def test_workflow():
    with managed_test_resource("Database-Layer", setup_db, cleanup_db) as db:
        print(f"Executing queries with {db}")
        # Test logic goes here

if __name__ == "__main__":
    test_workflow()
