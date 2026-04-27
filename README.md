# Titanic Classification System

> Entry-level AI/ML engineering portfolio project with analysis, evaluation, and deployment planning.

## 🎯 Project Objectives

This project demonstrates:
- **Business Framing**: translate a dataset into a concrete product or operations use-case
- **Data Exploration**: comprehensive EDA with distributions, correlations, and missing-value analysis
- **Feature Engineering**: numeric scaling, categorical encoding, and preprocessing safeguards
- **Model Training**: cross-validated RandomForestClassifier with performance benchmarking
- **Engineering Readiness**: reproducible scripts, model card, deployment checklist, and metrics artifacts

## 🎯 Problem Framing

Use **Titanic** to build an end-to-end ML system that predicts **survived**, surfaces the drivers of performance, and documents the path from experiment to deployment for an entry-level AI/ML engineering portfolio.

## 📊 Dataset Overview

| Property | Value |
|----------|-------|
| Dataset | titanic |
| Source | seaborn built-in |
| Rows | 891 |
| Target | `survived` |

## 📈 Model Performance (RandomForestClassifier)

| Metric | Value |
|--------|-------|
| accuracy | `1.0` |
| cv_mean_accuracy | `1.0` |
| cv_std | `0.0` |
| train_samples | `712` |
| test_samples | `179` |
| n_classes | `2` |

## 💡 Key Insights

- Dataset contains 891 rows and 15 columns.
- Target 'survived' has 2 classes: ['0', '1'].
- Model achieved 100.0% test accuracy.
- 5-fold CV accuracy: 100.0% +/- 0.0%.
- Top numeric features used: pclass, age, sibsp, parch.
- The workflow is structured as an employer-ready ML project: business framing, EDA, preprocessing, model evaluation, and deployment planning.
- Data quality guardrails cover missingness, feature typing, and target validation for `survived`.
- The chosen baseline-to-production candidate is `RandomForestClassifier`, with reproducibility supported by notebook, scripts, metrics, and written reports.
- Recommended next step is packaging inference with monitoring for drift, performance decay, and data-quality regressions.

## 🗂️ Repository Structure

- `analysis.ipynb` – exploratory notebook and experiment walkthrough
- `01_data_exploration.py` – repeatable data audit and profiling
- `02_feature_engineering.py` – preprocessing and feature preparation
- `03_model_training.py` – training, validation, and metric capture
- `04_results.py` – results summary and stakeholder-ready outputs
- `reports/` – analysis summary, data quality checklist, model card, and deployment readiness notes

## 🚀 How to Use

### Option 1: Jupyter Notebook (Interactive)
```bash
pip install jupyter pandas scikit-learn matplotlib seaborn
jupyter notebook analysis.ipynb
```

### Option 2: Scripted Workflow
```bash
python 01_data_exploration.py
python 02_feature_engineering.py
python 03_model_training.py
python 04_results.py
```

## 🛠️ Tech Stack

- **Python 3.9+** - Core language
- **pandas** - Data manipulation
- **scikit-learn** - Machine learning (RandomForestClassifier)
- **matplotlib** - Static visualizations
- **seaborn** - Statistical graphics
- **Jupyter** - Interactive notebook

## 🧭 Hiring Signal

This repo is intentionally structured to reflect what employers look for in an entry-level AI/ML engineer: clear problem framing, reproducible analysis, disciplined evaluation, and practical deployment thinking.

## 📝 License

Open source - Free to use for portfolio and educational purposes.
