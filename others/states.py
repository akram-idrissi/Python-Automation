import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizzName in range(35) :
    
    quizzfile=open('capitalsquiz_%s.txt'%(quizzName+1),'w')
    answerfile=open('capitalsquiz_answers_%s.txt'%(quizzName+1),'w')
    quizzfile.write("Name: \n\n"+"Date: \n\n"+"Period: \n\n")
    quizzfile.write(" ".rjust(20)+"State Capitals Quiz (Form %s)\n\n"%(quizzName+1))

# the meat of this code starts from here ma’am
    states=list(capitals.keys()) #takes keys of capital and store it into a list  
    random.shuffle(states)  #it organize data in this list randomly
    for questionNum in range(50) : #looping 50 times since we have 50 states :)
        correctAnsw=capitals[states[questionNum]] #searching for the correct capital and store it in correctAnsw
        wrongAnsw=list(capitals.values()) #take all values in capitals n store it in a list 
        del wrongAnsw[wrongAnsw.index(correctAnsw)] #search for the index of the answer and delete it from the wrongansw
        wrongAnsw=random.sample(wrongAnsw ,3) #piking 3 random false capitals 
        answerOptions=wrongAnsw+[correctAnsw] #concatenating answer with the 3 false answers and the correct one
        random.shuffle(answerOptions) #organize the 4 answers randomly 

        quizzfile.write("%s- what is the capital of %s ?\n"%(questionNum+1,states[questionNum]))
        for i in range(4): 
            quizzfile.write("\t%s. %s\n"%('ABCD'[i],answerOptions[i]))
        answerfile.write("%s. %s"%(questionNum+1,'ABCD'[answerOptions.index(correctAnsw)])+"\n")

        quizzfile.write("\n")


quizzfile.close
answerfile.close  

    



 



