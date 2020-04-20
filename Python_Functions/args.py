def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
courses = ('python','programming')
info={'name':'xyz','age':21}
print(student_info(*courses,**info))
