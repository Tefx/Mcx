# Mcx

A tmux-based SSH/Telnet Client for Managing Many-hosts

---

## Get Started
### Prerequisites
#### `tmux`
Since `Mcx` is `tmux`-based, you must use your system's package manager to install the `tmux` first. For example, you can use
```bash
apt-get install tmux
```
in Ubuntu, or
```bash
brew install tmux
```
in Mac OS X.
#### Python modules: 
The modules `pexpect` and `pypinyin` should be installed first via:

```bash
pip install pexpect pypinyin
```
#### Ftp client
An application that can handle the `"ftp://"` urls should be installed. If you do not use ftp, this can be ignored.
    
### Basic Installation
#### Clone this repository
```bash
git clone https://github.com/Tefx/Mcx.git
```
#### Configuration
1. Copy the sample configurations to `/etc/mcx` or `~/.mcx`:
    
    ```bash
    cp -r Mcx/conn_sample ~/.mcx
    ```
2. Change the ftp url handler by setting the value of`ftp_tool` in `$CONF_PATH/config.json`.
  - You can easily set it to `xdg-open` for Linux or `open` for Mac OS X.
  - You can alternatively set it to `filezilla` or any other specific app, as long as it can handle the url `ftp://user:password@ip`.
3. Put you host configurations inside `$CONF_PATH/hosts` folder.
  - Have a Look at the sample host configurations. It should be self-explanatory.
  - `conn_type` should be either `ssh` or `telnet`.
  - `auth_type` should be either `password` or `key`. If the value is `password`, the variable `password` must be set. If the value is `key`, an optional variable `passphrase` might be needed at the same time.
  - The sub-folders and any number of configuration files are acceptable. The `hosts` folder will be scanned recursively for all hosts.

### Usages
#### Launch

```bash
cd Mcx;tmux -f tmux.source
```

#### Keymap
Keybinding           | Description
---------------------|------------------------------------------------------------
<kbd> Prefix S </kbd>| search hosts by name.
<kbd> Prefix F </kbd>| open ftp application and connect to the current host.
<kbd> Prefix V </kbd>| open a vertically splited pane and connect to the same host.
<kbd> Prefix v </kbd>| open a horizontally splited pane and connect to the same host.
<kbd> Prefix C </kbd>| view all connected hosts. I call this listing pane as `host-listing-pane`.
<kbd> Ctrl-D </kbd>  | kill connections to the selected hosts. Works only in the `hast-listing-pane`.
  - Notes:
    - The <kbd>Prefix</kbd> should be <kbd>Ctrl-B</kbd> by default in `tmux`.
    - Using <kbd>Prefix S</kbd> to connect a host which is already have connections in other window is considered as connecting a new host. The different windows connected to the same host are shown as several hosts in the `host-listing-pane` and can be killed individually.
    - All other tmux-shortcuts should be usable as usual.
    - In searching, the patterns can be full Pinyin, Pinyin Initials, Pinyin first-letters or substrings. `/` is used for splitting different levels. For example, `"北京/new/测试MySQL/Server1"` can be matched by:
      - `bj`
      - `bj/csh`
      - `bj/cs/1`
      - `new/Ser`
      - `ceshi/1`
      -  And many other patterns. Try out by yourselves.
