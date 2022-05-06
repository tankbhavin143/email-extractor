import re

str = """Boult Audio Service 

Centres India Exotic Mile, 1st Floor, B-67, Wazirpur Industrial Area, 

Near Honda Showroom & Royal pepper Banquet, New Delhi PIN- 110052 Boult Audio customer care details ,Boult

 Tata Motor Connecting Aspiration LogoTata Motor Logo
Search
 
Menu
Contact Us - Tata Motors
Contact Us
At Tata Motors we believe in transparent communication and have built various touchpoints through which our stakeholders can get in touch with us.

For any assistance on
Commercial Vehicles, Cars & Utility Vehicles
For Commercial Vehicles
Email Id - cac@tatamotors.com Toll Free Number -1800 209 7979
For Passenger Vehicles
Email Id - customercare@tatamotors.com Toll Free Number -1800 209 8282
Head Office Commercial Vehicles Passenger Vehicles Media Investors
Tata Motors International Business
A Block, Shivasagar Estate,
Dr. Annie Besant Road,
Worli, Mumbai - 400018
Contact: +91(22) 67577200


Domestic Business
Tata Motors Ltd
4th Floor, Ahura Centre
82 Mahakali Caves Road
MIDC, Andheri East
Mumbai - 400093
Contact: 022 - 62407101

YOU MAY ALSO BE INTERESTED IN:Products Investors Markets Careers
ABOUT USDEALER APPLICATIONPassenger VehiclesCommercial VehiclesMEDIAMedia ContactDISTRIBUTOR APPLICATIONPRODUCTSMARKETSCSRINVESTORSCAREERSCONTACT US
twitter linkedin facebook youtube Instagram
© Copyright 2022 Tata Motors. All Rights Reserved.Legal Disclaimer Open Source License Disclosure
 
 Let’s bring joy and delight to the process of car buying together.
Customer support : support@carwale.com
New Car Dealer : ncd@carwale.com
Used Car Dealer : ucd@carwale.com
Enterprise Sales Inquiries : ES@carwale.com
Address:
12th Floor, Vishwaroop IT Park, S Pranavanandji Marg, Sector 30A, Vashi, Navi Mumbai, Maharashtra 400705
   Audio customer care number: +91)9555-602-502 ,Boult Audio customer care email: complaints@boultaudio.com OTHER QUERIES info@boultaudio.com  (+91)9555-602-502"""



#if __name__ == '__main__':
	#j = 1
	#y = re.split("\s",str)
	#for i in y:
	#	if re.findall("@",i) == ["@"]:
	#		with open("email.txt","a") as f:
	#			f.write(f"Email{j} : {i}\n")
			#	j +=1
			
	#with open("email.txt","r") as f:
	#	print(f.read())


#Other way to Extract email
if __name__ == '__main__':
	email = re.findall("[a-z0-9A-Z_.&%]+@[a-zA-Z0-9_&%]+[.][a-zA-Z]+",str)
	j = 1
	#for i in email:
		#with open("email.txt","a") as f:
			#f.write(f"Email {j} : {i}\n")
		#	j +=1
			
	with open("email.txt","r") as f:
		print(f.read())

