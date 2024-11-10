from setuptools import setup, find_packages

setup(
    name="ontology-lookup",
    version="0.1.0",
    description="Command-line tool to fetch ontology details from Ontology Lookup Service",
    author="Sandhya Jain",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "ontology-lookup=ontology_lookup.main:main",
        ],
    },
    python_requires=">=3.6",
)
