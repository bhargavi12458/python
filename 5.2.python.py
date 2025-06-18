class student:
    def_init_(self,name,marks):
        self.name=name
        self.marks=marks
        def print_student_info(student):
            print(f"name:{student.name},marks:{student.marks}")
            s1=student("tillu",92)
            print_student_info(s1)
            
