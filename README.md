# BigQuery Hackathon: Smart Substitute Recommender

A BigQuery-powered solution that suggests ideal product substitutes based on a deep understanding of product attributes, not just shared tags or categories.

## Project Overview

This project demonstrates how to build a smart product recommendation system using BigQuery and machine learning techniques. The system analyzes product attributes to suggest substitutes that are semantically similar rather than relying solely on traditional category-based matching.

## Notebooks

### 1. Setup_Table_Analysis_with_Bigquery.ipynb

This notebook handles the initial data setup and analysis using BigQuery:

- **Data Exploration**: Analyzes TheLook E-commerce dataset structure, including product counts, categories, brands, and departments
- **Feature Engineering**: Creates a `product_features` table with semantic descriptions of products
- **Embedding Generation**: Sets up a text embedding model using the `text-embedding-004` endpoint
- **Vector Search**: Generates product embeddings for semantic similarity search

Key operations:
- Dataset overview and statistics
- Product feature extraction and transformation
- Text embedding model creation
- Vector-based similarity calculations

### 2. Ecommerce_Recommendation_with_Python.ipynb

This notebook implements the recommendation system using Python with BigQuery integration:

- **Environment Setup**: Configures BigFrames and pandas for data processing
- **Smart Product Explorer**: Implements a class for enhanced product exploration with intelligent filtering
- **Recommendation Engine**: Builds a system that suggests product substitutes based on semantic similarity
- **Visualization**: Includes data visualization tools for exploring product relationships

The notebook demonstrates how to use the embeddings generated in the first notebook to create a sophisticated recommendation system that understands product relationships beyond simple categorization.

## Getting Started

1. Ensure you have access to Google Cloud and BigQuery
2. Run the `Setup_Table_Analysis_with_Bigquery.ipynb` notebook first to prepare the data
3. Then run `Ecommerce_Recommendation_with_Python.ipynb` to implement and test the recommendation system
