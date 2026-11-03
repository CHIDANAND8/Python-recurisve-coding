
student_name = input("Enter student name: ")

math = float(input("Enter marks for Mathematics: "))
science = float(input("Enter marks for Science: "))
english = float(input("Enter marks for English: "))
social = float(input("Enter marks for Social Studies: "))
language = float(input("Enter marks for Language: "))


pass_marks = 35
all_passed = True

print("\n" + "=" * 40)
print(f"  SUBJECT-WISE RESULTS FOR {student_name.upper()}")
print("=" * 40)

if math >= pass_marks:
    print(f"Mathematics    : {math}/100 (Pass)")
else:
    print(f"Mathematics    : {math}/100 (Fail)")
    all_passed = False

if science >= pass_marks:
    print(f"Science        : {science}/100 (Pass)")
else:
    print(f"Science        : {science}/100 (Fail)")
    all_passed = False

if english >= pass_marks:
    print(f"English        : {english}/100 (Pass)")
else:
    print(f"English        : {english}/100 (Fail)")
    all_passed = False

if social >= pass_marks:
    print(f"Social Studies : {social}/100 (Pass)")
else:
    print(f"Social Studies : {social}/100 (Fail)")
    all_passed = False

if language >= pass_marks:
    print(f"Language       : {language}/100 (Pass)")
else:
    print(f"Language       : {language}/100 (Fail)")
    all_passed = False

total_marks = math + science + english + social + language
max_marks = 500
percentage = (total_marks / max_marks) * 100

print("-" * 40)
print(f"Total Marks    : {total_marks:.1f} / {max_marks}")
print(f"Percentage     : {percentage:.2f}%")
print("-" * 40)


if not all_passed:
    print("Final Result   : FAILED")
    print("Grade          : F (Failed in one or more subjects)")
elif percentage >= 90:
    print("Final Result   : PASSED")
    print("Grade          : A+ (Outstanding / Distinction)")
elif percentage >= 80:
    print("Final Result   : PASSED")
    print("Grade          : A (First Class with Distinction)")
elif percentage >= 60:
    print("Final Result   : PASSED")
    print("Grade          : B (First Class)")
elif percentage >= 50:
    print("Final Result   : PASSED")
    print("Grade          : C (Second Class)")
elif percentage >= 35:
    print("Final Result   : PASSED")
    print("Grade          : D (Pass Class)")
else:
    print("Final Result   : FAILED")
    print("Grade          : F")

print("=" * 40)
