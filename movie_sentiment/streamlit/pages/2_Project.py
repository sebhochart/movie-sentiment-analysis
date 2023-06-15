import streamlit as st
from PIL import Image

st.set_page_config(page_title="CinemArcs - The Project",
                   page_icon="🎥",
                   layout="centered")

with open('movie_sentiment/streamlit/pages/2_style.css') as style_css:
    st.markdown(f'<style>{style_css.read()}</style>', unsafe_allow_html=True)

st.title('CinemArcs')
st.header('The Project')


st.subheader('Context')
st.markdown('''In his master’s thesis in anthropology, Kurt Vonnegut had the idea to plot story shapes in an axe
            of good fortune and bad fortune. He said that most stories follow the same type of arc and that
            there’s no reason why the simple shapes of stories can’t be fed into computers.
            ''')

st.markdown('''In 2016, a group of researchers from the University of Vermont and the University of Adelaide decided
            to put his theory to the test. They analyzed the shape of over two-thousand of books and found
            the six main shapes of stories:  \n - Rags to Riches (rise)  \n - Riches to Rags (fall)  \n - Man in a Hole (fall then rise)  \n - Icarus (rise then fall)  \n - Cinderella (rise then fall then rise)  \n - Oedipus (fall then rise then fall)
            ''')

image = Image.open('movie_sentiment/streamlit/img/emotional-arcs-1600x821.jpg')
st.image(image)

st.markdown('''Let's see if we can verify the same for movies!''')


# with st.expander('Plotting movies emotional arcs'):
st.subheader('Plotting movies emotional arcs')
st.markdown('''First we tried to plot the emotional arcs of movies using their script and sentiment analysis.
            ''')
st.markdown('''We started from the movie scripts dataset from Kaggle and splitted the movie scripts into sentences.
            We created segments of 50 sentences and we used a VADER model to analyze the sentiment of each segment.
            ''')

image = Image.open('movie_sentiment/streamlit/img/up_arc_raw.png')
st.image(image, caption="Raw visualization of sentiment trends for the movie 'Up'")

st.markdown('''The plot was showing a lot of noise so we applied moving average to smooth out the result and show the overall trend.
            ''')

image = Image.open('movie_sentiment/streamlit/img/up_arc_final.png')
st.image(image,  caption="Processed sentiment arc for the movie 'Up'")


# with st.expander('Second model: Classification'):
st.subheader('Classifying movie arcs')
st.markdown('''We generated a simplified version of the emotional arcs for all the movies database and
            made sure we have a consistent 30 data points per movie to start the classification of the arcs.
            ''')
st.markdown('''Then we standardized each movie arc and applied a PCA before we apply a Kmeans clustering algorithm
            to our dataset. After we tried several standardization and normalization techniques, as well as different
            numbers of centroids we found 6 main clusters for the movie arcs.
            ''')
st.markdown('''The 6 centroid shapes are close to the 6 types of curves we hoped to find: Cinderella, Riches to rags,
            Oedipus, Icarus, Man in a hole and Rags to riches.
            ''')

image = Image.open('movie_sentiment/streamlit/img/arcs_clusters.png')
st.image(image, caption='6 emotional arcs from Kmeans classification')


st.markdown('''We can see that the classified movies arcs mostly follow the same shape of arcs but that there is
            some outliers that were probably hard to classify. We computed a score of similarity between each
            movie arc and their classification using cosine similarity and decided that for every movie
            that has a score above 0.5 the classification was relevant enought.
            ''')
st.markdown('''In the end we were able to classify ~ 85% of the movies into these 6 types of stories!
            ''')

# with st.expander('Third model: Recommendation'):
st.subheader('Recommending movies that have the same type of story')
st.markdown('''Our last goal was to recommend movies that have the same type of emotional arc.
            We used cosine similarity to compute a similarity score between a movie and all our movies database.
            The algorithm returned movies with similar shapes but the themes of recommended movies could
            be very different.
            ''')

image = Image.open('movie_sentiment/streamlit/img/recommendation-1.png')
st.image(image, caption="Movies having their arc closest to the movie 'Up', with their similarity score.")

st.markdown('''We tried to add movie metadata to the algorithm. We also had tabular data from IMDB in the
            dataset and decided to go with genres and keywords. These features were vectorized with
            CountVectorizer and we got 25k features. We applied TruncatedSVD dimensionality reduction
            and kept the most significant 200 features that explained 80% of the variance.
            ''')
st.markdown('''We computed the cosine imilarity between the arcs and our preprocessed metadata. We kept
            the most similar movies using the average of both scores. The movie arcs were still similar
            but the recommendation was better.
            ''')

image = Image.open('movie_sentiment/streamlit/img/recommendation-2.png')
st.image(image, caption="Closest movies from 'Up' balanced with metadata. Score is similarity between arcs.")
