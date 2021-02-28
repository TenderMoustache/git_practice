{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 weight = 41.5\
print("Package weight: ",weight)\
\
#ground shipping \
ground_shipping_flat_rate = 20\
\
if weight <=2:\
  ground_shipping_price = weight*1.5+ground_shipping_flat_rate\
elif weight <=6:\
  ground_shipping_price = weight*3+ground_shipping_flat_rate\
elif weight <= 10:\
  ground_shipping_price = weight*4+ground_shipping_flat_rate\
else :\
  ground_shipping_price = weight*4.75+ground_shipping_flat_rate\
\
print("Ground Shipping: ",ground_shipping_price)\
\
#ground shipping premium\
\
ground_shipping_premium_price = 125\
\
print("Ground Shipping Premium: ",ground_shipping_premium_price)\
\
#drone shipping\
\
if weight <=2:\
  drone_shipping_price = weight*4.5\
elif weight <=6:\
  drone_shipping_price = weight*9\
elif weight <= 10:\
  drone_shipping_price = weight*12\
else :\
  drone_shipping_price = weight*14.25\
\
print("Drone shipping price: ",drone_shipping_price)\
}