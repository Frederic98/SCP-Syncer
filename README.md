# SCPSyncer
SCPSyncer is a python module that syncs files to a remote machine.
It does this by calculating file hashes on both sides, and pushing the files that have different hashes to the remote machine.

## Configuration files
There are 2 files that configure the behaviour of syncing

### .syncconfig
`.syncconfig` is a YAML file with the sync configuration
```yaml
CONFIG_NAME:
  inherit: CONFIG_NAME OF OTHER CONFIGURATION TO INHERIT MISSING KEYS FROM
  host: IP_OR_HOSTNAME
  user: USERNAME
  password: PASSWORD
  target_path: /PATH/ON/REMOTE
  commands:
    sync_start: COMMAND TO EXECUTE BEFORE SYNCING
    post_hash: COMMAND TO EXECUTE AFTER HASHES ARE CALCULATED
    sync_end: COMMAND TO EXECUTE AFTER SYNCING
  diff_extensions: ['.py', '.json']   # EXTENSIONS OF FILES THAT SHOULD HAVE DIFFS PRINTED
  diff_only: SET TO TRUE IF IT SHOULD JUST CALCULATE HASHES AND PRINT DIFFS
```

### .syncignore
A text file with globs of files to ignore when syncing - same structure as .gitignore file.
Multiple `.syncignore` files can be in (sub)directories

## Notes
If syncing a github repository on Windows, it may be necessary to stop git from normalizing line endings. To do so, open the local repository and edit the file `.git/config` to add the following settings:
```
[core]
  autocrlf = false
  eol = lf
```
This makes git synchronize the repository with `\n` as line endings, instead of the `\r\n` windows style.
