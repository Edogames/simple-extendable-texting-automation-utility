import os
import sys
import time
import datetime
import webbrowser
import random
from filecmp import clear_cache
from termcolor import cprint, colored

def clear():
	return os.system('cls' if os.name == 'nt' else 'clear')

class Choices:
	def __init__(self, choices):
		self.choices = choices

	def display_choices(self):
		newTxt = ""
		num = 0

		for i in self.choices:
			num += 1

			newTxt += f"{colored(num, 'white')} - {colored(i, 'red')} "

			newTxt += '\n'
		
		newTxt += '\n'
		newTxt += f"{colored(num + 1, 'white')} - {colored('bored/break time?', 'cyan')} "
		newTxt += f"{colored(num + 2, 'white')} - {colored('manual', 'cyan')} "
		newTxt += f"{colored(num + 3, 'white')} - {colored('credits', 'cyan')} "
		newTxt += f"{colored(num + 4, 'white')} - {colored('exit program', 'cyan')} "
		return colored(newTxt, 'red')

class Answers:
	def __init__(self, answers):
		self.answers = answers

	def get_answer(self, index):
		if isinstance(self.answers[index - 1], str) or len(self.answers[index - 1]) == 1:
			return f"{self.answers[index - 1][0]}\n"
		else:
			if len(self.answers[index - 1]) != 1:
				num = 0
				for i in self.answers[index - 1]:
					if num < len(self.answers[index - 1]) - 1:
						num += 1
						print(f"{num}. {i}")
						print()
				return f"{num + 1}. {i}\n"

# choose "bored/brake time?" option, and magic will hapen :3
# also you can insert here browser game links, to play if you are bored, or it's a brake time
browser = [
	['game', 'https://flappybird.io/'],
	['game', 'https://www.playretrogames.com'],
	['game', 'https://surviv.io/'],
	['game', 'http://slither.io/'],
	['meme', 'https://www.reddit.com/r/memes/'],
	['meme', 'https://www.memedroid.com/memes/top/week'],
]
# add your choice options below
choices = Choices([
	"How to not get blocked on facebook",
	"How to not get blocked on instagram",
	"Manual for instagram",
	"Start conversation",
	"Tell client about us",
	"Give a sample video link",
	"Give a sample e-card link",
	"Get Page link",
	"Suggestions",
	"Questions",
	"Example facebook page",
])
# add your answers below
answers = Answers([
	[
		"""
You should clear Facebook's out process

Facebook often runs a clear-out process to remove any suspicious
or duplicate or fake accounts from the platform. So, in case your
Facebook finds your account in this entire process, possibly your
account might get locked.
		""",
		"""
Performing illegal activity

Facebook ensures promotional content until it is surrounded by any
legal limitations. However, performing any sort of legal activity
on Facebook on both personal and professional front makes you entitled
to punishment, and that could result in locking or disabling of
Facebook Account.
		""",
		"""
Avoiding Facebook warnings

While performing any activity on Facebook which appears to be illegitimate,
you might receive a specific notice or a kind of warning from the FB Team.
However, neglecting the warning and repetition of any restricted activity
might increase the chances of a locked Facebook account.
		""",
		"""
Adding an excessive number of friends

Facebook already has Pre-Set limitations for accepting or sending any
friend requests. Now, in case you are sending or accepting more than 20
friend requests just in a day, you will surely be identified as a spammer or robot.
Maybe this could be one possible reason behind the locking of your Facebook account.
		"""
	],
	[
		"""
Don't mass follow and like

By trying to grow a notable number of likes and followers at one time,
you will receive a temporary block from Instagram. The reason for this
would be because they considered the limits on follows and likes.
A maximum number of likes per hour is 60.

A maximum number of follows per hour is 60.

A maximum number of messages per hour is 60.

But if your account is just new, the limits are different:

A maximum number of likes per hour is 30

A maximum number of comments per hour is 30

A maximum number of follow/unfollow per hour is 30.

Violating Instagram rules causes a temporary block. It involves limiting
the profile's function; You can't comment, like, follow or write in Direct Messages
for some time (from 2 hours to 2 weeks). If you are lucky to get blocked temporarily,
don't do anything with your profile, Just give it a little rest before
it is completely restored.
		""",
		"""
Don't share Images/Videos Violating Social Network Rules

Photos and videos with naked bodies, sexual content, and violence are considered unsuitable.
Whatever your goals are, posting such inappropriate content can get you banned, so be careful.
		""",
		"""
User complaint

Someone might find your account a threat, so they click the Report button.
If other people report your account too, Instagram will sooner or later block your profile.
People would complain of different reasons such as mass liking, mass following, abuses,
inappropriate content, spam, etc.
		""",
		"""
Complete your Instagram Profile

Add a little bio in your profile. Also, make sure you have a real profile picture.
This brings validity to your profile.
		""",
		"""
Post Regularly

You must post pictures on Instagram and remember that posting regularly is what that matters.
An active display of social profile can mainly save you from getting blocked.
		""",
		"""
Copyright Infringement

Copyright is a serious issue on Instagram. All pictures in your account have to be
either yours or permitted by the owner. If you want to share someone else's picture,
tag him/her in the photo (provided he/she has an Instagram account).
If you use pictures for a commercial purpose, you have to ask the owner's permission too.
Additionally, if you post a video with music which you don't have the rights,
Instagram will certainly remove it.

If you ignore the copyright rules, the author can report you to Instagram for using the photo
without their permission, and you would be blocked for copyright infringement.
		""",
		"""
The different IP address and device

If you log into your account from various devices and approve it via SMS,
Instagram is less likely to ban you. Though, if you log in with different devices and
IP-addresses, Instagram may think scammers hacked your account.
The social network responds to it instantly and blocks the profile for your own safety.
		""",
		"""
Perform reasonable actions

Keep your follow/unfollow activities balanced. Bulk actions might seem aggressive,
which may deactivate your account, and even worse, that you might get temporarily blocked.

In some cases, all you should do is giving some rest to your account.
Try to log in after some time such as 24 hours. It would help you to return your account.
		""",
		"""
Verify your email

This is an easy but highly crucial way to avoid getting blocked or banned.
When you verify your email, you prove that you are a real person.
		""",
		"""
Do not comment too many emojis

For some reason, Instagram doesn't like it when you comment emojis excessively.
Limit yourself to leave fewer emojis per comment.
		""",
		"""
Do not copy your comments over and over

Instagram keeps an extra eye on repeated comments.
The reason is that Instagram may consider you a bot.
		""",
		"""
Do not spam-comment

As I mentioned commenting is Instagram's biggest problem
when it is about spam on the platform. While spam-liking is used as a way
to get more attention to the accounts, it isn't harmful to anyone.
However, Instagram is pretty strict with how many comments you leave on posts
in a short time.
		""",
		"""
Do not spam-like posts

Liking a large number of posts on short time is known as a spammy action.
But when you start liking excessively, it is a sign to Instagram that you're acting spammy.
		"""
	],
	[
		"""
If you are new to Instagram, before you start following other profiles, make sure you post for yourself. Generally, a good start includes posting pictures regularly.

What should you do for not looking spammy?

· Avoid editing your captions after posting a photo.

· Don't put hashtags in your comments, put them in the caption.

· Don't post too many posts every day (up to 3).

How to tell if you are banned on Instagram?

If you face the following image, consider your account to be banned.

You will also know when you're not able to perform certain actions such as uploading
a photo, like, follow or comment.

Is it possible to get banned on Instagram permanently?

It depends on your activities after the temporary ban. If you keep mass following,
spamming and unfollow, and continue to post too many random comments on photos,
you may end up getting a permanent ban on your Instagram account.

How to recover Instagram's temporary ban?

1. Report to Instagram

You can report your problem to the administration by clicking the “Tell Us” or “Report” option.

2. Stop for two days and then try on the third day

You should end all actions for at least two days. It means no liking, commenting,
following or unfollowing. But of course, you can continue browsing on Instagram.

On the 3rd day, you can continue your normal activities and remember to avoid anything
that would make you look like a bot. You should like and comment only a couple
of photos every day.

3. Link Instagram with other social networks

It would help you to link your Instagram account with your other social media account.
You would seem more legit if you link your Instagram to other social media.

For linking Instagram with other social networks, do the following:

1. Go to Settings

2. Go into Privacy and Security > Linked accounts.

3.Link as many social networks as possible.

4. Edit your Bio

Make a little change in your bio. This might help your account and saves
you from any further troubles. But, do not play with your bio by editing it. 
Do it just once and wait for things to settle.

5. Clean and Reinstall

Unfortunately, as a last resort, you would have to clean all your previous
Instagram data and uninstall the app. Install the app after some time and
check if it is helpful.

So, Use the platform like a regular user, which means avoiding spammy actions,
and you'll be fine. Instagram's goal is to make the platform more enjoyable.

	"""
	],
	[
		"Hi , are you still a RE agent?",
		"Hello! How's your day going?",
		"Good afternoon! How's your day going?",
		"Hey! How's your business?",
	],
	[
		"We are a SMM company, who make realtor's Facebook page grow, and get much more potential clients from they're targeted city/country. Are you interested in it?",
		"I am a part of a SMM cmpany called 'My Broker Search'. We are promoting RE agent's and realtor's business pages! We are working with instagram and facebook pages.",
		"I am a part of a SMM cmpany called 'My Broker Search'. We are working with instagram and facebook pages, and right now, we are running a sale for a limited time on our services!",
		"I'm with “My Broker Search”, we help realtors and mortgage agents create a brand on social media. We design content and help you get more engagement/leads.",
		"We are offering a promotion on our Social Pro Package. We focus on creating a unique brand, separating you from everyone else and the generic content. We create a professional photo banner that will include your picture, logo, and all your contact info. We also post new listing/sold/ and or marketing videos, up to 14 times each month. Custom made each time with your branding. We also offer a digital business card with a QR code, digital email signature that has interactive icons, custom logo, Chat Bot for lead capture, and more. If you have 5 minutes, I can have a Sr. account manager give you a call?",
		"I'm at the creative side of the business. We're doing social page administration with high quality, unique, and professional-looking posts, created by our designers team! We administrate for you, making your page famous, and very attractive, so you don't have to bother about the page, and get more and more messages from the clients!"
	],
	[
		"https://youtu.be/qTCQmML9BFY?list=TLGGmO6hwUpARWYxNTA5MjAyMg",
		"https://youtu.be/gDH3tPuLjoc?list=TLGGaB9CgaC-SogxNTA5MjAyMg",
	],
	[
		"https://www.agentecard.com/style-11/",
		"https://www.agentecard.com/style-10/",
	],
	[
		"Can you provide me a link to your business page? I couldn't find it",
		"I'd like to look at your business page. Can you provide me a link?",
	],
	[
		"What about having a professional photo banner that includes your picture, your logo, and all your contact info?",
		"What about posting listing/branding videos constantly instead of casual listings?",
		"And what about having a Digital Business Card instead of ordinary one? Would you like to see some samples?",
	],
	[
		"Are you generating business using your Social Media?",
		"Have you created a Facebook/Instagram business page?",
		"I saw your Facebook Business page and it looks like you have a good start. Gave you a like for support. I wanted to ask if anyone helps you manage it or do you do it yourself?",
	],
	[
		"https://www.facebook.com/TaraLCookRealtor",
	],
])
# add your name below
names = [
	
]

def credits():
	print(f"Made by {colored('Edgar Tshagharyan', 'yellow')} for everyone.")
	
	if len(names) > 0:
		print()
		print("Thanks for editing to;")
		for i in names:
			cprint(i, 'yellow')
	
	print()
	print("Special thanks to you, for using me!")
	print()
	input("Press enter to go back.")
	return ""

def manual():
	print("This is Edgar's product for automating messaging process a little bit. Enjoy!")
	print()
	print("rules are simple, just type the number of needed choice, press enter, and that's it!")
	print("Program tells you where you need to type the number.")
	print()
	print("Adding your options is easy!")
	print("Find in the code where are Choices and Answers objects located")
	print("""
	they look like this 
	
	choice = Choice([
		'Choice name',
	])
	answers = Answers([
		'Answer text',
	])
	""")
	print("Put your choices and answers inside these things '[]', they must be between this '', and seperate them with a coma.")
	print("Don't forget to write text inside '', so the program understands that this is a text.")
	print()
	print("Other things are automated, but you are free to edit whole code if you want to! Just don't delete the developer's credits, but add your name instead.")
	print()
	print("P.S. after you add something, you'll need to restart the programm py typing in command line 'python main.py'(open the command line in same place, where the programm is located).")
	print()
	input("Press enter to go back.")
	return False

def exit():
	clear()
	print("Thank you for using me!")
	print("Exiting...")
	clear_cache()
	time.sleep(1)
	clear()
	return sys.exit(0)

def bored():
	start_time = time.time()
	open = random.choice(browser)
	webbrowser.open(open[1], new=0, autoraise=True)
	print(f"I've opened a {open[0]} in your main browser.\nHave some fun dude!")
	print()
	input("Press enter here when you're done.")
	clear()
	end_time = time.time() - start_time
	print(f"Out of work time: {datetime.timedelta(seconds=int(end_time))}.")
	print(f"Exact time: {end_time} seconds.")
	print()
	input("Press enter to go back.")

def bottom_border():
	size = os.get_terminal_size()
	bottom = colored("|", 'yellow')

	for _ in range(size.columns - 2):
		bottom += colored("_", 'cyan')
	bottom += colored("|", 'yellow')
	return bottom

def start():
	clear()

	cprint("Simple extendable texting automation utility(setau)", 'yellow')
	time.sleep(0.1)
	print("Chose one of the options below.")
	print()
	time.sleep(0.25)

	print(choices.display_choices())
	print()
	choice = input(colored("Your choice: ", 'green'))
	if choice != "":
		choice = int(choice)
	else:
		print("No such option!")
		time.sleep(1)
		clear_cache()
		return start()

	if choice < len(choices.choices) + 1:
		bottom = bottom_border()

		clear()
		print("Copy one of the texts below.")
		print()
		print(answers.get_answer(choice))
		print(bottom)
		print()

		input("Press enter to go back.")

		clear_cache()
		return start()
	elif choice == len(choices.choices) + 1: # bored
		clear()
		bored()
		clear_cache()
		return start()
	elif choice == len(choices.choices) + 2: # manual
		clear()
		manual()
		clear_cache()
		return start()
	elif choice == len(choices.choices) + 3: # credits
		clear()
		credits()
		clear_cache()
		return start()
	elif choice == len(choices.choices) + 4: # exit
		return exit()
	else:
		clear()
		print("No such option!")
		time.sleep(1)
		clear_cache()
		return start()

clear()

cprint('Welcome to "simple extendable texting automation utility"(setau)!', 'yellow')
time.sleep(2)
webbrowser.open("https://www.time-zones-map.com/")
webbrowser.open("https://whichtimezone.com/canada/canada-map/")
webbrowser.open("https://greenwichmeantime.com/time-zone/usa/phone-area-codes/")
cprint("Time zone maps opened!")
time.sleep(1.15)
webbrowser.open("https://savvytime.com/converter/cst-to-pst")
cprint("Time zone converter opened!")
time.sleep(1.15)
webbrowser.open("https://quillbot.com/")
cprint("Paraphraser opened!")
time.sleep(1.15)
clear()
cprint(f"Enjoy your texting with me, {os.getlogin()}!", 'cyan')
time.sleep(1.15)

start()
