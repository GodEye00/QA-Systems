import pandas as pd

# Load the manually rated evaluation data
evaluation_rated_df = pd.read_csv('../docs/evaluation_rated.csv')

# Define a function to compute accuracy
def compute_accuracy(top_n):
    return (evaluation_rated_df[f'Top {top_n} Accuracy'] == 'Yes').sum() / len(evaluation_rated_df) * 100

# Compute accuracy metrics
top_1_accuracy = compute_accuracy(1)
top_3_accuracy = compute_accuracy(3)

# Save the results to performance.csv
performance_df = pd.DataFrame({
    'Top 1 Accuracy': [top_1_accuracy],
    'Top 3 Accuracy': [top_3_accuracy]
})

performance_df.to_csv('../docs/performance.csv', index=False)
