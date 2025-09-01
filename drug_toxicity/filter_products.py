from libs.regioML.regioML import RegioML
from operator import itemgetter
class FilterProducts:
    @staticmethod
    def filter_aromatic_reactions(canonicalized_comp, products:list):
        regioML = RegioML()
        atoms = regioML.predictBonding(canonicalized_comp)
        max_prob = max(atoms, key=itemgetter(1))