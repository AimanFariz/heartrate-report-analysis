import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read the CSV file
file_path = r"C:\Users\user\Downloads\20231101_185044_The+University+of+Tulsa+Mens+Soccer_Soccer.csv"
df = pd.read_csv(file_path)

# Columns to analyze
columns_to_analyze = ['Player name', 'Time in HR zone 4 (80 - 89 %)', 'Time in HR zone 5 (90 - 100 %)',
                      'Maximum speed [km/h]', 'Sprints', 'Distance in Speed zone 3 [m] (14.40 - 19.78 km/h)',
                      'Distance in Speed zone 4 [m] (19.79 - 25.18 km/h)', 'Distance in Speed zone 5 [m] (25.19- km/h)',
                      'Number of accelerations (2.00 - 2.99 m/s²)', 'Number of accelerations (3.00 - 50.00 m/s²)',
                      'Training load score', 'HRV (RMSSD)']

# Create a subset of the DataFrame with selected columns
df_subset = df[columns_to_analyze]

# Convert relevant columns to numeric (some may contain non-numeric data)
numeric_columns = ['Time in HR zone 4 (80 - 89 %)', 'Time in HR zone 5 (90 - 100 %)', 'Maximum speed [km/h]',
                   'Sprints', 'Distance in Speed zone 3 [m] (14.40 - 19.78 km/h)',
                   'Distance in Speed zone 4 [m] (19.79 - 25.18 km/h)',
                   'Distance in Speed zone 5 [m] (25.19- km/h)',
                   'Number of accelerations (2.00 - 2.99 m/s²)', 'Number of accelerations (3.00 - 50.00 m/s²)',
                   'Training load score', 'HRV (RMSSD)']

# Use .loc to avoid SettingWithCopyWarning
df_subset.loc[:, numeric_columns] = df_subset[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Create a new column with shortened player names using .loc to avoid SettingWithCopyWarning
df_subset['Shortened Name'] = df_subset['Player name'].apply(lambda x: x.split(' ')[0])

# Create charts
plt.figure(figsize=(18, 12))

# Bar charts for Time in HR zone 4 and Time in HR zone 5 using the shortened names
plt.subplot(3, 3, 1)
sns.barplot(x='Shortened Name', y='Time in HR zone 4 (80 - 89 %)', data=df_subset)
plt.title('Time in HR zone 4')

plt.subplot(3, 3, 2)
sns.barplot(x='Shortened Name', y='Time in HR zone 5 (90 - 100 %)', data=df_subset)
plt.title('Time in HR zone 5')

# Bar charts for speed zones
speed_zones = ['Distance in Speed zone 3 [m] (14.40 - 19.78 km/h)',
               'Distance in Speed zone 4 [m] (19.79 - 25.18 km/h)',
               'Distance in Speed zone 5 [m] (25.19- km/h)']

for i, speed_zone in zip(range(1, len(speed_zones) + 1), speed_zones):  
    plt.subplot(3, 3, i + 2)  
    sns.barplot(x='Shortened Name', y=speed_zone, data=df_subset)
    plt.title(f'{speed_zone}')

# Bar charts for sprints and maximum speed
plt.subplot(3, 3, 6)
sns.barplot(x='Shortened Name', y='Sprints', data=df_subset)
plt.title('Number of Sprints')

plt.subplot(3, 3, 5)
sns.barplot(x='Shortened Name', y='Maximum speed [km/h]', data=df_subset)
plt.title('Maximum Speed')

# Bar charts for HRV (RMSSD), Training load score, Number of accelerations (2.00 - 2.99 m/s²), and Number of accelerations (3.00 - 50.00 m/s²)
plt.subplot(3, 3, 7)
sns.barplot(x='Shortened Name', y='HRV (RMSSD)', data=df_subset)
plt.title('HRV (RMSSD)')

plt.subplot(3, 3, 8)
sns.barplot(x='Shortened Name', y='Training load score', data=df_subset)
plt.title('Training Load Score')

plt.subplot(3, 3, 9)
sns.barplot(x='Shortened Name', y='Number of accelerations (2.00 - 2.99 m/s²)', data=df_subset)
plt.title('Number of accelerations (2.00 - 2.99 m/s²)')

plt.subplot(3, 3, 4)
sns.barplot(x='Shortened Name', y='Number of accelerations (3.00 - 50.00 m/s²)', data=df_subset)
plt.title('Number of accelerations (3.00 - 50.00 m/s²)')

# Save the figure to a new file
plt.tight_layout()
plt.savefig('analysis_results.pdf')

plt.show()
