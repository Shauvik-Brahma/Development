import streamlit as st

# Function to check login credentials
@st.experimental_singleton
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
    if "selected_city" not in st.session_state:
        st.session_state.selected_city = ""

    # Determine which page to display
    if st.session_state.logged_in and not st.session_state.city_selected:
        display_city_selection_page()
    elif st.session_state.logged_in and st.session_state.city_selected:
        display_form_page()
    else:
        display_login_page()

def display_login_page():
    st.title("Login Page")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            if check_credentials(username, password):
                st.session_state.logged_in = True
                st.success("Login successful!")
            else:
                st.error("Invalid username or password. Please try again.")

def display_city_selection_page():
    st.title("Select Your City")
    with st.form("city_form"):
        city = st.selectbox("Choose your city:", ["Kolkata", "Hyderabad", "Delhi"])
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.city_selected = True
            st.session_state.selected_city = city
            st.success(f"You have selected: {city}")

def display_form_page():
    st.title("User Information Form")
    with st.form("user_form"):
        name = st.text_input("Enter your name:")
        age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
        st.write(f"Selected City: {st.session_state.selected_city}")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Form submitted successfully!")
            st.write(f"Name: {name}")
            st.write(f"City: {st.session_state.selected_city}")
            st.write(f"Age: {age}")

# Run the app
if __name__ == "__main__":
    main()
