import requests

def get_data(get_url, post_id):
	try:
		isinstance(int(post_id), int)
		if int(post_id) <= 100 and int(post_id) > 0:
			print("okay")
			r = requests.get(get_url)
			return r.text
		else:
			print("Please enter a number between 1 and 100")
	except ValueError as e:
		print("You need to enter a whole number for your request to succeed: ", e)
	return "* Nothing to show *"

def main():
	post_id = input("Enter a number between 1 and 100: ")
	get_url = "https://jsonplaceholder.typicode.com/posts/" + post_id
	post_url = "https://jsonplaceholder.typicode.com/posts/"

	print("\n\tGetting your request...\n")
	print(get_data(get_url,post_id))

if __name__ == '__main__':
	main()
