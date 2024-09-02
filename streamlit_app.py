import streamlit as st

# Add custom CSS for hover effect on title
st.markdown(
    """
    <style>
    .hover-title {
        font-size: 40px;
        color: black;
        transition: color 0.3s, transform 0.3s;
    }
    .hover-title:hover {
        color: orange;
        transform: scale(1.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with hover effect
st.markdown('<h1 class="hover-title">Gelu Marie L. Ursal</h1>', unsafe_allow_html=True)

# Autobiography section
st.header("Autobiography")
st.write('''
Hello! I'm Gelu Marie L. Ursal, a 4th-year BSIT student at Cebu Institute of Technology University. 
I'm striving to establish a strong foundation in information technology, software and UI design, 
web development, and software engineering.
''')

# Additional Skills section
st.header("Additional Skills")

# Technical Skills
st.subheader("Technical Skills")
st.write(
    '''
    - **Programming Languages:** Java, Python, C, HTML/CSS
    - **Tools & Technologies:** XAMPP, Spring Boot, React JS, MySQL Workbench, Figma, Postman, Jupyter Notebook, Virtual Box
    - **Software:** MS Office (Word, Excel, PowerPoint), Outlook
    '''
)

# Soft Skills
st.subheader("Soft Skills")
st.write(
    '''
    - Problem-solving
    - Excellent communication skills
    - Team collaboration
    - Ability to work under pressure
    '''
)

# Language Skills
st.subheader("Language")
st.write("Fluent in English and Tagalog")

# Display contact information
st.header("Contact Information")
st.write(
    '''
    - **Email:** gelumarie34@gmail.com
    - **Phone:** 09275085932
    - **Location:** 307 – U Tres de Abril Street, Punta Princesa, Cebu City
    '''
)

st.write("Thank you for visiting my portfolio!")
