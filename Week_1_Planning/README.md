# Week 1: Project Planning & Strategy

## Core Task
Define the problem scope, end-to-end architecture (Data → NLP Pipeline → Model → Web App), weekly timeline, and risk mitigation strategies.

## Deliverable
**File**: `Project_Plan.md`
- Executive Summary
- Problem Statement
- Solution Architecture (5 phases)
- Dataset Overview
- Technology Stack
- Weekly Timeline
- Risk Matrix & Mitigation

## What to Include in Project Plan

### 1. Executive Summary
- Project title and objective
- Expected outcomes
- Key success metrics

### 2. Problem Statement
- What problem are we solving?
- Why does it matter?
- Business impact

### 3. Architecture Overview
```
Phase 1: Data Cleaning & EDA
Phase 2: NLP Preprocessing Pipeline  
Phase 3: Predictive Modeling
Phase 4: Web Application
Phase 5: Cloud Deployment
```

### 4. Dataset Description
- Source: Kaggle SMS Spam Collection
- Size: 5,572 messages
- Class distribution: 86.6% Ham, 13.4% Spam

### 5. Success Metrics
- Accuracy ≥ 95%
- Precision ≥ 98%
- Live deployable URL

### 6. Risk Matrix
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|-----------|
| Dataset not representative | Low | Medium | Use Kaggle public dataset |
| Class imbalance | High | High | Optimize for Precision |
| Overfitting | Medium | Medium | Use test set validation |
| Deployment failure | Medium | Low | Test locally first |

## Files to Create
- `Project_Plan.md` (2-3 pages)

## Next
→ Move to Week_2_EDA_DataPrep
