import requests
from plotly.graph_objs import Bar
from plotly import offline


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'accept': 'application/vnd.github.v3+json'}  # 要求使用第三版api
r = requests.get(url, headers=headers)
print(f"Stauts code:{r.status_code}")
response_dict = r.json()

print(response_dict.keys())
print(f"num:{response_dict['total_count']}")

repo_dicts = response_dict['items']
'''
print(f"response returned:{len(repo_dicts)}")
repo_0 = repo_dicts[0]
for k in repo_0.keys():
    print(k)
print(f"first name:{repo_0['name']}")
'''
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
data = [{
    'type': 'bar',
    'x': names,
    'y': stars,
}]
my_layout = {
    'title': 'favorite python repo',
    'xaxis': {'title': 'repositories'},
    'yaxis': {'title': 'stars'},
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'python_repos.html')
