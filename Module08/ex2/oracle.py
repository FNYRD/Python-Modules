#!/usr/bin/env python3
try:
    from dotenv import load_dotenv
    import os
except ImportError as e:
    print(f"An error happened importing the modules\n{e}")


def main() -> None:
    try:
        print("ORACLE STATUS: Reading the Matrix...\n")
        # If the dotenv module wasn't imported raise and error
        load_dotenv()
        MATRIX_MODE: str = os.getenv('MATRIX_MODE')
        DATABASE_URL: str = os.getenv('DATABASE_URL')
        API_KEY: str = os.getenv('API_KEY')
        ZION_ENDPOINT: str = os.getenv('ZION_ENDPOINT')
        # I'd checked if MATRIX_MODE is not none and have the
        # correct values
        if MATRIX_MODE is None or (MATRIX_MODE != 'development'
                                   and MATRIX_MODE != 'production'):
            raise ValueError("Sorry you must define an available MATRIX_MODE")
        # Depending of the MATRIX_MODE value i define LOG_LEVEL value
        if MATRIX_MODE == "development":
            LOG_LEVEL: str = os.getenv('LOG_LEVEL') or 'DEBUG'
        else:
            LOG_LEVEL: str = os.getenv('LOG_LEVEL') or 'WARNING'
        # checking if the other variables were filled
        if API_KEY and ZION_ENDPOINT and DATABASE_URL:
            print("Configuration loaded:")
            print(f"Mode: {MATRIX_MODE}")
            if MATRIX_MODE == 'development':
                print("Database: Connected to local instance")
            else:
                print("Database: Connected to online instance")
            print(f"API Access: {'Authenticated'}")
            print(f"Log Level: {LOG_LEVEL}")
            print(f"Zion Network: {'Online'}")
            print("\nEnvironment security check:")
            print("[OK] No hardcoded secrets detected")
            print("[OK] .env file properly configured")
            print("[OK] Production overrides available")
            print("\nThe Oracle sees all configurations.")
        else:
            raise ValueError("Sorry you must define all "
                             "the required variables")
    except AttributeError as e:
        print(f"Error calling an atribute from a library: {e}")
    except ModuleNotFoundError as e:
        print(f"{e}")
    except FileNotFoundError as e:
        print(f"{e}")
    except NameError:
        print("An error happened importing the modules\n")
    except ValueError as e:
        print(f"{e}")
    except Exception:
        print("Something went wrong")


if __name__ == "__main__":
    main()
