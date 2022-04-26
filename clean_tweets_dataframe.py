import pandas as pd

class CleanTweets:
    """
    This class is responsible for cleaning the twitter dataframe

    Returns:
    --------
    A dataframe
    """
    def _init_(self, df:pd.DataFrame):
        self.df = df
        print('Automation cleaning done...!!!')
        
    def drop_unwanted_column(self)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = self.df[self.df['retweet_count'] == 'retweet_count' ].index
        self.df.drop(unwanted_rows , inplace=True)
        self.df = self.df[self.df['polarity'] != 'polarity']
        
        return self.df
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        
        self.df = self.df.drop_duplicates().drop_duplicates(subset='original_text')
        
        return df
    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        self.df['created_at'] = pd.to_datetime(self.df['created_at'], errors='errors')
        
        self.df = self.df[self.df['created_at'] >= '2020-12-31' ]
        
        return self.df
    
    def convert_to_numbers(self)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        self.df['polarity'] = pd.to_numeric(self.df['polarity'], errors='errors')
        self.df['retweet_count'] = pd.to_numeric(self.df['retweet_count'], errors='errors')
        self.df['favorite_count'] = pd.to_numeric(self.df['favorite_count'], errors='errors')
        
        return self.df
    
    def remove_non_english_tweets(self)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        
        self.df = self.df.query("lang == 'en' ")
        
        return self.df

if __name__== "__main__":
    tweet_df = pd.read_csv("processed_tweet_data.csv")
    cleaner = CleanTweets(tweet_df)