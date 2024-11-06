# **Retrospective Analysis of the Science and Technology in Society Forum Discussions**

## **Overview**

This project focuses on analyzing discussions from the STS (Science and Technology in Society) Forum archives (2004-2023) to reveal key trends in global science and technology topics. The analysis identifies emerging, declining, and peaking topics while understanding the evolving roles of universities, governments, and industries within the forum’s discussions.

## **Project Files**

- **`main.py`**: The primary script for data cleaning and preprocessing.
- **`sts_nlp.ipynb`**: Jupyter Notebook for exploratory data analysis, topic modeling, and visualization.
- **`summaries.csv`**: The cleaned dataset containing session summaries.
- **`summaries_statement.csv`**: Data related to official statements from the forum.
- **`images/`**: Directory containing output figures, including word clouds, MDS topic maps, and co-occurrence visualizations.
- **`downloads/`**: Raw data and interim files from the data collection phase.
- **`main_statement.py`**: Script for additional processing of statement data.

## **Methods**

- **Text Mining**: Tokenization, normalization, and word frequency analysis.
- **Latent Dirichlet Allocation (LDA)**: Topic modeling to uncover key discussion themes.
- **Data Visualization**: Word clouds, topic distance maps using MDS, and co-occurrence networks.
- **Co-occurrence Network Creation**: Visualizing relationships between top terms using Gephi’s ForceAtlas algorithm.

## **Tools Used**

- **Python**: Core programming language.
- **NLTK**: Text processing.
- **Gensim**: LDA topic modeling.
- **Matplotlib & Seaborn**: Data visualization.
- **Scikit-learn**: Clustering and dimensionality reduction.
- **Gephi**: Co-occurrence network visualization.
- **BeautifulSoup**: Web scraping.

![Co-Occurrence Network Visualization](https://github.com/NorikaNarimatsu/STS_nlp/blob/main/images/gephi_nlp.png)


## **Acknowledgments**

This project was completed as a freelance effort to provide insights for the STS Forum, with a focus on shaping future discussions in global science and technology.
