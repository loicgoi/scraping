from pipelines.pipeline_scraping import run_scraping_pipeline

if __name__ == "__main__":
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"  # URL au choix ici
    df = run_scraping_pipeline(pages=50, base_url=base_url)