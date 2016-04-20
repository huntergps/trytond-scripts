# trytond-scripts
Handy scripts to manage trytond and its numerous modules

### How to use bash scripts  
It is assumed that you place this repo next to the *trytond* repo, so your structure will look like this:
```
(venv_tryton)kulver@k-ubuntu:~/projects/semilimes$ tree -L 1
.
├── sao
├── trytond
└── trytond-scripts
```  


### Downloading all the modules  
Just run this:  
`. download_all_modules.sh`  


### Switching modules' versions to any you want:  
Run this and don't forget to specify the desired version as a 1st parameter, like this:  
`. change_modules_version.sh 3.8`


### Installing all the modules:  
You need to get the `proteus` to run this, so:  
```
pip install proteus
python install_modules.py
```
In case anything goes wrong - please contact Alex Melkoff.

