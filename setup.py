#!/usr/bin/env python3

import shutil
import subprocess

class settings:
    script = "nea"
    path = "/usr/bin/"

def clean():
    if settings.path.endswith("/") ==  False:
        settings.path += "/"

def main():
    if settings.script != None and settings.path != None:
        clean()
        shutil.copyfile(settings.script, "%s%s" % (settings.path, settings.script))
        subprocess.run(["chmod", "+x", "%s%s" % (settings.path, settings.script)])
        print("Installed: '%s%s'" % (settings.path, settings.script))
        subprocess.run(["git", "config", "--global", "alias.nea", "'! %s%s'" % (settings.path, settings.script)])
        print("Git configurated: 'git nea ...'")

main()