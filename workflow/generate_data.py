import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate sample data
num_samples = 100
data = {
    'num_rooms': np.random.randint(1, 6, num_samples),  # 1 to 5 rooms
    'house_age': np.random.randint(1, 50, num_samples),  # 1 to 50 years
    'distance_to_center': np.random.uniform(1, 15, num_samples),  # 1 to 15 km
    'house_price': np.random.uniform(50, 500, num_samples)  # in $000s
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Adding some noise to 'house_price' based on 'num_rooms' and 'house_age'
df['house_price'] += df['num_rooms'] * 10 - df['house_age'] * 2

# Save to CSV
df.to_csv('data.csv', index=False)

print("Sample data.csv created with {} entries.".format(num_samples))
