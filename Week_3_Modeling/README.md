# Week 3: Predictive Modeling & Algorithm Selection

## Core Task
Convert clean text into numbers using TF-IDF vectorization, split data (80/20 train-test), and train candidate classification algorithms (Multinomial Naive Bayes, Bernoulli Naive Bayes, SVM, Random Forest).

## Deliverable
**File**: `Model_Selection_Report.md`
- Algorithm mechanics explained
- Performance comparison table
- Why Multinomial Naive Bayes selected
- Confusion matrix analysis
- .pkl model files exported

## What to Do

### 1. Load Cleaned Data
- Load `cleaned_data.csv` from Week 2

### 2. TF-IDF Vectorization
- Convert text to 3,000 features
- Sparse matrix representation

### 3. Train Test Split
- 80% training (4,363 messages)
- 20% testing (1,091 messages)

### 4. Train 5 Models
- Gaussian Naive Bayes
- Multinomial Naive Bayes ⭐
- Bernoulli Naive Bayes
- SVM
- Random Forest

### 5. Evaluate & Compare
- Accuracy, Precision, Recall
- Confusion matrix for best model
- Model selection justification

### 6. Export Models
- Save as .pkl files
- `tfidf_vectorizer.pkl`
- `spam_classifier_model.pkl`

## Files to Create
- `Model_Selection_Report.md` (2-3 pages)
- `model_training.ipynb` (execute cells)
- Model files in `../models/`

## Expected Performance
- Accuracy: 97.14%
- Precision: 100%
- Recall: 85.71%

## Next
→ Move to Week_4_Visualization
