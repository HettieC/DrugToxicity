from DrugToxicity.reactions import Reactions
class Liver:
    
    phaseI_reactions = [

        Reactions.aliphatic_hydroxylation,
        Reactions.aromatic_hydroxylation,
        Reactions.n_oxidation,
        Reactions.s_oxidation,
        Reactions.n_dealkylation,
        Reactions.o_dealkylation,
        Reactions.epoxidation,
        Reactions.alcohol_oxidation,
        Reactions.oxidative_deamination,
        Reactions.decarboxylation,
        Reactions.phenolamine_oxidation,
        Reactions.hydrolysis_ester,
        Reactions.deacetylation,
        Reactions.hydrolysis_aliphatic,
        Reactions.alcohol_dehydrogenation,
        Reactions.nitro_reduction1,
        Reactions.nitro_reduction2,
        Reactions.hydrolysis_epoxide,
        Reactions.hydrolysis_amide,
        Reactions.carbonyl_reduction,
        Reactions.dehalogenation

    ]
    phaseII_reactions=[

        Reactions.o_glucuronidation_phenols_alcohols,
        Reactions.o_glucuronidation_carboxylic_acids,
        Reactions.o_glucuronidation_amines,
        Reactions.o_glucuronidation_pyridine,
        Reactions.o_glucuronidation_thiols,
        Reactions.glucuronidation_alpha_diketones,
        Reactions.glucuronidation_alkynes,
        Reactions.sulfonation_alcohols,
        Reactions.sulfonation_aromatic_n_oxides,
        Reactions.gluthationylation_expoxides,
        Reactions.gluthationylation_alpha_beta_unsaturated_carbonlys,
        Reactions.gluthationylation_alkyl_halides,
        Reactions.gluthationylation_quinone_imines,
        Reactions.methylation_catechols,
        Reactions.methylation_hydroxyindoles,
        Reactions.methylation_amines,
        Reactions.methylation_pyridines,
        Reactions.methylation_imidazoles,
        Reactions.methylation_thiols,
        Reactions.methylation_thiopurines,
        Reactions.methylation_arsen,
        Reactions.acetylation_first_amines,
        Reactions.acetylation_hydrazine,
        Reactions.conjugation_glycine,
        Reactions.conjugation_glutamine,
        Reactions.conjugation_taurine
    ]

    def get_phaseI_reactions(self):
        return self.phaseI_reactions
    
    def get_phaseII_reactions(self):
        return self.phaseII_reactions
