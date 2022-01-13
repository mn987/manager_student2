from Data.Student import Student
import random
import pandas

class ManagerStudent:
    lisStudent = []

    def add_Student(self):
        name = input("Nhập tên sinh viên: ")
        age = input("Nhập tuổi sinh viên: ")
        gender = input("Nhập giới tính sinh viên: ")
        id = None
        math = input('Nhập điểm toán: ')
        literature = input('Nhập điểm văn: ')
        english = input('Nhập điểm tiếng anh: ')
        gpa = round((int(math) + int(literature) + int(english)) /3, 1)
        rank = self.rank_student(gpa)
        student = Student(name,age,gender, math, literature, english, str(gpa), rank, id)
        return student

    def add_Students(self): #thêm sinh viên
        self.lisStudent = []
        n = 0 # _ID

        while True:
            student = self.add_Student()
            n += 1

            a = True
            while a == True:
                choice = input("\n Bạn có muốn tiếp tục thêm sinh viên không (y/n)? ")
                print("\n")

                if choice == "y":
                    students = []
                    students.append(student.name)
                    students.append(student.age)
                    students.append(student.gender)
                    students.append(student.math)
                    students.append(student.literature)
                    students.append(student.english)
                    students.append(student.gpa)
                    students.append(student.rank)
                    # student.id = n
                    student.id = random.randint(100,1000)
                    students.append(str(student.id))
                    self.lisStudent.append(students)
                    break
                elif choice == "n":
                    students = []
                    students.append(student.name)
                    students.append(student.age)
                    students.append(student.gender)
                    students.append(student.math)
                    students.append(student.literature)
                    students.append(student.english)
                    students.append(student.gpa)
                    students.append(student.rank)
                    # student.id = n
                    student.id = random.randint(100, 1000)
                    students.append(str(student.id))
                    self.lisStudent.append(students)
                    a = False
                    break
                else:
                    print("Lệnh bạn vừa dùng không có trong yêu cầu, hãy nhập lại.")
                    continue


            if a == True:
                pass
            else:
                break
        return self.lisStudent

    def show_list_Students(self, lisStudent): #hiển thị danh sách sinh viên
        print("\n Danh sách bạn vừa thêm vào gồm " + str(len(lisStudent)) + " sinh viên: \n")
        n = 1
        for i in lisStudent:
            print("-------Sinh Viên " + str(n) + "-------")
            for j in range(len(i)):
                print("-Tên: " + i[j])
                print("-Tuổi: " + i[j + 1])
                print("-Giới tính: " + i[j + 2])
                print("-Điểm toán: " + i[j + 3])
                print("-Điểm văn: " + i[j + 4])
                print("-Điểm tiếng anh: " + i[j + 5])
                print("-Mã ID: " + i[j + 8])
                break
            n += 1

    def rank_student(self, gpa):
        rank = ""
        if float(gpa) <= 3.5:
            rank = "Yếu"
        elif 3.5 < float(gpa) < 6.5:
            rank = "Trung bình"
        elif 6.5 <= float(gpa) < 8:
            rank = "Khá"
        else:
            rank = "Giỏi"
        return rank

    def write_txt(self, student, file):
        i = 0
        file.write(student[i] + "\n")
        file.write(student[i + 1] + "\n")
        file.write(student[i + 2] + "\n")
        file.write(student[i + 3] + "\n")
        file.write(student[i + 4] + "\n")
        file.write(student[i + 5] + "\n")
        file.write(student[i + 6] + "\n")
        file.write(student[i + 7] + "\n")
        file.write(student[i + 8] + "\n")

    def write_student_txt(self, lisStudent): #ghi danh sách sinh viên vào file.txt
        name_file = input("Nhập tên file bạn muốn lưu vào: ")
        with open(name_file + ".txt", "w", encoding="utf-8") as file:
            file.write(str(len(lisStudent)) + "\n")
            for i in lisStudent:
                self.write_txt(i, file)

    def write_student_at_last_txt(self, lisStudent):
        list_temp = []
        name_file = input("Nhập tên file bạn muốn lưu vào: ")
        with open(name_file + ".txt", "r", encoding="utf-8") as file:
            count = int(file.readline())
            for i in range(count):
                name = file.readline()
                age = file.readline()
                gender = file.readline()
                math = file.readline()
                literature = file.readline()
                english = file.readline()
                gpa = file.readline()
                rank = file.readline()
                id = file.readline()
                name = name.strip("\n")
                age = age.strip("\n")
                gender = gender.strip("\n")
                math = math.strip("\n")
                literature = literature.strip("\n")
                english = english.strip("\n")
                gpa = gpa.strip("\n")
                rank = rank.strip("\n")
                id = id.strip("\n")
                student = (name, age, gender, math, literature, english, gpa, rank, id)
                list_temp.append(student)
        for i in lisStudent:
            student = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
            list_temp.append(student)
        return list_temp, name_file

    def write_student_txt_2(self, lisStudent, name_file): #ghi danh sách sinh viên vào file.txt
        with open(name_file + ".txt", "w", encoding="utf-8") as file:
            file.write(str(len(lisStudent)) + "\n")
            for i in lisStudent:
                self.write_txt(i, file)

    def read_file_txt(self, name_file):
        lisStudent = []
        with open(name_file + ".txt", "r", encoding="utf-8") as file:
            count = int(file.readline())
            for i in range(count):
                name = file.readline()
                age = file.readline()
                gender = file.readline()
                math = file.readline()
                literature = file.readline()
                english = file.readline()
                gpa = file.readline()
                rank = file.readline()
                id = file.readline()
                student = Student(name, age, gender, math, literature, english, gpa, rank, id)
                lisStudent.append(student)
        return lisStudent, name_file

    def show_student_from_txt(self, students):
        lisStudent = []
        for i in students:
            student = []
            student.append(i.name.strip("\n"))
            student.append(i.age.strip("\n"))
            student.append(i.gender.strip("\n"))
            student.append(i.math.strip("\n"))
            student.append(i.literature.strip("\n"))
            student.append(i.english.strip("\n"))
            student.append(i.gpa.strip("\n"))
            student.append(i.rank.strip("\n"))
            student.append(i.id.strip("\n"))
            lisStudent.append(student)
        return lisStudent

    def show_students_DataFrame(self,students):
        count = 0
        s = []
        c = []

        for i in students:
            stu = pandas.Series(i, index=['Họ Tên SV: ', 'Tuổi: ', 'Giới Tính: ', 'Điểm toán: ', 'Điểm văn: ', 'Điểm anh: ', 'Điểm TB: ', 'Xếp loại học lực', 'Mã SV: '])
            s.append(stu)
            c.append(str(count))
            count += 1

        dic = dict(zip(c, s))
        df = pandas.DataFrame(dic)
        return df

    def show_students(self,name_file):
        check = True
        while check == True:  # đọc file
            if check == True:
                students, name_file = self.read_file_txt(name_file)
                students = self.show_student_from_txt(students)
                lisStudent = students

                df = self.show_students_DataFrame(students)
                check = False
                return df, lisStudent

            if check == True:
                print("Hãy thử lại, file bạn vừa nhập không tìm thấy được.")
                continue

    def FindbyID(self, lisStudent, id_Student):
        check = True
        while check == True:
            for student in lisStudent:
                if student[8] == id_Student:
                    s = pandas.Series(student, index=['Họ Tên SV: ', 'Tuổi: ', 'Giới Tính: ', 'Điểm toán: ', 'Điểm văn: ', 'Điểm anh: ', 'Điểm TB: ', 'Xếp loại học lực', 'Mã SV: '])
                    return s
                    check = False
            if check == True:
                print("Không tìm thấy mã ID bạn vừa nhập, vui lòng thử lại." + "\n")
                id_Student = input("Nhập ID bạn muốn tìm kiếm: ")

    def Edit_info(self, student, choice):
        student = Student(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7], student[8])
        if choice == "1":
            student.name = input("Nhập tên: ")
        elif choice == "2":
            student.age = input("Nhập tuổi: ")
        elif choice == "3":
            student.gender = input("Nhập giới tính: ")
        elif choice == "4":
            student.math = input("Nhập điểm toán: ")
        elif choice == "5":
            student.literature = input("Nhập điểm văn: ")
        elif choice == "6":
            student.english = input("Nhập điểm anh: ")
        student.gpa = str(round((int(student.math) + int(student.literature) + int(student.english)) / 3, 1))
        student.rank = str(self.rank_student(student.gpa))
        return student

    def choice_in_range(self):
        print("1. Tên.")
        print("2. Tuổi.")
        print("3. Giới tính.")
        print("4. Điểm toán. ")
        print("5. Điểm văn. ")
        print("6. Điểm anh. ")
        check = True
        while check == True:

            choice = input("Bạn muốn sửa thông tin gì (1-6): ")
            try:
                choice = int(choice)
                if 0 < int(choice) < 7:
                    check = False
            except:
                print("Bạn phải nhập vào 1 số có trong bảng trên, vui lòng thử lại!")


        return choice

    def Edit_info_Students(self, lisStudent, id_Student):
        student = None
        check = True
        while check == True:
            for i in lisStudent:
                if i[8] == id_Student:
                    choice = self.choice_in_range()
                    choice = str(choice)
                    student = i
                    index = lisStudent.index(student)
                    stu = self.Edit_info(student, choice)
                    lisStudent[index] = [stu.name, stu.age, stu.gender, stu.math, stu.literature, stu.english, stu.gpa, stu.rank, stu.id]
                    print("\n----Đã sửa thành công!----\n")
                    check = False
            if check == True:
                print("Không tìm thấy mã ID bạn vừa nhập, vui lòng thử lại.")
                id_Student = input("Nhập ID bạn muốn tìm kiếm: ")
        return lisStudent

    def Delete_student_by_ID(self, lisStudent, id_Student):
        check = True
        while check == True:
            for student in lisStudent:
                if student[8] == id_Student:
                    lisStudent.remove(student)
                    print("\nSinh viên có id = " + str(id_Student) + " đã bị xóa!\n")
                    check = False
            if check == True:
                print("Không tìm thấy mã ID bạn vừa nhập, vui lòng thử lại.")
                id_Student = input("Nhập ID bạn muốn xóa: ")
        return lisStudent

    def Sort_by_name(self, lisStudent):
        print("Hiển trị danh sách sinh viên được sắp xếp theo tên: ")
        lisStudent = sort_dec(lisStudent)
        return lisStudent
    def Sort_by_id(self, lisStudent):
        print("Hiển trị danh sách sinh viên được sắp xếp theo ID: ")
        name_student = []
        age_student = []
        gender_student = []
        math_score = []
        literature_score = []
        english_score = []
        gpa = []
        rank = []
        id_student = []

        def convert_list(name, age, gender, math_score, literature_score, english_score, gpa, rank, id):
            list_temp = []
            list_temp.append(name)
            list_temp.append(age)
            list_temp.append(gender)
            list_temp.append(math_score)
            list_temp.append(literature_score)
            list_temp.append(english_score)
            list_temp.append(gpa)
            list_temp.append(rank)
            list_temp.append(id)
            return list_temp

        for student in lisStudent:

            name_student.append(student[0])
            age_student.append(student[1])
            gender_student.append(student[2])
            math_score.append(student[3])
            literature_score.append(student[4])
            english_score.append(student[5])
            gpa.append(student[6])
            rank.append(student[7])
            id_student.append(student[8])
        id_student, name_student, age_student, gender_student, math_score, literature_score, english_score, gpa, rank = sort_dec2(id_student, name_student, age_student,
                                                                         gender_student, math_score, literature_score, english_score, gpa, rank)
        student_done = []
        for i in range(len(id_student)):
            student_done.append(convert_list(name_student[i], age_student[i], gender_student[i], math_score[i], literature_score[i], english_score[i], gpa[i], rank[i], id_student[i]))

        return student_done

    def sort_by_rank(self, lisStudent):
        print("Hiện thị danh sách sinh viên sắp xếp theo học lực: " + "\n")
        list_temp = []
        for student in lisStudent:
            if student[7] == "Giỏi":
                list_temp.append(student)
        for student in lisStudent:
            if student[7] == "Khá":
                list_temp.append(student)
        for student in lisStudent:
            if student[7] == "Trung bình":
                list_temp.append(student)
        for student in lisStudent:
            if student[7] == "Yếu":
                list_temp.append(student)
        return list_temp
def sort_dec(array1):
    for m in range(0, len(array1)-1):
        for n in range(m+1, len(array1)):
            if array1[m] > array1[n]:
                array1[m],array1[n] = array1[n],array1[m]
    return array1

def sort_dec2(array1,array2,array3,array4,array5,array6,array7,array8,array9):
    for m in range(0, len(array1)-1):
        for n in range(m+1, len(array1)):
            if array1[m] > array1[n]:
                array1[m],array1[n] = array1[n],array1[m]
                array2[m],array2[n] = array2[n],array2[m]
                array3[m],array3[n] = array3[n],array3[m]
                array4[m],array4[n] = array4[n],array4[m]
                array5[m], array5[n] = array5[n], array5[m]
                array6[m], array6[n] = array6[n], array6[m]
                array7[m], array7[n] = array7[n], array7[m]
                array8[m], array8[n] = array8[n], array8[m]
                array9[m], array9[n] = array9[n], array9[m]
    return array1, array2, array3, array4, array5, array6, array7, array8, array9

# def main():
#     qlsv = ManagerStudent()
#     # # qlsv.add_Students()
#     # # qlsv.show_list_Students()
#     # # qlsv.write_student_txt()
#     # students = qlsv.read_file_txt()
#     # students = qlsv.show_student_from_txt(students)
#     # print(students)
#
# main()
