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
        return pandas.DataFrame({data['ticker']: data['values']},
                         index=map(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'), data['dates']),
                         dtype=float)
