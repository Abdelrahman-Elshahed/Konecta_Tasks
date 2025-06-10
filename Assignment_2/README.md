# Insurance Data Analysis and Visualization

A comprehensive exploratory data analysis (EDA) project on insurance data using Python data visualization libraries to uncover insights and patterns in medical insurance costs.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Analysis Workflow](#analysis-workflow)
- [Power BI Dashboard](#power-bi-dashboard)



## Project Overview

This project performs extensive exploratory data analysis on an insurance dataset to understand the factors that influence medical insurance costs. Through various statistical visualizations and correlation analysis, we explore relationships between demographic factors, health metrics, and insurance charges.

## Dataset Description

The dataset contains **1,338 records** with the following features:

| Feature | Type | Description |
|---------|------|-------------|
| **age** | Numerical | Age of the primary beneficiary (18-64 years) |
| **sex** | Categorical | Insurance contractor gender (male/female) |
| **bmi** | Numerical | Body mass index (15.0-54.0) |
| **children** | Numerical | Number of children/dependents (0-5) |
| **smoker** | Categorical | Smoking status (yes/no) |
| **region** | Categorical | Beneficiary's residential area (northeast, northwest, southeast, southwest) |
| **charges** | Numerical | Individual medical costs billed by health insurance |


## Project Structure

```
Assignment_2/
│
├── data/
│   └── Insurance.csv                   # Raw insurance dataset
│
├── notebook/
│   └── Assignment2.ipynb               # Main analysis notebook
│
├── power_bi/
│   └── visualization_powerbi.pbix      # Power BI dashboard
│
└── README.md                           # Project documentation
```



## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

**Clone the repository**
   ```bash
   git clone https://github.com/Abdelrahman-Elshahed/Konecta_Tasks.git
   cd Assignment_2
   ```
## Analysis Workflow

### 1. Data Collection and Preprocessing
- Load dataset using pandas
- Check data types and structure
- Identify missing values and duplicates
- Basic statistical summary

### 2. Numerical Features Analysis
**Features analyzed: Age, BMI, Charges**
- **Distribution Analysis**
  - Histograms with 20 bins
  - Kernel Density Estimation (KDE) plots
- **Outlier Detection**
  - Box plots for each numerical feature

### 3. Categorical Features Analysis
**Features analyzed: Sex, Smoker, Region, Children**
- **Frequency Distribution**
  - Count plots for each category
  - Bar charts with custom colors

### 4. Comparative Analysis
- **Charges by Categorical Variables**
  - Box plots showing charge distribution
  - Violin plots showing density distribution
  - Analysis across: Smoker status, Region, Gender, Number of children

### 5. Relationship Exploration
- **Scatter Plot Analysis**
  - BMI vs Charges (colored by smoker status)
  - Age vs Charges (colored by smoker status)
  - BMI vs Charges (colored by gender)
  - Age vs Charges (colored by gender)

### 6. Correlation Analysis
- **Correlation Heatmap**
  - Pearson correlation coefficients
  - Numerical features correlation matrix

### 7. Pairwise Relationships
- **Pair Plots**
  - All numerical features combinations
  - Colored by smoker status and gender
  - Diagonal histograms for distributions
 
## Power BI Dashboard
- **Interactive Business Intelligence Dashboard**
- ![Image](https://github.com/user-attachments/assets/a1929118-3e2f-4123-8961-578567e7ddb0)

  - **Key Performance Indicators (KPIs)**
    - Average insurance charges: $13.27K
    - Total customers: 1,338
    - Average BMI: 30.66
  
  - **Visualizations Include:**
    - Age vs Insurance Charges scatter plot with smoker status filtering
    - Gender distribution pie chart (50.52% female, 49.48% male)
    - Average charges by age histogram
    - Average charges by smoker status comparison
    - Average charges by number of children trend analysis
  
  - **Interactive Features:**
    - Filter by smoker status (yes/no)
    - Dynamic cross-filtering between visualizations
    - Drill-down capabilities for detailed analysis
