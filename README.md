# AutoDiff-K8s-L10n

**AutoDiff-K8s-L10n** is a project that creates diffs commits to compare a localization source file
and a translation file by using pull requests number in [kubernetes/website](https://github.com/kubernetes/website).

### 1. Set environment 
1) git fork

2) git clone

  ```bash
  $ git clone https://github.com/{USER_NAME}/AutoDiff-K8s-L10n.git
  $ cd AutoDiff-K8s-L10n
  ```

3) set virtualenv

  > You must install virtualenv
  ```bash
  $ ./init.sh
  ```

### 2. Use AutoDiff-K8s-L10n
Run `create_diff.py`. And check your commit list.

```bash
$ ./create_diff.py
PR NUMBER? #12314 (This pr number referred [kubernetes/website](https://github.com/kubernetes/website)
```

