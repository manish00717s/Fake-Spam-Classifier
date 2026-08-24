# Week 2: Exploratory Data Analysis & Data Preparation

## Core Task
Clean the dataset (remove duplicates/nulls, label encode targets), extract meta-features (character, word, and sentence counts), and build the 5-step NLP cleaning pipeline (lowercasing, tokenization, removing special characters/stopwords/punctuation, and Porter stemming).

## Deliverable
**File**: `Data_Preparation_Report.md`
- Before vs. After data structure
- Data cleaning process
- Meta-features extraction
- NLP preprocessing pipeline logic
- Visualizations: Class distribution, Distributions, Correlation heatmap, Word clouds, Top words

## What to Do

### 1. Prepare Data
- Load `spam.csv`
- Remove nulls and duplicates
- Rename columns (v1→target, v2→text)
- Label encode (Ham=0, Spam=1)

### 2. Exploratory Analysis
- Analyze class distribution (86.6% Ham, 13.4% Spam)
- Extract meta-features:
  - Number of characters
  - Number of words
  - Number of sentences
- Generate visualizations

### 3. NLP Preprocessing
Implement 5-step pipeline:
1. **Lowercasing** - Normalize case
2. **Tokenization** - Break into words
3. **Special character removal** - Keep alphanumeric
4. **Stopword removal** - Remove filler words
5. **Stemming** - Reduce to root forms

### 4. Visualizations (5 Required)
- ✓ `01_class_distribution.png` - Pie chart
- ✓ `02_distributions.png` - Histograms  
- ✓ `03_correlation_heatmap.png` - Heatmap
- ✓ `04_word_clouds.png` - Word clouds
- ✓ `05_top_words.png` - Bar charts

## Files to Create
- `Data_Preparation_Report.md` (2-3 pages)
- `data_preparation.ipynb` (execute cells)
- Visualizations in `../visualizations/`

## Notebook Execution
Run all cells in `data_preparation.ipynb` to generate:
- Cleaned dataset
- 5 visualizations
- Meta-features extraction

## Next
→ Move to Week_3_Modeling
