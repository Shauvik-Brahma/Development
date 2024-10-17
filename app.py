import streamlit as st

# Function to check login credentials
def check_credentials(username, password):
    correct_username = "2001"
    correct_password = "2001"
    return username == correct_username and password == correct_password

# Main app logic
def main():
    # Initialize session states
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "city_selected" not in st.session_state:
        st.session_state.city_selected = False
    
    # Determine which page to display
    if st.session_state.logged_in and not st.session_state.city_selected:
        display_city_selection_page()
    elif st.session_state.logged_in and st.session_state.city_selected:
        display_form_page()
    else:
        display_login_page()

def display_login_page():
    st.title("Login Page")
    
    # Input fields for login
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Login button logic
    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state.logged_in = True  # Update login state
            st.success("Login successful!")      # Show success message
        else:
            st.error("Invalid username or password. Please try again.")

def display_city_selection_page():
    st.title("Select Your City")
    
    # Dropdown selector for city selection
    city = st.selectbox("Choose your city:", ["Kolkata", "Hyderabad", "Delhi"])
    
    # Submit button for city selection
    if st.button("Submit"):
        st.session_state.city_selected = True  # Update city selection state
        st.session_state.selected_city = city  # Store selected city
        st.success(f"You have selected: {city}")  # Show selected city

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
        # Show submitted data after form submission
        st.success("Form submitted successfully!")
        st.write(f"Name: {name}")
        st.write(f"City: {city}")
        st.write(f"Age: {age}")

# Run the app
if __name__ == "__main__":
    main()
