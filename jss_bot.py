import streamlit as st


def app():
    gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 3em;
        }
        </style>
        <div class="gradient-text"> Welcome to JSS BOT</div>
        """

    st.markdown(gradient_text_html, unsafe_allow_html=True) 
    st.write("Hello Everyone, We the students  of JSS School have developed Keyword based chatbot on JSS") 
    

    st.write('')

    
    # Introduction
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        st.button('Mahavidyapeeta')
        st.write('')
        st.write('')
        st.write('')
        st.button('Suttur Math')
        st.write('')
        st.write('')
        st.write('')
        st.button('Rajendra mahaswamigalu')
        st.write('')
        st.write('')
        st.write('')
        st.button(' Deshikendra Mahaswamiji')

    with col2:
        st.button('School Education')
        st.write('')
        st.write('')
        st.write('')
        st.button('Technical Education')
        st.write('')
        st.write('')
        st.write('')
        st.button('Medical Education')
        st.write('')
        st.write('')
        st.write('')
        st.button('Entrepreneurship')

    with col3:
        st.button('Supportive Institutions')
        st.write('')
        st.write('')
        st.write('')
        st.button('JSS Mass Marriages')
        st.write('')
        st.write('')
        st.write('')
        st.button('JSS Hiriyara Mane ')
        st.write('')
        st.write('')
        st.write('')
        st.button('Vision and Mission' )
    
    
    with col4:
        st.button('Spiritual Mission')
        st.write('')
        st.write('')
        st.write('')
        st.button('Healthcare Services')
        st.write('')
        st.write('')
        st.write('')
        st.button('Social Services')
        st.write('')
        st.write('')
        st.write('')
        
        
    # Language selection
    

    

    def get_pedia_info(user_input, target_language='en'):
        pedia_info = {
            "mahavidyapeeta": """ JSS Mahavidyapeetha: Empowering Lives Through Education and Development  \n  \n   The journey of JSS Mahavidyapeetha (JSSMVP) began in 1928 with a small hostel for students in Mysore. Founded in 1954 by His Holiness Jagadguru Dr. Sri Shivarathri Rajendra Mahaswamiji, JSSMVP is committed to enhancing quality of life through education, health, and cultural development. With over 300 institutions serving 1,00,000+ students, JSSMVP offers education from primary to postgraduate levels across diverse disciplines, including technical, medical, and research fields. Its institutions span from rural villages to cities like Bengaluru, Noida, and internationally in the US, Mauritius, and Dubai. Beyond education, JSSMVP promotes rural development, healthcare, arts, and heritage restoration, fulfilling its mission to foster human development and uphold its legacy of transformative change.  """,

            "school education": """The JSS Mahavidyapeetha, an esteemed institution based in Mysuru, oversees a diverse array of educational programs aimed at fostering holistic development. Its initiatives span early childhood education through Balajagat and crèches, foundational learning in primary and high schools, and specialized institutions like Hindi Vidyalayas and Sahana Schools for children with special needs. The organization also manages pre-university colleges, degree and postgraduate institutes, and vocational training centers to ensure seamless progression in education.  \n  \n Innovative programs like Akshara Dasoha provide mid-day meals to support student retention and health, while unique initiatives like the JSS Halbhavi School of Art and the Karnataka Open School (JSSKOS) promote artistic expression and accessible education. With a focus on quality education and inclusivity, JSS Mahavidyapeetha actively bridges gaps in rural education, providing equal opportunities and fostering empowerment across communities​ """,

            "technical education" : """ The technical education initiatives under JSS Mahavidyapeetha encompass a diverse array of institutions and programs designed to impart practical and professional skills. This includes prominent engineering colleges like Sri Jayachamarajendra College of Engineering (SJCE) in Mysuru and JSS Academy of Technical Education campuses in Bengaluru, Noida, and Mauritius. Polytechnics under JSS provide diploma-level technical education across multiple disciplines, fostering a skilled workforce.\n \n  The Industrial Training Centres (ITCs) focus on equipping rural youth with employable skills through both short-term and long-term courses, covering areas like electrical wiring, motor repair, and pump maintenance. These centers align with the Modular Employable Skill (MES) scheme, ensuring industry-relevant training. Additionally, JSS supports initiatives in advanced technical education and entrepreneurship through its institutions like the JSSATE-STEP and advanced welding centers, further promoting innovation and self-reliance in technical professions​ """,

            "entrepreneurship": """ The JSS institutions in medical education provide a comprehensive ecosystem for academic excellence and healthcare service delivery. This includes specialized institutes like the JSS Ayurveda Medical College in Mysore, focusing on traditional medicine, and the JSS Institute of Nature Cure and Yogic Sciences, which emphasizes holistic health practices. Colleges such as the JSS College of Physiotherapy and JSS Institute of Speech and Hearing in Mysore and Dharwad offer modern training in rehabilitative and communication sciences. Nursing schools across Mysore, Kollegal, and Chamarajanagar, alongside the JSS College of Nursing, prepare skilled healthcare professionals. The JSS Medical and Dental Colleges are renowned for their contributions to medicine and dentistry, offering advanced education and cutting-edge research facilities. Together, these institutions uphold a commitment to quality education and affordable healthcare services while supporting innovative research initiatives """,

            "rajendra mahaswamigalu": """ Jagadguru Dr. Sri Shivarathri Rajendra Mahaswamiji, the 23rd pontiff of Srimath, was born on August 29, 1916, and became the head of the Srimath at the age of 12 in 1928. A scholar in Kannada and Sanskrit, he was deeply committed to social service, establishing numerous educational institutions, hostels, and hospitals under the JSS Mahavidyapeetha, founded in 1954. He pioneered initiatives for education (Jnana Dasoha), healthcare (Arogya Dasoha), and food and shelter (Anna Dasoha), addressing societal issues like inequality and poverty. His efforts extended to forming trusts and societies like the JSS Medical Service Trust and the Sri Shivarathreeshwara Rural Development Foundation. Despite early challenges, his unwavering dedication led to transformative contributions to society. He passed away on December 6, 1986, and his legacy is honored at his shrine in Suttur """,

            "deshikendra mahaswamiji": """ Jagadguru Sri Shivarathri Deshikendra Mahaswamiji, the 24th Peethadhipathi of the Sri Veerasimhasana Mahasamsthana Math at Suttur, assumed his responsibilities in 1986, succeeding his predecessor. He serves as the President of JSS Mahavidyapeetha and Chancellor of JSS Academy of Higher Education and Research and JSS Science and Technology University. Under his visionary leadership, JSSMVP has expanded its reach to over 300 institutions, two universities, 100,000 students, and 20,000 employees, making a significant impact across Karnataka, India, and globally in places like Mauritius, Dubai, and the USA.  \n  \n His contributions focus on addressing societal challenges in education, healthcare, and employment, with a commitment to uplifting communities from rural to urban settings. His efforts have modernized JSS institutions, aligning them with the expectations of the 21st century, making the Mahavidyapeetha one of the region's largest educational and employment hubs. His Holiness is widely lauded for his inclusive and transformative leadership.""",

            "suttur math": """Suttur Math, with a rich history spanning over a thousand years, stands as a prominent spiritual and educational center rooted in the Veerashaiva faith. Situated on the banks of the River Kapila in Karnataka, the Math has been a beacon of knowledge, wisdom, and human welfare, transcending regional boundaries to influence communities across India and globally. The Math emphasizes the core principles of tolerance and the sanctity of work, reflecting the reforms initiated by 12th-century saint Sri Basaveshwara.  \n  \n Guided by its pontiffs, Suttur Math has been instrumental in promoting spiritual growth, social justice, and economic upliftment. Its commitment to Veerashaivism focuses on universal brotherhood, human values, and ethics through its diverse spiritual, cultural, and educational initiatives. Today, Suttur Math continues as a vibrant movement fostering social and spiritual progress while spreading the ideals of compassion and equity worldwide.""",

            "medical education" : """The JSS Group of Institutions offers a wide range of programs in medical and allied health sciences through its esteemed colleges. These include the JSS Ayurveda Medical College, Mysore, focusing on traditional Indian medicine, and the JSS Institute of Nature Cure and Yogic Sciences, which integrates naturopathy and yoga for holistic healing. The JSS College of Physiotherapy trains students in rehabilitative therapies, while the JSS Institute of Speech and Hearing provides specialized education in audiology and speech therapy at its campuses in Mysuru and Dharwad. For nursing education, the JSS network encompasses multiple schools, such as those in Mysuru, Kollegal, and Chamarajanagar, as well as the JSS College of Nursing. Higher education institutions like the JSS Medical College and JSS Dental College emphasize excellence in medical and dental sciences, contributing significantly to healthcare education and research""",

            "supportive institutions" : """The Supportive Institutions of JSS Mahavidyapeetha focus on community welfare and skill development through various initiatives. The Jan Shikshan Sansthan enhances literacy and vocational skills for marginalized groups, while the JSS Krishi Vignana Kendra supports sustainable agriculture. RUDSETI provides free entrepreneurship training with accommodation, and the Advanced Welding Training Center delivers specialized skills in modern welding. The JSS Old Age Homes in Mysuru and Bengaluru offer care for the elderly, while JSSTICE is renowned for its IAS and KAS coaching. Additionally, initiatives like Karnataka Open School and vocational education empower non-traditional learners through flexible educational opportunities""",

            "jss mass marriages" : """Marital bliss for the poor Every year an annual mass marriage ceremony is organized as part of the Jatra Mahotsav at Suttur Srikeshetra. Around 250 couples tie the knot on the occasion. This apart, monthly mass marriages are also organized every month during which, on an average, at least 4 to 5 couples tie the knot. Besides a free Saree, Blouse, Dhoti, Shalya and Mangalya to the couple, free meal is also provided to the relatives of the couple. The mass marriage is open to people from all communities.""",

            "jss hiriyara mane" : """JSS Hiriyara Mane, established on August 11, 2000, in Mysore with the blessings of Jagadguru Sri Shivaratri Deshikendra Mahaswamiji, provides a haven for elderly individuals who lack family support. The two senior citizens' homes in Mysuru offer free lodging, boarding, and medical care. Inmates are engaged in activities like manufacturing chalk pieces and garlands, and they participate in mass prayers and enjoy a well-stocked library. On festivals, feasts and games are organized for their entertainment.  \n  \n At Suttur Srikshetra, JSS Hiriyara Mane also runs a free home for senior citizens with the capacity to house 50 people, along with a paid facility for 10 residents. The homes are equipped with modern amenities and maintained by dedicated staff""",

            "vision and mission" : """JSS Mahavidyapeetha (JSSMVP), headquartered in Mysuru, Karnataka, is a non-profit philanthropic organization dedicated to addressing key societal challenges in health, education, and economic mobility. Through its expansive network of institutions, JSSMVP impacts millions, both in India and abroad, by focusing on holistic human development.  \n  \n The organization's vision is to foster sustainable development by creating exceptional leaders who positively influence society. JSSMVP is committed to enhancing human values, encouraging scientific inquiry, and providing affordable, high-quality healthcare, all while promoting creativity, cultural empathy, and ethical wisdom across generations.""",

            "spiritual mission": """Founded in 1999 by His Holiness Jagadguru Sri Shivarathri Deshikendra Mahaswamiji, the JSS Spiritual Mission promotes India’s spiritual and cultural heritage worldwide through yoga, meditation, and publications. It operates under 501c3 status, focusing on universal values that transcend caste, creed, and race.  \n  \n Tracing its roots to the Suttur Jagadguru Sri Veerasimhasana Math, established in 1000 AD, the Mission aims to establish institutions for teaching human values, and conduct workshops and seminars for spiritual enrichment. It also revives traditional rituals and fosters collaborations with similar missions.""",

            "healthcare services": """JSS Mahavidyapeetha (JSSMVP) delivers comprehensive healthcare services and education across various domains, including allopathy, Ayurveda, physiotherapy, naturopathy, yogic science, speech and hearing, and nursing. Clinical training is facilitated through its 1,800-bed advanced JSS Hospital, located on MG Road, Mysore, offering state-of-the-art facilities. The new hospital, inaugurated in 2013 by the then President of India, Sri Pranab Mukherjee, serves as a cornerstone for medical education and patient care, reflecting JSSMVP’s dedication to holistic health and societal welfare""",

            "social services" : """ The Mysore Citizens’ Forum (MCF), led by Sri Shivarathri Deshikendra Swamiji, provides disaster relief and rehabilitation for victims of floods and tsunamis, including efforts in North Karnataka and North Kodagu. It also aims to create a consolidated relief fund for rapid aid. JSS Old Age Home in Mysore ensures senior citizens receive care in a compassionate environment. These efforts reflect the JSS community's broader commitment to social welfare and upliftment"""

        }

        user_input_lower = user_input.lower()

        if user_input_lower in pedia_info:
            return pedia_info[user_input_lower]
        else:
            return "I'm sorry, I'm not sure which term you're asking about. Can you please provide more details?"

    if "fest_messages" not in st.session_state:
        st.session_state.fest_messages = [{"role": "assistant", "content": "Discover Everything about JSS with our JSS BOT"}]

    for message in st.session_state.fest_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter the Term name"):
        st.session_state.fest_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = get_pedia_info(prompt)

        with st.spinner(text="Thinking..."):
            st.session_state.fest_messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.write(response, unsafe_allow_html=True)


if __name__ == "__main__":
    app()