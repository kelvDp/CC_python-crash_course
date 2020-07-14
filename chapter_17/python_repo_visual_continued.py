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
# Let’s create a
# custom tooltip to show each project’s description as well as the project’s
# owner.
repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make a visualization:
# Here’s a modified version of
# the data object for our chart that gives us a specific color and a clear border
# for each bar:
data = [{
    "type": "bar",
    "x": repo_names,
    "y": stars,
    "hovertext": labels,
    "marker": {
        "color": "rgb(60,100,150)",
        "line": {"width": 1.5, "color": "rgb(25,25,25)"}
    },
    "opacity": 0.6
}] # The marker settings shown here affect the design of the bars.

my_layout = {
    "title": "Most-starred Python Projects on GitHub",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Repository",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14}
    },
    "yaxis": {
        "title": "Stars",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14}
    }
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="python_repos_update.html")
