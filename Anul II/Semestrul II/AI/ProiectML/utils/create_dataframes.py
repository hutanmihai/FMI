import pandas as pd

train_labels_file = "../data/train_labels.txt"
train_df = pd.read_csv(train_labels_file, header=0, names=["id", "class"], sep=",")
train_df["id"] = train_df["id"].astype(str)
train_df["class"] = train_df["class"].astype(str)

validation_labels_file = "../data/validation_labels.txt"
validation_df = pd.read_csv(
    validation_labels_file, header=0, names=["id", "class"], sep=","
)
validation_df["id"] = validation_df["id"].astype(str)
validation_df["class"] = validation_df["class"].astype(str)

train_df["id"] = train_df["id"].apply(lambda x: str(x).zfill(6) + ".png")
validation_df["id"] = validation_df["id"].apply(lambda x: str(x).zfill(6) + ".png")

test_dataframe = pd.DataFrame()
test_dataframe["id"] = [str(i).zfill(6) + ".png" for i in range(17001, 22149 + 1)]

train_df.to_csv(
    "../data_frames/train_dataframe.csv",
    index=False,
    header=False,
    columns=["id", "class"],
)
validation_df.to_csv(
    "../data_frames/validation_dataframe.csv",
    index=False,
    header=False,
    columns=["id", "class"],
)
test_dataframe.to_csv(
    "../data_frames/test_dataframe.csv", index=False, header=False, columns=["id"]
)
