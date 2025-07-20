import json
from collections import defaultdict
from datetime import datetime

# Path to the JSON file
json_file = 'sample-weather-history.json'

def main():
    # Dictionary to store unique days per year
    days_per_year = defaultdict(set)

    with open(json_file, 'r') as f:
        data = json.load(f)

    for entry in data:
        # Try to extract the date field
        date_str = entry.get('date')
        if not date_str:
            continue
        try:
            # Parse the date (assuming ISO format)
            date_obj = datetime.fromisoformat(date_str)
            year = date_obj.year
            day = date_obj.date()
            days_per_year[year].add(day)
        except Exception:
            continue

    # Print the number of unique days per year
    for year in sorted(days_per_year):
        print(f"{year}: {len(days_per_year[year])} days")

if __name__ == "__main__":
    main()



