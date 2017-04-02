A tool to run your tests way more often than you need.

Basically:

```bash
    testincessantly . test-cmd ...
```

and every time you create/modify/delete a file under the current directory, `test-cmd ...` will get executed.

I typically invoke this as

```bash
    testincessantly -e '.*' -e '__pycache__' . pytest
```
The `-e` options exclude dotfiles and anything named `__pycache__`.

Okay, that was a lie. I actually typically invoke
```bash
    testincessantly -e '.*' -e '__pycache__' . chime-success pytest
```
`chime-success` is a script on my `PATH` that makes a noise indicating whether the argument-command passed or failed.
