import requests
from bs4 import BeautifulSoup

class NaverSearch:
    def __init__(self, keyword, advertiser):
        self.keyword = keyword
        self.advertiser = advertiser

    def __str__(self):
        return '광고주: {}, 키워드: {}'.format(self.advertiser, self.keyword)
    
    def currentPCTotalPowerLink(self):
        ENDPOINT = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + self.keyword
        page = requests.get(ENDPOINT)
        soup = BeautifulSoup(page.text, 'html.parser')
        power_link_body = soup.find('div', {'id': 'power_link_body'})
        AS = power_link_body.find_all('a', {'class': 'lnk_url'})
        return len(AS)

    def currentPCRank(self):
        ENDPOINT = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + self.keyword
        page = requests.get(ENDPOINT)
        soup = BeautifulSoup(page.text, 'html.parser')
        power_link_body = soup.find('div', {'id': 'power_link_body'})

        # ul = power_link_body.find('ul', {'class': 'lst_type'})
        AS = power_link_body.find_all('a', {'class': 'lnk_url'})
        rank = 0
        for index, a in enumerate(AS):
            if(self.advertiser in a.get_text()):
                return index + 1
        return -1

    def currentMOTotalPowerLink(self):
        ENDPOINT = 'https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query=' + self.keyword
        page = requests.get(ENDPOINT)
        soup = BeautifulSoup(page.text, 'html.parser')
        power_link_body = soup.find('ul', {'id': 'power_link_body'})
        AS = power_link_body.find_all('span', {'class': 'url'})
        return len(AS)
        rank = 0
        for index, a in enumerate(AS):
            if(self.advertiser in a.get_text()):
                return {'rank': index + 1, 'totalAds': len(AS)}

        return {'rank': rank, 'totalAds': len(AS)}

    def currentMORank(self):
        ENDPOINT = 'https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query=' + self.keyword
        page = requests.get(ENDPOINT)
        soup = BeautifulSoup(page.text, 'html.parser')
        power_link_body = soup.find('ul', {'id': 'power_link_body'})
        AS = power_link_body.find_all('span', {'class': 'url'})
        for index, a in enumerate(AS):
            if(self.advertiser in a.get_text()):
                return index+1
        return -1

    def __del__(self):
        print('keyword:',self.keyword, ', advertiser:', self.advertiser, ' 객체가 삭제되었습니다.')