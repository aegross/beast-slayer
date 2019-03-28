import time
import random

## variables
global havecrossbow
global havemedicine
global havesharpsword
global damage
global healthgone
havecrossbow = "false"
havemedicine = "false"
havesharpsword = "false"
damage = 0
healthgone = 0

## start game stuff
def startgame():
	time.sleep(1)
	displayIntro()
	time.sleep(4)
	displayInstructions()
	time.sleep(12)
	village_intro()

def displayIntro():
	print("")
	print("-------------------- Beast Slayer --------------------")
	print(" You are a scrap metal collector in a future far away.")
	print(" You search the vast desert for a metallic beast.     ")
	print(" Your goal is to kill it, but you do not know where   ")
	print(" it lies. You must find it, slay it, and claim its    ")
	print(" parts for money.                                     ")
	print("------------------------------------------------------")
	print("")
	print("       Now go, adventurer. The desert awaits...       ")
	print("")

def displayInstructions():
	print("------------------------------------------------------")
	print(" This game is an adventure where you choose the path.  ")
	print("")
	print(" You will be given various kinds of choices, and your ")
	print(" response will forward the story. When prompted with a")
	print(" choice, you will be given 2 or more options. You will")
	print(" type the response. They will ALWAYS be presented in  ")
	print(" lowercase only or as numbers. Respond in all lowercase")
	print(" letters or the respective number of your choice.     ")
	print("------------------------------------------------------")
	print("")

## play again function
def playagain():
	global havecrossbow
	global havemedicine
	global havesharpsword
	global damage
	global healthgone
	print("")
	user_input = input("Would you like to play again? ('yes' or 'no'): ")
	if user_input == "yes":
		for i in range(50):
			print("")
		havecrossbow = "false"
		havemedicine = "false"
		havesharpsword = "false"
		damage = 0
		healthgone = 0
		beastslayer()
	elif user_input == "no":
		quit()
	else:
		print("")
		print("Request not accepted. Remember, lowercase only.")
		playagain()

## Village to the South. The first area in the game
def village_intro():
	time.sleep(2)
	print("Your journey begins in the village south of the desert. You have already collected")
	print("your things, and are almost ready to set out. Before that, however, you have a few")
	print("options.")
	time.sleep(3)
	print("You can either explore the village one last time, or leave right away.")
	def village_intro_user():
		user_input = input("What would you like to do? ('explore' or 'leave'): ")
		if user_input == "explore":
			time.sleep(1)
			print("")
			print("You explore town one last time. You walk around, look through shops, and say")
			print("your goodbyes.")
			crossbowfind()
			oldladystory()
		elif user_input == "leave":
			time.sleep(1)
			print("")
			print("You decide not to look around again, and that you should just get going.")
			print("")
			oldladystory()
		else:
			print("")
			print("Request not accepted. Remember, lowercase only.")
			village_intro_user()
	village_intro_user()

def oldladystory():
	time.sleep(1)
	print("However, before you leave the village...")
	time.sleep(2)
	print("")
	print("An old woman walks up to you. She wears ripped clothes, and looks like her time is")
	print("growing short. She asks you a question.")
	time.sleep(3)
	print("Old Woman: Excuse me, young adventurer, would you care for a story?")
	time.sleep(1)
	def oldladyinput():
		user_input = input("Would you like to hear her story? ('yes' or 'no'): ")
		if user_input == "yes":
			time.sleep(1)
			print("")
			print("You nod, and the old woman starts her story.")
			time.sleep(1)
			print("Old Woman: A long time ago, in this desert, there lived large, fishlike creatures")
			print("	the size of cities. They existed long before the desert, and when the land became")
			print("	dry, they all died... they were known as leviathans. These great skeletons now exist")
			print("	all over the land, and have become home to smaller beasts. If you come across one")
			print("	during your travels, I would be careful... I wish you well.")
			print("")
			time.sleep(8)
			print("The old woman turns the corner. You follow her to thank her for the story, but she")
			print("has seemingly disappeared... ")
		elif user_input == "no":
			time.sleep(2)
			print("")
			print("You shake your head. The old woman walks away slowly.")
		else:
			print("")
			print("Request not accepted. Remember, lowercase only.")
			oldladyinput()
	oldladyinput()

def crossbowfind():
	global havecrossbow
	num = int(random.randint(1, 100))
	if num <= 50:
		time.sleep(2)
		print("")
		print("While searching the village, you happen to come across an abandoned shack you swear")
		print("you've never seen before. You take a step inside, and find nobody living there. In")
		print("the corner of the room, you spot something- a large crossbow and bolts. You figure ")
		print("nobody misses it, so you decide to take it.")
		time.sleep(5)
		print("--------------------------------------------------------------------------------------")
		print("You have obtained the crossbow! It will be helpful in your fight against the beast.")
		print("--------------------------------------------------------------------------------------")
		time.sleep(3)
		havecrossbow = "true"
		print("")
	else:
		print("")
		print("You did not find anything else of interest when searching the village.")
		print("")
		havecrossbow = "false"

## area 1: City
def city_enter():
	time.sleep(1)
	print("")
	print("You make your way to the city. All you know about it is that it was once a thriving trading")
	print("outpost, built up from the ground in a strange, mazelike structure. The framework is strange")
	print("and old, with buildings taller than 30 people.")
	time.sleep(3)
	print("")
	print("...")
	print("")
	time.sleep(2)
	print("Time passes. You finally see the city in the distance; the large buildings are old and decayed,")
	print("covered in dust and sand.")
	print("")
	time.sleep(2)
	print("When you enter, to your surprise, there seems to be nobody there. All you see are piles and")
	print("piles of human bones. Something attacked the outpost what looks like ages ago. There is almost")
	print("nothing of value left.")
	print("")
	time.sleep(4)
	print("However, you hear a crash. You go and investigate, and find a group of survivors! They glare at")
	print("you, and certainly don't look friendly. However, they are unarmed. ")
	print("You have a few options concerning your plan of action. You can either talk to the group, search")
	print("the city, or leave.")
	time.sleep(6)
	def city_user():
		user_input = input("What would you like to do? ('talk', 'search', or 'leave'): ")
		if user_input == "talk":
			time.sleep(1)
			print("")
			print("You decide to talk to the survivor group. What looks like their leader starts speaking.")
			time.sleep(1)
			print("???: Hello, traveler. Why are you here?")
			print("You explain that you are a scrap metal collector trying to find and kill the metal beast.")
			time.sleep(3)
			print("???: YOU SEARCH FOR THE BEAST? That monster destroyed the whole outpost twenty years ago. Lad, it")
			print("	should not be done. You should live your life while you can. We could only leave the city twice")
			print("	to bury our dead. They lie in a graveyard to the north. All of the rest are but mere bones here.")
			time.sleep(6)
			print("You thank him for the caution and head out of the city.")
			time.sleep(2)
			print("(If you go to the graveyard, maybe you will find something of use...)")
			print("")
			leftanylocation()
		elif user_input == "search":
			time.sleep(1)
			print("You leave the survivor group and search the city. All of the food or materials have been looted long")
			print("ago, and you find nothing except some pieces of scrap metal. You take these with you for some extra")
			print("cash.")
			time.sleep(4)
			leftanylocation()
		elif user_input == "leave":
			leftanylocation()
		else:
			print("")
			print("Request not accepted. Remember, lowercase only.")
			city_user()
	city_user()

## area 2: Temple
def temple_enter():
	global havemedicine
	time.sleep(1)
	print("")
	print("You decide to go to the temple. It is relatively close to the edge of the desert, and is often")
	print("traveled to by those seeking some form of aid. While you were in the village, you heard rumors")
	print("about the temple being taken over by bandits. ")
	print("")
	time.sleep(4)
	print("You make it to the temple. There are large stained glass murals of various figures and creatures.")
	print("You don't see any immediate sign of bandits, but you figure that there is still a good level of ")
	print("danger, and you stay on your feet. Upon entering, you find a chapel in front of you and some dark")
	print("hallways to your sides.")
	print("")
	time.sleep(5)
	print("You can either search the temple, pray for your journey, or leave.")
	time.sleep(1)
	def temple_user():
		user_input = input("What would you like to do? ('search', 'pray', or 'leave'): ")
		if user_input == "search":
			print("")
			time.sleep(1)
			print("You decide to search the temple. You head down one of the two hallways.")
			end_bad_templesearch()
		elif user_input == "pray":
			if havemedicine == "true":
				print("")
				time.sleep(1)
				print("???: Hah, you really want to try that? I'm one step ahead of you, buddy.")
				print("You turn around in shock to find a bandit behind you, with a knife to your throat. You")
				print("probably shouldn't have come back to steal more things, you know.")
				time.sleep(4)
				print("")
				print("...")
				print("")
				time.sleep(1)
				playagain()
			else:
				time.sleep(1)
				print("")
				print("You decide that a prayer couldn't hurt. Normally you're not one to believe in these things, but it's")
				print("worth a shot.")
				time.sleep(2)
				medicinefind()
				time.sleep(1)
				leftanylocation()
		elif user_input == "leave":
			time.sleep(1)
			leftanylocation()
		else:
			print("")
			print("Request not accepted. Remember, lowercase only.")
	temple_user()

def medicinefind():
	global havemedicine
	print("")
	time.sleep(1)
	print("You get down on your knees and prey. You hear a soft click in front of you. You look up, alarmed, but")
	print("only find that a small door has opened in front of you. You reach in, and pull out a small bottle. Upon")
	print("close inspection, you see that it is medicine! It's a potent kind that normally only rich people own. ")
	print("")
	time.sleep(4)
	print("You suspect that you have found something the bandits have hidden, and worry about getting caught. You")
	print("leave the building right away.")
	time.sleep(3)
	print("-----------------------------------------------------------------------------------")
	print("You have obtained the medicine! It will be helpful in your fight against the beast.")
	print("-----------------------------------------------------------------------------------")
	havemedicine = "true"

## area 3: Graveyard
def graveyard_enter():
	print("")
	time.sleep(1)
	print("You decide to find and search the graveyard. You know that the beast you are trying to hunt has slain")
	print("many, and a good amount of those slain whose bodies were recovered are probably buried there. You think")
	print("that you may find a clue of some kind.")
	print("")
	time.sleep(5)
	print("You reach the graveyard. Like the people buried there, the atmosphere is dead. What were once lively")
	print("flowers, plants, and trees are all dead; mere shadows of their former selves. You look around the")
	print("hundreds of tombstones, searching for a hint or clue at the beast's location. You stumble upon a small")
	print("headstone with an epitaph that reads:")
	print("                       'Dedicated to my son, who died whilst fighting a monster'                       ")
	print(" 'That wretched thing has taken you away from me. If I could muster the strength, I would walk straight ")
	print("  into its home, its den of lies, and kill it. Sadly I cannot do that, and I must now return to the ")
	print("  village. I am too weak. I will dedicate my life to telling those like you to be weary of the beast,")
	print("  of the great skeletons where your spirit lies.'")
	time.sleep(17)
	print("")
	print("...")
	print("")
	time.sleep(2)
	print("With this newfound information, you decide that there is not much else you can do here. You can either")
	print("pay your respects to the dead, or leave without doing so.")
	time.sleep(2)
	def graveyard_user():
		user_input = input("Would you like to pay your respects or leave? ('respect' or 'leave')")
		if user_input == "respect":
			time.sleep(1)
			print("")
			print("You decide that you should pay your respects to all of those buried here. You have no conventional")
			print("gifts, so you take a small piece of your rations and leave it at the entrance. Just then, you feel")
			print("a warm gust of wind. It brings your spirits up, and you set out in a good mood.")
			time.sleep(6)
			leftanylocation()
		elif user_input == "leave":
			time.sleep(1)
			end_bad_graveyardleave()
		elif user_input == "f":
			time.sleep(1)
			print("")
			print("Haha, very funny. The spirits are pleased with your, uh, strange gesture of respect?")
			print("To be honest, they don't really know what you mean...")
			time.sleep(4)
			leftanylocation()
		elif user_input == "F":
			time.sleep(1)
			print("")
			print("Haha, very funny. The spirits are pleased with your, uh, strange gesture of respect?")
			print("To be honest, they don't really know what you mean...")
			time.sleep(4)
			leftanylocation()
		else:
			print("")
			print("Request not accepted. Remember, lowercase only.")
			graveyard_user()
	graveyard_user()

## area 4: Ruins
def ruins_enter():
	global havesharpsword
	print("")
	time.sleep(1)
	print("")
	print("You decide to head for the ruins. They are from an unknown civilization long ago, and were destroyed when that")
	print("civilization ceased to exist. Of what you've heard, it is home to many strange artifacts. It was a hotspot for")
	print("scrap collectors like you when it was first discovered; there were lots of devices with rare metals making up")
	print("their framework. However, nobody of your time knows how they work.")
	print("")
	time.sleep(6)
	print("You reach the ruins, which are a decrepit sight of crumbled buildings and other various structures. The only one ")
	print("left completely standing has old walls, colored with yellow and red. There is a broken sign with what looks like ")
	print("an 'm' on it. How mysterious.")
	print("")
	time.sleep(5)
	print("You decide that you could take a look around to see if there is anything left from other collectors. You figure")
	print("that it has been completely picked clean, but you can give it a shot if you want. You could also wander around,")
	print("marvelling at the old buildings.")
	time.sleep(5)
	def ruins_user():
		user_input = input("What would you like to do? ('forage', 'wander', or 'leave'): ")
		if user_input == "forage":
			time.sleep(1)
			num = int(random.randint(1, 100))
			if num <= 25:
				end_bad_ruinforage()
			else:
				if havesharpsword == "true":
					time.sleep(1)
					print("You have already been to the stall and sharpened your sword. you cannot do it again.")
					leftanylocation()
				else:
					time.sleep(1)
					findsharpen()
					time.sleep(2)
					leftanylocation()
		elif user_input == "wander":
			time.sleep(1)
			print("")
			print("You decide not to waste your time foraging, and wander around. You take a look inside of the building")
			print("with the 'm' sign. You see chairs, an open counter, and broken panes of glass above it. The whole")
			print("place is covered in dust. You investigate the counter, and behind it, you found a small red box. It")
			print("smiles at you. Creepy.")
			time.sleep(6)
			print("You leave right away. The image doesn't vanish from your mind for a while...")
			time.sleep(2)
			leftanylocation()
		elif user_input == "leave":
			time.sleep(1)
			leftanylocation()
		else:
			print("")
			print("Request not accepted. Remember, lowercase only.")
			ruins_user()
	ruins_user()

def findsharpen():
	global havesharpsword
	print("")
	time.sleep(1)
	print("While foraging in the ruins, you spot a small building in the distance. It looks like a little shop, but")
	print("there is only one thing in the stall, though; a box. Inside is a sharpening stone! You decide to use this")
	print("on your sword, which should make it stronger.")
	time.sleep(4)
	print("")
	print("------------------------------------------------------------------------------------")
	print("You have sharpened your sword! That will be helpful in your fight against the beast.")
	print("------------------------------------------------------------------------------------")
	time.sleep(1)
	havesharpsword = "true"

## area 5: Oasis
def oasis_enter():
	print("")
	time.sleep(1)
	print("You decide to try and find the oasis that you have heard rumors of. Those rumors describe a sizeable patch of")
	print("grass, complete with a pool of water and trees. It would be a great stop on your journey if you were able to")
	print("find it.")
	time.sleep(4)
	print("...")
	time.sleep(1)
	print("...")
	time.sleep(2)
	print("...")
	time.sleep(3)
	print("After a while of searching, you see something glimmering in the distance. You see water and grass. You have found the")
	print("oasis! You add it to your map, to hopefully help guide adventurers in the future.")
	print("You walk for a little longer and reach the grass. It feels soft beneath you, and you lie down. You sleep for a while.")
	time.sleep(6)
	print("When you wake up, you can either eat some of the oasis' fruit, drink some water from the pond, or leave.")
	time.sleep(1)
	def oasis_user():
		user_input = input("What are you going to do? ('eat', 'drink', or 'leave'): ")
		if user_input == "eat":
			time.sleep(1)
			end_bad_oasiseat()
		elif user_input == "drink":
			print("")
			time.sleep(1)
			print("You decide to leave the fruit, as you have heard stories of curses that trap you when you eat the food")
			print("grown in places like this. You take a drink, then fill up your water pouch. You feel refreshed after")
			print("your drink and decide to head on your way.")
			time.sleep(5)
			leftanylocation()
		elif user_input == "leave":
			time.sleep(1)
			leftanylocation()
		else:
			print("")
			print("Request not accepted. Remember, lowercase only.")
			oasis_user()
	oasis_user()

## area 6: Cavern
def cavern_enter():
	print("")
	time.sleep(1)
	print("You decide to try and locate the cavern, thinking that may be the home of the beast.")
	print("You search and search and search some more, but you never find it. You find yourself dizzy and")
	print("your sight is blurred. You are hungry and tired, but you have run out of rations. You have died")
	print("of exposure out in the desert. Your body is covered by sand and never found.")
	print("")
	time.sleep(8)
	print(" (The cavern does not exist. This is not a luck based event; I wouldn't recommend choosing this again.) ")
	print("THE END")
	time.sleep(2)
	playagain()

## area 7: Skeleton
def skeleton_enter():
	print("")
	time.sleep(1)
	print("You decide to search for the great skeleton. You end up searching the desert for a long time,")
	print("unsure if you will ever find it. When you are soon about to give up hope, you see it in the ")
	print("distance.")
	print("")
	time.sleep(3)
	print("A large fishlike skeleton lays before you. It's so big that a whole settlement of people could")
	print("make it their home. Astonished by the pure size of it, you make your way towards it. The ground")
	print("rumbles.")
	print("")
	time.sleep(3)
	print("When you get there, you hear a strange noise, which almost sounds like the ticking of a clock. You")
	print("know that you have reached your destination; THE BEAST IS HERE.")
	print("Now, all you need to do is find it. There are three main sections of the skeleton, and it could")
	print("be in any of them. You can search the head, the body, or the tail.")
	print("")
	time.sleep(7)
	print("----------------------------------------------------------------------------------------------------")
	print("This is the final location before the boss fight. If you are not content with your equipment,")
	print("this is the final time to turn back. The choices work a bit differently here; you can keep selecting")
	print("locations UNTIL you find the beast, OR you can leave. You won't leave automatically.)")
	print("----------------------------------------------------------------------------------------------------")
	print("")
	time.sleep(5)
	def skeleton_user():
		user_input = input("Choose where you would like to search. ('head', 'body', 'tail', or 'leave'): ")
		if user_input == "head":
			print("")
			time.sleep(1)
			print("You have chosen to search the skull of the skeleton. It takes you a while to walk over, but")
			print("you marvel at the size of it. You wonder how something this large was able to live...")
			print("")
			time.sleep(3)
			print("Suddenly, you hear a thud behind you. You turn around to find the beast staring at you, bearing")
			print("its fangs. It lets out a garbled mechanical roar and charges towards you.")
			print("")
			time.sleep(3)
			print("YOUR FIGHT WITH THE BEAST BEGINS!")
			beastfight()
		elif user_input == "body":
			print("")
			time.sleep(1)
			print("You have chosen to search the body of the skeleton. You stay on your feet, weary of danger. However,")
			print("you don't find the beast. All you find are piles of bones; human and animal. The beast is an enemy of")
			print("all, leaving none alive.")
			time.sleep(5)
			print("")
			skeleton_user()
		elif user_input == "tail":
			print("")
			time.sleep(1)
			print("You have chosen to search the tail of the skeleton. You look around, finding nothing but metal")
			print("springs and broken sheets. You suspect that this may be some of the beast's parts, and you pocket")
			print("what you can carry without being too weighed down.")
			time.sleep(5)
			print("")
			skeleton_user()
		elif user_input == "leave":
			time.sleep(1)
			leftanylocation()
		else:
			print("")
			print("Request not accepted. Remember, lowercase only.")
			skeleton_user()
	skeleton_user()

#### subsection of area 7: beast fight
def beastfight():
	print("")
	time.sleep(1)
	print("-------------------------------------------------------------------------------------------------")
	print("This fight is a turn based battle. You will chose to either attack or dodge, which will determine")
	print("the damage you do and how much damage you take. The amount of damage that you and the beast do to")
	print("each other is set in a specific range, but luck based. ")
	print("-------------------------------------------------------------------------------------------------")
	time.sleep(7)
	if havecrossbow == "true":
		print("   (You have the crossbow. You will do 10 extra damage every attack turn, and 5 extra damage every")
		print("    dodge turn (unless your ATTACK misses)")
		time.sleep(5)
	else:
		print("   (You do not have the crossbow. If you had it, it would help you here.)")
		time.sleep(2)
	if havemedicine == "true":
		print("   (You have the medicine. If your health falls below 10, it will be restored to 50.")
		time.sleep(5)
	else:
		print("   (You do not have the medicine. If you had it, it would help you here.)")
		time.sleep(2)
	if havesharpsword == "true":
		print("   (You have the sharpened sword. You will do 120% damage of what you attack, but ONLY if you are ")
		print("    attacking. The bonus of the crossbow is not affected by this.)")
		time.sleep(5)
	else:
		print("   (You do not have the sharpened sword. If you had it, it would help you here.)")
		time.sleep(2)
	global playerhealth
	global beasthealth
	playerhealth = 75.0
	beasthealth = 150.0
	while playerhealth>=0.0000000000000001 and beasthealth>=0.0000000000000001:
		time.sleep(1)
		print("Your health: ",playerhealth)
		print("Enemy health: ",beasthealth)
		time.sleep(2)
		def battleinput():
			user_input = input("Are you going to attack or dodge? ('attack' or 'dodge'): ")
			if user_input == "attack":
				time.sleep(1)
				attack()
				time.sleep(2)
				medicinerecovery()
				time.sleep(1)
			elif user_input == "dodge":
				time.sleep(1)
				dodge()
				time.sleep(2)
				medicinerecovery()
				time.sleep(1)
			else:
				print("")
				print("Request not accepted. Remember, lowercase only.")
				battleinput()
		battleinput()
	if playerhealth <= 0:
		time.sleep(1)
		end_bad_beast()
	elif beasthealth <=0:
		time.sleep(1)
		end_good()
	elif playerhealth <= 0 and beasthealth <=0:
		time.sleep(1)
		end_good()
	else:
		print("Uhh... you broke it. You broke the game. That isn't good. This has a REALLY low chance of happening...")
		end_bad_beastinput()

def attack():
	global playerhealth
	global beasthealth
	num = int(random.randint(1, 100))
	if num <= 85:
		damage = int(random.randint(15.0, 20.0))
		if havecrossbow == "false" and havesharpsword == "false":
			print("")
			print("You do",damage,"damage to the beast!")
			time.sleep(1)
			beasthealth = beasthealth - damage
		elif havecrossbow == "true" and havesharpsword == "false":
			print("")
			print("You do",damage,"damage to the beast, plus an extra 10 damage!")
			time.sleep(2)
			beasthealth = beasthealth - (damage+10.0)
		elif havecrossbow == "false" and havesharpsword == "true":
			print("")
			print("You do",damage,"damage to the beast, multiplied by 120%!")
			time.sleep(2)
			beasthealth = beasthealth - (damage+(damage/5.0))
		else:
			print("")
			print("You do",damage,"damage to the beast, multiplied by 120%, plus an extra 10 damage!")
			time.sleep(2)
			beasthealth = beasthealth -(damage+(damage/5.0)+10.0)
	else:
		print("")
		time.sleep(1)
		print("You try to attack the beast, but you miss! (no damage done.)")
	num = int(random.randint(1, 100))
	if num <= 75:
		healthgone = int(random.randint(15.0, 25.0))
		playerhealth = playerhealth - healthgone
		print("")
		print("The beast hits you, and takes away",healthgone,"hitpoints from your health.")
		time.sleep(2)
	else:
		print("")
		print("The beast tries to attack you, but misses! (no damage received.)")
		time.sleep(2)

def dodge():
	global playerhealth
	global beasthealth
	num = int(random.randint(1, 100))
	if havecrossbow == "true":
		print("")
		print("You do an extra 5 damage while dodging!")
		time.sleep(1)
		beasthealth = beasthealth - 5.0
	else:
		print("")
		print("You do no damage while dodging.")
		time.sleep(1)
	if num <= 20:
		healthgone = int(random.randint(15.0, 25.0))
		playerhealth = playerhealth - healthgone
		print("")
		print("The beast somehow manages to hit you, and takes away",healthgone,"from your health.")
		time.sleep(2)
	else:
		print("The beast tries to attack you, but misses! (no damage received.)")
		time.sleep(2)

def medicinerecovery():
	global playerhealth
	global havemedicine
	if havemedicine=="true" and playerhealth<=10:
		print("")
		playerhealth = 50
		print("You are low on health, but you are lucky; you have the medicine! Your health is")
		print("restored to",playerhealth,"!")
		time.sleep(4)
		havemedicine = "false"
	elif havemedicine=="true" and playerhealth>=10:
		print("(you do not need to heal yet.)")
		time.sleep(1)
	elif havemedicine=="false" and playerhealth>=10:
		time.sleep(1)
	else:
		print("You are low on health, but do not have the medicine/already used it. You cannot heal.")
		time.sleep(3)

## list of areas
def selectlocation():
	user_input = input("Where would you like to go? (input a number [1-7] that correlates to your choice.): ")
	if user_input == "1":
		print("")
		time.sleep(1)
		print("You have chosen: The City to the west of the village")
		city_enter()
	elif user_input == "2":
		print("")
		time.sleep(1)
		print("You have chosen: The Temple to the north of the village")
		temple_enter()
	elif user_input == "3":
		print("")
		time.sleep(1)
		print("You have chosen: The Graveyard to the northwest of the village")
		graveyard_enter()
	elif user_input == "4":
		print("")
		time.sleep(1)
		print("You have chosen: The Ruins to the east of the village")
		ruins_enter()
	elif user_input == "5":
		print("")
		time.sleep(1)
		print("You have chosen: The Oasis, location unknown")
		oasis_enter()
	elif user_input == "6":
		print("")
		time.sleep(1)
		print("You have chosen: The Cavern, location unknown")
		cavern_enter()
	elif user_input == "7":
		print("")
		time.sleep(1)
		print("You have chosen: The Skeleton, location unknown")
		skeleton_enter()
	else:
		print("")
		print("Request not accepted. Please choose a number 1-7.")
		selectlocation()

def leftvillagesouth():
	print("")
	time.sleep(1)
	print("You have finally set out of the village, and are now going to search the desert. You have a")
	print("map of the desert, which shows these locations: ")
	time.sleep(3)
	print("1. City to the west")
	time.sleep(1)
	print("2. Temple to the north")
	time.sleep(1)
	print("3. Graveyard to the northwest")
	time.sleep(1)
	print("4. Ruins to the east")
	time.sleep(1)
	print("There are also some places in the desert that aren't on your map that you have only heard rumors")
	print("of, and may or may not exist...")
	time.sleep(3)
	print("5. Oasis")
	time.sleep(1)
	print("6. Cavern")
	time.sleep(1)
	print("7. Skeleton")
	time.sleep(1)
	print("")
	selectlocation()

def leftanylocation():
	print("")
	time.sleep(1)
	print("After leaving, you open up your map and look at the places you can go. You could also")
	print("return to where you just were, if you'd like. You cannot return to the village to the")
	print("south.")
	time.sleep(3)
	print("")
	print("1. City")
	print("2. Temple")
	print("3. Graveyard")
	print("4. Ruins")
	print("5. Oasis")
	print("6. Cavern")
	print("7. Skeleton")
	print("")
	time.sleep(1)
	selectlocation()

## endings
def end_good():
	print("")
	time.sleep(1)
	print("You have sucessfully slain the beast! You gather its parts and head back to the village")
	print("south of the desert. You are praised, and after selling the beast's parts, you are set")
	print("for the rest of your life. ")
	time.sleep(5)
	print("THE END")
	playagain()

def end_bad_beast():
	global havecrossbow
	global havemedicine
	global havesharpsword
	global damage
	global healthgone
	print("")
	time.sleep(1)
	print("While fighting the beast, you are having trouble keeping up with its movements. It strikes")
	print("you again and again, and you eventually cannot move. It deals the final blow and roars in")
	print("fury.")
	time.sleep(4)
	print("THE END")
	time.sleep(1)
	print("You can either start over from the beginning of the game, or you can start from the boss fight.")
	time.sleep(1)
	def end_bad_beastinput():
		print("")
		user_input = input("Would you like to start from the boss fight, start over entirely, or quit? ('fight', 'startover', or 'quit'): ")
		if user_input == "startover":
			for i in range(50):
				print("")
			havecrossbow = "false"
			havemedicine = "false"
			havesharpsword = "false"
			damage = 0
			healthgone = 0
			beastslayer()
		elif user_input == "quit":
			quit()
		elif user_input == "fight":
			time.sleep(1)
			beastfight()
		else:
			print("")
			print("Request not accepted. Remember, lowercase only.")
			end_bad_beastinput()
	end_bad_beastinput()


def end_bad_templesearch():
	print("")
	time.sleep(1)
	print("While searching the temple, you forget to check for traps. You hear a soft click to your")
	print("side, and once you turn around, you are doused in oil. Another click sounds, and soon")
	print("enough, you are up in flames.")
	time.sleep(3)
	print("...")
	time.sleep(2)
	print("A little while later, bandits come across your body. They laugh at the success of their")
	print("traps and take your things.")
	time.sleep(2)
	print("THE END")
	playagain()

def end_bad_graveyardleave():
	print("")
	time.sleep(1)
	print("You decide that paying your respects is a waste of time, and leave the Graveyard. However,")
	print("before you are able to leave, a chill wind blows, and the entrance gate slams in front of ")
	print("you. Your thoughts and disrespect have angered the spirits inhabiting the Graveyard! They")
	print("swarm around you, causing you to get colder and colder. Eventually, you cannot move- you are")
	print("frozen in place. You die shortly afterward, and your spirit wanders endlessly...")
	time.sleep(10)
	print("THE END")
	playagain()

def end_bad_oasiseat():
	print("")
	time.sleep(1)
	print("You decide that you are hungry, and choose to pick some fruit off of the various fruit trees.")
	print("After taking your spoils, you sit down next to the water and start to eat. Time flies, and you")
	print("never become full. You've been roped into a vicious curse, where the fruit you eat never fills")
	print("your stomach. However, you cannot stop eating. You keep picking fruit and eating until you die")
	print("of thirst, even though the water was so close by...")
	time.sleep(10)
	print("THE END")
	playagain()

def end_bad_ruinforage():
	print("")
	time.sleep(1)
	print("While foraging for materials in the ruins, you spot something shimmering in the distance. You")
	print("start to walk over to it, but while doing so, you trip over some rubble and fall. The ground")
	print("below you falls out and reveals a deep hidden pit with spikes at the bottom. At this point,")
	print("it is too late to stop yourself...")
	time.sleep(8)
	print("THE END")
	playagain()

## rungame function
def beastslayer():
	startgame()
	leftvillagesouth()

## rungame
beastslayer()
