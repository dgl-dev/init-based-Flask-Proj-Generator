# init-based-Flask-Proj-Generator
Flask Proj skeleton generator based on Flask MEGATutorial by Miguel Grinberg

## Purpose
Flask projects structured as taught in this tutorial are extensible and 
understandable,
This generator addresses a point of confusion - having different things
(the Flask application and the package) with the same name "app"

### From the tutorial

    Remember the two app entities? 
    Here you can see both together in the same sentence. 
    The Flask application instance is called app and is a member of the 
    app package. 
    The from app import app statement imports the app variable that is 
    a member of the app package. If you find this confusing, you can
    rename either the package or the variable to something else.

    Just to make sure that you are doing everything correctly, 
    below you can see a diagram of the project structure so far:

    microblog/
      venv/
      app/
        __init__.py
        routes.py
      microblog.py

## Design
  1. Gather input
     1. Project name
     2. App name
     3. Requirements.txt - defaults to ???
     4. ?