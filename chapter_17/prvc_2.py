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

# Because Plotly allows you to use HTML on text elements, we can easily add
# links to a chart. Let’s use the x-axis labels as a way to let the viewer visit any
# project’s home page on GitHub. We need to pull the URLs from the data
# and use them when generating the x-axis labels:

repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_names = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repolink = f"<a href='{repo_url}'>{repo_names}</a>"
    repo_links.append(repolink)

    stars.append(repo_dict["stargazers_count"])
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    label = f"{owner}<br />{description}"
    labels.append(label)


data = [{
    "type": "bar",
    "x": repo_links,
    "y": stars,
    "hovertext": labels,
    "marker": {
        "color": "rgb(60,100,150)",
        "line": {"width": 1.5, "color": "rgb(25,25,25)"}
    },
    "opacity": 0.6
}]

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
offline.plot(fig, filename="prvc.html")
