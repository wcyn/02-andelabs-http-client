import requests


print("\n\t*** Python HTTP API cmd App ***\n\t%s\n" %("-"*31))
print("Welcome to this simple Python HTTP API command line app")
print("Let's get some data from the 'jsonplaceholder.typicode.com' website")



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

def post_data(post_url,title, body, userId=11):
	post_data = {
		'title': title,
		'body': body,
		'userId': userId
		}
	r = requests.post(post_url, data=post_data)
	return r.text

def main():
	post_id = input("Enter a number between 1 and 100: ")
	get_url = "https://jsonplaceholder.typicode.com/posts/" + post_id
	post_url = "https://jsonplaceholder.typicode.com/posts/"

	print("\n\tGetting your request...\n")
	print(get_data(get_url,post_id))

	print("\nNow let's add a new post...")
	title = input("Enter a title for your post: ")
	body = input("Enter a body for your post: ")

	print("\n\tCreating your new post...\n")
	print(post_data(post_url,title,body))

if __name__ == '__main__':
	main()
