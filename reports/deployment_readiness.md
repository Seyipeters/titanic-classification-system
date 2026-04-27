# Deployment Readiness

## Candidate System
- Project: Titanic Classification System
- Model: RandomForestClassifier
- Dataset: titanic

## Production Checklist
- [x] Reproducible training and evaluation artifacts committed to source control
- [x] Baseline metrics captured in `metrics.json`
- [x] Model assumptions documented in `reports/model_card.md`
- [ ] Package inference entrypoint behind an API or scheduled batch job
- [ ] Add model registry, experiment tracking, and CI checks
- [ ] Add monitoring for target drift, feature drift, and latency

## Employer Signal
This project shows the transition from analysis to engineering by documenting how the experiment could be turned into a production-grade ML service.
