import streamlit as st
from PIL import Image

st.set_page_config(page_title="Movie Sentiment Analysis - Home",
                   page_icon="🎥",
                   layout="wide")



with open('movie_sentiment/streamlit/style.css') as style_css:
    st.markdown(f'<style>{style_css.read()}</style>', unsafe_allow_html=True)


st.title('Movie Sentiment Analysis')

with st.container():
    st.header('About us')
    st.text('''
            As data science students at Le Wagon, we developed a project to analyze emotional arcs of movie scripts
            using NLP. We created models to visualize the arcs for almost 3000 movies, classified them into 6
            types of story shapes and created a recommendation algorithm to suggest movies having the same type of
            story.
            ''')
    st.text('''
            You can use this application to find out more about how we applied sentiment analysis to movie scripts.
            The Project tab explains the project and the steps we went through to solve these challenges.
            The Demo tab allows you to visualize the emotional arc for each movie and the recommended movies!
            ''')

st.header('Team')

col1, col2, col3 = st.columns(3, gap='medium')

#Alessandra
with col3:
    name_ac = 'Alessandra Campos'
    link_ac = 'https://media.licdn.com/dms/image/D4D03AQF396z-lPaSAw/profile-displayphoto-shrink_400_400/0/1686582266779?e=1692230400&v=beta&t=Asehb1oDPAR5i5zVaB9wNIdeFkIL3WACrbh6LZ5uJvk'
    linkedin_ac = 'https://www.linkedin.com/in/alessandra-medeiros-de-campos-1017b2b9/'
    github_ac = 'https://github.com/alemedeiroscampos'

    st.image(link_ac, caption=name_ac, width=120)
    col11, col12 = st.columns([1,3])
    col11.markdown(f"[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)]({linkedin_ac})")
    col12.markdown(f"[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)]({github_ac})")

#Hossein
with col2:
    name_hp = 'Hossein Poorhemati'
    link_hp = 'https://media.licdn.com/dms/image/C4D03AQG8I7RX6nsCCQ/profile-displayphoto-shrink_400_400/0/1574787780582?e=1692230400&v=beta&t=nX_hIE8yqtzq4hpPdOneh7NOtEz7SDsNLCFxa-1kDvs'
    linkedin_hp = 'https://www.linkedin.com/in/hossein-poorhemati/'
    github_hp = 'https://github.com/Hosseinpoorhemati'

    st.image(link_hp, caption=name_hp, width=120)
    col21, col22 = st.columns([1,3])
    col21.markdown(f"[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)]({linkedin_hp})")
    col22.markdown(f"[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)]({github_hp})")

#Sebastien
with col1:
    name_sh = 'Sebastien Hochart'
    link_sh = 'https://media.licdn.com/dms/image/C4D03AQHVpt_imrBHzg/profile-displayphoto-shrink_400_400/0/1585332487144?e=1692230400&v=beta&t=jiqv46vopBrhElVFaoJcCCW1s0jFL_p6Hih7lspngHI'
    linkedin_sh = 'https://www.linkedin.com/in/sebastien-hochart-84040b45/'
    github_sh = 'https://github.com/sebhochart'

    st.image(link_sh, caption=name_sh, width=120)
    col31, col32 = st.columns([1,3])
    col31.markdown(f"[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)]({linkedin_sh})")
    col32.markdown(f"[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)]({github_sh})")
