#!/bin/python
import os
from proteus import config, Model, Wizard, Report


DB_NAME = os.environ.get('DATABASE_NAME')
CONFIG_FILE_PATH = '/tryton/config.ini'

INSTALLED = []
FAILED = []
SKIPPED = []
# BLACKLIST = ["product_classification_taxonomic",
#              "purchase_request"]

config = config.set_trytond(DB_NAME, config_file=CONFIG_FILE_PATH)


def main():
    Module = Model.get("ir.module")

    not_installed_modules = Module.find([("state", "!=", "installed")])

    for not_installed_module in not_installed_modules:

        # double check in case this module was installed as dependency
        if not_installed_module.state != u"installed":
            install_module(not_installed_module)

    for array in (INSTALLED, SKIPPED, FAILED):
        remove_doubles(array)

    print 'Done. \n' \
          'Installed modules: \n%s\n' \
          'Failed modules: \n%s\n' % (
        '\n'.join(INSTALLED) or '-',
        '\n'.join(FAILED) or '-'
    )


def remove_doubles(array):
    return list(set(array)).sort()


def install_module(module):
    """Lookup uninstalled dependencies and recuresively install them."""
    # if module.name in BLACKLIST:
    #     print("[!] Skipped installation of blacklisted module {}".format(module.name))
    #     SKIPPED.append(module.name)
    #     return False

    # install missing dependencies recursively
    missing_dependencies = [m for m in module.parents if m.state != u"installed"]
    for missing_dependency in missing_dependencies:

        if missing_dependency.name in FAILED:
            return False

        if not install_module(missing_dependency):
            print("[!] Skipped installation of {} because of failed dependencies".format(module.name))
            return False

    # mark module to install and run installation wizard
    print("Installing module {}".format(module.name))
    try:
        module.click("install")
        Wizard('ir.module.install_upgrade').execute('upgrade')
    except Exception as e:
        print("[!] Failed to install {}".format(module.name))
        print(e.message)
        FAILED.append(module.name)
        return False
    else:
        INSTALLED.append(module.name)
    return True

if __name__ == "__main__":
    main()
