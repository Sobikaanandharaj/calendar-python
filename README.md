# Fizzy Calendar

A simple, interactive Command Line Interface (CLI) Python application for calendar operations, holiday tracking, and age calculations.

## 🚀 Features

*   **Full Year Calendar:** Display the complete calendar for any given year.
*   **Specific Month View:** View a specific month of any year at a glance.
*   **Holiday Checker:** Check if a specific date matches pre-configured national or festive holidays.
*   **Birthday Tracker:** Look up registered birthdays by entering a specific date.
*   **Precise Age Calculator:** Calculate exact age in years, months, and days based on a Date of Birth (DOB).

## 🛠️ Prerequisites

This project requires Python 3 and the `python-dateutil` library to accurately compute exact age differences.

Install the required library using `pip`:

```bash
pip install python-dateutil
```

## 💻 How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the project directory:
   ```bash
   cd fizzy-calendar
   ```
3. Run the script:
   ```bash
   python fizzy_calendar.py
   ```

## 📝 Usage Example

Upon running the script, you will be presented with a menu system:

```text
---------------- Fizzy Calendar --------------

1. Calendar
2. Specific Month
3. Holiday
4. Birthday
5. Age in years, months and days
6. Exit

Please Enter Your Choice: 5
Enter your DOB (YYYY-MM-DD) : 2006-11-13
Age: 19 years, 8 months, and 3 days
```

## 🔧 Customization

You can manually update the predefined dates directly in the source code:
*   Update the `holi` dictionary in the `holiday()` function to add more annual holidays.
*   Update the `bir` dictionary in the `birthday()` function to save your friends' and family's birth dates.
