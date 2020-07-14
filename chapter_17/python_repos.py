import requests

# # Make an API call and store the response:
# url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
# headers = {"Accept": "application/vnd.github.v3+json"}
# r = requests.get(url, headers=headers)
#
# print(f"Status code: {r.status_code}")
#
# # Store the API response inside a var:
# response_dict = r.json()
#
# # Process the results:
# print(response_dict.keys())

# With the information from the API call stored as a dictionary, we can work
# with the data stored there. Let’s generate some output that summarizes the
# information. This is a good way to make sure we received the information
# we expected and to start examining the information we’re interested in:

# Make an API call and store the response:
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

print(f"Status code: {r.status_code}")

# Store the API response inside a var:
response_dict = r.json()
print(f"Total repositories : {response_dict['total_count']}")

# Explore info on repos:
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repo:
repo_dicts = repo_dicts[0]
# print(f"\nKeys : {len(repo_dicts)}")
# for key in sorted(repo_dicts.keys()):
#     print(key)

# Let’s pull out the values for some of the keys in repo_dict:
print("\nSelected information about first repository:")
print(f"Name: {repo_dicts['name']}")
print(f"Owner: {repo_dicts['owner']['login']}")
print(f"Stars: {repo_dicts['stargazers_count']}")
print(f"Repository: {repo_dicts['html_url']}")
print(f"Created: {repo_dicts['created_at']}")
print(f"Updated: {repo_dicts['updated_at']}")
print(f"Description: {repo_dicts['description']}")