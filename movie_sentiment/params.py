# processed data
DICT_PICKLE_FILE = './movie_sentiment/processed_data/arcs_dict.pickle'
MIN_LENGHT_ARCS = 30
DICT_PICKLE_FILE_DYN_AVG = './movie_sentiment/processed_data/arcs_dict_dyn_avg.pickle'

# classified arcs
CLASSIFIED_ARCS_PICKLE_FILE = './movie_sentiment/processed_data/classified_movies_arcs.pickle'
CENTROID_ARCS_PICKLE_FILE = './movie_sentiment/processed_data/centroid_arcs.pickle'
ARCS_SHAPES = {
    0: '~ Rags to riches',
    1: 'Riches to rags',
    2: 'Icarus',
    3: 'Oedipus',
    4: 'Cinderella',
    5: 'Man in a hole'
}

# recommendation cache
RECO_META_PICKLE_FILE = './movie_sentiment/processed_data/reco_meta_preprocessed.pickle'

# raw data
RAW_SCRIPTS_PATH = './raw_data/screenplay_data/data/raw_texts/raw_texts/'
METADATA_PATH = './raw_data/movie_metadata/movie_meta_data.csv'
