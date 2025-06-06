
# Challenge - Openspace Classifier

This project helps organize colleagues randomly into tables with limited seats.

## Structure

- `main.py`: Main script to run the organizer
- `colleagues.csv`: List of names (one per line)
- `utils/`:
  - `table.py`: Defines the Seat and Table classes
  - `openspace.py`: Logic to organize colleagues into seats
  - `file_utils.py`: Reserved for file utilities (optional)

## How to Run

1. Make sure you have Python installed.
2. Install pandas and openpyxl:
   ```bash
   pip install pandas openpyxl
