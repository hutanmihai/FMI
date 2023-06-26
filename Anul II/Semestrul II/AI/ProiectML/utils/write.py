import pandas as pd


def write(predicted_labels):
    labels = [int(i) for i in predicted_labels]

    # Create a DataFrame with the predicted labels
    ids = [f"0{i}" for i in range(17001, 22149 + 1)]
    predictions_df = pd.DataFrame({"id": ids, "class": labels})

    # Write the DataFrame to a CSV file
    predictions_df.to_csv("../submission.csv", index=False)
