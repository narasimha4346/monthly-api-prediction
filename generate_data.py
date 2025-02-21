import json
import random
from datetime import datetime, timedelta

# Define the output JSON file path
OUTPUT_FILE = "test_reports.json"

def generate_sample_data():
    """Generates 500 sample test report entries and saves them to a JSON file."""
    data = []
    start_date = datetime(2023, 1, 1)

    for i in range(500):
        entry = {
            "id": i + 1,
            "projectName": f"Project-{random.randint(1, 10)}",
            "authors": f"Author-{random.randint(1, 5)}",
            "storyTests": random.randint(50, 200),
            "regressionTestsAutomated": random.randint(30, 150),
            "regressionTestsManual": random.randint(20, 100),
            "totalTestsByApplication": random.randint(100, 500),
            "storyPassed": random.randint(40, 150),
            "storyFailed": random.randint(0, 10),
            "storyUnexecuted": random.randint(0, 5),
            "storyBlocked": random.randint(0, 5),
            "storySkipped": random.randint(0, 5),
            "storyCritical": random.randint(0, 3),
            "storyNew": random.randint(0, 10),
            "storyUnused": random.randint(0, 5),
            "storyBugs": random.randint(0, 5),
            "arPassed": random.randint(30, 140),
            "arFailed": random.randint(0, 10),
            "arUnexecuted": random.randint(0, 5),
            "arBlocked": random.randint(0, 5),
            "arSkipped": random.randint(0, 5),
            "arCritical": random.randint(0, 3),
            "arNew": random.randint(0, 10),
            "arUnused": random.randint(0, 5),
            "arBugs": random.randint(0, 5),
            "mrPassed": random.randint(20, 90),
            "mrFailed": random.randint(0, 10),
            "mrUnexecuted": random.randint(0, 5),
            "mrBlocked": random.randint(0, 5),
            "mrSkipped": random.randint(0, 5),
            "mrCritical": random.randint(0, 3),
            "mrNew": random.randint(0, 10),
            "mrUnused": random.randint(0, 5),
            "mrBugs": random.randint(0, 5),
            "createdAt": (start_date + timedelta(days=i * 7)).isoformat()
        }
        data.append(entry)

    # Save the data to a JSON file
    with open(OUTPUT_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Generated {len(data)} sample entries in {OUTPUT_FILE}")

# Run the function if the script is executed directly
if __name__ == "__main__":
    generate_sample_data()
