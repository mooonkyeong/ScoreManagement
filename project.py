import sys

def file_open(s, f_name = "students.txt"):
    with open(f_name, "r") as f:
        for line in f:
            sid, name, mid, fin = line.strip().split("\t")
            avg, grad = c_grad(mid, fin)
            info = [sid, name, mid, fin, avg, grad]
            s.append(info)

# 등급 변환
def c_grad(m, f):
    avg = (int(m) + int(f))/2
    if avg >= 90:
        g = "A"
    elif avg >= 80:
        g = "B"
    elif avg >= 70:
        g = "C"
    elif avg >= 60:
        g = "D"
    else:
        g = "F"

    return avg, g


# 리스트 보여주기
def show(s):
    s_list = s
    s_list.sort(key = lambda x:x[4], reverse = True)

    print(f" {'Student':<7}  {'Name':>14}    {'Midterm':<8}  {'Final':<8} {'Average':<8} {'Grade'}")
    print("-"*62)
    for i in s_list:
        print(f" {i[0]:<8} {i[1]:>15}      {i[2]:<8} {i[3]:<8} {i[4]:<8} {i[5]}")
        
#검색
def search(s):
    s_list = s
    fnd = 0
    u_id = input("Student ID : ")
    
    #리스트에 학번 있는 경우
    for i in s_list:
        if u_id == i[0]:
            show([i])
            fnd = 1

    # 리스트에 학번 없는 경우
    if fnd == 0:
        print("NO SUCH PERSON")
        

# 점수 수정
def insert_score(li, t):
    score = int(input("Input new score : "))
    if score > 100 or score<0:
        pass
    else:
        show([li])
        print("Score change")
        li[t] = score
        mid, fin = li[2], li[3]
        avg, grd = c_grad(mid, fin)
        li[4], li[5] = avg, grd
        show([li])

def changescore(list):
    s_id = input("Student ID ")
    fnd = 0
    for i in list:
        # 리스트에 학번 있는 경우
        if s_id in i[0]:
            term = input("Mid/Final? ").lower()
            fnd = 1
            if term == "mid":
                insert_score(i, 2)
                pass
            elif term == "final":
                insert_score(i, 3)
                pass
            else:
                pass
    if fnd == 0:
        print("NO SUCH PERSON.")

# 점수 추가
def add(s):
    s_list = s
    fnd = 0
    id = input("Student ID : ")
    for i in s_list:
        if id in i[0]:
            print("ALREADY EXISTS.")
            fnd = 1
            break
    if fnd == 0:
        name = input("Name : ")
        mid = input("Midterm Score : ")
        fin = input("Final Score : ")
        avg, grad = c_grad(mid, fin)
        new_list = [id, name, mid, fin, avg, grad]
        s_list.append(new_list)
        print("Student added.")
    return s

#등급 검색
def searchgrade(s):
    s_list = s
    g_list = []
    grd = input("Grade to search : ").upper()
    
    if grd not in ['A', 'B', 'C', 'D', 'F']:
        pass
    else:
        for i in s_list:
            if grd in i[5]:
                g_list.append(i)

    if len(g_list) > 0:
        show(g_list)
    else:
        print("NO RESULTS.")


# 삭제
def remove(s):
    num = 0
    fnd = 0
    if len(s)> 0:
        sid = input("Student ID : ")
        for i in s:
            if sid in i[0]:
                del s[num]
                print("Student removed.")
                fnd = 1
                break
            num += 1 
        if fnd == 0:
            print("NO SUCH PERSHON.")
    else:
        print("List is empty")


# 종료
def quit(s):
    s_list = s
    re = input("Save data? [yes/no] ").lower()
    if re == "yes":
        f_name = input("File name : ")
        with open(f_name, "w") as f:
            for sid, name, mid, fin, avg, grd in s_list:
                f.write(f"{sid}\t{name}\t{mid}\t{fin}\t{avg}\t{grd}\n")
    elif re == "no":
        pass


# main
# 파일 이름 불러와서 평균, 등급 계산 후 평균 기준으로 정렬해 출력
s = []
if len(sys.argv) >= 2:
    file_open(s, sys.argv[1])
else:
    file_open(s)
show(s)
    
while True:
    print(" ")
    user = input("# ").lower()
    if user =="show":
        show(s)
    elif user == "search":
        search(s)
    elif user == "changescore":
        changescore(s)
    elif user == "add":
        s = add(s)
    elif user == "searchgrade":
        searchgrade(s)
    elif user == "remove":
        remove(s)
    elif user == "quit":
        quit(s)
        break
    else:
        pass

