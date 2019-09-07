import json


class School(object):
  def __init__(self, name:str, year_in:int, year_out:int, major:str = None):
    self.name = name
    self.year_in = year_in
    self.year_out = year_out
    self.major = major
    
class Skills(object):
  def __init__(self, skill_name:str , level:str):
    self.skill_name = skill_name
    self.level = level
    
class Biodata(object):
  def __init__(self, name:str, age:int, address:str, hobbies:list, is_married:bool, list_school:list, skills:list, interest_in_coding:bool):
    self.name = name
    self.age = age
    self.address = address
    self.hobbies = hobbies
    self.is_married = is_married
    self.list_school = list_school
    self.skills = skills
    self.interest_in_coding = interest_in_coding
  
if __name__ == "__main__":
  name = input("your name :")
  age = int(input("your age :"))
  address = input("your address :")
  
  h = input("how many hobbie (number):")
  hobbies = ['hobi 1', 'hobi 2']
  for i in range(int(h)):
    n = i+1
    ho = input("your hobbie->"+str(i+1)+":")
    hobbies.append(ho)
  
  is_marr = input("are you married(y/n) :")
  is_married = True if is_marr == 'y' else False
  
  list_ = ['SD','SMP','SMA','Universitas']
  list_school = []
  for i in list_:
    print('SCHOOL->',i)
    school = {}
    name = input("School name:")
    year_in = input("Year in:")
    year_out = input("Year out:")
    major = input("Major(if any):")
    l_school = School(name, year_in, year_out, major)
    list_school.append(json.dumps(l_school.__dict__))

  s = input("how many skill (number):")
  skills = []
  for i in range(int(s)):
    skill = {}
    skill_name = input('Skill->'+str(i+1)+', skill_name :')
    level = input('Skill->'+str(i+1)+', level(beginner, advanced, expert) :')
    l_skills = Skills(skill_name, level)
    skills.append(json.dumps(l_skills.__dict__))
  
  interest_ = input("interest in coding(y/n) :")
  interest_in_coding = True if interest_ == 'y' else False
    
  bio = Biodata(name, age, address, hobbies, is_married, list_school, skills, interest_in_coding)
  CV = json.dumps(bio.__dict__)
  print(CV)
