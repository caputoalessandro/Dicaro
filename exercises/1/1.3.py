from nltk.corpus import wordnet as wn
import csv
from res import RESOURCES_PATH
import pandas as pd

# 1 cerca concetto preso da property  norm su wordnet
# 2 prendere i  synset
# 3 utilizzare le informazioni  offerte dalle property norms per scegliere il synset giusto
# quindi wsd utilizzando quello già imlementato con radicioni
# 4 trovato il synset, leghiamo il synset all'informazione,  ovvero facciamo  un match tra le feature
# chhe troviamo nelle property norm e quelle he troviamo nella definizione di wn, in più diciamo
# quali delle feature nelle porperty  norm potrebbero essere aggiunte


def make_csv_from_dat():
    norms_path = RESOURCES_PATH / "norms.dat"
    new_norms_path = RESOURCES_PATH / "norms.csv"

    #read dat to a list of lists
    dat_content = [i.strip().split() for i in open(norms_path).readlines()]

    # write it as a new CSV file
    with open(new_norms_path, "w") as f:
        writer = csv.writer(f)
        writer.writerows(dat_content)


def get_concepts_features(path):
    table = pd.read_fwf(path)
    # domain = table["domain"]
    print(table)


def main():
    make_csv_from_dat()
    csv_path = RESOURCES_PATH / "norms.csv"
    dat_path = RESOURCES_PATH / "norms.dat"
    get_concepts_features(dat_path)
    print("we")


if __name__ == "__main__":
    main()

