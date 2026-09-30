#if문 연습

user = "haein"

if user == "haein":
    print("전해인 님, 안녕하세요.")
else:
    print("다른 사용자입니다.")

user_2 = "female"

if user_2 == "male":
    print("당신은 남자입니다.")
else :
    print("당신은 여자입니다.")

#for문 연습

task = "0"
tasks = ["1. 파이썬 수업 듣기", "2. 오늘 배운 것 복습하기", "3. 포트폴리오 제작하기"]

print(" - 오늘 할 일 목록 - ")

for task in tasks:
    print(task)

#조건문과 반복문 연습

students = [{"name": "해인", "score": 90}, {"name": "수인", "score": 55}]
ss = "-"
s = "0"
result = "0"

print("시험 합격 여부")

for s in students:
    if s["score"] >= 60:
        result = "합격"
    else:
        result = "불합격"
    print(f"{ss} {s["name"]}: {result}")

#함수 재사용 연습

def calculate_stats(score_list):
    total = sum(score_list)
    avg = total / len(score_list)
    return total, avg

scores = [95, 63, 92]
total, avg = calculate_stats(scores)

print(f"총점 : {total}, 평균: {avg:.2f}")

