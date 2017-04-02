A tool to run your tests way more often than necessary.

Basically, just run:

```bash
    $ testincessantly dir test-cmd ...
```

and every time you create/modify/delete a file under `dir`, `test-cmd ...` will get executed.

I typically invoke this as

```bash
    $ testincessantly -e '.*' -e '__pycache__' . pytest
```
The `-e` options exclude dotfiles and anything named `__pycache__`.

Okay, that was a lie. I actually typically invoke
```bash
    $ testincessantly -e '.*' -e '__pycache__' . chime-success pytest
```
`chime-success` is [a script](https://gist.github.com/speezepearson/83c234c40d16c9f7fba73d8bca7a1a75) on my `PATH` that makes a noise indicating whether the argument-command passed or failed. Now, every time I save a file, I get a chime telling me whether things are still good or not.
