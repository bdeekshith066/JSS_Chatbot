
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
st.set_page_config(layout="wide", page_title="JSS_BOT",
        page_icon="🏫",)

import intellibot, jss_bot



# Reducing whitespace on the top of the page
st.markdown("""
<style>

.block-container
{
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)



class MultiApp:
    def __init__(self):
        self.app = []

    def add_app(self, title, func):
        self.app.append({
            "title": title,
            "function": func
        })   

    def run(self):  # Need to include self as the first parameter
        with st.sidebar:
            st.markdown("""
          <style>
            .gradient-text {
              margin-top: -20px;
            }
          </style>
        """, unsafe_allow_html=True)
            
            typing_animation = """
            <h3 style="text-align: left;">
            <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=75&Left=true&vLeft=true&width=500&height=109&lines=JSS_BOT🏫" alt="Typing Animation" />
            </h3>
            """
            st.markdown(typing_animation, unsafe_allow_html=True)
            st.sidebar.write("")
            
            
            
            app = option_menu(
                menu_title='Sections',
                options=['JSS_Bot🤖','IntelliBOT🤖'],
                default_index=0,
            )
            
           
            st.sidebar.write("")
            st.sidebar.write("")
            

            components.html(
                    """
                <!DOCTYPE html>
                <html>
                <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                * {
                box-sizing: border-box;
                margin: 0; /* Remove default margin */
                padding: 0; /* Remove default padding */
                }
                body {
                font-family: Verdana, sans-serif;
                }
                .mySlides {
                display: none;
                }
                img {
                vertical-align: middle;
                width: 100%; /* Make images fill their containers */
                margin: 0; /* Remove any margin */
                padding: 0; /* Remove any padding */
                }
                /* Slideshow container */
                .slideshow-container {
                max-width: 300px;
                max-height : 300px;
                position: 100%;
                margin: 0;
                }

                /* Number text (1/3 etc) */
                .numbertext {
                color: #f2f2f2;
                font-size: 12px;
                padding: 8px 12px;
                position: absolute;
                top: 0;
                }
                /* Fading animation */
                .fade {
                animation-name: fade;
                animation-duration: 1.5s;
                }
                @keyframes fade {
                from {opacity: .4} 
                to {opacity: 1}
                }
                </style>
                </head>
                <body>
                <div class="slideshow-container">
                <div class="mySlides fade">
                    <div class="numbertext">1 / 3</div>
                    <img src="https://i.ytimg.com/vi/On8JXtf0GhM/maxresdefault.jpg">
                    
                </div>
                <div class="mySlides fade">
                    <div class="numbertext">2 / 3</div>
                    <img src="https://jssonline.org/wp-content/uploads/2020/07/jss-higher-school-jaynagar-01.jpg">
                    
                </div>
                <div class="mySlides fade">
                    <div class="numbertext">3 / 3</div>
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBnitNXupOa-VWZpQ-5rrEwAqOheFMl3-B0A&s">
                    
                </div>
                </div>
                <script>
                let slideIndex = 0;
                showSlides();

                function showSlides() {
                    let i;
                    let slides = document.getElementsByClassName("mySlides");
                    for (i = 0; i < slides.length; i++) {
                    slides[i].style.display = "none";  
                    }
                    slideIndex++;
                    if (slideIndex > slides.length) {slideIndex = 1}    
                    slides[slideIndex-1].style.display = "block";  
                    setTimeout(showSlides, 2000); // Change image every 2 seconds
                }
                </script>
                </body>
                </html>
                    """,
                    height=200, width=300
                )
            st.sidebar.write("")
            
            location_url = "https://maps.app.goo.gl/qgmQbdePJNeWyrWf7"
            location_link = f"[JSS School Banashankari 8th Block]({location_url})"
            st.sidebar.header(f"Developed  by Students of")
            st.sidebar.subheader(location_link)
            
        if app == "JSS_Bot🤖":
            jss_bot.app()
        elif app == "IntelliBOT🤖":
            intellibot.app() 

        
        
           

# Create an instance of the MultiApp class and run the app
MultiApp().run()