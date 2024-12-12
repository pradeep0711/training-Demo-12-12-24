project_score = float(input("Enter the project score:"))
internal_score = float(input("Enter the internal score:"))
external_score = float(input("Enter the external score:"))
if(project_score >= 50 and internal_score >= 50 and external_score >= 50):
    score = 0.7*project_score+0.1*internal_score+0.2*external_score
    if score > 90:
        print("Grade A")
    elif  score > 80:
        print("Grade B")
    else :
        print("Grade C")
else :
    if project_score<50:
      print("Failed in Project Score",project_score)
    if internal_score<50:
      print("Failed in Internal Score",internal_score)
    if external_score<50:
      print("Failed in External Score",external_score)