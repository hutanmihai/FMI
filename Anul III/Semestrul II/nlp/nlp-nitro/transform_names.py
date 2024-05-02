import spacy
import csv
import tqdm
from constants import TEST_CSV, TRAIN_CSV
import pandas as pd
from spacy.lang.ro.examples import sentences

nlp = spacy.load("ro_core_news_sm")

df_train = pd.read_csv(TRAIN_CSV)
df_test = pd.read_csv(TEST_CSV)

# cut the data to only 5000 rows
# df_train = df_train[:10]
# df_test = df_test[:10]

replacements = {"ţ": "ț", "ş": "ș", "Ţ": "Ț", "Ş": "Ș"}

df_train["title"] = df_train["title"].replace(replacements, regex=True)
df_train["content"] = df_train["content"].replace(replacements, regex=True)

df_test["title"] = df_test["title"].replace(replacements, regex=True)
df_test["content"] = df_test["content"].replace(replacements, regex=True)

allowed_entities = ["GPE", "PERSON", "ORGANIZATION"]

def transform_name(df, filename, is_train):
    data = [
        ["id", "title", "content"],
        []
    ]

    if is_train:
        data[0].append("class")

    for i in tqdm.tqdm(range(len(df))):
        title_str = str(df["title"][i])
        content_str = str(df["content"][i])
        title_and_content = title_str + " " + content_str

        doc = nlp(title_and_content)
        for ent in doc.ents:
            if ent.label_ in allowed_entities:
                if ent.text[0] >= 'A' and ent.text[0] <= 'Z':
                    title_str = title_str.replace(ent.text, "$NE$")
                    content_str = content_str.replace(ent.text, "$NE$")
                    # print(ent.text, len(ent.text))

        new_row = [str(df['id'][i]), title_str, content_str]
        if is_train:
            new_row.append(str(df['class'][i]))

        data.append(new_row)
        data.append([])

    with open(filename, "w", newline="\n", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(data[0])
        writer.writerows(data[1:])

transform_name(df_train, "../modified_data/train.csv", True)
transform_name(df_test, "../modified_data/test.csv", False)