import pandas as pd

DATASET = "ecoli"


if __name__ == '__main__':
    dataset = pd.read_csv("../../../data/{}.data".format(DATASET), header=None)

    dual = {
        "cp": "cytoplasm",
        "im": "membrane",
        "pp": "membrane",
        "om": "membrane"
    }

    dual_dataset = dataset.replace({8: dual})
    dual_dataset.to_csv("../data/{}_dual.data".format(DATASET), header=False, index=False)

    membrane = ["im", "pp", "om"]

    membrane_dataset = dataset.loc[dataset[8].isin(membrane)]
    membrane_dataset.reset_index(inplace=True)
    membrane_dataset = membrane_dataset.drop(columns=["index"])

    membrane_dataset.to_csv("../data/{}_membrane.data".format(DATASET), header=False, index=False)

    inner_membrane = ["im", "imU", "imL", "imS"]

    original_dataset = pd.read_csv("../../../data/{}_original.data".format(DATASET), header=None)

    inner_dataset = original_dataset.loc[original_dataset[8].isin(inner_membrane)]
    inner_dataset.reset_index(inplace=True)
    inner_dataset = inner_dataset.drop(columns=["index"])

    inner_dataset.to_csv("../data/{}_inner.data".format(DATASET), header=False, index=False)

    outer_membrane = ["om", "omL"]

    outer_dataset = original_dataset.loc[original_dataset[8].isin(outer_membrane)]
    outer_dataset.reset_index(inplace=True)
    outer_dataset = outer_dataset.drop(columns=["index"])

    outer_dataset.to_csv("../data/{}_outer.data".format(DATASET), header=False, index=False)
