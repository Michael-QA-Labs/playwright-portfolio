# SauceDemo E2E Test Suite

Automated end-to-end test suite for the SauceDemo web application, built with Python, Playwright, and pytest using the Page Object Model design pattern.

## Project Structure

    playwright-portfolio/
    ├── pages/
    │   ├── login_page.py        # Login page interactions
    │   ├── inventory_page.py    # Product inventory interactions
    │   ├── cart_page.py         # Shopping cart interactions
    │   └── checkout_page.py     # Checkout flow interactions
    ├── tests/
    │   └── e2e/
    │       ├── test_login.py    # Authentication test cases
    │       └── test_checkout.py # Purchase flow test cases
    ├── conftest.py              # Pytest fixtures and browser config
    ├── pytest.ini               # Pytest settings
    └── requirements.txt         # Project dependencies

## Tech Stack

- Python 3.14
- Playwright 1.60 — browser automation
- pytest — test framework
- Page Object Model — design pattern for maintainable test architecture

## Test Coverage

### Authentication
- Valid login redirects to inventory page
- Locked out user sees error message
- Invalid password shows error
- Empty credentials shows validation message

### Purchase Flow
- Full happy path: login → add item → cart → checkout → order confirmation
- Incomplete checkout form triggers validation error

## Setup

Clone the repo and create a virtual environment:

    git clone https://github.com/Michael-QA-Labs/playwright-portfolio.git
    cd playwright-portfolio
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    playwright install

## Running Tests

Run the full suite:

    pytest tests/ -v

Run a specific file:

    pytest tests/e2e/test_login.py -v

Run headless:

    pytest tests/ -v --headed=false

## Design Decisions

**Page Object Model** — Each page is its own class. Selectors and interactions live in the page object, not the test. If the UI changes, one file gets updated, not every test that touches that page.

**Role-based locators** — Tests use get_by_role and get_by_placeholder instead of XPath or fragile CSS selectors. This mirrors how a user actually sees the page and makes tests more resilient to UI changes.

**Negative test cases** — Suite covers locked out users, wrong credentials, empty fields, and incomplete checkout. Real bugs live in edge cases, not just the happy path.

## Author

Michael Garcia — QA Engineer
GitHub: https://github.com/Michael-QA-Labs
LinkedIn: https://www.linkedin.com/in/your-profile
