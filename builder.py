import os
import sys
import toml

PYPROJECT_TOML = 'pyproject.toml'

config = toml.load(PYPROJECT_TOML)

args = sys.argv[1:]
if len(args) == 0:
    print(open("version.txt").read())
elif len(args) == 1:
    
    os.system("git add *")
    os.system(f"""git commit -am "{args[0]}" """)

    open("version.txt", "w").write(args[0])
    config["project"]["version"] = args[0]
    toml.dump(config, open(PYPROJECT_TOML, "w"))
    buffer = open(f"src/{config["project"]["name"]}/__init__.py","r").read().split("\n")[2:]
    buffer = f"__version__ = '{config["project"]["version"]}'\n__name__ = '{config["project"]["name"]}'\n"+('\n'.join(buffer))
    open(f"src/{config["project"]["name"]}/__init__.py","w").write(buffer)

    os.system("python -m build")
    os.system("pip uninstall -y toml_template")
    os.system("pip install "+os.path.join("dist", f"toml_template-{config['project']["version"]}-py3-none-any.whl"))