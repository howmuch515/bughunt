# bughunt-cli

This command line tool supports bughunting projects.

## install

```shell
git clone git@github.com:howmuch515/bughunt-cli.git
cd bughunt-cli
rye build
rye install --path ./dist/bughunt_cli-*-py3-none-any.whl
```

## usage

```shell

bughunt init <myproject>

```

The `myproject` directory structure will be as follows.

```md

myproject/
├── memo.md
├── scan/
├── report/
└── dict/

```
