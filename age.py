def finding_age(name,age):
    return f"Hello! {fullname} You will be {total_age} in 5 years."
fullname = input("Enter your fullname: ")
age =  int(input("Enter your age: "))
total_age = age+5
print(finding_age(fullname,age))