import requests


print("\n\t*** Python HTTP API cmd App ***\n\t%s\n" %("-"*31))
print("Welcome to this simple Python HTTP API command line app")
print("Let's get some data from the 'jsonplaceholder.typicode.com' website")



def get_data(get_url, post_id):
	try:
		isinstance(int(post_id), int)
		if int(post_id) <= 100 and int(post_id) > 0:
			r = requests.get(get_url + post_id)
			print(type(r))
			print(r.__dict__)
			# print(r.status)
			return r
		else:
			print("Please enter a number between 1 and 100")
	except ValueError as e:
		print("You need to enter a whole number for your request to succeed")
		raise(e)
	return "* Nothing to show *"

def post_data(post_url,title, body, userId=11):
	post_data = {
		'title': title,
		'body': body,
		'userId': userId
		}
	r = requests.post(post_url, data=post_data)
	return r

def main():
	url = "https://jsonplaceholder.typicode.com/posts/"

	post_id = input("Enter a number between 1 and 100: ")
	print("\n\tGetting your request...\n")
	get_r = get_data(url,post_id)
	print("Response:\n %sStatus code: %s" % (get_r.text, get_r.status_code))

	print("\nNow let's add a new post...")
	title = input("Enter a title for your post: ")
	body = input("Enter a body for your post: ")

	print("\n\tCreating your new post...\n")
	post_r = post_data(url,title,body)
	print("Response:\n %sStatus code: %s" % (post_r.text, post_r.status_code))


if __name__ == '__main__':
	main()
