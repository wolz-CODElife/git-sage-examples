DB_HOST = "localhost"
DB_NAME = "customer_db"
DB_USER = "admin"
DB_PASSWORD = "SuperSecretPassword!"
API_KEY = "sk_test_51Q_FAKE_EXAMPLE_KEY_abc123"

def get_settings():
    return {
        "db_host": DB_HOST,
        "db_name": DB_NAME,
        "db_user": DB_USER,
        "db_pass": DB_PASSWORD,
        "api_key": API_KEY,
    }

if __name__ == "__main__":
    print("Loaded settings:", get_settings())
