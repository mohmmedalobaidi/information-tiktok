

# = = = = = = = = = = = =

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
C ='\033[0;36m' # Cyan
W ='\033[0;37m' # White

# = = = = = = = = = = = =



print(B+"""


|¯¯¯¯¯¯¯||¯¯||¯¯|/¯¯/|¯¯¯¯¯¯¯| /¯¯/\¯¯\'|¯¯|/¯¯/
 ¯¯|   '|¯¯’|   '||   '|   '(  ¯¯|   '|¯¯’|    |  |   '||   '|   '( 
    '|__|’'   |__||__|\__\    '|__|’'    \__\/__/'|__|\__\




""")
print('''
\033[0;37mName Tool\033[0;37m: \033[2;36minformation-TikTok
\033[0;37mBY: ENG MOHAMMED \033[2;36mALOBAIDY
\033[2;32mGITHUB\033[0;37m: \033[2;36m@\033[0;37mEngmohammedalobaidy
\033[2;36mTWITTER\033[0;37m: \033[2;36m@\033[0;37meng_m_alobaidy 
\033[2;36mversion\033[0;37m: 1.0\033[2;36mv''')
print("\033[2;36m•\033[0;37m×××××××××××××××\033[2;36m•\033[0;37m×××××××××××××××\033[2;36m•\033[0;37m×××××××××××××××\033[2;36m•")

def TIKINFO():

	try:

		import requests

	except ModuleNotFoundError:

		os.system("pip install requests")

	username = input("\033[0;37m[\033[2;36m•\033[0;37m]Enter UserName : "+B)

	url = f"https://tiktok-best-experience.p.rapidapi.com/user/{username}"

	headers = {

		"x-rapidapi-key":"d0cbbe1f79mshe3c74080d9d0da5p1de4ddjsn21db44140e77",

		"x-rapidapi-host":"tiktok-best-experience.p.rapidapi.com",

		"User-Agent":"TikTracker/1.2 (com.markuswu.TikTracker; build:1; iOS 14.4.0) Alamofire/5.4.4"

	}

	try:	

		r = requests.get(url,headers=headers).json()
		print("")

		print(W+"")

		

	

		try:

			unique_id = r["Data"]["unique_id"]

			print(f"- UserName : {unique_id}")

		except KeyError:

			print("- UserName : Not Found")

			

		

		

		

		try:

			nickname = r["data"]["nickname"]

			print(f"- NickName : {nickname}")

		except KeyError:

			print("- NickName : unknow")

			

		

		

		try:

			followers = r["Data"]["follower_count"]	

			print(f"- Followers : {followers}")

		except KeyError:

			print("- Followers : 0")

		

		try:

			following = r["data"]["following_count"]

			print(f"- Following : {following}")

		except KeyError:

			print("- Following : 0")

		

		

		try:

			likes = r["Data"]["total_favorited"]

			print(f"- Likes : {likes}")

		except KeyError:

			print("- Likes : 0")

		try:

			custom_verify = r["Data"]["custom_verify"]

			print(f"- Custom Verify : {custom_verify}")

		except KeyError:

			pass 

		try:

			verify = r["Data"]["enterprise_verify_reason"]

			print(f"- Verify : {verify}")

		except KeyError:

			pass

		try:

			following_visibility = r["data"]["privacy_setting"]["following_visibility"]

			

			if following_visibility == 1:				

				print(f"- Show Who is Following : True")

				pass

			else:

				print("- Show Who is Following : False")

				

		except KeyError:

			pass

	

	

		try:

			

			music_count = r["data"]["original_musician"]["music_count"]

			print(f"- Music Count : {music_count}")

		except KeyError:

			print("- Music Count : 0")

		

		try:

			music_used = r["data"]["original_musician"]["music_used_count"]

			print(f"- Music Used : {music_used}")

		except KeyError:

			print("- Music Used : 0")

		try:

			uid = r["data"]["uid"]

			print(f"- Uid : {uid}")

		except KeyError:

			print("- Uid : unknow")

		

		try:

			youtub_Channel = r["data"]["youtube_channel_id"]

			print(f"- Youtub Channel id : {youtub_Channel}")

		except KeyError:

			print("- Youtub Channel id : not found")

		try:

			insta = r["data"]["ins_id"]

			print(f"- Insta UserName : {insta}")

		except KeyError:

			print("- Insta UerName : not found")

		

		try:

			bio = r["data"]["signature"]

			print(f"- Bio : {bio}")

		except KeyError:

			print("- Bio : no bio")

	except Exception as e:

		print(Z+"Unknow Error !")

	



TIKINFO()

