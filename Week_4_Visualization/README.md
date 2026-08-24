# Week 4: Data Visualization & Storytelling

## Core Task
Generate and interpret key charts: class imbalance pie chart, character/word distribution histograms, feature correlation heatmap, and Spam vs. Ham WordClouds.

## Prerequisites ⚠️
**IMPORTANT**: Complete these FIRST:
1. ✓ Week 2: Run `data_preparation.ipynb` (generates 5 visualizations)
2. ✓ Week 3: Run `model_training.ipynb` (generates 2 more visualizations)

This creates all 7 visualizations needed for Week 4.

## Deliverables

### 1. Jupyter Notebook (Execute This)
**File**: `visualization_analysis.ipynb`
- Loads all 7 visualizations
- Displays each chart
- Provides detailed analysis
- Documents business implications
- Execute this notebook to analyze visualizations

### 2. Report Document (Write This)
**File**: `Data_Storytelling_Report.md` (2-3 pages)
- Executive summary
- Analysis of each visualization
- Business/stakeholder context
- Key insights
- Recommendations

## The 7 Visualizations

**From Week 2 (5 charts):**
1. Class distribution pie chart (imbalance analysis)
2. Feature distributions histograms (message length patterns)
3. Correlation heatmap (feature relationships)
4. Word clouds (spam vs ham words)
5. Top 30 words (frequency analysis)

**From Week 3 (2 charts):**
6. Confusion matrix (best model performance)
7. Model comparison (all algorithms)

## How to Complete Week 4

### Step 1: Verify Visualizations Exist
Run this in terminal:
```bash
ls ../visualizations/
# Should see: 01_class_distribution.png through 07_model_comparison.png
```

### Step 2: Run the Notebook
```bash
jupyter notebook
# Open visualization_analysis.ipynb
# Execute all cells
```

### Step 3: Write Report
Use the notebook output to write `Data_Storytelling_Report.md`:
- For each visualization:
  - What it shows
  - Key insight
  - Business implication

### Step 4: Submit
- ✓ visualization_analysis.ipynb (executed)
- ✓ Data_Storytelling_Report.md (2-3 pages)
- ✓ All 7 visualizations (auto-generated)

## Analysis Template

For each visualization, include:

```markdown
## Visualization [X]: [Name]

### What It Shows
[Description of chart]

### Key Insights
- Insight 1
- Insight 2
- Insight 3

### Business Implications
- Impact 1
- Impact 2
```

## Report Structure
- Executive Summary
- Visualization 1 Analysis (Class Distribution)
- Visualization 2 Analysis (Feature Distributions)
- Visualization 3 Analysis (Correlation Heatmap)
- Visualization 4 Analysis (Word Clouds)
- Visualization 5 Analysis (Top 30 Words)
- Visualization 6 Analysis (Confusion Matrix)
- Visualization 7 Analysis (Model Comparison)
- Overall Findings & Recommendations

## Files in This Folder
- `README.md` (this file)
- `visualization_analysis.ipynb` (run this - includes all analyses)
- `Data_Storytelling_Report.md` (write this report)

## Expected Output
After executing the notebook:
- 7 visualizations displayed
- Analysis and insights provided
- Business implications explained

## Next
→ Move to Week_5_Evaluation
