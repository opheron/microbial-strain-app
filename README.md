# Using the App
### Installation
First, clone the repo. Then, in terminal navigate into the repo folder and install Poetry with this command:
```
- curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
If the above does not work, check here for more info on Poetry: https://pypi.org/project/poetry/

Then, do:
```
- poetry install
- poetry shell
- python setup_database.py
```

### Running the app
Do:
```
flask run
```

### Closing the app
Do:
Ctrl + C
```
exit
```

In your browser, navigate to: http://127.0.0.1:5000/


# Design decisions
- Working off the instructions to create core functionality and not consider extraneous features, I approached this as a barebones MVP and left the front-end as minimal as functionally reasonable.
- Creation date: Although I considered setting the creation date automatically, I ultimately chose to have a manually-entered date since the entity might have been created on a different date than the current day. Form validation and automated date-formatting would be an immediate next-step.
- I chose to use a SQL database because the relations seemed well-contrained. I added an id key field to each entity type in order to maintain uniqueness.
- I chose Sqlite instead of the usual Postgres to improve ease of installation of the app. With Postgres, the contains_plasmids and contains_genes fields would be foreign key stores and the snapgene_files fields would be file system paths.

# Next Steps
- Integrate into CI/CD pipeline and expand test coverage
- Deploy to staging/production
- Implement client-side and server-side form validation
- Implement data backup system
- Implement user authentication and permissions
- Complete CRUD actions
- Complete REST API
- Improve front-end UI/UX
- Improve file upload system to include multi-file uploads.