import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

response_dictionary = r.json()
print(f"Total repos found: {response_dictionary['total_count']}")

repos = response_dictionary["items"]
print(f"Repos returned: {len(repos)}")

# repo_dicts = repos[0]
# When we make a visualization for this data, we’ll want to include more than
# one repository. Let’s write a loop to print selected information about each
# repository the API call returns so we can include them all in the
# visualization:

print("\nSelected information about repository:")
for repo_dicts in repos:
    print(f"\nName: {repo_dicts['name']}")
    print(f"Owner: {repo_dicts['owner']['login']}")
    print(f"Stars: {repo_dicts['stargazers_count']}")
    print(f"Repository: {repo_dicts['html_url']}")
    print(f"Created: {repo_dicts['created_at']}")
    print(f"Updated: {repo_dicts['updated_at']}")
    print(f"Description: {repo_dicts['description']}")
