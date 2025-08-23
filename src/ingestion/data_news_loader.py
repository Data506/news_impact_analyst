# Libraries
import os
import sys
import pandas as pd
from datetime import datetime
import feedparser

# al inicio del .py
from pathlib import Path
import sys

THIS_FILE = Path(__file__).resolve()
PROJECT_ROOT = THIS_FILE.parents[1] 
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.paths import RAW_DATA_DIR


def get_rss_news(ticker: str, max_articles: int = 20) -> pd.DataFrame:
    url = f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={ticker}&region=US&lang=en-US"
    feed = feedparser.parse(url)

    news = []
    for entry in feed.entries[:max_articles]:
        news.append({
            "ticker": ticker,
            "title": entry.title,
            "url": entry.link,
            "published_date": datetime(*entry.published_parsed[:6]).isoformat() if 'published_parsed' in entry else None,
            "summary": entry.summary if 'summary' in entry else None
        })

    return pd.DataFrame(news)

tickers = [
    # Biotech / Pharma
    "PFE", "MRNA", "BNTX", "JNJ", "AZN", "AMGN", "REGN", "LLY", "GILD", "BIIB",
    
    # Tech
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA", "INTC", "AMD", "PLTR",
    
    # Consumer
    "PG", "KO", "PEP", "WMT", "COST", "TGT", "MCD", "SBUX", "NKE", "UL"
]

all_news = []

for ticker in tickers:
    try:
        df_ticker_news = get_rss_news(ticker, max_articles=20)
        all_news.append(df_ticker_news)
        print(f"✔ Collected {len(df_ticker_news)} articles from {ticker}")
    except Exception as e:
        print(f"❌ Error collecting from {ticker}: {e}")

df_all_news = pd.concat(all_news, ignore_index=True)

# Drop duplicates
hist_news = pd.read_csv(RAW_DATA_DIR + '\\news.csv', sep=';', decimal='.', encoding='utf-8-sig', index_col=0)

pd.concat([df_all_news, hist_news], axis=0).drop_duplicates().to_csv(RAW_DATA_DIR + '\\news.csv',
                                                                    sep=';',
                                                                    decimal='.',
                                                                    encoding='utf-8-sig')