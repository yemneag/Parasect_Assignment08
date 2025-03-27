# chart.py
# File Name : FunWithAIBenchmarkData
# Student Name: Abel Yemaneab, Will Claus, Hailey Manuel
# email:  yemaneag@mail.uc.edu, clausws@mail.uc.edu, manuelhv@mail.uc.edu
# Assignment Number: Assignment 08 
# Due Date:  03/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This assignment teaches us how to visualize data and import pictures into python.

# Brief Description of what this module does. This module teaches us how to work with and manipulate data.
# Citations: I used ChatGPT

import pandas as pd
import matplotlib.pyplot as plt
"""
class LetterFrequency:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)  # Load the CSV file
    
    def display_data(self):
        # Display first few rows of the dataframe
        print(self.df.head())
    
    def plot_letter_frequency(self):
        # Assuming the 4th column contains the letters (index 3)
        letter_column = self.df.iloc[:, 3]  # Select the 4th column (index 3)
        
        # Count occurrences of each letter
        letter_counts = letter_column.value_counts()  
        
        # Plot the bar chart
        plt.bar(letter_counts.index, letter_counts.values, color='skyblue')
        
        # Labels and title
        plt.xlabel("Letters")
        plt.ylabel("Count")
        plt.title("Frequency of Letters in 4th Column")
        
        # Show the plot
        plt.show()
"""

class LetterFrequency:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)  # Load the CSV file
    
    def display_data(self):
        # Display the first few rows of the dataframe to verify structure
        print(self.df.head())
    
    def plot_letter_frequency(self):
        # Extract column F (index 5, zero-based indexing means it's index 5)
        column_f = self.df.iloc[:, 5]  # Assuming F is the 6th column
        
        # Drop NaN values (if any)
        column_f = column_f.dropna()
        
        # Count occurrences of each unique letter
        letter_counts = column_f.value_counts()
        
        # Plot bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(letter_counts.index, letter_counts.values, color='skyblue')
        
        # Labels and title
        plt.xlabel("Letters")
        plt.ylabel("Count")
        plt.title("Frequency of Letters in Column F")
        
        # Show plot
        plt.show()

# Example of how to 