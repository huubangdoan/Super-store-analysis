## This is the project to solve problems such as:
+ make prediction
+ find the connection
+ spot thing unusual
+ indentify the theme# 📊 Super Store Dashboard

A sales & profit analytics dashboard built with **Streamlit** and **Plotly**, based on the Superstore dataset.

## 🎯 Goal
Visualize sales data to answer key business questions:
- Which regions and product categories drive the most revenue and profit?
- How does discount level affect profit?
- Which customer segment contributes the most revenue?
- Which states/cities have the highest sales?

## 🗂️ Dataset
Source: [Superstore Dataset - Kaggle](https://www.kaggle.com/datasets/itssuru/super-store)

Main columns: `Ship Mode`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Category`, `Sub-Category`, `Sales`, `Quantity`, `Discount`, `Profit`

## 📁 Project Structure
```
├── data/
│   ├── raw/
│   │   └── SampleSuperstore.csv     
│   └── processed/
│       └── describeSuperstore.csv   
├── reports/
│   └── findings.md          
├── app.py                  
├── requirements.txt
└── README.md

```
## ▶️ Running the Dashboard

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

## 📈 Dashboard Features
- **Filters**: Region, Category, Segment (sidebar)
- **KPI cards**: Total Sales, Total Profit, Total Quantity, Profit Margin
- **Charts**:
  - Sales by Sub-Category
  - Profit by Region
  - Sales share by Segment
  - Discount vs Profit (scatter plot)
- **Table**: Top 10 States by Sales

## 🔍 Analysis Findings
See detailed insights and observations in [`reports/findings.md`](reports/findings.md)

## 🛠️ Tech Stack
- Python
- Streamlit
- Pandas
- Plotly Express

## 🚀 Live Demo
`https://super-store-dashboard1.streamlit.app/`

## 📄 License
The dataset belongs to the original author on Kaggle. Code in this repo is intended for learning/portfolio purposes.
+ catagory features
+ find the pattern
## My exploration is in finding.md in reports folder.
## link of my dataset: 
https://www.kaggle.com/datasets/itssuru/super-store
