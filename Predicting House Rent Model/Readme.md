# House Rental Price Prediction

Predict listing rent using Decision Tree and Random Forest regression.

## Method

Drop Posted On, Floor and Area Locality. Reserve 20% of rows with random state 42 and remove numerical outliers from training rows only. OneHotEncoder is fitted inside each training-CV fold and handles unseen categories. GridSearchCV uses five folds and mean squared error for both models; predictions use the selected best_estimator_.

Each feature-importance table and chart uses its own model and transformed feature names. The Random Forest chart now sorts imp_df rather than the Decision Tree lap_df. Metrics use the entire holdout; SHAP summary and waterfall plots explain its first 200 rows to bound execution cost.

## Validated result

Clean run on 4 October 2026:

| Model | MAE | RMSE | R-squared | MAPE |
|---|---:|---:|---:|---:|
| Decision Tree | 16,914.5129 | 60,150.8237 | 0.0922 | 48.91% |
| Random Forest | 12,591.2989 | 41,353.3243 | 0.5709 | 40.28% |

The historical dataset contains wide rent variation and large prediction errors. These are exploratory holdout results, not evidence of current-market accuracy. Pre-split EDA is descriptive; model preprocessing and tuning do not use holdout labels.

## Run

Use requirements.txt and run all notebook cells in order. The CSV may sit beside the notebook or under its project folder when starting from the repository root. The original Kaggle input path remains a fallback. SHAP is installed through pinned requirements, not from a notebook shell command. See the root README for automated execution.
