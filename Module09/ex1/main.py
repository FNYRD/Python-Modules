#!/usr/bin/env python3
try:
    from alien_contact import AlienContact
    from data_generator.data_generator import AlienContactGenerator
    from data_generator.data_generator import DataConfig
    from typing import List, Dict, Any
    from pydantic import ValidationError
except ImportError as e:
    print(f"An error happened importing the modules\n{e}")


def main() -> None:
    try:
        print("Alien Contact Log Validation")
        print("======================================")
        print("Valid contact report:")
        data_config: DataConfig = DataConfig()
        data: AlienContactGenerator = AlienContactGenerator(data_config)
        rawdata: List[Dict[str, Any]] = data.generate_contact_data(1)
        contact1: AlienContact = AlienContact.model_validate(rawdata[0])
        print(f"ID: {contact1.contact_id}\n"
              f"Type: {contact1.contact_type.value}\n"
              f"Location: {contact1.location}\n"
              f"Signal: {contact1.signal_strength}/10\n"
              f"Duration: {contact1.duration_minutes} minutes\n"
              f"Witnesses: {contact1.witness_count}\n"
              f"Message: {contact1.message_received}")
        print("======================================")
        print("Expected validation error:")
        rawdata = data.generate_contact_data(1)
        rawdata[0]['contact_type'] = 'telepathic'
        rawdata[0]['witness_count'] = 1
        contact2: AlienContact = AlienContact.model_validate(rawdata[0])
        print(contact2.contact_id)
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg'].removeprefix('Value error, ')}")
    except ValueError as e:
        print(f"Error: one or more arguments didn't math the data type:\n{e}")
    except AttributeError as e:
        print(f"Error: You're trying to use an invalid attribute:\n{e}")
    except Exception as e:
        print(f"Error: Somthing went wrong:\n{e}")


if __name__ == "__main__":
    main()
