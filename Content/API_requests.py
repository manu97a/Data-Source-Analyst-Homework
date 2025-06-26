# Search Repositories (public)

def search_public_repositories(query = "machine learning", per_page = 10 , page = 1, created_after=None, min_stars=None):
  if per_page > 100:
    print(f"Error. per_page cannot be greater than 100 (Github Limit)")
    return None,None
  if (page * per_page) > 1000:
    print(f"Error. per_page*page cannot be greater than 1000 results (Github Limit)")
    return None,None
  new_query = query
  if created_after:
    new_query += f"+created:>={created_after}"
  if min_stars:
    new_query += f"+stars:>={min_stars}"
  api_url = f"https://api.github.com/search/repositories?q={new_query}&per_page={per_page}&page={page}"
  res = requests.get(api_url, headers=headers)
  if res.status_code == 200:
    repositories = res.json()
    print(f"Repositories for the topic '{query}' : \n")
    for repo in repositories['items'][:5]:
      print(f"{repo['full_name']}")
      print(f"Description: {repo['description']}\n")
    return repositories, api_url
  else:
    print(f"Error {res.status_code}:{res.json()}")
    return None,api_url

#Commits of a repository

def get_commits(owner="midudev",repo= "aprendiendo-react", per_page= 10, since= None, until=None,page=1):
  if per_page > 100:
    print(f"Error. per_page cannot be greater than 100 (Github Limit)")
    return
  if (page * per_page) > 1000:
    print(f"Error. per_page*page cannot be greater than 1000 results (Github Limit)")
    return 
  parameters = {
      "per_page": per_page,
      "page":page
  }
  if since:
    parameters["since"] = since
  if until:
    parameters["until"] = until
  api_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
  res = requests.get(api_url, headers=headers,params=parameters)
  if res.status_code == 200:
    commits = res.json()
    print(f"The last {per_page} commits of {owner}/{repo}")
    for commit in commits:
      print(f"{commit['commit']['author']['date']}- {commit['commit']['author']['name']}")
      print(f"{commit['commit']['message']}\n")

  else:
    print(f"Error {res.status_code}:{res.json()}")

# Repo content

def repo_content(owner = "midudev", repo= "aprendiendo-react", path=""):
   api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
   res = requests.get(api_url, headers=headers)
   if res.status_code == 200:
    content = res.json()
    print(f"Owner:  {owner} \n Name of the repo: {repo}\n Content: {content} \n")
    if isinstance(content,list):
      download_links = []
      for item in content:
        print(f"- {item['type'].capitalize()}: {item['name']}")
        if item['type'] == "file":
          print(f"Download link: {item['download_url']}")
          download_links.append(item['download_url'])
      return download_links
    elif isinstance(content, dict) and content.get("type") == "file":
      print(f"File: {content['name']}")
      print(f"Download link: {content['download_url']}")
      return content['download_url']
    else:
      print("This is not a recognized file or folder")
   else:
    print(f"Error {res.status_code}: {res.json()}")