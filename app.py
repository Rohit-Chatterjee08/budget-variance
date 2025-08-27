# app_budget.py

import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time # We'll import time to simulate steps

# --- 1. The Core Analysis and Visualization Logic ---
# <<< CHANGED: Added the 'progress' argument
def analyze_variance(budget_file, actuals_file, progress=gr.Progress()):
    """
    Takes uploaded budget and actuals files, performs variance analysis,
    and returns a summary DataFrame and a visualization.
    """
    try:
        # --- A. Data Loading with Progress Update ---
        progress(0.1, desc="Loading files...")
        if budget_file is None or actuals_file is None:
            raise ValueError("Please upload both a budget and an actuals file.")
            
        budget_df = pd.read_csv(budget_file.name)
        actuals_df = pd.read_csv(actuals_file.name)
        time.sleep(0.5) # Simulate work

        # Basic validation of required columns
        progress(0.3, desc="Validating file columns...")
        if 'Category' not in budget_df.columns or 'Budget' not in budget_df.columns:
            raise ValueError("Budget file must contain 'Category' and 'Budget' columns.")
        if 'Category' not in actuals_df.columns or 'Amount' not in actuals_df.columns:
            raise ValueError("Actuals file must contain 'Category' and 'Amount' columns.")
        time.sleep(0.5)

        # --- B. Analysis with Progress Update ---
        progress(0.5, desc="Aggregating transactions... (This may take a while for large files)")
        actuals_grouped = actuals_df.groupby('Category')['Amount'].sum().reset_index()
        actuals_grouped.rename(columns={'Amount': 'Actual'}, inplace=True)
        
        progress(0.7, desc="Calculating variance...")
        summary_df = pd.merge(budget_df, actuals_grouped, on='Category', how='left')
        summary_df['Actual'].fillna(0, inplace=True)
        summary_df['Variance'] = summary_df['Budget'] - summary_df['Actual']
        time.sleep(0.5)

        # --- C. Visualization with Progress Update ---
        progress(0.8, desc="Creating visualization...")
        colors = ['green' if x >= 0 else 'red' for x in summary_df['Variance']]
        
        fig, ax = plt.subplots(figsize=(12, 7))
        sns.barplot(x='Category', y='Variance', data=summary_df, palette=colors, ax=ax)
        
        ax.axhline(0, color='black', linewidth=0.8)
        ax.set_title('Budget Variance Analysis', fontsize=16)
        ax.set_xlabel('Spending Category', fontsize=12)
        ax.set_ylabel('Variance (Budget - Actual)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        time.sleep(0.5)

        progress(1.0, desc="Done!")
        return summary_df, fig, "Analysis Complete!"

    except Exception as e:
        return None, None, f"Error: {e}"

# --- 2. Build the Gradio App ---
with gr.Blocks(theme=gr.themes.Soft(), title="Budget Variance Analyzer") as app:
    gr.Markdown("# 📊 Budget Variance Analyzer")
    gr.Markdown("Upload your budget and actual spending files (CSV) to see how you're doing.")

    with gr.Row():
        budget_input = gr.File(label="Upload Budget CSV")
        actuals_input = gr.File(label="Upload Actuals CSV")
    
    analyze_button = gr.Button("Analyze", variant="primary")
    
    status_output = gr.Textbox(label="Status")
    
    with gr.Row():
        summary_output = gr.DataFrame(label="Variance Summary")
        plot_output = gr.Plot(label="Variance Chart")

    # <<< CHANGED: No changes here, Gradio automatically handles the progress bar
    analyze_button.click(
        fn=analyze_variance,
        inputs=[budget_input, actuals_input],
        outputs=[summary_output, plot_output, status_output]
    )
    
    gr.Examples(
        examples=[["sample_budget.csv", "sample_actuals.csv"]],
        inputs=[budget_input, actuals_input],
        fn=analyze_variance,
        outputs=[summary_output, plot_output, status_output],
        cache_examples=True
    )

app.launch()