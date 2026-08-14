# CodeAlpha Task 2 - Exploratory Data Analysis (EDA)

## 📊 Project Overview

This project performs Exploratory Data Analysis (EDA) on a book dataset
collected through web scraping.

The analysis explores book prices, ratings, availability, data quality,
patterns, trends, and the relationship between price and rating.

## 🎯 Objectives

- Understand the structure of the dataset
- Explore variables and data types
- Check for missing values and duplicate records
- Analyze book price distribution
- Analyze rating distribution
- Identify trends and patterns
- Detect potential price outliers
- Study the relationship between price and rating
- Create professional data visualizations
- Generate meaningful insights

## 🛠️ Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## 📁 Dataset

The dataset contains 20 books with the following columns:

| Column | Description |
|---|---|
| Title | Name of the book |
| Price | Price of the book |
| Availability | Stock availability |
| Rating | Book rating from One to Five |

## 🔍 EDA Performed

The notebook includes:

1. Dataset structure and data types
2. Statistical summary
3. Missing value analysis
4. Duplicate record analysis
5. Price analysis
6. Rating distribution
7. Price distribution visualization
8. Rating visualization
9. Price vs Rating analysis
10. Correlation analysis
11. Outlier detection using the IQR method
12. Average price by rating

## 📈 Key Findings

- The dataset contains **20 books**.
- There are **no missing values**.
- There are **no duplicate records**.
- The average book price is **£38.05**.
- The minimum book price is **£13.99**.
- The maximum book price is **£57.25**.
- The most common rating is **One**, with 6 books.
- No potential price outliers were detected using the IQR method.
- The price-rating correlation is **-0.076**, indicating a very weak
  negative linear relationship.
- The highest average price occurs for books with a rating of **Three**
  (£42.32).

## ✅ Conclusion

The EDA provides useful insights into book prices and ratings.
The dataset is clean, with no missing values or duplicate records.

The analysis shows that book prices vary considerably, while the weak
price-rating correlation suggests that price is not a strong indicator
of book rating in this dataset.

The visualizations and statistical analysis provide a foundation for
further data analysis and visualization tasks.