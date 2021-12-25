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
## RE-Design
  Several files contain import statements which must be modified to 
reference the appName  - ie: the name of the app package 
containing __init__.py 

I tried appending those - but that's flakey and one of them has an 
imbedded import, ... 

So, I'm changing to have generate methods for each of these file

The files are: 
  - appRun - bash - contains exports and flask run
  - appStart.py - a one liner what imports app from appPkg
  - routes.py - must have from appPkg import app
Each of these will have a method gen_xxx and will load a file from resources
  - to allow the user to customize - these files will be named appRun.sh.template,
appStart.py.template and routes.py.template