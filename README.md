# Shiny for Python Framework

### Running the shiny app

To run this app, run the following commands 

* Create a project directory 

```
cd your_project_directory
```

* Clone the repository

```
git clone https://github.com/mwangi-george/Shiny-for-Python.git
```

* Navigate to the app directory

```
cd your_project_directory/Shiny-for-Python
```

* Create a virtual environment and activate it

```
python -m venv .venv
```

* Activate virtual environment

for windows powershell

```
.venv/Scripts/activate
```

for linux

```
source .venv/Scripts/activate
```


* Install dependencies (This may take a couple of minutes)

```
pip install -r dashboard/requirements.txt
```

* Launch application 

```
shiny run --reload --launch-browser dashboard/app.py
```

This should start the app at http://127.0.0.1:8000/