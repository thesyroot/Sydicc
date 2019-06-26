from time import time
from colorama import Fore, init

init();

tuplai = ['0','1','2','3','4','5','6','7','8','9'];	#&i 10
tuplac = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','ñ',
'Ñ','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z'];	#&c 54
tuplainde = ['0','1','2','3','4','5','6','7','8','9','a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i',
'I','j','J','k','K','l','L','m','M','n','N','ñ','Ñ','o','O','p','P','q','Q','r','R',
's','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z',' ','-','_','\\','/','(',')','=',
'&','%','$','#','\"','!',',','.',':',';','>','<','¿','?','|','|','°','¬','@',
'^','{','}','[',']','+','*','~','¡','\'','¨','´','`','ƒ',''];	#&n 106 +el''
tuplas = [' ','-','_','\\','/','(',')','=','&','%','$','#','\"','!',',','.',':',';','>','<','¿','?','|',
'|','°','¬','@','^','{','}','[',']','+','*','~','¡','\'','¨','´','`','ƒ'];	#&s 41

extension = "txt";
timel = -1;

print(Fore.GREEN+"""     ======================================================"""+Fore.RED+"""
	███████╗██╗   ██╗██████╗ ██╗ ██████╗ ██████╗
	██╔════╝╚██╗ ██╔╝██╔══██╗██║██╔════╝██╔════╝
	███████╗ ╚████╔╝ ██║  ██║██║██║     ██║     
	╚════██║  ╚██╔╝  ██║  ██║██║██║     ██║     
	███████║   ██║   ██████╔╝██║╚██████╗╚██████╗
	╚══════╝   ╚═╝   ╚═════╝ ╚═╝ ╚═════╝ ╚═════╝.syr
"""+Fore.GREEN+"""     ======================================================"""+Fore.WHITE);

netname=input("").strip(" ");
comand=input(" << ");

netn=(netname.replace("[","\"").replace("]","\"")).split("\"");
neta=netn[0].strip(" ").split("\'");
netname=neta[1].strip(" ");
netcom=neta[2].strip(" ").split("-");
for com in netcom:
	com=com.strip(" ");
	if(com!=""):
		if(com.find("x")!=-1):
			extension=com.lstrip("x ").strip(" ").strip(".");
		elif(com.find("x")==-1):
			timel=int(com.lstrip("t ").strip(" "));
			if(timel<0):
				timel=-1;
for i in range(0,len(netn)):
	if(i%2!=0):
		tuplax=[];
		tupladd=[];
		tuplal=[];
		netl=netn[i].strip(" ").split(";");
		for elem in netl:
			elem=elem.strip(" ");
			if(elem=="&c"):
				tuplainfo=elem;
			elif(elem=="&i"):
				tuplainfo=elem;
			elif(elem=="&s"):
				tuplainfo=elem;
			elif(elem=="&n"):
				tuplainfo=elem;
			elif(elem.find("- ")!=-1):
				elem=elem.strip("- ").strip(" ");
				tuplax.extend(elem.split(","));
			elif(elem.find("+ ")!=-1):
				elem=elem.strip("+ ").strip(" ");
				tupladd.extend(elem.split(","));
			elif(elem.find("<>")!=-1):
				tuplal.extend(elem.split("<>"));

		if(tuplainfo=="&c"):
			if(len(tuplax)!=0):
				for quit in tuplax:
					tuplac.remove(quit);

			if(len(tuplal)!=0):
				if(tuplal[0]=="start"):
					tuplal[0]=tuplac[0];
				if(tuplal[0]=="end"):
					tuplal[0]=tuplac[len(tuplac)-1];
				if(tuplal[1]=="start"):
					tuplal[1]=tuplac[0];
				if(tuplal[1]=="end"):
					tuplal[1]=tuplac[len(tuplac)-1];

				elem1=tuplac.index(tuplal[0]);
				elem2=tuplac.index(tuplal[1]);

				if(elem1>elem2):
					for i in range(0,elem2):
						tuplac.pop(0);
					for i in range(elem1,len(tuplac)-1):
						tuplac.pop();
				if(elem1<elem2):
					for i in range(0,elem1):
						tuplac.pop(0);
					for i in range(elem2,len(tuplac)-1):
						tuplac.pop();
				if(elem1==elem2):
					for i in range(0,elem1):
						tuplac.pop(0);
					for i in range(elem1,len(tuplac)-1):
						tuplac.pop();

			if(len(tupladd)!=0):
				tuplac.extend(tupladd);

		elif(tuplainfo=="&i"):
			if(len(tuplax)!=0):
				for quit in tuplax:
					tuplai.remove(quit);

			if(len(tuplal)!=0):
				if(tuplal[0]=="start"):
					tuplal[0]=tuplai[0];
				if(tuplal[0]=="end"):
					tuplal[0]=tuplai[len(tuplai)-1];
				if(tuplal[1]=="start"):
					tuplal[1]=tuplai[0];
				if(tuplal[1]=="end"):
					tuplal[1]=tuplai[len(tuplai)-1];

				elem1=tuplai.index(tuplal[0]);
				elem2=tuplai.index(tuplal[1]);

				if(elem1>elem2):
					for i in range(0,elem2):
						tuplai.pop(0);
					for i in range(elem1,len(tuplai)-1):
						tuplai.pop();
				if(elem1<elem2):
					for i in range(0,elem1):
						tuplai.pop(0);
					for i in range(elem2,len(tuplai)-1):
						tuplai.pop();
				if(elem1==elem2):
					for i in range(0,elem1):
						tuplai.pop(0);
					for i in range(elem1,len(tuplai)-1):
						tuplai.pop();

			if(len(tupladd)!=0):
				tuplai.extend(tupladd);

		elif(tuplainfo=="&s"):
			if(len(tuplax)!=0):
				for quit in tuplax:
					tuplas.remove(quit);

			if(len(tuplal)!=0):
				if(tuplal[0]=="start"):
					tuplal[0]=tuplas[0];
				if(tuplal[0]=="end"):
					tuplal[0]=tuplas[len(tuplas)-1];
				if(tuplal[1]=="start"):
					tuplal[1]=tuplas[0];
				if(tuplal[1]=="end"):
					tuplal[1]=tuplas[len(tuplas)-1];

				elem1=tuplas.index(tuplal[0]);
				elem2=tuplas.index(tuplal[1]);

				if(elem1>elem2):
					for i in range(0,elem2):
						tuplas.pop(0);
					for i in range(elem1,len(tuplas)-1):
						tuplas.pop();
				if(elem1<elem2):
					for i in range(0,elem1):
						tuplas.pop(0);
					for i in range(elem2,len(tuplas)-1):
						tuplas.pop();
				if(elem1==elem2):
					for i in range(0,elem1):
						tuplas.pop(0);
					for i in range(elem1,len(tuplas)-1):
						tuplas.pop();

			if(len(tupladd)!=0):
				tuplas.extend(tupladd);

		elif(tuplainfo=="&n"):
			if(len(tuplax)!=0):
				for quit in tuplax:
					tuplainde.remove(quit);

			if(len(tuplal)!=0):
				if(tuplal[0]=="start"):
					tuplal[0]=tuplainde[0];
				if(tuplal[0]=="end"):
					tuplal[0]=tuplainde[len(tuplainde)-1];
				if(tuplal[1]=="start"):
					tuplal[1]=tuplainde[0];
				if(tuplal[1]=="end"):
					tuplal[1]=tuplainde[len(tuplainde)-1];

				elem1=tuplainde.index(tuplal[0]);
				elem2=tuplainde.index(tuplal[1]);

				if(elem1>elem2):
					for i in range(0,elem2):
						tuplainde.pop(0);
					for i in range(elem1,len(tuplainde)-1):
						tuplainde.pop();
				if(elem1<elem2):
					for i in range(0,elem1):
						tuplainde.pop(0);
					for i in range(elem2,len(tuplainde)-1):
						tuplainde.pop();
				if(elem1==elem2):
					for i in range(0,elem1):
						tuplainde.pop(0);
					for i in range(elem1,len(tuplainde)-1):
						tuplainde.pop();

			if(len(tupladd)!=0):
				tuplainde.extend(tupladd);

tiempo_inicial= time();

def chc (comand):
	valores=[];

	try:
		if(timel!=-1):
			if(time()-tiempo_inicial<=timel):
				for letra in tuplac:
					auxc=list(comand.partition("&c"));
					auxc[1]=letra;
					line="".join(auxc);
					if(line.find("&c")!=-1):
						for elem in chc(line):
							valores.append(elem);
					elif(line.find("&i")!=-1):
						for elem in chi(line):
							valores.append(elem);
					elif(line.find("&n")!=-1):
						for elem in chn(line):
							valores.append(elem);
					elif(line.find("&s")!=-1):
						for elem in chs(line):
							valores.append(elem);
					else:
						valores.append(line);
		else:
			for letra in tuplac:
				auxc=list(comand.partition("&c"));
				auxc[1]=letra;
				line="".join(auxc);
				if(line.find("&c")!=-1):
					for elem in chc(line):
						valores.append(elem);
				elif(line.find("&i")!=-1):
					for elem in chi(line):
						valores.append(elem);
				elif(line.find("&n")!=-1):
					for elem in chn(line):
						valores.append(elem);
				elif(line.find("&s")!=-1):
					for elem in chs(line):
						valores.append(elem);
				else:
					valores.append(line);

		return valores;
	except KeyboardInterrupt:
		return valores;

def chi (comand):
	valores=[];

	try:
		if(timel!=-1):
			if(time()-tiempo_inicial<=timel):
				for letra in tuplai:
					auxc=list(comand.partition("&i"));
					auxc[1]=letra;
					line="".join(auxc);
					if(line.find("&c")!=-1):
						for elem in chc(line):
							valores.append(elem);
					elif(line.find("&i")!=-1):
						for elem in chi(line):
							valores.append(elem);
					elif(line.find("&n")!=-1):
						for elem in chn(line):
							valores.append(elem);
					elif(line.find("&s")!=-1):
						for elem in chs(line):
							valores.append(elem);
					else:
						valores.append(line);
		else:
			for letra in tuplai:
				auxc=list(comand.partition("&i"));
				auxc[1]=letra;
				line="".join(auxc);
				if(line.find("&c")!=-1):
					for elem in chc(line):
						valores.append(elem);
				elif(line.find("&i")!=-1):
					for elem in chi(line):
						valores.append(elem);
				elif(line.find("&n")!=-1):
					for elem in chn(line):
						valores.append(elem);
				elif(line.find("&s")!=-1):
					for elem in chs(line):
						valores.append(elem);
				else:
					valores.append(line);

		return valores;
	except KeyboardInterrupt:
		return valores;

def chn (comand):
	valores=[];

	try:
		if(timel!=-1):
			if(time()-tiempo_inicial<=timel):
				for letra in tuplainde:
					auxc=list(comand.partition("&n"));
					auxc[1]=letra;
					line="".join(auxc);
					if(line.find("&c")!=-1):
						for elem in chc(line):
							valores.append(elem);
					elif(line.find("&i")!=-1):
						for elem in chi(line):
							valores.append(elem);
					elif(line.find("&n")!=-1):
						for elem in chn(line):
							valores.append(elem);
					elif(line.find("&s")!=-1):
						for elem in chs(line):
							valores.append(elem);
					else:
						valores.append(line);
		else:
			for letra in tuplainde:
				auxc=list(comand.partition("&n"));
				auxc[1]=letra;
				line="".join(auxc);
				if(line.find("&c")!=-1):
					for elem in chc(line):
						valores.append(elem);
				elif(line.find("&i")!=-1):
					for elem in chi(line):
						valores.append(elem);
				elif(line.find("&n")!=-1):
					for elem in chn(line):
						valores.append(elem);
				elif(line.find("&s")!=-1):
					for elem in chs(line):
						valores.append(elem);
				else:
					valores.append(line);

		return valores;
	except KeyboardInterrupt:
		return valores;

def chs (comand):
	valores=[];

	try:
		if(timel!=-1):
			if(time()-tiempo_inicial<=timel):
				for letra in tuplas:
					auxc=list(comand.partition("&s"));
					auxc[1]=letra;
					line="".join(auxc);
					if(line.find("&c")!=-1):
						for elem in chc(line):
							valores.append(elem);
					elif(line.find("&i")!=-1):
						for elem in chi(line):
							valores.append(elem);
					elif(line.find("&n")!=-1):
						for elem in chn(line):
							valores.append(elem);
					elif(line.find("&s")!=-1):
						for elem in chs(line):
							valores.append(elem);
					else:
						valores.append(line);
		else:
			for letra in tuplas:
				auxc=list(comand.partition("&s"));
				auxc[1]=letra;
				line="".join(auxc);
				if(line.find("&c")!=-1):
					for elem in chc(line):
						valores.append(elem);
				elif(line.find("&i")!=-1):
					for elem in chi(line):
						valores.append(elem);
				elif(line.find("&n")!=-1):
					for elem in chn(line):
						valores.append(elem);
				elif(line.find("&s")!=-1):
					for elem in chs(line):
						valores.append(elem);
				else:
					valores.append(line);

		return valores;
	except KeyboardInterrupt:
		return valores;

if(comand.find("&c")!=-1 or comand.find("&n")!=-1 or comand.find("&i")!=-1 or comand.find("&s")!=-1):
	with open(netname.replace(" ","_").strip(" ")+"."+extension,"w+") as filepass:
		contaux=[];
		contaux.append(comand.find("&c"));
		contaux.append(comand.find("&i"));
		contaux.append(comand.find("&n"));
		contaux.append(comand.find("&s"));

		for i in range(0,len(contaux)):
			if(contaux[i]==-1):
				contaux[i]=max(contaux)+1;
		auxi = contaux.index(min(contaux));

		if(auxi==0):
			filepass.write("\n".join(chc(comand)));
		elif(auxi==1):
			filepass.write("\n".join(chi(comand)));
		elif(auxi==2):
			filepass.write("\n".join(chn(comand)));
		elif(auxi==3):
			filepass.write("\n".join(chs(comand)));

		print("\a");
else:
	print("No ha ingresado caracteres especiales\nSi quiere que cree el diccionario ingrese los caracteres \"&i\" \"&c\" \"&i\" \"&s\"");