# Mcx

An tmux-based multi-connections manager

---

## Get Started
### Prerequisites
#### `tmux`
Since `Mcx` is `tmux`-based, you must use your package manager to install the `tmux` first.
#### Python modules: 
The modules `pexpect` and `pypinyin` should be installed via:
```bash
pip install pexpect pypinyin
```
#### Ftp client
An app that can handle ftp urls. If you do not use ftp, this can be ignored.
    
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
2. Change ftp url handler by setting the value of`ftp_tool` in `$CONF_PATH/config.json`.
  - You can easily set it to `xdg-open` for Linux or `open` for Mac OS X.
  - You can alternatively set it to `filezilla` or other specific apps, unless they can handle the ftp url with form `ftp://user:password@ip`.
3. Put you host configurations inside `$CONF_PATH/hosts`.
  - Have a Look at the sample host configurations. It should be self-explanatory.
  - The variable `conn_type` should be either `ssh` or `telnet`.
  - For now, I have only implemented the `password` authentication approach. I will add the `key` approach ASAP, which uses the security public keys.
  - The sub-folders and any number of configuration files are acceptable. The `hosts` folder will be scanned recursively for all hosts.

### Usages
#### Launch

```bash
cd Mcx;tmux -f tmux.source
```

#### Keymap
Keybinding           | Description
---------------------|------------------------------------------------------------
<kbd> Prefix S </kbd>| search hosts by name
<kbd> Prefix F </kbd>| open ftp app connected to current host
<kbd> Prefix V </kbd>| open a vertically splited pane and connect to the same host
<kbd> Prefix v </kbd>| open a horizontally splited pane and connect to the same host
<kbd> Prefix C </kbd>| view all connected hosts. I call this listing pane as host-listing-pane.
<kbd> Ctrl-D </kbd>  | kill connections to the selected hosts. Works only in the hast-listing-pane.
  - Notes:
    - The <kbd>Prefix</kbd> should be <kbd>Ctrl-B</kbd> by default in `tmux`.
    - Using <kbd>Prefix S</kbd> to connected an host which is already have connections in other window is considered as a new host. The windows are shown as two in the host-listing-pane and can be killed individually.
    - All other tmux-shortcuts should be usable as usuall.
    - In searching, the pattern can be full Pinyin, Pinyin Initials, Pinyin first-letters, substrings. `/` is used for split different levels. For example, `"北京/new/测试MySQL/Server1"` can be matched by:
      - `bj`
      - `bj/csh`
      - `bj/cs/1`
      - `new/Ser`
      - `ceshi/1`
      -  And many other pattern. Try out by yourselves.
