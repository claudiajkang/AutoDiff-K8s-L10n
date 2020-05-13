import requests
from git import Repo
import os

PR_NUM = input("PR NUMBER? ").replace("#", "")

GIT_BASE_PR_URL = f'https://api.github.com/repos/kubernetes/website/pulls/{PR_NUM}'

git_pr_res = requests.get(GIT_BASE_PR_URL).json()
L10N_WORKING_BRANCH = git_pr_res['base']['ref']
L10N_LANG = L10N_WORKING_BRANCH.split('-')[-1].split('.')[0]

GIT_BASE_FILE_URL = f'{GIT_BASE_PR_URL}/files'
git_all_res = requests.get(GIT_BASE_FILE_URL).json()

for git_res in git_all_res:
    KO_FILE_URL = git_res['raw_url']
    EN_FILE_URL = git_res['raw_url']\
        .replace(git_res['sha'], L10N_WORKING_BRANCH)\
        .replace(f'/{L10N_LANG}', '/en')

    NEW_FILE_NAME = git_res['filename']\
        .replace("content/ko/docs/", "")\
        .replace("content/ko/", "")\
        .replace('/', '-')

    curDir = os.getcwd()
    repo = Repo(curDir)

    PR_URL = GIT_BASE_PR_URL.replace('api.', '')\
        .replace('/repos', '')\
        .replace('pulls', 'pull')

    en_res = requests.get(EN_FILE_URL)
    f = open(f'{curDir}/{NEW_FILE_NAME}', "wb")
    f.write(en_res.content)
    f.close()
    repo.index.add(NEW_FILE_NAME)
    repo.index.commit(f'#{PR_NUM} : add original {NEW_FILE_NAME}\n\n- PR url : {PR_URL}\n- file url : {EN_FILE_URL}')

    ko_res = requests.get(KO_FILE_URL)
    f = open(f'{curDir}/{NEW_FILE_NAME}', "wb")
    f.write(ko_res.content)
    f.close()
    repo.index.add(NEW_FILE_NAME)
    repo.index.commit(f'#{PR_NUM} : update translated {NEW_FILE_NAME}\n\n- PR url : {PR_URL}\n- file url : {KO_FILE_URL}')