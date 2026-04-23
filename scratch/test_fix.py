
import os
import sys

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.gbif.api import GbifApi
from src.models.entrypoints import GBIFOccurrenceSearchParams

def test_event_date_range():
    api = GbifApi()
    params = GBIFOccurrenceSearchParams(
        taxonKey=[2431920],
        eventDate=["2025-06-01", "2025-08-31"],
        decimalLatitude="44.12,44.32",
        decimalLongitude="-122.32,-122.12",
        hasCoordinate=True
    )
    
    url = api.build_occurrence_search_url(params)
    print(f"Generated URL: {url}")

    # Note: urlencode converts ',' to '%2C'
    if "eventDate=2025-06-01%2C2025-08-31" in url:
        print("SUCCESS: eventDate is correctly formatted as a range (URL encoded).")
    elif "eventDate=2025-06-01&eventDate=2025-08-31" in url:
        print("FAILURE: eventDate is still being repeated.")
    else:
        print("FAILURE: Unknown format.")

if __name__ == "__main__":
    test_event_date_range()
