Dept_A = {'Name': 'safiya', 'Age': 22}
Dept_B = {'Height': 159}
Dept_C = {'BloodType': 'B+'}


Patient_Profile = {}

Patient_Profile.update(Dept_A)
Patient_Profile.update(Dept_B)
Patient_Profile.update(Dept_C)

print("Complete Patient Record:")
print(Patient_Profile)
