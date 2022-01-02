"""
IbFgen
"""
import os
import shutil
import stat


def gen_appStart():
    pass


def gen_runApp():
    pass


def gen_routes(appPkg, tgt, cwd):
    """
    :param appPkg:      the name of the app pkg
    :type appPkg:           pkg
    :param tgt:                path to dir where proj is to be gend
    :type tgt:                  str
    :return:                    none
    :rtype:
    """
    with open(cwd + "/resources/routes.py.template", "r") as inf:
        l = inf.readlines()             # Read file into list

    for line in l:
        if "<app>" in line:
            # print(f"app: {line}")
            line = line.replace("<app>", appPkg)
            # print(f"after repl: {line}")

    with  open(tgt + "/routes.py", "w") as ofl:
        ofl.writelines(l)



        #     open(tgt + "/routes.py", "w") as ofl:
        # # print(f"inf: {inf} , ofl: {ofl}")
        # line = inf.readline()
        # print(f"line in inf: {line}")
        # if "<app>" in line:
        #     print(f"app: {line}")
        #     line.replace("<app>", appPkg)
        # ofl.write(line)  # over-write existing


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
                appPkg,            # The app name
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
        # print("rm -rf " + proj["projName"])
        try:
            os.mkdir(proj["projName"])  # create the proj dir
        except FileExistsError:      # If exists, NUKE it
            shutil.rmtree(proj["projName"])
            os.mkdir(proj["projName"])

        os.chdir(proj["projName"])  # move to the proj dir
        touch.touch('config.py')  # create config.py
        shutil.copy(proj['cwd'] + '/resources/config.py', ".")  # copy the default config.py
        touch.touch('runApp.sh.template')
        shutil.copy(proj['cwd'] + '/resources/runApp.sh.template', ".")  # copy the default runApp.sh.template
        touch.touch('appStart.py.template')
        shutil.copy(proj['cwd'] + '/resources/appStart.py.template', ".")  # copy the default apsStart
        append_import('./appStart.py.template', "from " + proj['appPkg'] + " import app")  # append the import stmt
        # os.chmod('./runApp.sh.template', stat.S_IXUSR)      ## Set exec to user
        os.mkdir(proj['appPkg'])  # create app dir
        os.chdir(proj['appPkg'])  # move to app dir
        touch.touch('__init__.py')  # create  __init__.pycat
        shutil.copy(proj['cwd'] + '/resources/__init__.py', ".")  # copy the default __init__.py
        append_import('./__init__.py', "from " + proj['appPkg'] + "import routes")  # append the import stmt
        touch.touch('routes.py')  # make the routes directory
        # shutil.copy(proj['cwd'] + '/resources/gend/routes.py', ".")  # copy the generated routes.py
        touch.touch('forms.py')  # make the templates directory
        # shutil.copy(proj['cwd'] + '/resources/forms.py', ".")  # copy the default forms.py
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
        # os.system('ls')

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
    import touch

    proj = {
        "projRoot": "",  # Full path to target dir or work area
        "projName": "",  # valid Flask project name
        "appPkg"  : "",  # valid Flask app name
        "config"  : "",  # config.sys - using Config class
        "rqmts"   : "",  # Full path to requirements.txt - see README for default if ""
        'pgList'  : []  # List of page names
        # ??????
        }

    print(f"Welcome to IbFgen")
    print(proj)

    proj["projName"] = str(input("Enter valid python proj name: "))
    proj["appPkg"] = str(input("Enter valid Flask package name: "))
    proj["projRoot"] = str(input("Enter full path to target dir: "))
    proj["rqmts"] = str(
        input("Enter full path to your requirements.txt or hit enter for default: ") or 'default_requirements.txt')
    cwd_path = Path(os.getcwd())  # Path to current module
    proj["cwd"] = str(cwd_path.parents[0])  # back up to main
    proj["pkgDir"] = proj["projRoot"] + '/' + proj["projName"] + '/' + proj[
        "appPkg"]  # file path for routes.py, forms.py, ...
    # print(f"Pkg files path: {proj['pkgDir']}")

    flake8_check(proj)  # check for PEP8 compliance
    print(proj)

    tgt = proj['cwd'] + '/resources/gend'  # work area for generated files
    try:
        os.mkdir(tgt)  # create the gend dir
    except FileExistsError:  # If exists, NUKE it
        shutil.rmtree(tgt)
        os.mkdir(tgt)
    os.chdir(tgt)
# gen routes, forms, ... which will be needed by generate(proj)
    gen_routes(proj["appPkg"], tgt, proj['cwd'])  # gen custom routes.py

    generate(proj)


if __name__ == '__main__':
    main()
