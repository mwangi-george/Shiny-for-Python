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

* Create a virtual environment and activate it

```
python -m venv .venv

.venv/Scripts/activate
```

* Install dependencies 

```
pip install -r dashbord/requirements.txt
```

* Launch application 

```
shiny run --reload --launch-browser dashboard/app.py
```