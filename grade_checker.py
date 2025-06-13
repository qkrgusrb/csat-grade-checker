def get_grade_and_comment(subject, score):
    """
    과목과 점수를 입력받아 등급과 코멘트를 반환하는 함수
    """
    # 국어 등급컷
    korean_cuts = {1: 94, 2: 88, 3: 82, 4: 75, 5: 66, 6: 56, 7: 45, 8: 34}
    # 수학 등급컷
    math_cuts = {1: 92, 2: 84, 3: 76, 4: 66, 5: 53, 6: 39, 7: 28, 8: 20}
    # 영어 등급컷 (절대평가)
    english_cuts = {1: 90, 2: 80, 3: 70, 4: 60, 5: 50, 6: 40, 7: 30, 8: 20}

    cuts = {}
    if subject == '국어':
        cuts = korean_cuts
    elif subject == '수학':
        cuts = math_cuts
    elif subject == '영어':
        cuts = english_cuts
    else:
        return "잘못된 과목명입니다.", ""

    grade = 9  # 기본 등급을 9로 설정
    for g, cut_score in cuts.items():
        if score >= cut_score:
            grade = g
            break

    comments = {
        1: "🎉 정말 대단해요! 1등급이라니, 당신의 노력에 박수를 보냅니다!",
        2: "👍 훌륭한 성적입니다! 2등급도 정말 값진 결과예요.",
        3: "😊 잘했어요! 3등급은 안정적인 시작을 의미하죠. 다음엔 더 잘할 수 있을 거예요.",
        4: "🙂 괜찮아요! 4등급도 나쁘지 않은 성적이에요. 가능성은 충분합니다.",
        5: "🤔 조금 아쉬운 결과네요. 하지만 여기서부터가 진짜 시작입니다!",
        6: "💪 힘내세요! 다음 시험에서는 더 좋은 결과를 얻을 수 있도록 응원할게요.",
        7: "🧐 부족한 부분을 채우면 다음엔 분명 더 나아질 거예요.",
        8: "😥 괜찮아요, 누구나 실수는 할 수 있어요. 다시 일어나면 됩니다!",
        9: "🙏 결과에 너무 실망하지 마세요. 새로운 시작의 기회로 삼아봐요."
    }

    return f"{grade}등급", comments.get(grade, "")

# --- 프로그램 시작 ---
if __name__ == "__main__":
    print("✨ 2024 수능 성적 등급 확인 프로그램 ✨")
    print("----------------------------------------")

    while True:
        try:
            subject_name = input("과목명을 입력하세요 (국어, 수학, 영어 중 하나): ")
            if subject_name not in ['국어', '수학', '영어']:
                print("🚨 국어, 수학, 영어 중에서만 선택해주세요.")
                continue

            score_str = input(f"{subject_name} 원점수를 입력하세요 (0-100): ")
            user_score = int(score_str)

            if not 0 <= user_score <= 100:
                print("🚨 점수는 0에서 100 사이의 숫자로 입력해주세요.")
                continue

            grade_result, comment_result = get_grade_and_comment(subject_name, user_score)

            print("\n--- 결과 ---")
            print(f"당신의 {subject_name} 성적은 '{grade_result}' 입니다.")
            print(comment_result)
            print("------------\n")

        except ValueError:
            print("🚨 잘못된 입력입니다. 숫자로 점수를 입력해주세요.")
        except Exception as e:
            print(f"오류가 발생했습니다: {e}")

        another = input("다른 과목도 확인하시겠습니까? (y/n): ").lower()
        if another != 'y':
            print("프로그램을 종료합니다. 이용해주셔서 감사합니다. 😊")
            break