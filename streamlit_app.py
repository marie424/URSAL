import streamlit as st

# Add custom CSS for horizontal layout
st.markdown(
    """
    <style>
    .horizontal-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }
    .horizontal-item {
        flex: 1;
        min-width: 200px; /* Adjust as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add custom CSS for hover effect on title with background image
st.markdown(
    """
    <style>
    .hover-title {
        font-size: 40px;
        color: black;
        background-image: url('/workspaces/URSAL/background.jpg'); /* Path to your background image */
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        padding: 20px;
        transition: color 0.3s, transform 0.3s;
        text-align: center;
        display: inline-block;
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
st.write('''
Hello! I'm Gelu Marie L. Ursal, a 4th-year BSIT student at Cebu Institute of Technology University. 
I'm striving to establish a strong foundation in information technology, software and UI design, 
web development, and software engineering.
''')

# Horizontal layout for Additional Skills and Contact Information
st.markdown('<div class="horizontal-container">', unsafe_allow_html=True)

# Technical Skills
st.markdown('<div class="horizontal-item"><h2>Technical Skills</h2>', unsafe_allow_html=True)
st.write(
    '''
    - **Programming Languages:** Java, Python, C, HTML/CSS
    - **Tools & Technologies:** XAMPP, Spring Boot, React JS, MySQL Workbench, Figma, Postman, Jupyter Notebook, Virtual Box
    - **Software:** MS Office (Word, Excel, PowerPoint), Outlook
    '''
)
st.markdown('</div>', unsafe_allow_html=True)

# Soft Skills
st.markdown('<div class="horizontal-item"><h2>Soft Skills</h2>', unsafe_allow_html=True)
st.write(
    '''
    - Problem-solving
    - Excellent communication skills
    - Team collaboration
    - Ability to work under pressure
    '''
)
st.markdown('</div>', unsafe_allow_html=True)

# Language Skills
st.markdown('<div class="horizontal-item"><h2>Language</h2>', unsafe_allow_html=True)
st.write("Fluent in English and Tagalog")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

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
