from DrugToxicity.Validator.validator import Validator
from DrugToxicity.liver import Liver
from rdkit import Chem
class DrugToxicityClass:
    validator = Validator()
    liver = Liver()

    @staticmethod
    def __products_to_smiles(products: list) -> list:
        return [Chem.MolToSmiles(x) for x in products]

    def predict_phaseI(self, compound) -> list:
        reactions_phaseI = self.liver.get_phaseI_reactions()

        products = []
        comp = Chem.MolFromSmiles(compound)
        for reaction in reactions_phaseI:
            product = reaction(comp)
            products.extend(product)

        filtered_phaseI_products = self.__filter_products(self,products)




        return filtered_phaseI_products

    def predict_phaseII(self, filtered_phaseI_products) -> list:
        reactions_phaseII = self.liver.get_phaseII_reactions()

        products = []
        for reactant in filtered_phaseI_products:
            reactant2 = Chem.MolFromSmiles(reactant)
            for reaction in reactions_phaseII:
                product = reaction(reactant2)
                products.extend(product)
            
        return self.__filter_products(self,products)


    def __filter_products(self, products: list) -> list:
        products = self.__products_to_smiles(products)
        real_products = []
        for product in products:
            if self.validator.validate(product):
                real_products.append(product)
        return real_products
            


