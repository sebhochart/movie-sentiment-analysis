import streamlit as st

st.set_page_config(page_title="Movie Sentiment Analysis - The Project",
                   page_icon="🎥",
                   layout="wide")


st.title('Movie Sentiment Analysis')
st.header('The Project')

col1, col2 = st.columns([2,10])

with col1:
    link_movie1 = 'https://cdn.shopify.com/s/files/1/1416/8662/products/titanic_1997_fr_original_film_art_a_1600x.jpg?v=1619289843'
    st.image(link_movie1)
    link_movie2 = 'https://i.pinimg.com/originals/ad/2d/45/ad2d4570c8a6f58c4e62fc0d2851b9ac.jpg'
    st.image(link_movie2)

with col2:
    # with st.expander('Context'):
    st.subheader('Context')
    st.markdown('''Kurt Vonnegut stated in 1995 that all stories follow 6 emotional arcs, but is true?
                Can we plot the sentiment of different movies and see one of Kurt's arcs?
                ''')
    st.markdown('''more explanation''')

    # with st.expander('Pre-processing: Movie Scripts'):
    st.subheader('Pre-processing: Movie Scripts')
    st.markdown('''explanation
                ''')

    # with st.expander('First model: Sentiment Analysis'):
    st.subheader('First model: Sentiment Analysis')
    st.markdown('''Use of the pre-trained model VADER for sentiment analysis.
                ''')

    # with st.expander('Second model: Classification'):
    st.subheader('Second model: Classification')
    st.markdown('''explanation
                ''')

    # with st.expander('Third model: Recommendation'):
    st.subheader('Third model: Recommendation')
    st.markdown('''explanation
                ''')
