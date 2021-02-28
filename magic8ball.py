{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random\
name = "Mo"\
\
question = "Am I in love?"\
\
answer = ""\
\
random_number = random.randint(1,13)\
\
#print(random_number)\
\
if random_number == 1:\
  answer="Yes, Definitely."\
elif random_number == 2:\
  answer="It is decidedly so."\
elif random_number == 3:\
  answer="Without a doubt."\
elif random_number == 4:\
  answer="Reply hazy, try again."\
elif random_number == 5:\
  answer="Ask again later."\
elif random_number == 6:\
  answer="Better not tell you now."\
elif random_number == 7:\
  answer="My sources say no."\
elif random_number == 8:\
  answer="Outlook not so good."\
elif random_number == 9:\
  answer="Maybe yes, maybe no."\
elif random_number == 10:\
  answer="You are asking the wrong question."\
elif random_number == 11:\
  answer="Definitely, but it won't impact you."\
elif random_number == 12:\
  answer="Are you still stuck on that, move on man!"\
else:\
  answer="Very doubtful."\
\
if name == "":\
  print("Question: "+question)\
else: print(name+" asks: "+question)\
\
if question == "":\
  print("What do you want to know?")\
else:\
  print("Magic 8-ball answer: "+answer)\
}