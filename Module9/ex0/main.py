#!/usr/bin/env python3
try:
    from space_station import SpaceStation
    from data_generator.data_generator import SpaceStationGenerator
    from data_generator.data_generator import DataConfig
    from typing import List, Dict, Any
    from pydantic import ValidationError
except ImportError as e:
    print(f"An error happened importing the modules\n{e}")


def main() -> None:
    try:
        data_config: DataConfig = DataConfig()
        data = SpaceStationGenerator(data_config)
        rawdata: List[Dict[str, Any]] = data.generate_station_data(1)
        station1: SpaceStation = SpaceStation.model_validate(rawdata[0])
        status: str = ''
        status = 'Operational' if station1.is_operational else 'Inoperational'
        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        print(f"ID: {station1.station_id}\nName: {station1.name}\n"
              f"Crew: {station1.crew_size} people\n"
              f"Power: {station1.power_level}%\n"
              f"Oxygen: {station1.oxygen_level}%\n"
              f"Status: {status}")
        print("\n========================================")
        station2: SpaceStation = SpaceStation(
                                    station_id='QCH189',
                                    name='Deep Space Observatory',
                                    crew_size=28, power_level=70.8,
                                    oxygen_level=88.1,
                                    last_maintenance='2023-08-24T00:00:00',
                                    is_operational=False,
                                    notes='System diagnostics required'
                                    )
        print(station2)
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg'].removeprefix('Value error, ')}")
    except ValueError as e:
        print(f"Error: one or more arguments didn't math the data type:\n{e}")
    except AttributeError as e:
        print(f"Error: You're trying to use an invalid attribute:\n{e}")
    except Exception as e:
        print(f"Erro: Somthing went wrong:\n{e}")


if __name__ == "__main__":
    main()
