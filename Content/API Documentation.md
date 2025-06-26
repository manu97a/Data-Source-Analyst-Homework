# Github API 
For this task you have to know the functions that I created for request some data from the Github API.
## Content
1. [Github Token](#id1)
2. [Authenticate process](#id2)
3. [Implemented functions](#id3) 
    - 3.1 [search_public_repositories()](#search_public_repositories)
    - 3.2 [get_commits()](#get_commits)
    - 3.3 [repo_content()](#repo_content)
4. [Github API Limits](#id4)

<a id='id1'></a>

## Github token
If you want to test deeply the Github API you need to use a Github token to get more First, you have to get your Github Token, for this follow this steps:
* Sign in to GitHub.
* Go to your profile settings.
* Go to Developer settings.
* Select personal access tokens and click Generate New Token.
* Name your token.
* Choose the permissions your token requires.
* Copy your token. 
### Important: Copy your token and save it, you wont be able to retrieve it later.

Using the authentication token will allow you to make up to 5000 requests per hour. While without the token you can only make a total of 60 requests


<a id='id2'></a>

## Authenticate process
For use this API, first you have to consider to authenticate your user with a Github token.
For this you can go directly to the Jupyter Notebook avaliable on this repository, where you can run all the cells and verify your Github Token. For test your connection you may use the function test_connection for validate your connection to the API and verify your username.
### Important! For this function I have used getpass in which when running the jupyter notebook it will request the token once you enter the keyboard.This is done to avoid making the token public.

<a id='id3'></a>

## Implemented functions

<a id='search_public_repositories'></a>

### Searching public repositories 
```
search_public_repositories()
```
#### Paremeters:
* query: Search term (example,"python") . Type *str*.
* per_page: Number of results per page. Type *int*.
* page: Page number. Type *int*.
* created_after (optional): Filter by creation date using the format: "2023-01-01". Type *str*.
* min_stars: Minimun number of stars. Type *int*.

#### Return:
This function return a tuple (repositories_data, api_url)
* repositories_data: A Python dictionary with the JSON or (None on failure).
* api_url: The full URL used for the API request.

### Example
```
repos, url = search_public_repositories("machine learning", created_after="2021-07-12")
```
<a id='get_commits'></a>

### Getting commits from a repository

```
get_commits()
```

#### Parameters:
* owner: Username or organization that owns the repository. Type: *str*.
* repo: Repository name. Type: *str*.
* per_page: Number of commits per page (maximum: 100). Type: *int*.
* page: Page number. Type: *int*.
* since (optional): Filter commits after a given date ("YYYY-MM-DDTHH:MM:SSZ"). Type: *str*.
* until (optional): Filter commits before a given date. Type: *str*.
#### Return:
This function return a tuple (commits, api_url)
* commits: A Python dictionary with the JSON response or (None on failure).
* api_url: The full URL used for the API request.
### Example
```
commits_data, url = get_commits(owner="midudev",repo="aprendiendo-react",per_page=5)
```
<a id='repo_content'></a>

### Get repository content

```
repo_content()
```
#### Parameters:
* owner: Repository username or organization. Type: *str*.
* repo: Repository name. Type: *str*.
* path (optional): Path inside the repository (file or directory) Type: *str*.

#### Return:
* If the path is a folder: returns a list of download URLs for all the files.
* If the path is for a specific file returns a single download URL.
* If there is an error: returns None.

```
links = repo_content(owner="midudev",repo="porfolio.dev")
```

<a id='id4'></a>

### Github API Limits
The Github API have some limits that you have to keep in mind when you are generating requests to the diferent endpoints. 

* First without a token you only can make 60 request per hour.
* With a token you can make 5000 requests.
* For the functions: Searching public repositories and Getting commits from a repository. The most important limitations are:
    * The number of results per page cannot exceed 100.
    * The product of page * per_page must not be greater than 1000.

The functions Searching Public Repositories and Getting Commits from a Repository implement input validation and error control to avoid triggering empty responses due to pagination or result limit constraints.