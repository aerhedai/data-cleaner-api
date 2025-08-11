# Data Cleaner API

The **Data Cleaner API** is a modular microservice that automates cleaning of tabular datasets.  
It removes duplicates, handles missing values, corrects data types, and standardises column names — preparing datasets for downstream analysis or modelling.  

This API is part of the **Aerhed AI Universal Dataset Agent** project, designed for composable, reusable dataset processing.

---

## Features

- 🚀 **REST API** for cleaning datasets  
- 📂 Supports **CSV**, **Excel**, **Parquet**, and **JSON**  
- 🧹 Removes duplicates & trims whitespace  
- 🛠 Handles missing values (drop or impute with defaults)  
- 🧾 Normalises column names to snake_case  
- ⚡ Fast & lightweight with **FastAPI**  
- 🧪 Built-in testing & CI/CD ready

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/aerhedai/data-cleaner-api.git
cd data-cleaner-api
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Run the API locally
```bash
uvicorn app.main:app --reload
```

Once running, visit:  
➡ **Swagger Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
➡ **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

---

## Example API Call

### Request
```bash
curl -X POST "http://127.0.0.1:8000/clean" \
-H "Content-Type: multipart/form-data" \
-F "file=@sample.csv"
```

### Response
```json
{
  "message": "Dataset cleaned successfully",
  "rows_before": 100,
  "rows_after": 95,
  "columns": ["name", "age", "city"],
  "download_url": "/downloads/cleaned_dataset.csv"
}
```

---

## File Structure
```
data-cleaner-api/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI entry point
│   ├── routes.py         # API endpoints
│   ├── services.py       # Cleaning logic
│   ├── utils.py          # Helper functions
│   └── config.py         # Settings & constants
├── tests/
│   ├── __init__.py
│   ├── test_routes.py    # Endpoint tests
│   └── test_services.py  # Cleaning logic tests
├── requirements.txt      # Dependencies
├── README.md             # Documentation
├── .gitignore
└── LICENSE
```

---

## Development Workflow

1. **Branching**  
   - `main` → stable production code  
   - `dev` → active development  
   - feature branches for new features: `feature/data-cleaning-options`

2. **Commits**  
   - Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):
     - `feat:` – new feature
     - `fix:` – bug fix
     - `docs:` – documentation only changes
     - `refactor:` – code change without functional impact
     - `test:` – adding or updating tests

3. **Pull Requests**  
   - Always open a PR from feature branch → `dev`
   - Use PR templates for clarity

4. **Testing**  
   - Run `pytest` locally before pushing
   - Ensure 80%+ test coverage

---

## Docker Deployment

### Build the image
```bash
docker build -t data-cleaner-api .
```

### Run the container
```bash
docker run -d -p 8000:8000 data-cleaner-api
```

---

## Contributing

We welcome contributions!  
Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Make your changes and write tests
4. Submit a pull request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
