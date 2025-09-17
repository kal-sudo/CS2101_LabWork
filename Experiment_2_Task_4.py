org_structure = {
    "Visitor": {
        "Board of Governors": {
            "Director": {
                "HOD-CSE/ECE/Sciences/Humanities and management": {},
                "Chief Warden": {
                    "Hostel Warden": {}
                },
                "FIC": {},
                "Coordinators-Training &Placement, Institute Website and Email Services, ERP": {},
                "Professor": {
                    "Associate Professor": {
                        "Assistant Professor": {
                            "Dr. Bharat Singh": {"department": "CSE"},
                            "Dr. Shashi Kant": {"department": "Mathematics"},
                            "Dr. Ranjan Behera": {"department": "CSE"},
                            "Dr. Ravi Shanker": {"department": "ECE"}
                        }
                    }
                }
            },
            "Finance Committee": {
                "Registrar": {
                    "Joint Registrar/Deputy Registrar": {
                        "Assistant Registrar": {}
                    }
                },
                "Associate Dean Faculty Affairs": {}
            },
            "Building & Works Committee": {
                "Associate Dean R&D": {},
                "Associate Dean Student Affairs": {}
            },
            "Senate": {
                "Associate Dean Academic Affairs": {
                    "Examination Coordinator": {}
                }
            }
        }
    }
}


def find_professor_department(org_chart, prof_name):
    if isinstance(org_chart, dict):
        if "department" in org_chart:
            return org_chart.get("department")
        else:
            for key, value in org_chart.items():
                if key == prof_name:
                    if isinstance(value, dict) and "department" in value:
                        return value["department"]
                result = find_professor_department(value, prof_name)
                if result:
                    return result
    return None

def main():
    professor_name = input("Enter the name of the Assistant Professor: ").strip()
    professors = {
        "Dr. V. N. S. R. Bupathi": {"department": "CSE"},
        "Dr. Arpita Tulsyan": {"department": "CSE"},
        "Dr. Nitesh Kumar": {"department": "ECE"},
        "Dr. Mukesh Kumar": {"department": "ECE"}
    }
    
    found_department = professors.get(professor_name)

    if found_department:
        print(f"The department for {professor_name} is: {found_department['department']}")
    else:
        print(f"Assistant Professor '{professor_name}' not found.")
