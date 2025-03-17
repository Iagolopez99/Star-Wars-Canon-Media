# Star Wars Media Tracker

A Streamlit-based web application for tracking and visualizing Star Wars canon media consumption. Users can create profiles, mark media as consumed, and view statistics on their progress.

## Features
- User authentication (login/logout)
- Interactive media table with filtering options
- Track consumed media for different users
- Progress statistics and visualizations

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd star_wars_tracker
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App
Start the Streamlit app with:
```bash
streamlit run main.py
```

## File Structure
```
star_wars_tracker/
│── data/
│   ├── media.csv                 # Star Wars media table (if using CSV)
│   ├── users.db                   # SQLite database for user profiles
│── app/
│   ├── auth.py                    # Handles user authentication
│   ├── database.py                 # Database interaction functions
│   ├── media.py                    # Media filtering and loading
│   ├── stats.py                    # User statistics functions
│── pages/
│   ├── home.py                     # Dashboard page
│   ├── profile.py                  # User profile and progress tracking
│   ├── media_list.py                # Full media list
│── main.py                          # Streamlit entry point
│── requirements.txt                  # Dependencies list
│── README.md                         # Documentation
```

## Future Improvements
- Add user authentication with OAuth
- Implement a leaderboard for user rankings
- Enhance UI with better styling

## License
[Your preferred license]
