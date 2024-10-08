import streamlit as st

# Define the CSS style
st.markdown(
    """
    <style>
    body {
        background-color: #FF5722; /* Dark orange color for the whole screen */
        color: white; /* Set default text color to white for better contrast */
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif; /* Optional: for consistent font across the page */
    }
  
    .hover-title:hover {
        color: #FF7043; /* Orange color for title on hover */
        transform: scale(1.2);
    }
    .skills-box {
        background-color: #FF5722; /* Pink color for boxes */
        padding: 20px;
        border-radius: 10px; /* Rounded corners for the boxes */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow for better visibility */
    }
    .skills-box h2 {
        color: white; /* White text for section titles inside the boxes */
    }
    .skills-box ul {
        list-style-type: disc; /* Bullet points for lists */
        padding-left: 20px; /* Indentation for the list */
    }
    .skills-box li {
        color: white; /* White text for list items */
    }
    .centered-message {
        text-align: center;
        margin: 40px 0; /* Adjust margin as needed */
        font-size: 20px;
        color: black;
        padding: 10px;
        border-radius: 10px; /* Rounded corners for the message box */
        transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effect */
    }
    .centered-message:hover {
        background-color: #FF5722; /* Dark orange background on hover */
        color: white; /* White text on hover */
    }
    .about-me-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["About Me", "Technical Skills", "Soft Skills", "Language", "Contact Me"])

# Title with hover effect
st.markdown('<h1 class="hover-title">Gelu Marie L. Ursal</h1>', unsafe_allow_html=True)

# About Me section
if selection == "About Me":
    st.write('''
    Hello! I'm Gelu Marie L. Ursal, a 4th-year BSIT student at Cebu Institute of Technology University. 
    I'm striving to establish a strong foundation in information technology, software and UI design, 
    web development, and software engineering.
    ''')

# Technical Skills section
elif selection == "Technical Skills":
    st.markdown('<div class="skills-box"><h2>Technical Skills</h2>', unsafe_allow_html=True)
    st.write(
        '''
        <ul>
            <li><strong>Programming Languages:</strong> Java, Python, C, HTML/CSS</li>
            <li><strong>Tools & Technologies:</strong> XAMPP, Spring Boot, React JS, MySQL Workbench, Figma, Postman, Jupyter Notebook, Virtual Box</li>
            <li><strong>Software:</strong> MS Office (Word, Excel, PowerPoint), Outlook</li>
        </ul>
        ''',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Soft Skills section
elif selection == "Soft Skills":
    st.markdown('<div class="skills-box"><h2>Soft Skills</h2>', unsafe_allow_html=True)
    st.write(
        '''
        <ul>
            <li>Problem-solving</li>
            <li>Excellent communication skills</li>
            <li>Team collaboration</li>
            <li>Ability to work under pressure</li>
        </ul>
        ''',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Language Skills section
elif selection == "Language":
    st.markdown('<div class="skills-box"><h2>Language</h2>', unsafe_allow_html=True)
    st.write(
        '''
        <ul>
            <li>Fluent in English</li>
            <li>Fluent in Tagalog</li>
        </ul>
        ''',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Me section
elif selection == "Contact Me":
    st.write('''
    - **Email:** gelumarie34@gmail.com
    - **Phone:** 09275085932
    - **Location:** 307 – U Tres de Abril Street, Punta Princesa, Cebu City
    ''')
    
  

st.markdown('<div class="centered-message">Thank you for visiting!😊</div>', unsafe_allow_html=True)
