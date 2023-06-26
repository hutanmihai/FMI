# AI-Brain-Anomaly-Detection

# Overview

## Description

This is a brain anomaly detection challenge in which competitors train a classifier on a data set containing CT scans of
the brain. Competitors are scored based on classification accuracy on a given test set.

## Evaluation

The evaluation metric for this competition is Mean F1-Score. The 𝐹1
score, commonly used in information retrieval, measures accuracy using the statistics precision p and recall r.
Precision is the ratio of true positives (tp) to all predicted positives (tp + fp). Recall is the ratio of true
positives to all actual positives (tp + fn). The 𝐹1
score is given by:

$F_{1} = 2 \cdot \frac{p \cdot r}{p+r}$ where $p = \frac{tp}{tp + fp}$, $r = \frac{tp}{tp + fn}$

The F1 metric weights recall and precision equally, and a good retrieval algorithm will maximize both precision and
recall simultaneously. Thus, moderately good performance on both will be favored over extremely good performance on one
and poor performance on the other.

### Public versus Private Test Evaluation

The public leaderboard is calculated on approximately 20% of the test data. These examples are randomly chosen. The
final results will be based on the other 80%, so the final standings may be different. In this context, you will have to
choose 2 submissions that you think will attain the best performance on the 80% of the test data that is not used for
the public leaderboard.

### Submission Format

For every sample in the dataset, submission files should contain two columns: id and class. The id coincides with
filename containing the data sample. The class should be an integer value (0 or 1) representing the predicted class
label for the sample.

The file should contain a header and have the following format:

```
id,class
1,0
2,0
...
```

# Data

## Dataset Description

The task is to discriminate between two classes of brain CT scans, one that contains anomalies (label 1) and one that is
normal (class 0). Each sample is a grayscale image of 224x224 pixels.

Each example is assigned to one of the two classes. The training set consists of 15,000 labeled examples. The validation
set consists of 2,000 labeled examples. The test set consists of another 5,149 examples. The test labels are not
provided with the data.

### File descriptions

- data.zip - the image samples (one sample per .PNG file)
- train_labels.txt - the training labels (one label per row)
- validation_labels.txt - the training labels (one label per row)
- sample_submission.csv - a sample submission file in the correct format

### Metadata file format

The labels associtated to the training samples are provided in the train_labels_.txt file with the following format:

```
id, class
000001,0

...
017000,1
```

For example, the first row indicates that the data sample file named '000001.png' belongs to class 0 (no bleeding).

# FINAL STANDINGS

| Rank | Name                  | Score |
|------|-----------------------|-------|
| 8    | Hutan Mihai-Alexandru | 0.73415|

# References
https://www.kaggle.com/competitions/unibuc-brain-ad/leaderboard
