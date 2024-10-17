import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Define the scope for Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Path to the service account credentials JSON file
SERVICE_ACCOUNT_FILE = 'C:/Users/Shauvik Brahma/Credentials.json'  # Replace with the correct path

# Authenticate using the service account
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Initialize the Google Sheets API client
client = gspread.authorize(creds)

# Open the Google Sheet by ID
spread_sheet_id = '17aKq7oJ6umnInjTYFuTGB-kHTqDGtT53dIoGT5d-Riw'  # Replace with your spreadsheet ID
sheet = client.open_by_key(spread_sheet_id).sheet1  # Open the first sheet

# Function to check login credentials
def check_credentials(username, password):
    correct_username = "2001"
    correct_password = "2001"
    return username == correct_username and password == correct_password

# Main app logic
def main():
    # Initialize session states
    if "page" not in st.session_state:
        st.session_state.page = "login"  # Start on the login page

    # Display the appropriate page based on session state
    if st.session_state.page == "login":
        display_login_page()
    elif st.session_state.page == "city_selection":
        display_city_selection_page()
    elif st.session_state.page == "form":
        display_form_page()

def display_login_page():
    st.title("Login Page")
    
    # Input fields for login
    username = st.text_input("Username", "")
    password = st.text_input("Password", type="password", value="")
    
    # Login button logic
    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state.page = "city_selection"  # Navigate to city selection
            st.success("Login successful!")  # Show success message
        else:
            st.error("Invalid username or password. Please try again.")

    # Prompt to click the login button twice
    st.warning("Click the Login Button twice.")

def display_city_selection_page():
    st.title("Select Your City")
    
    # Dropdown selector for city selection
    city = st.selectbox("Choose your city:", ["Kolkata", "Hyderabad", "Delhi"])
    
    # Submit button for city selection
    if st.button("Submit"):
        st.session_state.selected_city = city  # Store selected city
        st.session_state.page = "form"  # Navigate to the form page

    # Prompt to click the submit button twice
    st.warning("Click the Submit Button twice.")

def display_form_page():
    st.title("User Information Form")
    
    # Input form fields
    with st.form("user_form"):
        name = st.text_input("Enter your name:")
        city = st.session_state.selected_city  # Show selected city from previous page
        age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
        
        # Display selected city
        st.write(f"Selected City: {city}")
        
        # Submit button
        submitted = st.form_submit_button("Submit")
    
    if submitted:
        # Append data to Google Sheets
        sheet.append_row([name, age, city])
        
        # Show success message
        st.success("Form submitted successfully!")
        st.write(f"Name: {name}")
        st.write(f"City: {city}")
        st.write(f"Age: {age}")

# Run the app
if __name__ == "__main__":
    main()
