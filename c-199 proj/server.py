import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address = "127.0.0.1"
port=8000

server.bind((ip_address,port))
server.listen()

all_clients= []
questions = [ " What is the Italian word for PIE? \n a.Mozarella\n b.Pasty\n c.Patty\n d.Pizza", " Water boils at 212 Units at which scale? \n a.Fahrenheit\n b.Celsius\n c.Rankine\n d.Kelvin", " Which sea creature has three hearts? \n a.Dolphin\n b.Octopus\n c.Walrus\n d.Seal", " Who was the character famous in our childhood rhymes associated with a lamb? \n a.Mary\n b.Jack\n c.Johnny\n d.Mukesh", " How many bones does an adult human have? \n a.206\n b.208\n c.201\n d.196", " How many wonders are there in the world? \n a.7\n b.8\n c.10\n d.4", " What element does not exist? \n a.Xf\n b.Re\n c.Si\n d.Pa", " How many states are there in India? \n a.24\n b.29\n c.30\n d.31", " Who invented the telephone? \n a.A.G Bell\n b.John Wick\n c.Thomas Edison\n d.G Marconi", " Who is Loki? \n a.God of Thunder\n b.God of Dwarves\n c.God of Mischief\n d.God of Gods", " Who was the first Indian female astronaut ? \n a.Sunita Williams\n b.Kalpana Chawla\n c.None of them"]
answers=["d","a","b","a","a","a","a","b","a","c","b","d","d","c","a","b","a"]
print("server has started")

def getRandomQuestion(conn):
    randomIndex = random.randint(0,len(questions)-1)
    randomQuestions = questions[randomIndex]
    randomAnswer = answers[randomIndex]
    conn.send(randomQuestions.encode("utf-8"))
    return randomIndex,randomQuestions,randomAnswer

def removeQuestion(index):
    questions.pop(index)
    answers.pop(index)

while True:
    conn,addr = server.accept()
    all_clients.append(conn)
    print(addr)
    newThread =Thread(target=getRandomQuestion,args=(conn))
    newThread.start()

