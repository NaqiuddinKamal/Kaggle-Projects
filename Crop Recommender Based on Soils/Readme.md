# Crop Recommendation System

Recommend a crop from soil and climate features using logistic regression.

## Method

Reserve one stratified 20% holdout (random state 42). Rank single features with five-fold cross-validation on the training partition only; fit StandardScaler inside every fold. Freeze the three selected features before training the final pipeline and evaluating the holdout once. Correlation plots also use only training rows.

## Validated result

The 4 October 2026 clean run selected rainfall, humidity and potassium. It used 1,760 training rows and 440 holdout rows and achieved weighted F1 **0.894643**. This replaces the historical 0.86 claim, which used the holdout during feature selection; the two scores should not be treated as a like-for-like improvement.

The training-CV feature comparison and correlation heatmap are rendered in the executed notebook. The result concerns this dataset and split; field performance has not been evaluated.

## Run

Use requirements.txt and run all notebook cells in order. The CSV may sit beside the notebook or under its project folder when starting from the repository root. The original Kaggle input path remains a fallback. See the root README for automated execution.
