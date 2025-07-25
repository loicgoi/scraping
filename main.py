from pipelines.pipeline_scraping import run_scraping_pipeline
from pipelines.pipeline_api import run_api_pipeline

if __name__ == "__main__":
    # Scraping classique
    run_scraping_pipeline(base_url="http://books.toscrape.com/catalogue/page-{}.html", pages=50)

    # Requête Google Books
    run_api_pipeline(query="food", max_results=40)