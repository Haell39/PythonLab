"""
^^ Deleting and Renaming Files

Syntax: -->

The rename() function renames a file. The syntax is rename (old
name, new name). 

The remove() function deletes a file. The syntax is
remove(filename). 
"""

import os
from os import remove, rename

deletePath = "PythonOneDay/bancoDados/delete.txt"
renameFromPath = "PythonOneDay/bancoDados/rename.txt"
renameToPath = "PythonOneDay/bancoDados/newFilename.txt"

try:
    # Remover
    if os.path.exists(deletePath):
        os.remove(deletePath)
        print(f'Arquivo "{deletePath}" removido!')
    else:
        print(f'Arquivo "{deletePath}" não encontrado.')

    # Renomear
    if os.path.exists(renameFromPath):
        os.rename(renameFromPath, renameToPath)
        print(f"Arquivo '{renameFromPath}' renomeado para '{renameToPath}'.")
    else:
        print(f"Arquivo '{renameFromPath}' não encontrado!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
