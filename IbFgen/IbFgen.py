"""
IbFgen
"""
import os
import stat


def append_import(fp, impt_stmt):
    """
    append_import(fp, impt_stmt)
    :param fp:  filepath
    :type fp:
    :param impt_stmt:  import stmt to append
    :type impt_stmt:
    :return:    none - throws FileNotFound
    :rtype:
    """
    with open(fp, "a") as fo:
        # Append import stmt at the end of file
        fo.write(impt_stmt)


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
        touch.touch('config.py')        # create config.py
        shutil.copy(proj['cwd'] + '/resources/config.py', ".")  # copy the default config.py
        touch.touch('runner')
        shutil.copy(proj['cwd'] + '/resources/runner', ".")  # copy the default runner
        append_import('./runner', "from " + proj['appName'] + " import app")     # append the import stmt
        os.chmod('./runner', stat.S_IXUSR)      ## Set exec to user
        os.mkdir(proj['appName'])   # create app dir
        os.chdir(proj['appName'])  # move to app dir
        touch.touch('__init__.py')      # create  __init__.py
        shutil.copy(proj['cwd'] + '/resources/__init__.py', ".")  # copy the default __init__.py
        append_import('./__init__.py', "from " + proj['appName'] + "import routes")    # append the import stmt
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
        shutil.copy(proj['cwd'] + '/resources/base.html', ".")  # copy the default base.html
        touch.touch('index.html')  # create index.html
        shutil.copy(proj['cwd'] + '/resources/index.html', ".")  # copy the default index.html
        touch.touch('contact.html')  # create contact.html
        shutil.copy(proj['cwd'] + '/resources/contact.html', ".")  # copy the default bg.jpg image


    else:
        print('Error: proj root does not exist.')

    
def main():
    from pathlib import Path

    proj = {
        "projRoot": "",  # Full path to target dir or work area
        "projName": "",  # valid Flask project name
        "appName" : "",  # valid Flask app name
        "config"  : "",  # config.sys - using Config class
        "rqmts"   : "",  # Full path to requirements.txt - see README for default if ""
        'pgList'  : []  # List of page names
        # ??????
        }

    print(f"Welcome to IbFgen")
    print(proj)

    proj["projName"] = str(input("Enter valid python proj name: "))
    proj["appName"] = str(input("Enter valid Flask package name: "))
    proj["projRoot"]= str(input("Enter full path to target dir: "))
    proj["rqmts"] = str(input("Enter full path to your requirements.txt or hit enter for default: ") or 'default_requirements.txt')
    cwd_path = Path(os.getcwd())        # Path to current module
    proj["cwd"]  = str(cwd_path.parents[0]) # back up to main

    flake8_check(proj)           # check for PEP8 compliance
    print(proj)

    generate(proj)

if __name__ == '__main__':
    main()