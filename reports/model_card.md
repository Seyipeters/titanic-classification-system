# Model Card

## Overview
- Project: Titanic Classification System
- Model: RandomForestClassifier
- Target: `survived`
- Dataset: titanic

## Intended Use
This model is intended for portfolio demonstration of entry-level AI/ML engineering skills: structured experimentation, reproducible preprocessing, and measurable evaluation.

## Metrics
- accuracy: 1.0
- cv_mean_accuracy: 1.0
- cv_std: 0.0
- train_samples: 712
- test_samples: 179
- n_classes: 2

## Risks and Limitations
- Data source may not match live production distributions
- Encoded categorical handling should be upgraded for production feature stores
- Thresholding, fairness, and monitoring require domain-specific follow-up

## Key Learnings
- Dataset contains 891 rows and 15 columns.
- Target 'survived' has 2 classes: ['0', '1'].
- Model achieved 100.0% test accuracy.
- 5-fold CV accuracy: 100.0% +/- 0.0%.
- Top numeric features used: pclass, age, sibsp, parch.
