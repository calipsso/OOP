student1 = ("jana", 17)
student2 = ("karol", 70)
student3 = ("beata", 69)
print(type(student3))

studenti = [student1, student2, student3]
print(type(studenti))

def najstarsi(studenti):
  return studenti[1]



max_vek = max(studenti, key=najstarsi)

print(max_vek)

users = {
  "meno":"kamil",
  "vek":86,
  "zamestnanie":"ucitel",
  "aktivny":True
}
users["vyska"] = 180
print(users)