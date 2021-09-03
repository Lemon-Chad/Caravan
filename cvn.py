import os
import pickle
from Network import Network
import zipfile
import pathlib
import json

n = Network()
while True:
    cmd = input("Caravan : ")
    if cmd.startswith("upload "):
        filename = cmd.replace("upload ", "", 1)
        if not os.path.exists(filename):
            print("-- File does not exist!"); continue
        if not filename.endswith(".zip"):
            print("-- Must be a zip file!"); continue
        file = open(filename, "rb").read()
        n.send(pickle.dumps(f"filesend|<{{???}}>|{filename}"))
        n.send(file)
        x = n.send(input("Key: ").encode("utf-8")).decode("utf-8")

        print(x)
        if x != "Key accepted":
            continue
        print("External Package Dependencies\nType |end| when finished\n")
        while True:
            d = input("- ")
            x = n.send(d.encode("utf-8")).decode("utf-8")
            if d == '|end|': break
            print(x)
        print("Package uploaded!")
    elif cmd.startswith("get "):
        package = cmd.replace("get ", "", 1)
        x = n.send(pickle.dumps(f'fileget|<{{???}}>|{package}')).decode("utf-8")
        print(x)

        if "invalid" in x.lower():
            continue
        if not os.path.exists("caravan/"):
            os.mkdir("caravan/")
        packages = pickle.loads(n.send("File Request".encode("utf-8")))
        print(f"Total size: {sum([len(o) for _, o in packages.items()]) / 1000} KB\n")
        for packagename, packagebytes in packages.items():
            packagename: str
            package = f"caravan/{packagename}"
            open(package, "wb+").write(packagebytes)
            print(f"Installed {packagename} to {package}")
            zf = zipfile.ZipFile(package, "r")
            # modfolder = f"caravan/{packagename[:-4]}/"
            modfolder = f"caravan/"
            print(f"Extracting {package} to {modfolder}")
            if not os.path.exists(modfolder):
                os.mkdir(modfolder)
            zf.extractall(modfolder)
            zf.close()
            print("Package extracted")
            os.remove(package)
            print(f"Removed {package}\n")
        print("Packages installed!")
    elif cmd == "help":
        print('''
get <package> - Installs the specified package from the caravan.
upload <package> - Sends local file to the caravan.
        ''')
