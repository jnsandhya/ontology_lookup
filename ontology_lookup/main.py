import requests
import argparse

class OntologyService:
    BASE_URL = "https://www.ebi.ac.uk/ols/api/ontologies"

    def __init__(self, ontology_id):
        self.ontology_id = ontology_id

    def fetch_ontology_details(self):
        url = f"{self.BASE_URL}/{self.ontology_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as err:
            return {"error": f"Request error occurred: {err}"}

        if response.status_code == 200:
            data = response.json()
            return {
                "Title": data.get("config", {}).get("title", "N/A"),
                "Description": data.get("config", {}).get("description", "N/A"),
                "Number of Terms": data.get("numberOfTerms", "N/A"),
                "Status": data.get("status", "N/A"),
            }
        else:
            return {"error": "Ontology ID not recognized or service unavailable."}

    def display_details(self):
        details = self.fetch_ontology_details()
        if "error" in details:
            print(f"Error: {details['error']}")
        else:
            print("Ontology Details:")
            print(f"  Title: {details['Title']}")
            print(f"  Description: {details['Description']}")
            print(f"  Number of Terms: {details['Number of Terms']}")
            print(f"  Status: {details['Status']}")

def main():
    parser = argparse.ArgumentParser(description="Fetch Ontology details using Ontology Lookup Service API.")
    parser.add_argument("ontology_id", type=str, help="The ontology ID to fetch information for.")
    args = parser.parse_args()

    service = OntologyService(args.ontology_id)
    service.display_details()

if __name__ == "__main__":
    main()
