# Lab 1: Rule Based System


def check_result(score, attendance, assignment):

    # checking all required conditions

    if score >= 70 and attendance >= 75 and assignment == "Complete":
        print("Student Passed")
    else:
        print("Student Failed")


# Test Cases

print("Test Case 1: Pass Case")
check_result(85, 90, "Complete")


print("\nTest Case 2: Score Failure")
check_result(60, 90, "Complete")


print("\nTest Case 3: Attendance Failure")
check_result(80, 60, "Complete")


print("\nTest Case 4: Boundary Case")
check_result(70, 75, "Complete")
