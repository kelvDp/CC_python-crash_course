import requests
from plotly.graph_objs import Bar
from plotly import offline

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
print(f"Total repositories : {response_dict['total_count']}")

repo_dicts = response_dict["items"]
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

# Make a visualization:
data = [{
    "type": "bar",
    "x": repo_names,
    "y": stars
}]

my_layout = {
    "title": "Most-starred Python Projects on GitHub",
    "xaxis": {"title": "Repository"},
    "yaxis": {"title": "Stars"}
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="python_repos.html")
