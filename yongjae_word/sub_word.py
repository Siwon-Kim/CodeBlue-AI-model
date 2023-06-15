symptom_scores = {
    "category1": {
        '소실된의식': 12,
        "심부전": 12,
        '뇌경색': 11,
        '사지마비': 11,
        '의식변화': 10,
        '기억상실': 10,
        "발작": 10,
        '혼란상태': 9,
        '가슴통증': 6,
    },
    "category2": {
        '청각손실': 12,
        '시야손실': 9,
        '감각소실': 9,
        "경련": 7,
        "저림": 6,
        '손발차가움': 6,
        '심한두통': 5,
        '기운없음': 3,
        "오심": 3,
        "구토": 3,
    },
    "category3": {
        "호흡곤란": 3, #원래 8점인데 호흡음과 호흡곤란은 같이 온다는 전제하에 3점세팅
        "호흡음": 3, #원래 8점 임시점수부여(호흡/곤란/호흡/음 합성어 때문)
        '흉부압박감': 6,
        "코막힘": 4,
        "기침": 3,
    },
    "category4": {
        "저체온증": 8,
        '혈압저하': 8,
        '사지부종': 7,
        '혈압상승': 5,
        "빈혈": 6,
        "황달": 5,
        '목의부종': 4,
    },
    "category5": {
        '출혈': 9,
        "혈뇨": 6,
        '점막출혈': 5,
        "근육통": 5,
        "화상": 5,
        "코피": 4,
        "고열": 4,
    },
    "category6": {
        '음식섭취곤란': 6,
        '알레르기반응': 4,
        '가려운발진': 4,
        '체중감소': 3,
    },
}

def get_severity_level(score):
    if score > 80:
        return "level 1"
    elif score > 60:
        return "level 2"
    elif score > 40:
        return "level 3"
    elif score > 20:
        return "level 4 "
    else:
        return "level 5"