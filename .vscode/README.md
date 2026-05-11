
 Life Decision Simulator Pro
 
 
Project Description

The Life Decision Simulator is a professional financial modeling tool built with Python and Streamlit. It is designed to help users visualize the long-term impact of their financial choices. By inputting real-life variables like salary, taxes, and savings goals, the app projects future wealth accumulation.

A key feature of this app is the Spending Advisor, which analyzes the "Opportunity Cost" of major purchases. It dynamically advises whether a user should spend money on an item (like a car or vacation) or invest that money instead, based on their long-term financial health.


How to Run the App

To run the production version of the application:

Ensure you have Python 3.x installed.

Install the required libraries using pip:


Bash
pip install streamlit pandas
Execute the app from the root directory:

Bash
streamlit run dist/main.py


Help & User Instructions

Setup your Profile: Use the sidebar to enter your Annual Salary, Tax Rate, and the percentage of income you want to save.

Handle Windfalls: Enter any sudden income (like a bonus) or emergency expenses in the "Sudden Events" section.

Get Spending Advice: In the main dashboard, enter an item you want to buy and its cost. The app will provide a Verdict (Safe, Caution, or Do Not Buy) based on how much future wealth you would lose.

Save & Compare: - Click "Save This Scenario" to store your current data.

Use the "Overlay" dropdown to see your current path compared to saved scenarios on the chart.

Use the "Delete" dropdown in the Scenario Manager to remove old entries.

File Structure
/ (Root): Contains the main documentation (README.md) and the project demo (demo.mp4).

/src: The development "Playground." This is where the code was actively written and tested (GitDoc tracked all changes here).

main.py: The entry point for development.

logic.py: Contains the math functions for wealth calculation and the Spending Advisor logic.

/data: Storage for development-phase JSON files.

/dist: The stable "Production" version. This is the polished, bug-free version intended for grading.

main.py: The production entry point.

logic.py: Stable investment logic.

/data: Contains scenarios.json, the database for saved user scenarios.


Development Process (Version Control)

This project follows a strict version control workflow using VSCode + GitDoc.

AutoSave: Enabled.

Auto-Commit: GitDoc committed every code change to GitHub, documenting the "evolution" of the logic from a simple script to a full app.

Transition: Stable features were moved from src/ to dist/ once verified as working.


AI & Open Source Disclosure

AI Use: AI was used exclusively for generating project documentation and this README file. The application logic, financial math, and Streamlit integration were developed manually by the author.

Open Source: Layout patterns for Streamlit columns and metrics were referenced from the official Streamlit documentation.