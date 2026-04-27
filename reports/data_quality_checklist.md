# Data Quality Checklist

- Dataset: titanic
- Rows: 891
- Columns: 15
- Target: `survived`

## Checks
- [x] Load dataset and verify schema
- [x] Quantify missingness and null-heavy columns
- [x] Validate target availability and type
- [x] Separate numeric and categorical feature groups
- [ ] Add drift checks before production deployment

## Highest Missingness Columns
- deck: 77.22% missing
- age: 19.87% missing
- embarked: 0.22% missing
- embark_town: 0.22% missing
- survived: 0.0% missing
