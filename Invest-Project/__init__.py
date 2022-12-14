from start_decorator import start_decorator, download
from abc import ABC, abstractmethod


@start_decorator
def project():
    class StockOperations(ABC):

        @abstractmethod
        def buy_stocks(self, amount: int):
            pass

        @abstractmethod
        def sell_stocks(self, amount: int):
            pass

        @abstractmethod
        def get_total_stocks(self):
            pass

    class GoogleStocks(StockOperations):
        price_for_one_stock = 550

        def __init__(self, amount_of_google_stocks: int = 0):
            self.amount_of_google_stocks = amount_of_google_stocks

        def buy_stocks(self, amount: int):
            self.amount_of_google_stocks = self.amount_of_google_stocks + amount
            return f'You successfully bought {amount} google stocks. \nYour current amount of GoogleStocks =' \
                   f' {self.amount_of_google_stocks}'

        def sell_stocks(self, amount: int):
            self.amount_of_google_stocks = self.amount_of_google_stocks - amount
            return f'You successfully sold {amount} google stocks. \nYour current amount of' \
                   f' GoogleStocks = {self.amount_of_google_stocks}'

        def get_total_stocks(self):
            if investor.currency == 'dollar':
                return f'All your Google stocks are valued ' \
                       f'at: {self.amount_of_google_stocks * GoogleStocks.price_for_one_stock} ' \
                       f'dollars.'
            elif investor.currency == 'euro':
                return f'All your Google stocks are valued ' \
                       f'at: {self.amount_of_google_stocks * GoogleStocks.price_for_one_stock} ' \
                       f'euros.'

    class FacebookStocks(StockOperations):
        facebook_price_for_one_stock = 400

        def __init__(self, amount_of_facebook_stocks: int = 0):
            self.amount_of_facebook_stocks = amount_of_facebook_stocks

        def buy_stocks(self, amount: int):
            self.amount_of_facebook_stocks = self.amount_of_facebook_stocks + amount
            return f'You successfully bought {amount} facebook stocks. \nYour current amount of Facebook Stocks = ' \
                   f'{self.amount_of_facebook_stocks}'

        def sell_stocks(self, amount: int):
            self.amount_of_facebook_stocks = self.amount_of_facebook_stocks - amount
            return f'You successfully sold {amount} facebook stocks. \nYour current amount of FacebookStocks =' \
                   f' {self.amount_of_facebook_stocks}'

        def get_total_stocks(self):
            if investor.currency == 'dollar':
                return f'All your Facebook stocks are valued ' \
                       f'at: {self.amount_of_facebook_stocks * FacebookStocks.facebook_price_for_one_stock} ' \
                       f'dollars.'
            elif investor.currency == 'euro':
                return f'All your Facebook stocks are valued ' \
                       f'at: {self.amount_of_facebook_stocks * FacebookStocks.facebook_price_for_one_stock} ' \
                       f'euros.'

    class NetflixStocks(StockOperations):
        netflix_price_for_one_stock = 330

        def __init__(self, amount_of_netflix_stocks: int = 0):
            self.amount_of_netflix_stocks = amount_of_netflix_stocks

        def buy_stocks(self, amount: int):
            self.amount_of_netflix_stocks = self.amount_of_netflix_stocks + amount
            return f'You successfully bought {amount} netflix stocks. \nYour current amount of NetflixStocks =' \
                   f' {self.amount_of_netflix_stocks}'

        def sell_stocks(self, amount: int):
            self.amount_of_netflix_stocks = self.amount_of_netflix_stocks - amount
            return f'You successfully sold {amount} netflix stocks. \nYour current amount of NetflixStocks =' \
                   f' {self.amount_of_netflix_stocks}'

        def get_total_stocks(self):
            if investor.currency == 'dollar':
                return f'All your Netflix stocks are valued ' \
                       f'at: {self.amount_of_netflix_stocks * NetflixStocks.netflix_price_for_one_stock} ' \
                       f'dollars.'
            elif investor.currency == 'euro':
                return f'All your Netlifx stocks are valued ' \
                       f'at: {self.amount_of_netflix_stocks * NetflixStocks.netflix_price_for_one_stock} ' \
                       f'euros.'

    class TeslaStocks(StockOperations):
        tesla_price_for_one_stock = 270

        def __init__(self, amount_of_tesla_stocks: int = 0):
            self.amount_of_tesla_stocks = amount_of_tesla_stocks

        def buy_stocks(self, amount: int):
            self.amount_of_tesla_stocks = self.amount_of_tesla_stocks + amount
            return f'You successfully bought {amount} tesla stocks. \nYour current amount of Tesla Stocks =' \
                   f' {self.amount_of_tesla_stocks}'

        def sell_stocks(self, amount: int):
            self.amount_of_tesla_stocks = self.amount_of_tesla_stocks - amount
            return f'You successfully sold {amount} tesla stocks. \nYour current amount of Tesla Stock =' \
                   f' {self.amount_of_tesla_stocks}'

        def get_total_stocks(self):
            if investor.currency == 'dollar':
                return f'You own Tesla stocks worth:' \
                       f' {self.amount_of_tesla_stocks * TeslaStocks.tesla_price_for_one_stock} dollars.'
            elif investor.currency == 'euro':
                return f'You own Tesla stocks worth:' \
                       f' {self.amount_of_tesla_stocks * TeslaStocks.tesla_price_for_one_stock} euros.'

    class Investors(TeslaStocks, NetflixStocks, FacebookStocks, GoogleStocks):
        currency = 'dollar'

        def __init__(self, nickname, amount_of_tesla_stocks, amount_of_netflix_stocks, amount_of_facebook_stocks,
                     amount_of_google_stocks, balance):
            TeslaStocks.__init__(self, amount_of_tesla_stocks)
            NetflixStocks.__init__(self, amount_of_netflix_stocks)
            FacebookStocks.__init__(self, amount_of_facebook_stocks)
            GoogleStocks.__init__(self, amount_of_google_stocks)
            self.__nickname = nickname
            self.__balance = balance

        def get_balance(self):
            return self.__balance

        def set_balance(self, new_balance):
            self.__balance = new_balance

        account_balance = property(fget=get_balance, fset=set_balance, doc="Methods to make get/set operations"
                                                                           " with investor's balance")

        @property
        def nickname(self):
            """this is method with property to make operations with user's nickname.
            This method returns only nickname value."""
            return self.__nickname

        @nickname.setter
        def nickname(self, new_nickname):
            self.__nickname = new_nickname

        @staticmethod
        def get_full_balance():
            return f'You have: {investor.amount_of_google_stocks} Google stocks.\n' \
                   f'You have: {investor.amount_of_tesla_stocks} Tesla stocks.\n' \
                   f'You have: {investor.amount_of_facebook_stocks} Facebook stocks.\n' \
                   f'You have: {investor.amount_of_netflix_stocks} Netflix stocks.'

        @classmethod
        def change_currency(cls, new_currency):
            if cls.currency == 'dollar' and new_currency == 'euro':
                cls.currency = 'euro'
                old_value = cls.price_for_one_stock
                cls.price_for_one_stock = cls.price_for_one_stock * 1.05
                return f'your {old_value} dollars for 1 stock was changed on {cls.price_for_one_stock}' \
                       f' euro for 1 stock'

            elif cls.currency == 'euro' and new_currency == 'dollar':
                cls.currency = 'dollar'
                old_value = cls.price_for_one_stock
                cls.price_for_one_stock = cls.price_for_one_stock / 1.05
                return f'your {old_value} euro for 1 stock was changed on {cls.price_for_one_stock}' \
                       f' dollar for 1 stock'

    nickname = str(input('Please, enter your nickname: '))
    investor = Investors(nickname, 0, 0, 0, 0, 500)
    start = str
    while start != '7':
        start = str(input(f'What do you want {investor.nickname}?\nI want to check my actives - enter 1'
                          '\nI want to buy new stock - enter 2\nI want to sell stock - enter 3\n'
                          'Change currency - enter 4\n'
                          'Change my nickname - enter - 5\n'
                          'Check my account balance - enter 6\n'
                          'End program - enter 7\n'))
        if start == '1':
            download()
            check_what = str
            while check_what != '6':
                check_what = str(input('What do you need to check?\n'
                                       'My Google stocks - press 1\n'
                                       'My Netflix stocks - press 2\n'
                                       'My Facebook stocks - press 3\n'
                                       'My Tesla stocks - press 4\n'
                                       'I want to check all my stocks in all companies - press 5\n'
                                       'Quit - press 6\n'))

                if check_what == '1':
                    download()
                    print(f'Price for 1 google stock now - '
                          f'{GoogleStocks.price_for_one_stock} {investor.currency}')
                    print(GoogleStocks.get_total_stocks(investor))
                    print('You have -', investor.amount_of_google_stocks, 'stocks.')

                elif check_what == '2':
                    download()
                    print(f'Price for 1 netflix stock now - '
                          f'{NetflixStocks.netflix_price_for_one_stock} {investor.currency}')
                    print(NetflixStocks.get_total_stocks(investor))
                    print('You have -', investor.amount_of_netflix_stocks, 'stocks.')
                elif check_what == '3':
                    download()
                    print(f'Price for 1 facebook stock now - '
                          f'{FacebookStocks.facebook_price_for_one_stock} {investor.currency}')
                    print(FacebookStocks.get_total_stocks(investor))
                    print('You have -', investor.amount_of_facebook_stocks, 'stocks.')
                elif check_what == '4':
                    download()
                    print(f'Price for 1 tesla stock now - '
                          f'{TeslaStocks.tesla_price_for_one_stock} {investor.currency}')
                    print(TeslaStocks.get_total_stocks(investor))
                    print('You have -', investor.amount_of_tesla_stocks, 'stocks.')
                elif check_what == '5':
                    download()
                    print(investor.get_full_balance())

                elif check_what == '6':
                    download()

                else:
                    download()
                    print('-' * 10, 'Ops. Seems that you entered incorrect value. Please, choose digit 1,2,3,4 or 5.',
                          '-' * 10)

        elif start == '2':
            download()
            buy_what = str
            while buy_what != '5':
                buy_what = str(input('What do you want to buy?\n'
                                     'Google stocks - press 1\n'
                                     'Netflix stocks - press 2\n'
                                     'Facebook stocks - press 3\n'
                                     'Tesla stocks - press 4\n'
                                     'Quit - press 5\n'))

                if buy_what == '1':
                    download()
                    how_much = int(input('How much stocks do you want ?'))
                    download()
                    GoogleStocks.buy_stocks(investor, how_much)
                    print('Thank you! Your purchase was successfully.')
                    print('Now you have:', investor.amount_of_google_stocks, 'google stocks.')
                    print(GoogleStocks.get_total_stocks(investor))
                elif buy_what == '2':
                    download()
                    how_much = int(input('How much stocks do you want ?'))
                    download()
                    NetflixStocks.buy_stocks(investor, how_much)
                    print('Thank you! Your purchase was successfully.')
                    print('Now you have:', investor.amount_of_netflix_stocks, 'netflix stocks.')
                    print(NetflixStocks.get_total_stocks(investor))
                if buy_what == '3':
                    download()
                    how_much = int(input('How much stock do you want ?'))
                    download()
                    FacebookStocks.buy_stocks(investor, how_much)
                    print('Thank you! Your purchase was successfully.')
                    print('Now you have:', investor.amount_of_facebook_stocks, 'facebook stocks.')
                    print(FacebookStocks.get_total_stocks(investor))
                if buy_what == '4':
                    download()
                    how_much = int(input('How much stocks do you want ?'))
                    download()
                    TeslaStocks.buy_stocks(investor, how_much)
                    print('Thank you! Your purchase was successfully.')
                    print('Now you have:', investor.amount_of_tesla_stocks, 'tesla stocks.')
                    print(TeslaStocks.get_total_stocks(investor))
        elif start == '3':
            download()
            sell_what = str
            while sell_what != '5':
                sell_what = str(input('What do you want to sell?\n'
                                      'Google stocks - press 1\n'
                                      'Netflix stocks - press 2\n'
                                      'Facebook stocks - press 3\n'
                                      'Tesla stocks - press 4\n'
                                      'Quit - press 5\n'))

                if sell_what == '1':
                    download()
                    how_much = int(input('How much stock do you want to sell?'))
                    GoogleStocks.sell_stocks(investor, how_much)
                    print('Thank you! Your sale was successfully.')
                    print('Now you have:', investor.amount_of_google_stocks, 'google stocks.')
                    print(GoogleStocks.get_total_stocks(investor))
                elif sell_what == '2':
                    download()
                    how_much = int(input('How much stock do you want to sell?'))
                    NetflixStocks.sell_stocks(investor, how_much)
                    print('Thank you! Your sale was successfully.')
                    print('Now you have:', investor.amount_of_netflix_stocks, 'netflix stocks.')
                    print(NetflixStocks.get_total_stocks(investor))
                elif sell_what == '3':
                    download()
                    how_much = int(input('How much stock do you want to sell?'))
                    FacebookStocks.sell_stocks(investor, how_much)
                    print('Thank you! Your sale was successfully.')
                    print('Now you have:', investor.amount_of_facebook_stocks, 'facebook stocks.')
                    print(FacebookStocks.get_total_stocks(investor))
                elif sell_what == '4':
                    download()
                    how_much = int(input('How much stock do you want to sell?'))
                    TeslaStocks.sell_stocks(investor, how_much)
                    print('Thank you! Your sale was successfully.')
                    print('Now you have:', investor.amount_of_tesla_stocks, 'tesla stocks.')
                    print(TeslaStocks.get_total_stocks(investor))

        elif start == '4':
            download()
            old_currency = investor.currency
            new_currency = str(input('What currency do you prefer?\n'
                                     'Euro or Dollar?\n'
                                     'Dollar - enter 1\n'
                                     'Euro - enter 2\n'
                                     'Quit - enter 3\n'))
            if new_currency == '1':
                if investor.currency == 'dollar':
                    download()
                    print('The Dollar currency was already chosen.')
                else:
                    download()
                    investor.currency = 'dollar'
                    print(f'Congratulations! Your {old_currency} currency was changed on {investor.currency} currency!')
                    GoogleStocks.price_for_one_stock = GoogleStocks.price_for_one_stock * 1.05
                    TeslaStocks.tesla_price_for_one_stock = TeslaStocks.tesla_price_for_one_stock * 1.05
                    FacebookStocks.facebook_price_for_one_stock = FacebookStocks.facebook_price_for_one_stock * 1.05
                    NetflixStocks.netflix_price_for_one_stock = NetflixStocks.netflix_price_for_one_stock * 1.05

            elif new_currency == '2':
                if investor.currency == 'euro':
                    print('The Euro currency was already chosen.')
                else:
                    investor.currency = 'euro'
                    print(f'Congratulations! Your {old_currency} currency was changed on {investor.currency} currency!')
                    GoogleStocks.price_for_one_stock = GoogleStocks.price_for_one_stock / 1.05
                    TeslaStocks.tesla_price_for_one_stock = TeslaStocks.tesla_price_for_one_stock / 1.05
                    FacebookStocks.facebook_price_for_one_stock = FacebookStocks.facebook_price_for_one_stock / 1.05
                    NetflixStocks.netflix_price_for_one_stock = NetflixStocks.netflix_price_for_one_stock / 1.05

            elif new_currency == '3':
                download()
            else:
                download()
                print('Something wrong. Please, try again.')

        elif start == '5':
            download()
            old_nickname = nickname
            new_nickname = str(input('What new nickname do you want? Please, enter: '))
            investor.nickname = new_nickname
            print(f'Congratulations! Your {old_nickname} nickname was changed on {new_nickname} nickname.')
        elif start == '6':
            download()
            print(investor.account_balance, ' ', investor.currency, 's', sep='')
        elif start == '7':
            download()
            print('Bye-Bye!')
        else:
            download()
            print('-' * 10, 'Ops. Seems that you entered incorrect value. Please, choose digit 1,2,3,4 or 5.', '-' * 10)
