# SMS Spam Classifier - 6 Week Project

A complete machine learning project to classify SMS messages as Spam or Legitimate, following a structured 6-week curriculum from problem definition through cloud deployment.

## 📁 Project Structure

```
spam-classifier/
├── Week_1_Planning/              # Project planning & strategy
│   ├── Project_Plan.md           # Executive summary & architecture
│   └── README.md
├── Week_2_EDA_DataPrep/          # Data exploration & preparation
│   ├── data_preparation.ipynb    # Jupyter notebook to execute
│   └── README.md
├── Week_3_Modeling/              # Model training & selection
│   ├── model_training.ipynb      # Jupyter notebook to execute
│   └── README.md
├── Week_4_Visualization/         # Data storytelling with charts
│   ├── README.md                 # Analysis instructions
│   └── (visualizations auto-generated)
├── Week_5_Evaluation/            # Model performance & optimization
│   ├── README.md                 # Evaluation guidelines
│   └── (analysis documents)
├── Week_6_Deployment/            # Web app & cloud deployment
│   ├── app/
│   │   ├── streamlit_app.py      # Web interface
│   │   └── preprocessing.py      # NLP pipeline
│   └── README.md
├── data/                         # Downloaded dataset folder
├── requirements.txt              # Python dependencies
├── Procfile                      # Cloud deployment config
├── setup.sh                      # Streamlit setup
├── nltk.txt                      # NLTK data requirements
└── README.md                     # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Git

### Setup Instructions

1. **Clone Repository**
   ```bash
   git clone <repository-url>
   cd spam-classifier
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Dataset**
   - Download `spam.csv` from [Kaggle SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
   - Place in `data/` folder

5. **Follow Weekly Structure**
   - **Week 1**: Read `Week_1_Planning/Project_Plan.md`
   - **Week 2**: Run `Week_2_EDA_DataPrep/data_preparation.ipynb`
   - **Week 3**: Run `Week_3_Modeling/model_training.ipynb`
   - **Week 4**: Write analysis based on visualizations
   - **Week 5**: Write evaluation report
   - **Week 6**: Deploy app using instructions

## 📊 Weekly Breakdown

| Week | Task | Core Deliverable | Key Output |
|------|------|------------------|-----------|
| **1** | Planning & Strategy | Project_Plan.md | Architecture defined |
| **2** | EDA & Data Prep | data_preparation.ipynb | Cleaned dataset + 5 visualizations |
| **3** | Modeling | model_training.ipynb | Trained model + .pkl files |
| **4** | Visualization | Data_Storytelling_Report.md | 7 professional charts analyzed |
| **5** | Evaluation | Model_Performance_Audit.md | Precision analysis & optimization |
| **6** | Deployment | Final_Case_Study.md | Live web app + GitHub repo |

## 🎯 Project Highlights

### Performance Metrics
- **Accuracy**: 97.14%
- **Precision**: 100% (optimized to eliminate false positives)
- **Recall**: 85.71%
- **F1-Score**: 92.31%

### Dataset
- **Size**: 5,572 SMS messages
- **Classes**: 86.6% Legitimate (Ham), 13.4% Spam
- **Source**: Kaggle SMS Spam Collection

### Architecture
```
Raw SMS Messages
    ↓
Phase 1: Data Cleaning & EDA
    ↓
Phase 2: NLP Preprocessing (5-step pipeline)
    ↓
Phase 3: TF-IDF Vectorization (3,000 features)
    ↓
Phase 4: Model Training (5 algorithms tested)
    ↓
Phase 5: Evaluation & Selection (Multinomial NB chosen)
    ↓
Phase 6: Web App & Cloud Deployment
    ↓
Live Predictions on New Messages
```

## 🛠️ Technologies Used

### Data & ML
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **NLTK**: Natural Language Processing
- **Scikit-learn**: Machine learning algorithms
- **TF-IDF**: Text vectorization

### Visualization
- **Matplotlib**: Basic charts
- **Seaborn**: Statistical plots
- **WordCloud**: Word frequency visualization

### Web & Deployment
- **Streamlit**: Web application framework
- **Pickle**: Model serialization
- **Streamlit Cloud/Heroku/Render**: Cloud deployment

## 📝 Each Week Includes

### Week Folder Structure
```
Week_X_Topic/
├── README.md              # Instructions for the week
├── notebook.ipynb         # Jupyter notebook (if applicable)
└── Report.md             # Deliverable document (if applicable)
```

### Deliverables
- **README.md**: Clear instructions for what to do
- **Jupyter Notebooks**: Ready-to-execute code (Weeks 2 & 3)
- **Report Templates**: Markdown files for documentation
- **Visualizations**: Auto-generated charts in `visualizations/`

## 🔄 Workflow

### For Each Week:
1. **Read**: Open `Week_X/README.md` for instructions
2. **Execute**: Run Jupyter notebooks (if applicable)
3. **Analyze**: Review outputs and insights
4. **Document**: Write required report
5. **Submit**: Save all deliverables

## 🌐 Deployment

### Local Testing
```bash
streamlit run Week_6_Deployment/app/streamlit_app.py
```

### Cloud Deployment (Choose One)

**Streamlit Cloud (Easiest)**
- Push to GitHub
- Connect at streamlit.io/cloud
- Auto-deploys in 2-3 minutes

**Heroku**
```bash
heroku login
heroku create your-app-name
git push heroku main
```

**Render.com**
- Connect GitHub repo
- Configure web service
- Deploy

## 📚 Key Learning Outcomes

By completing this project, you'll understand:

✅ **End-to-End ML Pipeline** - From raw data to production  
✅ **NLP Techniques** - Text preprocessing and vectorization  
✅ **Model Comparison** - Testing multiple algorithms  
✅ **Precision vs Accuracy** - Business-focused metrics  
✅ **Web Development** - Building ML interfaces with Streamlit  
✅ **Cloud Deployment** - Moving models to production  
✅ **Data Storytelling** - Communicating insights visually  
✅ **Professional Practices** - Code organization and documentation  

## 📋 Submission Checklist

- [ ] Week 1: Project Plan completed
- [ ] Week 2: Notebook executed, data report written
- [ ] Week 3: Notebook executed, model report written
- [ ] Week 4: Visualizations analyzed, storytelling report written
- [ ] Week 5: Evaluation report completed
- [ ] Week 6: Web app deployed, case study written
- [ ] GitHub: All code pushed to repository
- [ ] README: Updated with live URL

## 🎓 For Your Resume

This project demonstrates:
- Machine Learning expertise
- NLP and text processing skills
- Data analysis and visualization
- Software engineering practices
- Cloud deployment knowledge
- Problem-solving approach

## 📞 File References

### Main Documentation
- `Week_1_Planning/Project_Plan.md` - Full architecture and planning
- `Week_2_EDA_DataPrep/README.md` - Data preparation guide
- `Week_3_Modeling/README.md` - Model training guide
- `Week_4_Visualization/README.md` - Visualization analysis
- `Week_5_Evaluation/README.md` - Evaluation methodology
- `Week_6_Deployment/README.md` - Deployment instructions

### Code Files
- `Week_2_EDA_DataPrep/data_preparation.ipynb` - Data exploration
- `Week_3_Modeling/model_training.ipynb` - Model training
- `Week_6_Deployment/app/streamlit_app.py` - Web application
- `Week_6_Deployment/app/preprocessing.py` - NLP module

## 🚀 Next Steps

1. **Clone this repository**
2. **Read `Week_1_Planning/Project_Plan.md`** to understand the full scope
3. **Start Week 2**: Download dataset and run the notebook
4. **Follow each week in order** (6 weeks total)
5. **Deploy and share your live app** in Week 6

---

**Happy Learning! 🎉**

Start with `Week_1_Planning/README.md` →
