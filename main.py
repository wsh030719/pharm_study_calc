import time

def student_management():
    print("\n--- [1] LLM-Based Automated Feedback Pipeline ---")
    name = input("Enter student name (학생 이름 입력): ")
    try:
        math_score = int(input("Enter Math score (수학 점수 0-100): "))
        bio_score = int(input("Enter Biology score (생명과학 점수 0-100): "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    print("\n🤖 AI가 성적 데이터를 분석하여 맞춤형 리포트를 생성 중입니다...")
    time.sleep(1.5)
    
    print("\n==================================================")
    print(f"       📝 AI FEEDBACK REPORT FOR {name.upper()}       ")
    print("==================================================")
    print(f"• Math Score: {math_score}/100")
    print(f"• Biology Score: {bio_score}/100")
    print("--------------------------------------------------")
    print("[AI Analysis & Automated Message for Parents]")
    
    # 성적에 따른 AI 피드백 메시지 자동 생성 시뮬레이션
    avg = (math_score + bio_score) / 2
    if avg >= 90:
        status = "Excellent"
        msg = f"안녕하세요 학부모님, 오늘 {name} 학생은 전반적인 개념 이해도가 매우 뛰어납니다. 현재 페이스를 유지하면 실전에서도 고득점이 확실시됩니다."
    elif avg >= 70:
        status = "Good"
        msg = f"안녕하세요 학부모님, 오늘 {name} 학생은 핵심 개념을 잘 소화했으나 일부 심화 문항에서 아쉬움이 있었습니다. 오답 노트 위주로 보완하겠습니다."
    else:
        status = "Needs Improvement"
        msg = f"안녕하세요 학부모님, 오늘 {name} 학생은 기초 개념 리마인드가 필요한 상태입니다. 다음 시간까지 필수 키워드 암기 과제를 집중 점검하겠습니다."
        
    print(f"• Status: {status}")
    print(f"• SMS Draft:\n  \"{msg}\"")
    print("==================================================\n")

def pharmacy_learning():
    print("\n--- [2] Pharmacy & Bio Concept Flashcard Generator ---")
    print("AI 플래시카드를 생성할 토픽을 선택하세요:")
    print("1. Pharmacokinetics (약물동태학 기초)")
    print("2. Molecular Biology (분자생물학 - DNA 복제)")
    print("3. Custom Topic (학습할 개념 직접 입력)")
    
    choice = input("Choose option (1-3): ")
    
    if choice == "1":
        topic = "Pharmacokinetics (ADME)"
        content = "• Definition: Absorption, Distribution, Metabolism, and Excretion of drugs.\n• Key Formula: CLT = Dose / AUC\n• Core Concept: 체내 약물 농도 변화를 수학적으로 모델링하는 기초 이론."
    elif choice == "2":
        topic = "DNA Replication"
        content = "• Definition: Process of producing two identical replicas from one original DNA molecule.\n• Key Enzyme: DNA Polymerase, Helicase, Primase\n• Core Concept: 유전 정보의 정확한 전달을 위한 생물학적 복제 메커니즘."
    elif choice == "3":
        custom_topic = input("Enter your own bio/pharm topic: ")
        topic = custom_topic
        content = f"• Definition: Automated Summary for '{custom_topic}'.\n• Core Concept: 입력하신 개념에 대한 핵심 키워드 중심의 활성 상기(Active Recall) 학습 모드 활성화."
    else:
        print("❌ Invalid choice.")
        return

    print("\n🤖 AI가 전공 개념을 핵심 플래시카드로 가공 중입니다...")
    time.sleep(1)
    
    print("\n[ 🎴 AI GENERATED FLASHCARD ]")
    print(f"Topic: {topic}")
    print("-" * 50)
    print(content)
    print("-" * 50 + "\n")

def main():
    while True:
        print("=========================================")
        print("       Welcome to EduPharm-AI v1.0       ")
        print("=========================================")
        print("1. Student Management & AI Feedback")
        print("2. Pharmacy & Bio Learning Flashcards")
        print("3. Exit Program")
        print("=========================================")
        
        choice = input("Select Menu (1-3): ")
        
        if choice == "1":
            student_management()
        elif choice == "2":
            pharmacy_learning()
        elif choice == "3":
            print("\nThank you for using EduPharm-AI. Goodbye!")
            break
        else:
            print("\n❌ Invalid selection. Please try again.\n")

if __name__ == "__main__":
    main()
