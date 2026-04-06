# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python trading project for fetching stock price data (JoinQuant, AKShare), storing in PostgreSQL via SQLAlchemy, and performing analysis with OpenAI/Qwen.

## Setup

```bash
# Install dependencies
pip install -e .

# Or via uv
uv sync
```

## Run

```bash
# Run main data fetch and storage
python -m src.trading.base_data.test_hist

# Run analysis
python -m src.trading.analysis.first_qwen
```

## Architecture

```
src/trading/
├── base_data/      # Price data fetching (jqdatasdk, akshare)
│   ├── pricedata.py    # get_price(), get_day_price(), get_minute_price()
│   └── test_hist.py    # Development script example
├── models/         # SQLAlchemy ORM models
│   └── security_price.py  # SecurityPrice table (day_price)
└── analysis/       # Analysis modules (OpenAI/Qwen integration)
    └── first_qwen.py     # Qwen API streaming example
```

## Key Data Flow

1. `pricedata.py` fetches data from JoinQuant (jqdatasdk) or AKShare
2. `models/security_price.py` defines `SecurityPrice` ORM model mapped to PostgreSQL `day_price` table
3. Use `security_price.add_batch()` to bulk-insert price data
4. `analysis/` modules perform analysis on stored/retrieved data

## Database

- PostgreSQL at `127.0.0.1/postgres` (credentials: `postgres:postgres`)
- SQLAlchemy scoped sessions with thread-local isolation
- Unique constraint on (security, date) prevents duplicates

## Dependencies

- **Data sources**: jqdatasdk, akshare
- **Storage**: sqlalchemy, psycopg2-binary
- **Analysis**: pandas, matplotlib, mplfinance, openai
