import os 

os.chdir("C:\\Users\\Ce pc\\Desktop\\Math-Fac")
list_names = ["ALGEBRE I - EXERCICES RÉSOLUS","Module Analyse 1 Exercices corrigés","Cours d'Analyse I"]
i = 0
# os.remove(path="C:\\Users\\Ce pc\\Desktop\\Math-Fac\\PageWeb (2).pdf")
for filename in os.listdir(os.getcwd()) :
    filenames = filename.split('.')
    f_name,f_extension = filenames
    f_name = list_names[i]
    i+=1
    full_name = f_name +"."+f_extension
    os.rename(filename,full_name)




