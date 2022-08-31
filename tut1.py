first_name="Bro"
last_name="zone"
full_name=first_name +" "+ last_name
print(full_name);
age=12
age=age+1
print(age)
numb=35.56
print("Number : ")
print(float("25"));
print(int("34"));
print(bool("0"));

#Length of String...
print(len("Bro Code"));

#finding character position..
print(("Bro Code").find("C"));

#capitalizing the first Letter of Word...
print(("bro code").capitalize());

#capitalizing the whole word...
print(("bro code").upper());

#lowering the elements..
print(("bro CODe").lower());

#see wether the value is digit or not..
print(("Bro Code").isdigit());

#check wether string contains Alphabet nor not(no whitespace)..
print(("BroCode").isalpha());

#count how many times o is repeated or nt
print("brooopo".count("o"));

#replace o with a...
print("Bros".replace("o","a"));

#print words as your choice times...
print("Bros "*3);

#string.format -> {} used in printing...
name="zee"
last_name="fee"
print("This word {} stands for {}".format(name, last_name))

#string format with position...
print("This word {1} stands for {0}".format(name,last_name))

#string format with variable space...
print("This word{:^10} stands for {}".format(name,last_name))

#formatting number...
print("this number is : {:.2f}".format(25.5678)) #present number after dot