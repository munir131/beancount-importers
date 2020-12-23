import os, sys
from smart_importer import apply_hooks, PredictPostings, PredictPayees

# beancount doesn't run from this directory
sys.path.append(os.path.dirname(__file__))

# importers located in the importers directory
from importers.icici import icici
# All the accounts must be declared already in your my.beancount file, to make use of this importer.
CONFIG = [
    apply_hooks(icici.IciciBankImporter('Assets:IN:Bank:ICICI:Savings'), [PredictPayees()])    
 ]
