# 서울시 대기 오픈 API
import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# print(r) <Response [200]>
json = r.json()
# print (json['RealtimeCityAir']['row'][0]['NO2'])

# 구를 입력받고 미세먼지 값 구하기
def get_index(gu_name):
	data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
	jdata = data.json()
	gu_infos = jdata['RealtimeCityAir']['row']
	for gu_info in gu_infos:
		if gu_info['MSRSTE_NM'] == gu_name:
			return print(gu_info['IDEX_MVL'])
	return print('옳지 않은 구 이름입니다')

get_index('구')