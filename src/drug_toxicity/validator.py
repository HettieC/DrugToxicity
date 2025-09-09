from __future__ import annotations

from dataclasses import dataclass, field

import pubchempy as pubchem
from molvs import standardize_smiles


@dataclass
class Validator:
    _cache: set = field(default_factory=set)

    def validate(self, smile_string: str) -> bool:
        try:
            smile_standardized = standardize_smiles(smile_string)

            # FIXME @Hettie
            # This print should be replaced with a logging call, so that users can decide
            # whether they want to see it or not
            print(smile_standardized)
            if smile_standardized in self._cache:
                return True
            result = pubchem.get_compounds(smile_standardized, "smiles")

            # FIXME @Hettie
            # Check the type of result, could be `DataFrame` or list[Compound]
            # the code below might crash because of that, so cast if you know the exact type
            cid = result[0].to_dict(properties=["cid"]).get("cid")
            if cid is None:
                return False
            self._cache.add(smile_standardized)
            return True

        # FIXME @Hettie
        # This also catches `KeyboardInterrupt` and `SystemExit`, which can lead to bad
        # behaviour. Do you know the exact errors that are being raised here?
        # See https://docs.astral.sh/ruff/rules/blind-except/
        except Exception:
            return False
