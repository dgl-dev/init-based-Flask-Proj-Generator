"""
IbFgen
"""
import os


def flake8_check(proj):
    pass


def generate(proj):
    """
    Generates the proj directory structure

    Creates the directories and initializes the html

    Checks names with flake8

    Args:
        proj (dict): A dictionary
        keys:   projName,       # [R] The name of the proj
                appName,            # The app name
                pageList,               # [R] A list (a,b,...) of page names
                navbar,                     # [R] Selector D or H - Default or Hamburger navbar
                root,                          # [R] root dir for proj
                resources,               # [O] Directory containing default contents.
                            If user specifies this, it is pre-pended to default
                            resources

    Returns:
        type: Tree of the Project

    Raises:
        Exception: None

    """
    import os
    import subprocess
    import shutil
    import touch

    from pprint import pprint
    
    if os.path.exists(proj["projRoot"]):
        os.chdir(proj["projRoot"])  # move to the proj root
        #print("rm -rf " + proj["projName"])
        os.system("rm -rf " + proj["projName"])
        os.mkdir(proj["projName"])  # create the proj dir
        os.chdir(proj["projName"])  # move to the proj dir
        os.mkdir('templates')  # make the templates directory
        os.mkdir('static')  # make the static dir
        os.chdir('static')  # move to static dir
        os.mkdir('css')  # make the css dir
        os.mkdir('img')  # make the img dir
        os.mkdir('js')  # make the js dir
        os.chdir('css')  # move to the css dir
        touch.touch('style.css')  # create the style.css file
        os.chdir('../js')  # backup and down to js dir
        touch.touch('script.js')  # create the script.js file
        os.chdir('../img')  # backup and down to img dir
        # print(f"wtfaw: {os.getcwd()}")
        # print(f"isDir?: {os.path.isdir('.')}")
        # print(f"path of jpg: {proj['cwd'] + '/resources/bg.jpg'}")
        shutil.copy(proj['cwd'] + '/resources/bg.jpg', ".")  # copy the default bg.jpg image
        #os.system('ls')


        os.chdir('../../templates')  # backup and down to templates dir
        touch.touch('base.html')  # create base.html -the BS master
        touch.touch('index.html')  # create index.html
        touch.touch('contact.html')  # create contact.html

    else:
        print('Error: proj root does not exist.')

    
def main():
    from pathlib import Path

    proj = {
        "projRoot": "",  # Full path to target dir or work area
        "projName": "",  # valid Flask project name
        "appName" : "",  # valid Flask app name
        "rqmts"   : "",  # Full path to requirements.txt - see README for default if ""
        'pgList'  : []  # List of page names
        # ??????
    }

    print(f"Welcome to IbFgen")
    print(proj)

    proj["projName"] = input("Enter valid python proj name: ")
    proj["appName"] = input("Enter valid Flask package name: ")
    proj["projRoot"]= input("Enter full path to target dir: ")
    cwd_path = Path(os.getcwd())        # Path to current module
    proj["cwd"]  = str(cwd_path.parents[0]) # back up to main

    flake8_check(proj)           # check for PEP8 compliance
    print(proj)

    generate(proj)

if __name__ == '__main__':
    main()