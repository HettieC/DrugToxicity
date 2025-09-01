from molvs import standardize_smiles
from DrugToxicity.Cache.cache import Cache
import pubchempy as pubchem

class Validator:
    
    cacheSystem = Cache()
    #TO DO: Does not work 100% properly
    @classmethod
    def validate(cls, smile_string: str) -> bool:
        try:
            smile_standardized = standardize_smiles(smile_string)
            print(smile_standardized)
            if cls.cacheSystem.is_cached(smile_standardized):
                return True
            result = pubchem.get_compounds(smile_standardized, "smiles")
            cid = result[0].to_dict(properties=['cid']).get("cid")
            if cid is None:
                return False
            else:
                cls.cacheSystem.add(smile_standardized)
                return True
        except Exception:
            return False





