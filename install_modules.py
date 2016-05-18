#!/bin/python
import os
from proteus import config, Model, Wizard, Report


CONFIG_FILE_PATH = os.environ.get('TRYTOND_CONFIG', '/tryton/config.ini')

FAILED = []
BLACKLIST = ["product_classification_taxonomic",
             "purchase_request"]

config = config.set_trytond("tryton_database", config_file=CONFIG_FILE_PATH)


def main():
    Module = Model.get("ir.module")

    uninstalled_modules = Module.find([("state", "!=", "installed")])

    for uninstalled_module in uninstalled_modules:

        # double check in case this module was installed as dependency
        if uninstalled_module.state != u"installed":
            install_module(uninstalled_module)

    # print out list of modules that failed to install
    if FAILED:
        print("\nFAILED MODULES:")
        print("\n".join(FAILED))


def install_module(module):
    """Lookup uninstalled dependencies and recuresively install them."""
    if module.name in BLACKLIST:
        print("[!] Skipped installation of blacklisted module {}".format(module.name))
        return False

    # install missing dependencies recursively
    missing_dependencies = [m for m in module.parents if m.state != u"installed"]
    for missing_dependency in missing_dependencies:

        if missing_dependency.name in FAILED:
            return False

        if not install_module(missing_dependency):
            print("[!] Skipped installation of {} because of "
                  "failed dependencies".format(module.name))
            return False

    # mark module to install and run installation wizard
    print("Installing module {}".format(module.name))
    try:
        module.click("install")
        Wizard('ir.module.install_upgrade').execute('upgrade')
    except Exception as e:
        print("[!] Failed to install {}".format(module.name))
        FAILED.append(module.name)
        return False

    return True

if __name__ == "__main__":
    main()
