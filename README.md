# 📊 Budget Variance Analyzer

An interactive web application that provides a clear analysis of actual spending versus a planned budget.

## Live Demo

You can try the live application here: **[Your Hugging Face Space URL]**

---

## Overview

This tool helps users track their financial health by visualizing the difference—or "variance"—between their budget and their actual transactions. It's a practical financial analysis application, not a predictive model.

**Key Features:**
-   **CSV Upload:** Allows users to upload their own budget and transaction files.
-   **Automated Analysis:** Automatically aggregates transactions by category and calculates the variance against the budget.
-   **Clear Visualization:** Generates a color-coded bar chart where green bars indicate being under budget (favorable) and red bars indicate overspending (unfavorable).
-   **User-Friendly:** Includes a progress bar to provide feedback when processing large transaction files.

---

## How to Use

The application requires two CSV files with specific columns:

1.  **Budget File:** A CSV containing at least two columns: `Category` and `Budget`.
2.  **Actuals File:** A CSV of transactions containing at least two columns: `Category` and `Amount`.

Simply upload both files using the interface and click the "Analyze" button to see the results.

---

## Technology Stack

-   **Backend & Analysis:** Python, Pandas
-   **Web Framework/UI:** Gradio
-   **Plotting:** Matplotlib, Seaborn

---

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [Your GitHub Repository URL]
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd [repository-name]
    ```
3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **(Optional) Generate sample files:**
    ```bash
    python create_samples.py
    ```
5.  **Run the application:**
    ```bash
    python app_budget.py
    ```
