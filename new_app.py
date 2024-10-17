import json
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Define the scope for Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Define your credentials dictionary directly
credentials_dict = {
  "type": "service_account",
  "project_id": "chrome-sandbox-438912-p8",
  "private_key_id": "7535204225c15c7844e5be588091d5792fa7a98e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCd9XK+qieXZSlO\n5DbsgfDo3Q64/vIFuo+lCuDOh2ka5UAJwtLN0bGZ2V+BTAjVhV9pzaoAwLOfbYDQ\nC9Or5qFBueEg5dA/6uRhXrym4p1vnKCfJuUO6GooxVnj17NI0LYNV8YLZ7972fVK\n81pxHvD0JxmU1+xMDdtGkr7DnbFWUooEWjGc/0UpqMyO832ikAYqoxWdMGczDk+s\nKCIo6AezUb2/5mF5Ct90wSxrfF7GAbpBy6l7eGd4I3WuSl+/aLhih3PZaF1dBjVF\nYiKyWXeq6eRxww03WAg7q6grc6S3p7A7S0bq+CdsMoLS2Py1grbHn1e+xl10u1dY\n5TgVnHcrAgMBAAECggEAF6Jd21JenyPslNhyXAaAkyRe62YrX0O6nMauZqh9x5+X\n6n34iFbWRynuRMx+y+KV/qDeTW4yfL8SgCPXit0fW/63GnLYVcqhsOykYdH+yBrm\n246jGjfDM+Yncimth85sAZNprKjcI+izmiskPqW9sW0CQlzhBxYnAihlxk4bdnSh\n6nykElsvFyVpAvUczaxQ3VZmBX1rcx5MIXrCIdEtUqJaDvZFaWEXTTMokMHSU5vU\n+aTrqpRvHmTU3KhVYtzZCugn0uAXL6YU5svmL7Y6nqZrhulOaMyn5AGchhk6+xnB\nUvbXampuGmFUSrXSrSic2SvothuGniZbR3Ex9/tz2QKBgQDP8gcZ2sjAGn0D96WH\nCx9rNn3sEmiGHCYvqHI32iZ8YTo286tW9uINVcDfsgBws+4dWMtvAmFpB5W0TRCI\njhPDundDiTyc5Wp2aXCRKBnVnpWK48tbkhpWS22xoV5Axdass3nboolLwRvm4xYN\nTVYX1HYaL32U7dBZEXMJ9Lh92QKBgQDCdjrZ2/cRfQiCTlUeUZ5AkmlTpZKFzSO6\ntUZ5miYpM+l/2Ft9qpuRqO8IIX851+gCAoF2ahoRwA4PUETMzSdOTinMRUuWbKva\nKVWE7o2zj3NNu4dJXyjernPcJyLWdm3V6oGsny+b99KYnHtV6W5GdjYIFEr2Mkwj\nkcFyi7NGowKBgCBlUlnizdevyL4vfKg3QWPQj3mRvJr4E7LlCTZOVCSYeRtKhuz7\ndWgibfPrpUnpnjUQOlFHC6nzNo1qXCMKD2Y0zJPG85x12UotTw4uMygmlqGWr33K\nmzPKeIJt42Mv7yvkoh1niwA0S4aC5lKYM8tunB+kOmpTSlw17bglWgCxAoGBAJNm\nIr24KdKrv6Nl1Mcifp3bXNL2kdWx5P9FIKJT4dEhdEBfsxnSFBGYx3aWTWV+7nF3\njMJBMnl55i5dXYkPiFemj7AyZlUjEjBPXG9iky4j8fZdyvImm0gPW+roD1QYeLDJ\nDHnYP7ItawgatLIuOlRWjiYZm6h5/5SGiudUVROZAoGBAK4CcNECkM45zJIct/uG\ntGThk05H0HP5KJZu8RK3sPGMyTZoOI3UsLQ2fgrf+/qSGO3fONMuJIx+JzF4Mgjr\nxuDm25jN1444AzSgDu5Y5Tn4Hu3prCkyWNvuC4Z9rJXEGJCs3bxJTdMQA6OiOTrW\nq7uykJTDj4x101UEv0Gz++1I\n-----END PRIVATE KEY-----\n",
  "client_email": "python-account@chrome-sandbox-438912-p8.iam.gserviceaccount.com",
  "client_id": "108480939264380301011",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/python-account%40chrome-sandbox-438912-p8.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"

}

# Authenticate using the service account
creds = Credentials.from_service_account_info(credentials_dict, scopes=SCOPES)

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
