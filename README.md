# BigQuery Hackathon: Smart Substitute Recommender

A BigQuery-powered solution that suggests ideal product substitutes based on a deep understanding of product attributes, not just shared tags or categories.

## Project Overview

This project demonstrates how to build a smart product recommendation system using BigQuery and machine learning techniques. The system analyzes product attributes to suggest substitutes that are semantically similar rather than relying solely on traditional category-based matching.

# Project Structure
```
-  bigquery-hackathon
   |-- .env.example
   |-- .gitignore
   |-- README.md
   |-- pyproject.toml
   |-- uv.lock
   |-- Setup_Table_Analysis_with_Bigquery.ipynb
   |-- Ecommerce_Recommendation_with_Python.ipynb
```
### Prerequisites

- Google Cloud account with BigQuery enabled and get service account JSON key
- Python 3.10+
- `uv` package manager
- `virtualenv` (recommended for isolated environment setup)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/bigquery-hackathon.git
   cd bigquery-hackathon
   ```

2. Set up a virtual environment and setup dependencies
   ```
   uv init
   uv sync
   ```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update `GOOGLE_APPLICATION_CREDENTIALS` with your service account JSON key path

4. Run the notebooks in your virtual environment:

```
source .venv/bin/activate
python -m ipykernel install --user --name=bigquery-hackathon --display-name "Python (bigquery-hackathon)"
uv run --with jupyter jupyter lab
```

This will open Jupyter Lab in your browser where you can run the notebooks. Make sure to select the `Python (bigquery-hackathon)` kernel when running the notebooks.

## Notebooks

### 1. Setup_Table_Analysis_with_Bigquery.ipynb

This notebook handles the initial data setup and analysis using BigQuery:

- **Data Exploration**: Analyzes TheLook E-commerce dataset structure, including product counts, categories, brands, and departments
- **Feature Engineering**: Creates a `product_features` table with semantic descriptions of products
- **Embedding Generation**: Sets up a text embedding model using the `text-embedding-004` endpoint
- **Vector Search**: Generates product embeddings for semantic similarity search
- **Semantic Similarity**: Calculates cosine similarity between product embeddings to find semantically similar products with different categories or brands with 

Key operations:
- Dataset overview and statistics
- Product feature extraction and transformation
- Text embedding model creation
- Vector-based similarity calculations

Mostly this notebook includes 7 different types of semantic search:

**Test 1: Basic Similar Product (semantic):** This test identifies products that are semantically similar to a target product using cosine distance between their embeddings. It orders results by similarity score.

**Test 2: Smart Multi-Factor Recommendations (semantic):** This test provides recommendations by combining semantic similarity with other factors like price similarity, category bonus, and brand bonus to create a weighted 'total score'.

**Test 3: Cross-Category Discovery:** This test aims to find similar products across different categories from the target product's category, based purely on semantic similarity.

**Test 4: Price-Conscious Recommendations (semantic):** This test focuses on recommending semantically similar products that also fall within a certain price range (e.g., cheaper or same price) compared to the target product.

**Test 5: Trend-Aware Recommendations (semantic):** This test combines semantic similarity with product popularity (order count) to recommend products that are both semantically similar and trending.

**Test 6: Department-Level Exploration (semantic):** This test explores semantically similar products in a different department than the target product's department.

**Test 7: Inventory-Level in-Stock Substitutes (semantic):** This test identifies semantically similar products that are currently in stock, ensuring that recommendations are available for purchase.

### 2. Ecommerce_Recommendation_with_Python.ipynb

This notebook implements the more indepth recommendation system using Python with BigQuery integration:

- **Environment Setup**: Configures BigFrames and pandas for data processing
- **Smart Product Explorer**: Implements a class for enhanced product exploration with intelligent filtering
- **Recommendation Engine**: Builds a system that suggests product substitutes based on semantic similarity
- **Visualization**: Includes data visualization tools for exploring product relationships

The notebook demonstrates how to use the embeddings generated in the first notebook to create a sophisticated recommendation system that understands product relationships beyond simple categorization.

## Getting Started

1. Ensure you have access to Google Cloud and BigQuery
2. Run the `Setup_Table_Analysis_with_Bigquery.ipynb` notebook first to prepare the data
3. Then run `Ecommerce_Recommendation_with_Python.ipynb` to implement and test the recommendation system
