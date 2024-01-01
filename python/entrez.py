from Bio import Entrez
from typing import str, Dict, List, Any
Entrez.email = "graham.n.taggart.dut@gmail.com"
handle = Entrez.einfo()
result = handle.read()
handle.close()

print(result)

def ezinfo(organism=str, ) -> Dict:
    pass

def ezsearch(organims=str) -> Dict:
    pass

def ezpost(organims=str) -> Any:
    pass

def ezsummary():
    pass

def ezfetch():
    pass

def ezlink():
    pass

def ezgquery():
    pass

def ezspell():
    pass