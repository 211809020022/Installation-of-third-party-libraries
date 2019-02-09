#BatchInstall.py
import os
libs={"numpy","matplotib","pillow","sklearn","requests","jieba",\
      "beaytifulsoup4","wheel","networkx","sympy","pyinstaller","django",\
      "flask","werobort","pyqt5","pandas","pyopengl","pypdf2","docpt","pygame"}
try:
    for lib in libs:
        os.system("pip install"+lib)
        print("Successful")
except:
    print("Failed Somehow")

