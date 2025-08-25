from playwright.sync_api import sync_playwright
import pandas as pd

def scrape_indiamart(product):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://www.indiamart.com/products/{product}.html")
        items = page.query_selector_all(".lst-product")
        data = []
        for item in items:
            try:
                name = item.query_selector(".prdct-name").inner_text()
                price = item.query_selector(".prdct-price").inner_text()
                data.append({"name": name, "price": price})
            except:
                continue
        browser.close()
    df = pd.DataFrame(data)
    df.to_csv("../../data/marketplace.csv", index=False)
    return df

if __name__ == "__main__":
    df = scrape_indiamart("basmati-rice")
    print(df.head())
