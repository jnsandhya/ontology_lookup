# Ontology Lookup

**Ontology Lookup** is a command-line tool and Python package that interacts with the [Ontology Lookup Service (OLS) API](https://www.ebi.ac.uk/ols/docs/api) to fetch details about a specific ontology. Given an ontology ID, it returns details such as the title, description, number of terms, and status.

## Features

- Retrieves ontology information by ontology ID
- Displays ontology title, description, term count, and status
- Command-line interface (CLI) for easy access
- Extensible design for further development and integration

## Requirements

- Python 3.6 or higher
- `requests` library (installable via `requirements.txt`)

## Installation

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/username/ontology_lookup.git
cd ontology_lookup
```

### Install Dependencies
It’s recommended to use a virtual environment. Install dependencies using requirements.txt:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirement.txt
```
Alternatively, you can install the package in editable mode (to directly use the package’s dependencies specified in setup.py):
```bash
pip install -e .
```
## Usage
The ontology_lookup package can be used as a command-line tool. Provide an ontology ID to retrieve information about the ontology.

Command-Line Usage
After installation, you can use the command-line tool ontology-lookup as follows:
```bash
ontology-lookup <ontology_id>
```
### Example
```bash
ontology-lookup efo
```
### Output:
```yaml
Ontology Details:
  Title: Experimental Factor Ontology
  Description: The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables available in EBI databases, and for external projects such as the NHGRI GWAS catalogue. It combines parts of several biological ontologies, such as anatomy, disease and chemical compounds. The scope of EFO is to support the annotation, analysis and visualization of data handled by many groups at the EBI and as the core ontology for OpenTargets.org
  Number of Terms: 57806
  Status: LOADED
```

## Library Usage
You can also use ontology_lookup programmatically in your Python code.

```python
from ontology_lookup.main import OntologyService
# Create an instance of OntologyService with an ontology ID
service = OntologyService("efo")

# Fetch ontology details
details = service.fetch_ontology_details()
print(details)
```

## Development
If you want to contribute to the development of this package, please follow these steps:

Fork this repository.
Create a new branch for your feature or bugfix.
Make your changes and commit them with descriptive messages.
Push your branch to your fork.
Submit a pull request with a description of your changes.
Running Tests
Ensure that all dependencies are installed, 

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or issues, please reach out through the repository’s issue tracker.

## Explanation

- **Introduction**: Briefly explains the package’s purpose.
- **Installation**: Provides instructions for setting up a virtual environment, installing dependencies, and installing the package in editable mode.
- **Usage**: Describes both command-line and programmatic usage.
- **Development**: Includes instructions for contributing and testing.
- **License**: Specifies the license (assuming MIT, as per common open-source practice).
- **Contact**: Suggests using the issue tracker for questions.








