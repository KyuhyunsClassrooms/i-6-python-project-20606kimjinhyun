pets = []

count = int(input("진단할 동물 수를 입력하세요: "))

for i in range(count):
    print("\n", i + 1, "번째 동물 정보 입력")

    name = input("동물 이름: ")
    animal_type = input("동물 종류: ")
    temp = float(input("체온: "))
    symptom = input("증상을 문장으로 입력하세요: ")

    pets.append([name, animal_type, temp, symptom])


# 증상 리스트 [증상, 위험 점수]
symptom_keywords = [
    ["구토", 2],
    ["설사", 2],
    ["기침", 1],
    ["재채기", 1],
    ["무기력", 2],
    ["식욕부진", 2],
    ["호흡곤란", 3],
    ["떨림", 2],
    ["경련", 4],
    ["탈수", 3],
    ["혈변", 4],
    ["혈뇨", 4],
    ["걷기 어려움", 3],
    ["숨을 헐떡임", 2]
]


# 체온 판정 함수
def check_temperature(animal, temp):

    if animal == "강아지" or animal == "개":
        normal_min = 37.5
        normal_max = 39.2

    elif animal == "고양이":
        normal_min = 38.0
        normal_max = 39.5

    else:
        normal_min = 38.5
        normal_max = 40.0

    if temp < normal_min:
        return "저체온", 2

    elif temp > normal_max:
        return "고체온", 2

    else:
        return "정상", 0


# 증상 분석 함수
def analyze_symptom(text):

    score = 0
    found = []

    for symptom in symptom_keywords:

        if symptom[0] in text:
            found.append(symptom[0])
            score += symptom[1]

    return found, score


# 건강 판정 함수
def judge_health(score):

    if score >= 6:
        return "위험"

    elif score >= 3:
        return "주의 필요"

    else:
        return "양호"


# 추천 행동 함수
def recommend_action(result, level):

    if level == "위험":

        if result == "고체온":
            return "물을 공급하고 활동을 줄인 후 즉시 병원을 방문하세요."

        elif result == "저체온":
            return "담요 등으로 체온을 유지하고 즉시 병원을 방문하세요."

        else:
            return "증상이 심하므로 즉시 병원을 방문하세요."

    elif level == "주의 필요":
        return "충분히 쉬게 하고 상태를 계속 관찰하세요."

    else:
        return "현재 상태를 유지하며 꾸준히 관찰하세요."


# ===== 진단서 출력 =====
for pet in pets:

    temp_result, temp_score = check_temperature(
        pet[1],
        pet[2]
    )

    found_symptoms, symptom_score = analyze_symptom(
        pet[3]
    )

    total_score = temp_score + symptom_score

    health = judge_health(total_score)

    advice = recommend_action(
        temp_result,
        health
    )

    print("\n===== 동물 건강 진단서 =====")
    print("동물 이름:", pet[0])
    print("동물 종류:", pet[1])
    print("체온:", pet[2])
    print("체온 상태:", temp_result)

    if len(found_symptoms) > 0:
        print("감지된 증상:", ", ".join(found_symptoms))
    else:
        print("감지된 증상: 없음")

    print("위험 점수:", total_score)
    print("최종 판정:", health)
    print("추천 행동:", advice)