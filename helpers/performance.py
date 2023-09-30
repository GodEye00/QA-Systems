import pandas as pd

# Load the manually rated evaluation data
evaluation_rated_df = pd.read_csv('../docs/evaluation_rated.csv', encoding='ISO-8859-1')

# declare an empty array to store the performance accuracy
performance_df = []

# Define a function to compute accuracy
def compute_accuracy():
    summation = 0
    performance = []
    for _, row in evaluation_rated_df.iterrows():
        summation += sum([row[f'Is Passage {j} Relevant? (Yes/No)'] == 'Yes' for j in range(1, 4)])
        top_1_accuracy = (summation)/1 * 100
        top_3_accuracy = (summation)/3 * 100
        performance.append({
        'Top 1 Accuracy': top_1_accuracy,
        'Top 3 Accuracy': top_3_accuracy
    })
    return performance


# Compute accuracy metrics
performance_df = compute_accuracy()

# Convert to DataFrame
performance_df = pd.DataFrame(performance_df)

# Save the results to performance.csv
performance_df.to_csv('../docs/performance.csv', index=False)
