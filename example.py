import searchUtil
# 네이버 서치 유틸

# ----------------------------------
# keyword: 검색 키워드
# advertiser: 광고주 URL substring
# ----------------------------------

keyword = "콜라겐"
advertiser = "newtreemall"

# init class
collagenKeyword = searchUtil.NaverSearch(keyword, advertiser)
print(collagenKeyword)
# 광고주: newtreemall, 키워드: 콜라겐


# currentPCTotalPowerLink Method
# 현재 해당 키워드로 PC에 첫페이지에 뜨는 총 파워링크 개수
totalAds = collagenKeyword.currentPCTotalPowerLink()
print(totalAds)


# currentPCRank Method
# 현재 PC 랭크 순위
# return 값이 -1일 경우 첫페이지에 없는 상태
rank = collagenKeyword.currentPCRank()
print(rank)


# currentMoTotalPowerLink Method
# 현재 해당 키워드로 보이는 모바일 파워링크 첫페이지에 뜨는 모든 광고
totalMobileAds = collagenKeyword.currentMOTotalPowerLink()
print(totalMobileAds)

# currentMORank Method
# 현재 MO 랭크 순위
# return 값이 -1일 경우 첫페이지에 없는 상태
mobileRank = collagenKeyword.currentMORank()
print(mobileRank)

del collagenKeyword