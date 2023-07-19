pyinstaller --specpath /test.spec --onefile test.py
PyInstaller test.spec //Con esto me funciono

pyuic5 -x test.ui -o test.py


pyinstaller --onefile -w -i "icon.ico" test.py

from PyInstaller.utils.hooks import collect_data_files


datas=collect_data_files("tabula")


BUscar columnas por nombre(entre todos los nombres de columna), si no las encuantra pide a usuario que indique el nuevo nombre y la busca, sino salta esa columna y sigue con el proceso, 