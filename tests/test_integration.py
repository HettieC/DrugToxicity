from drug_toxicity import Predictor


def test_pipeline() -> None:
    main = Predictor()

    compound_smiles = "[#8]"
    phase_1_rxns = main.predict_phase_i(compound_smiles)
    phase_2_rxns = main.predict_phase_ii(phase_1_rxns)

    assert not phase_2_rxns
