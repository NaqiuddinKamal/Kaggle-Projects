 # House Rental Price Prediction

This project aims to predict house rental prices based on various features related to the property listing.

## Data Processing

The raw data is preprocessed by:

- Removing unwanted columns like "Posted On" 
- Dropping columns with many unique categorical values like "Floor" and "Area Locality"
- Label encoding the remaining categorical features

## Exploratory Data Analysis

Some visualizations are created to understand data distributions:

- Bar plots showing average rent by categories like Area Type, City etc.
- Pie charts showing distribution of top categories for features like Area Type, Furnishing Status etc.  
- Boxplots and violinplots to see distributions of numerical features like Size, Number of Bedrooms etc.

Correlation heatmap is also plotted to see relationships between features. 

## Model Building

The data is split into training and test sets. Outliers in the numerical features are removed from training data using z-scores.

Two models are trained:

- Decision Tree Regressor 
- Random Forest Regressor

Hyperparameter tuning is done using GridSearchCV to find the best parameters.

Performance metrics calculated:

- MAE, MSE, RMSE
- R-squared
- MAPE

Feature importance plots are created to understand which features are most informative to the models.

SHAP summary plots and waterfall plots are also analyzed.

## Conclusion

In the end, the report summarizes which model performs better for this case of rental price prediction. The important features driving the prediction are also highlighted. Scope for future work is discussed.
