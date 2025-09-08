from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from rdkit import Chem

from . import liver, reactions
from .validator import Validator

if TYPE_CHECKING:
    from collections.abc import Iterable

    from rdkit.Chem.rdchem import Mol

__all__ = [
    "liver",
    "reactions",
    "Predictor",
    "Validator",
]


@dataclass
class Predictor:
    validator: Validator = field(default_factory=Validator)

    @staticmethod
    def _products_to_smiles(products: list[Mol]) -> list[str]:
        return [Chem.MolToSmiles(x) for x in products]

    def _filter_products(self, products: list[Mol]) -> list[str]:
        return [
            smiles
            for smiles in self._products_to_smiles(products)
            if self.validator.validate(smiles)
        ]

    def predict_phase_i(self, compound: str) -> list:
        products = []
        comp = Chem.MolFromSmiles(compound)
        for reaction in liver.get_phase_i_reactions():
            product = reaction(comp)
            products.extend(product)

        return self._filter_products(products)

    def predict_phase_ii(self, filtered_phase_i_products: Iterable[str]) -> list:
        products = []
        for reactant in filtered_phase_i_products:
            reactant2 = Chem.MolFromSmiles(reactant)
            for reaction in liver.get_phase_ii_reactions():
                product = reaction(reactant2)
                products.extend(product)

        return self._filter_products(products)
