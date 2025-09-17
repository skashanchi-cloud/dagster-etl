Dagster ETL Monorepo

This repository hosts multiple ETL pipelines built with Dagster
.
Each ETL lives under the projects/
 directory and is managed as a modular Dagster code location.

The repo is structured so you can run and test pipelines locally, and then deploy them seamlessly to Dagster Cloud.

🚀 Getting Started
1. Clone the repository
git clone https://github.com/skashanchi-cloud/dagster-etl.git
cd dagster-etl

2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

3. Install dependencies
pip install -e ".[dev]"

4. Run Dagster locally
dagster dev


Then open http://localhost:3000
 in your browser to explore assets, jobs, and runs.

📂 Repository Structure
dagster-etl/
├─ projects/              # Each ETL lives here
│   └─ test_etl/          # Example ETL project
│      ├─ assets.py       # Asset (extract/transform/load) definitions
│      ├─ definitions.py  # Dagster Definitions entrypoint
│      └─ __init__.py
├─ pyproject.toml         # Python project + Dagster config
├─ setup.py               # Packaging config
├─ setup.cfg              # Linting/test configs
├─ README.md              # This file
└─ .gitignore             # Ignore venv, caches, etc.


projects/ → Container for all ETL subprojects. Add new ETLs here (e.g., sales_etl, marketing_etl).

assets.py → Define extract, transform, and load logic as Dagster assets.

definitions.py → Collect assets and define the Dagster Definitions object.

pyproject.toml → Includes [tool.dagster] pointing to the ETL definitions.

🧪 Development
Adding Dependencies

Add Python dependencies in pyproject.toml under [project.dependencies] and reinstall:

pip install -e .

Running Tests

Tests for each ETL can live inside its own folder or in a central tests/ directory:

pytest

☁️ Deployment to Dagster Cloud

Push this repo to GitHub (already done ✅).

Connect the repo to your Dagster Cloud workspace.

Dagster Cloud will use the pyproject.toml [tool.dagster] block to discover code locations.

Each ETL in projects/ can be materialized, scheduled, and monitored from Dagster Cloud.

For more details, see Dagster Cloud deployment docs
.

🔮 Roadmap

Add more ETLs under projects/

Configure sensors/schedules for automation

CI/CD integration with GitHub Actions for automated deploys
