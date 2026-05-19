#!/usr/bin/env python3
try:
    from data_generator.data_generator import CrewMissionGenerator
    from data_generator.data_generator import DataConfig
    from space_crew import CrewMember
    from space_crew import SpaceMission
    from typing import List, Dict, Any
    from pydantic import ValidationError
except ImportError as e:
    print(f"An error happened importing the modules\n{e}")


def main() -> None:
    try:
        print("Space Mission Crew Validation")
        print("=========================================")
        print("Valid mission created:")
        data_config: DataConfig = DataConfig()
        generator: CrewMissionGenerator = CrewMissionGenerator(data_config)
        member_data: List[Dict[str, Any]] = generator.generate_crew_member(1)
        member_data['member_id'] = 'M01'
        # This member's creation is just to demostrate that the model works
        member: CrewMember = CrewMember.model_validate(member_data)
        member.name
        # =================================================================
        mission_data: List[Dict[str, Any]] = generator.generate_mission_data()
        space_mission: SpaceMission
        space_mission = SpaceMission.model_validate(mission_data[0])
        print(f"Mission: {space_mission.mission_name}")
        print(f"ID: {space_mission.mission_id}")
        print(f"Destination: {space_mission.destination}")
        print(f"Duration: {space_mission.duration_days} days")
        print(f"Budget: ${space_mission.budget_millions}M")
        print(f"Crew size: {len(space_mission.crew)}")
        print("Crew members:")
        for member in space_mission.crew:
            print(f"- {member.name} ({member.rank.value}) "
                  f"- {member.specialization}")
        print("\n=========================================")
        for member in mission_data[1]['crew']:
            member['rank'] = 'cadet'
        space_mission_error: SpaceMission
        space_mission_error = SpaceMission.model_validate(mission_data[1])
        print(space_mission_error)
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg'].removeprefix('Value error, ')}")
    except ValueError as e:
        print(f"Error: one or more arguments didn't math the data type:\n{e}")
    except AttributeError as e:
        print(f"Error: You're trying to use an invalid attribute:\n{e}")
    except Exception as e:
        print(f"Error: Something went wrong:\n{e}")


if __name__ == "__main__":
    main()
