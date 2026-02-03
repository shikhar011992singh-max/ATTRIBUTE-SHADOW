class Chai:
      temperature = "cold"
      strength    = "strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "mild"
print("after changing",cutting.temperature)
print("direct look into class" ,Chai.temperature)

del cutting.temperature # since del funct is used, it'll be printed/shadowed to value written above & not del permanent as mention in func.
print(cutting.temperature) 