import pandas
import datetime


class PandasConverter(object):

    def convert_data(self, data):
        """
        Convert data to pandas DataFrame
        Args:
            data (dict): dict

        Returns:
            pandas.DataFrame

        """
        return pandas.DataFrame(
            {data['ticker']: data['data']['values']},
            index=map(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'), data['data']['dates']),
            dtype=float
        )

    def convert_results(self, results):
        """
        Convert results to pandas DataFrame
        Args:
            results (dict): results from api response

        Returns:
            pandas.DataFrame: pandas.DataFrame data
        """
        dataframe = pandas.DataFrame()
        while 1:
            try:
                data = next(results)
                dataframe = pandas.concat([dataframe, self.convert_data(data)], axis=1)
            except:
                break
        return dataframe
