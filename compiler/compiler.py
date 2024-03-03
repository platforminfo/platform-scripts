# platform-scripts compiler

import sys
import os
import nuitka

# constants
BUILDTYPE = "debug"
VERSION = "001_alpha"

# runtime args
operations = {"run", "compile"}
filepath = sys.argv[2]
fileoperation = sys.argv[1]

# Pre-run check:
if not os.path.isfile(str(filepath)):
    raise ValueError(
        "Invalid file path specified. If you have specified a valid PLSC file, please provide the full file path.")
elif os.path.splittext(str(filepath))[1].lower() != ".plsc":
    raise ValueError(
        "The provided file does not have the correct extension. Please specify a valid file.")
elif fileoperation not in operations:
    raise ValueError("Invalid operation. Please provide a valid operation")
elif fileoperation == "help":
    print(f"""
platform-scripts transpiler version {VERSION} \n
\n
Operations:
help: Show this help ment \n
compile: Compile a PLSC file \n
run: Run a PLSC file \n
""")
    sys.exit()


section = None

subsection = None

imports = {
    "Dialog": ["PyMsgBox"],
    "Install": ["urllib", "subprocess"],
    "Configure": ["subprocess", "urllib"],
    "Registry": ["winreg"],
    "ElevationAllowed": ["elevate"]
}

platform_compat = {
    "Registry": ["windows"]
}

attrs = {
    "Dialog": {"title", "text", "buttons"},
}

subsection_types = {
    "Buttons"
}

libraries = []
settings = {}
operations = []


class Operation:
    def __init__(self, type):
        object_type = type
        attrs = dict()
        lines = {
            "Dialog": f"pymsgbox.confirm(text='{self.attrs["text"]}', title='{self.attrs["title"]}', buttons={
                str(self.attrs["Buttons"].keys())
            })",
        }

    def add(self, attr_name, attr_val):
        self.attrs[attr_name] = str(attr_val)

    def subsection(self, attr_name, oper, name, val):
        if oper == 0:
            attrs[attr_name] = dict()
            subsection = attr_name
        elif oper == 1:
            attrs[subsection][name] = val

    def readType(self):
        return self.object_type

    def retstr(self):
        return self.lines[self.object_type]


with open[filepath, "w"] as plsc:
    for i in filepath.readlines:
        if i.strip() == "{CompileConfig}":
            section == 0
        elif i.strip() == "{Run}":
            section == 1
        else:
            if section == 0:
                x = i.strip().split("=")
                settings[x[0]] == settings[x[1]]
                if x[0] in imports.keys():
                    libraries += imports(x[0])
            elif section == 1:
                x = i.strip().split("=")
                if x[-1] == "[" and subsection == None and x[0] not in subsection_types:
                    oper = Operation(f"{x[0]}")
                elif x[-1] == "[" and x[0] in subsection_types:
                    pass
