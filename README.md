# Substack essay backup — Between Code and Culture

A Python scraper that downloads published essays from [Between Code and Culture](https://www.between-code-and-culture.tech/) and saves them as Markdown files. Used as a personal backup of published essays.

Essays are saved to `published_md/between-code-and-culture/` with frontmatter metadata (title, subtitle, author, publication, date).

## Features

- Scrapes all posts or a specific number
- Supports a single post URL via `--url https://...substack.com/p/my-post`
- Downloads Substack-hosted images locally with `--images`
- Generates a browsable HTML interface (`substack_html_pages/`)
- Supports premium (paid) content when logged in

## Setup

```bash
git clone <repo>
cd substack-to-md

# Optional: create a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# .\venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your Substack credentials (required for premium content):

```bash
cp .env.example .env
```

```
SUBSTACK_EMAIL=your@email.com
SUBSTACK_PASSWORD=yourpassword
```

Requires Chrome for Selenium-based premium scraping.

## Usage

The scraper defaults to `https://www.between-code-and-culture.tech/` and saves to `published_md/`. Run with no arguments to scrape all posts:

```bash
python substack_scraper.py
```

Scrape a specific number of posts:

```bash
python substack_scraper.py --number 10
```

Scrape a different Substack URL:

```bash
python substack_scraper.py --url https://example.substack.com --directory /path/to/save
```

Scrape a single post:

```bash
python substack_scraper.py --url https://example.substack.com/p/my-post
```

Download images locally:

```bash
python substack_scraper.py --images
```

Scrape premium (paid) content:

```bash
python substack_scraper.py --premium
```

## Output structure

```
published_md/
└── between-code-and-culture/
    ├── 2026-03-10-you-lost-them-before-you-got-there.md
    ├── 2026-03-02-one-person-is-a-complainer.md
    └── ...

data/
└── between-code-and-culture.json  # metadata for HTML browser

substack_html_pages/
└── between-code-and-culture.html  # browsable interface
```

## Running tests

```bash
pytest tests/
```
