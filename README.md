# Maternal & Child Health Indicator Prediction

## Project Overview

This project develops machine learning models to predict six crucial Maternal and Child Health (MCH) indicators at the village level across 59 Low and Middle-Income Countries (LMICs). By combining Demographic and Health Surveys (DHS) with satellite imagery, we create predictive models that can help identify areas in need of healthcare interventions even when ground survey data is unavailable.

## Indicators Predicted

Our models predict these key health metrics:
- Mean BMI (Body Mass Index)
- Median BMI
- Unmet Need Rate (for family planning)
- Under-5 Mortality Rate
- Skilled Birth Attendant Rate
- Stunted Rate (childhood stunting)

## Methodology

### 1. Dataset Construction

We created a comprehensive dataset by combining:
- **DHS Survey Data**: Demographic and health information from 59 countries
- **Satellite Imagery**: High-resolution Google Earth images geotagged to each DHS cluster
- **Feature Pool**: Initial dataset included ~11,500 attributes per location

### 2. Data Processing Pipeline

Our end-to-end workflow handles the large-scale data challenges:

```
Raw Data → Chunking → Preprocessing → Feature Selection → Model Training → Evaluation
```

#### Chunking Strategy
- Partitioned the massive dataset to avoid memory constraints
- Processed chunks independently and recombined results
- Enabled parallel processing of the extensive feature set

#### Preprocessing
- Applied tailored imputation strategies for missing values
- Removed low-variance (<0.1) features
- Eliminated highly correlated (>0.9) features
- Reduced dimensionality while preserving signal

### 3. Feature Engineering & Selection

We employed a multi-stage approach to handle the high-dimensional feature space:

1. **Initial Filtering**: Removed features with >80% missing values or near-zero variance
2. **Dimensionality Reduction**: Applied PCA to retain 90% variance (456 components)
3. **Feature Importance**: Used Mutual Information to rank features by relevance to each target
4. **Target-Specific Selection**: Created optimized feature subsets for each health indicator

### 4. Modeling Approach

We tested multiple algorithms against our baseline:

- **Evaluation Metric**: Mean Column-wise RMSE (MCRMSE)
- **Baseline**: LightGBM with full feature set
- **Models Evaluated**: 
  - Tree-based: Random Forest, XGBoost, CatBoost
  - Linear models
  - SVM
  - Neural Networks

### 5. Hyperparameter Optimization

- Employed GridSearchCV and RandomSearchCV for initial tuning
- Used Optuna's TPE sampler on GPU for advanced optimization
- Conducted systematic row-sampling experiments to improve model fit

## Results

| Health Indicator | Best Model | RMSE |
|------------------|------------|------|
| Mean BMI | XGBoost | 2.17 |
| Median BMI | XGBoost | 2.04 |
| Unmet Need Rate | XGBoost | 1.89 |
| Under-5 Mortality | XGBoost | 2.31 |
| Skilled Birth Attendant | XGBoost | 1.76 |
| Stunted Rate | Random Forest | 0.94 |

**Best Overall MCRMSE**: 11.108

## Key Insights

- Feature importance analysis revealed that geographic and socioeconomic variables were the strongest predictors across all indicators
- Satellite imagery features provided significant improvements for stunting and mortality predictions
- Country-specific models outperformed global models, suggesting localized approaches may be more effective
  
## Future Work

- Develop ensemble methods combining the strengths of multiple model types
- Integrate additional satellite-derived features (e.g., MOSAIKS framework)
- Implement multi-fold cross-validation for more robust hyperparameter tuning
- Create interactive visualizations for results interpretation
- Extend the approach to other health indicators and regions
