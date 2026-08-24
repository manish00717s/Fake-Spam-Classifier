# SMS Spam Classifier - Project Plan

**Student**: [Your Name]  
**Date**: [Submission Date]  
**Course**: [Course Name]

---

## Executive Summary

This project develops an automated SMS spam classification system using machine learning and natural language processing. By analyzing 5,572 historical messages, we will train a predictive model that classifies incoming SMS messages as Spam or Legitimate with 97%+ accuracy and 100% precision (preventing false positives).

**Expected Outcome**: A production-ready web application deployed on the cloud where users can submit messages and receive real-time spam/ham predictions.

---

## Problem Statement

### The Problem
- Users receive 5-10 spam messages daily on average
- Manual filtering is time-consuming and error-prone
- Important messages (job offers, notifications) get lost in spam
- Traditional rule-based systems can't adapt to new spam tactics

### Why It Matters
- Spam wastes user time and creates security risks
- Legitimate messages may be blocked incorrectly
- Businesses need scalable, automated solutions

### Our Solution
Build an ML-powered SMS classifier that:
- ✓ Analyzes message content automatically
- ✓ Learns patterns from historical data (5,572 messages)
- ✓ Adapts to new spam tactics over time
- ✓ Accessible via web interface
- ✓ Deployable to production

---

## Solution Architecture

### 5-Phase Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│ Phase 1: Data Cleaning & Exploratory Data Analysis (EDA)   │
│ - Load 5,572 SMS messages                                  │
│ - Remove duplicates & nulls                                │
│ - Label encoding (Ham=0, Spam=1)                           │
│ - Extract meta-features (char, word, sentence counts)      │
│ → Deliverable: Cleaned dataset + 5 visualizations          │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 2: NLP Text Preprocessing Pipeline                   │
│ - 5-step text cleaning:                                    │
│   1. Lowercasing                                           │
│   2. Tokenization                                          │
│   3. Special character removal                             │
│   4. Stopword & punctuation removal                        │
│   5. Porter stemming                                       │
│ → Deliverable: Preprocessed text + word clouds             │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 3: Predictive Modeling & Algorithm Selection         │
│ - TF-IDF vectorization (3,000 features)                    │
│ - Train 5 models:                                          │
│   - Gaussian Naive Bayes                                   │
│   - Multinomial Naive Bayes (SELECTED)                     │
│   - Bernoulli Naive Bayes                                  │
│   - SVM                                                    │
│   - Random Forest                                          │
│ → Deliverable: Trained models + confusion matrix           │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 4: Web Application Development                       │
│ - Build Streamlit UI                                       │
│ - Text input for user messages                             │
│ - Real-time predictions                                    │
│ - Display confidence scores                                │
│ → Deliverable: Working web app (localhost)                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 5: Cloud Deployment (MLOps)                          │
│ - Serialize models to .pkl files                           │
│ - Create environment files                                 │
│ - Deploy to Streamlit Cloud/Heroku/Render                  │
│ → Deliverable: Live URL (publicly accessible)              │
└─────────────────────────────────────────────────────────────┘
```

---

## Dataset Description

### Source
**Kaggle SMS Spam Collection Dataset**
- URL: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
- License: Public Domain

### Dataset Stats
| Metric | Value |
|--------|-------|
| Total Messages | 5,572 |
| Legitimate (Ham) | 4,827 (86.6%) |
| Spam | 745 (13.4%) |
| Average Message Length | 12 words |
| Languages | Primarily English |

### Class Imbalance Challenge
- Highly imbalanced dataset (13.4% minority class)
- Solution: Optimize for **Precision** instead of Accuracy
  - Reason: False positives (blocking good messages) are worse than false negatives
  - Goal: 100% Precision (no good messages blocked)

---

## Technology Stack

### Programming & Data Science
- **Language**: Python 3.8+
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **NLP**: NLTK (Natural Language Toolkit)
- **Visualization**: Matplotlib, Seaborn, WordCloud

### Web Framework
- **Framework**: Streamlit
- **Why**: Simple, Python-based, perfect for ML apps

### Model Serialization
- **Format**: Pickle (.pkl files)
- **Why**: Standard for ML model deployment

### Deployment Platforms
- **Primary**: Streamlit Cloud (easiest)
- **Alternative**: Heroku or Render.com

---

## Key Performance Metrics

### Model Performance Targets
- **Accuracy**: ≥ 95% (overall correct predictions)
- **Precision**: ≥ 98% (optimize to prevent false positives)
- **Recall**: ≥ 80% (catch most spam)
- **F1-Score**: ≥ 90% (balanced metric)

### Expected Results (Based on Research)
```
Model: Multinomial Naive Bayes + TF-IDF
- Accuracy:  97.14%
- Precision: 100%   ⭐ (Our priority)
- Recall:    85.71%
- F1-Score:  92.31%
```

### Deployment Metrics
- **Uptime**: 99%+
- **Response Time**: <1 second per prediction
- **Accessibility**: 100% (mobile & desktop)

---

## Weekly Timeline

### Week 1: Project Planning ✓
**Duration**: 1 week (done)
- Define problem scope
- Outline 5-phase architecture
- Document timeline
- **Deliverable**: Project Plan (this document)

### Week 2: EDA & Data Preparation
**Duration**: 1 week
- Load and clean dataset
- Generate 5 visualizations
- Build preprocessing pipeline
- Extract meta-features
- **Deliverable**: Data Preparation Report + cleaned dataset

### Week 3: Predictive Modeling
**Duration**: 1 week
- Apply TF-IDF vectorization
- Train 5 ML algorithms
- Compare performance
- Select best model
- **Deliverable**: Model Selection Report + trained models

### Week 4: Data Visualization & Storytelling
**Duration**: 1 week
- Generate comprehensive visualizations
- Interpret charts
- Create business context
- Write storytelling report
- **Deliverable**: Data Storytelling Report

### Week 5: Model Evaluation & Optimization
**Duration**: 1 week
- Analyze confusion matrix
- Explain Precision vs Accuracy
- Test hyperparameters
- Validate model
- **Deliverable**: Model Performance Audit

### Week 6: Deployment & Final Report
**Duration**: 1 week
- Build Streamlit web app
- Deploy to cloud
- Create configuration files
- Write final case study
- **Deliverable**: Final Case Study + Live URL

**Total Project Duration**: 6 weeks

---

## Risk Analysis & Mitigation

### Risk Matrix

| # | Risk | Impact | Probability | Mitigation | Owner |
|---|------|--------|-------------|-----------|-------|
| 1 | Dataset not representative | Low | Low | Use verified Kaggle dataset | Team |
| 2 | Class imbalance bias | High | High | Optimize for Precision metric | Analyst |
| 3 | Poor model performance | High | Medium | Train multiple algorithms, compare | ML Engineer |
| 4 | Overfitting on training data | High | Medium | Use test set, cross-validation | ML Engineer |
| 5 | NLP preprocessing errors | Medium | Low | Validate with word clouds | NLP Specialist |
| 6 | Cloud deployment failure | High | Low | Test locally first, use setup files | DevOps |
| 7 | Model retraining complexity | Medium | Medium | Serialize models to .pkl files | ML Engineer |
| 8 | Scope creep (adding features) | Medium | Medium | Strict requirements, weekly review | PM |

### Mitigation Strategies

**Strategy 1: Use Verified Data**
- Use only public Kaggle dataset
- Validate data structure before processing

**Strategy 2: Focus on Precision**
- Set evaluation metric to Precision (not Accuracy)
- Accept some spam slipping through (better trade-off)

**Strategy 3: Model Comparison**
- Train 5 different algorithms
- Select best performer via rigorous testing

**Strategy 4: Local Testing First**
- Test web app locally before cloud deployment
- Verify predictions are accurate
- Document any issues

**Strategy 5: Modular Code**
- Separate preprocessing, modeling, deployment
- Easy to debug and modify
- Reusable components

---

## Success Criteria

### Must Have (Critical)
- ✓ Model achieves ≥ 95% accuracy
- ✓ Model achieves ≥ 98% precision
- ✓ Web app deployed to live URL
- ✓ GitHub repository with all code
- ✓ Complete documentation

### Should Have (Important)
- ✓ 5+ professional visualizations
- ✓ Model explanation/interpretation
- ✓ Business insights from data
- ✓ Deployment guide for others

### Nice to Have (Optional)
- ✓ Model comparison analysis
- ✓ Advanced hyperparameter tuning
- ✓ Ensemble methods testing
- ✓ Performance monitoring dashboard

---

## Learning Objectives

Upon project completion, team members will understand:

1. **End-to-End ML Workflow**
   - From raw data to production deployment
   - Iterative process from problem definition to solution

2. **NLP Techniques**
   - Text preprocessing pipeline (5-step process)
   - Vectorization methods (TF-IDF)
   - Practical stemming and tokenization

3. **Machine Learning Fundamentals**
   - Algorithm selection and comparison
   - Model evaluation metrics
   - Precision vs Recall trade-offs
   - Confusion matrices and interpretation

4. **Software Engineering Practices**
   - Code organization and modularity
   - Documentation standards
   - Version control (Git)
   - Production deployment

5. **Data Science Communication**
   - Visualizing data insights
   - Storytelling with data
   - Stakeholder communication

---

## Resource Requirements

### Data
- SMS Spam Collection dataset (5,572 messages)
- Source: Kaggle (public, free)
- Download: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

### Software & Tools
- Python 3.8+ (free, open-source)
- Jupyter Notebook (free)
- GitHub (free for public repos)
- Streamlit Cloud (free tier available)

### Skills Required
- Python programming
- Basic statistics/ML concepts
- Git version control
- Data visualization

### Time Commitment
- Total: 6-11 hours across 6 weeks
- Per week: 1-2 hours
- Most time: Data exploration and model training

---

## Approval & Sign-Off

**Project Approved By**: _______________  
**Approving Manager**: _______________  
**Date**: _______________  

**Status**: ✓ Ready for Week 2

---

## Next Steps

1. → Move to **Week_2_EDA_DataPrep**
2. → Download `spam.csv` from Kaggle
3. → Execute data preparation notebook
4. → Generate visualizations
5. → Write Data Preparation Report

---

**End of Project Plan**
