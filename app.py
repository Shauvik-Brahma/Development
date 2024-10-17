import streamlit as st

# Function to check login credentials
def check_credentials(username, password):
    correct_username = "2001"
    correct_password = "2001"
    return username == correct_username and password == correct_password

# Main app logic
def main():
    # State for login
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    # State for page navigation
    if "page" not in st.session_state:
        st.session_state.page = "login"

    # Login page
    if not st.session_state.logged_in and st.session_state.page == "login":
        st.title("Login Page")
        
        # Input fields for login
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        # Login button logic
        if st.button("Login"):
            if check_credentials(username, password):
                st.session_state.logged_in = True
                st.session_state.page = "form"
            else:
                st.error("Invalid username or password. Please try again.")

    # Form page after successful login
    if st.session_state.logged_in and st.session_state.page == "form":
        st.title("User Information Form")
        
        # Input form fields
        with st.form("user_form"):
            name = st.text_input("Enter your name:")
            city = st.text_input("Enter your city:")
            age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
            
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
