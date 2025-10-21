# 🐍 ScoreManagement Program

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/mooonkyeong/ScoreManagement?style=social)](https://github.com/mooonkyeong/ScoreManagement/stargazers)

> **Python 기반의 간단하고 직관적인 콘솔 성적 관리 시스템입니다.**
> 파일 입출력(`students.txt`)을 통해 학생들의 학번, 이름, 중간/기말 성적을 관리하고, 평균 및 학점(A~F)을 자동 계산합니다.

<br>

---

## ✨ 주요 기능 (Features)

이 프로그램은 콘솔 환경에서 다음 기능을 제공합니다.

| 명령어 | 기능 설명 |
| :--- | :--- |
| **`show`** | 모든 학생의 목록을 **평균 점수 기준 내림차순**으로 정렬하여 출력합니다. |
| **`search`** | 학번(Student ID)을 입력받아 해당 학생의 정보를 출력합니다. |
| **`changescore`**| 학번과 시험 종류(Mid/Final)를 선택하여 점수를 수정하고, 평균/학점을 재계산합니다. |
| **`add`** | 새로운 학생의 학번, 이름, 중간/기말 점수를 추가합니다. |
| **`searchgrade`**| 학점(Grade, A/B/C/D/F)을 입력받아 해당 학점을 받은 학생들만 출력합니다. |
| **`remove`** | 학번을 입력받아 해당 학생의 정보를 삭제합니다. |
| **`quit`** | 프로그램 종료 시, 변경된 데이터를 새로운 파일에 저장할지 여부를 선택합니다. |

<br>

---

## ⚙️ 실행 환경 및 기술 스택 (Tech Stack)

| 구분 | 내용 |
| :--- | :--- |
| **개발 언어** | **Python 3** |
| **환경** | **콘솔/터미널 환경** (GUI 없음) |
| **데이터 저장**| **텍스트 파일 입출력** (`students.txt`) |

<br>

---

## 🚀 설치 및 실행 방법 (Installation & Run)

### 1. 저장소 클론 (Clone Repository)

```bash
git clone [https://github.com/mooonkyeong/ScoreManagement.git](https://github.com/mooonkyeong/ScoreManagement.git)
cd ScoreManagement
```
<br>

### 2. 데이터 파일 준비 (Optional)

프로그램은 기본적으로 students.txt 파일을 읽습니다. 파일이 없는 경우, 빈 파일을 생성하거나 다음 형식에 맞춰 학생 정보를 입력합니다.

students.txt 파일 형식: (각 항목은 탭(\t)으로 구분)

[학번]	[이름]	[중간점수]	[기말점수]
20230001	KimJaeHwan	95	85
20230002	LeeSuJin	70	75
...

<br>

### 3. 프로그램 실행

A. 기본 실행 (기본 파일: students.txt 사용)
Bash

python your_script_name.py

    참고: 코드 파일명이 main.py라면 python main.py로 실행하세요.

B. 사용자 지정 파일로 실행 (명령줄 인자 사용)
Bash

python your_script_name.py my_data.txt

<br>

## 📋 학점 기준 (Grade Criteria)

프로그램은 중간(Midterm)과 기말(Final) 점수의 평균을 기준으로 학점을 부여합니다.  
<br>
평균 점수 (Average)	학점 (Grade)  
&emsp; 90점 이상 &emsp;&emsp;&emsp; A  
&emsp; 80점 이상 &emsp;&emsp;&emsp; B  
&emsp; 70점 이상 &emsp;&emsp;&emsp; C  
&emsp; 60점 이상 &emsp;&emsp;&emsp; D  
&emsp; 60점 미만 &emsp;&emsp;&emsp; F  

<br>

## 🧑‍💻 기여 (Contribution)

이 프로젝트는 학습 및 실습 목적으로 작성되었습니다. 개선할 점이나 추가하고 싶은 기능(예: 예외 처리 강화, GUI 도입 등)이 있다면 언제든지 기여해주십시오.

<br>

## 📄 라이선스 (License)

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 LICENSE 파일을 참조하세요.
