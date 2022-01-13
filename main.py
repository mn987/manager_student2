from Manager.Manager import ManagerStudent

def main():
    lisStudent = []
    id_Student = None
    name_file = None

    while True:
        print('''
        -----------------------------------------------
        | 0. Thoát chương trình.                       |
        | 1. Thêm Sinh Viên.                           |
        | 2. Lưu danh sách Sinh viên vào cuối thư mục. |
        | 3. Làm mới danh sách và lưu vào thư mục.     |
        | 4. Hiển thị danh sách Sinh Viên từ thư mục.  |
        | 5. Tìm kiếm Sinh Viên.                       |
        | 6. Sửa thông tin Sinh Viên                   |
        | 7. Xóa Sinh viên theo ID.                    |
        | 8. Sắp xếp Sinh Viên theo tên.               |
        | 9. Sắp xếp Sinh Viên theo ID.                |
        | 10. Sắp xếp Sinh Viên theo 'Học lực'.        |
        ------------------------------------------------
        ''')

        qlsv = ManagerStudent()

        choice = input("Nhập 1 số bất kì để thực hiện chức năng: ")
        try:
            choice == int(choice)
            if 0 <= int(choice) < 11:
                pass
            else:
                print("\n-----Bạn phải nhập vào 1 số có trong bảng trên, vui lòng thử lại-----\n")
                input("----Nhấn Enter để tiếp tục----")
        except:
            print("\n-----Bạn phải nhập vào 1 số có trong bảng trên, vui lòng thử lại-----\n")
            input("----Nhấn Enter để tiếp tục----")
            pass

        if choice == "0":
            print("-----Đang thoát chương trình-----")
            break
        if choice == "1":
            lisStudent = qlsv.add_Students()
            qlsv.show_list_Students(lisStudent)
            input("\n----Nhấn Enter để tiếp tục----")
        if choice == "2":
            lisStudent, name_file = qlsv.write_student_at_last_txt(lisStudent)
            qlsv.write_student_txt_2(lisStudent, name_file)
            print("\n ----Đã lưu thành công!----\n")
            input("\n----Nhấn Enter để tiếp tục----")
        if choice == "3":
            qlsv.write_student_txt(lisStudent)
            print("\n ----Đã lưu thành công!----\n")
            input("\n----Nhấn Enter để tiếp tục----")
        if choice == "4":
            name_file = input("Nhập tên file bạn muốn hiển thị: ")
            df, lisStudent = qlsv.show_students(name_file)
            print(df)
            input("\n----Nhấn Enter để tiếp tục----")
        if choice == "5":
            id_Student = input("Nhập ID bạn muốn tìm kiếm: ")
            s = qlsv.FindbyID(lisStudent, id_Student)
            print(s)
            input("\n----Nhấn Enter để tiếp tục----")
        if choice == "6":
            id_Student = input("Nhập ID bạn muốn sửa: ")
            lisStudent = qlsv.Edit_info_Students(lisStudent, id_Student)
            qlsv.write_student_txt(lisStudent)
            input("\n----Nhấn Enter để tiếp tục----")
        if choice == "7":
            id_Student = input("Nhập ID bạn muốn xóa: ")
            lisStudent = qlsv.Delete_student_by_ID(lisStudent, id_Student)
            qlsv.write_student_txt(lisStudent)
            input("\n----Nhấn Enter để tiếp tục----")
        if choice == "8":
            lisStudent = qlsv.Sort_by_name(lisStudent)
            df = qlsv.show_students_DataFrame(lisStudent)
            print(df)
            input("\n----Nhấn Enter để tiếp tục----")
        if choice == "9":
            lisStudent = qlsv.Sort_by_id(lisStudent)
            df = qlsv.show_students_DataFrame(lisStudent)
            print(df)
            input("\n----Nhấn Enter để tiếp tục----")
        if choice == "10":
            lisStudent = qlsv.sort_by_rank(lisStudent)
            df = qlsv.show_students_DataFrame(lisStudent)
            print(df)
            input("\n----Nhấn Enter để tiếp tục----")

main()
