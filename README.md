# Nea
🦑 *Commit for me* 🦑

## REQUIREMENTS:

- CURL

## Install:

- ```sudo python3 setup.py```

## Usage:
```
usage: nea [-h] [-s] [-r] [-m MESSAGE] [-t TYPE]

optional arguments:
  -h, --help            show this help message and exit
  -s, --setup           Setup the configuration
  -r, --reset           Reset the configuration
  -m MESSAGE, --message MESSAGE
                        Message for your commit
  -t TYPE, --type TYPE  Commit type
```

## Configuration:

```JSON
{
    "config" : {
        "type" : {
            "feat"   : "⭐️",
            "fix"    : "🔧",
            "doc"    : "📃",
            "style"  : "📷",
            "perf"   : "⌛️",
            "test"   : "📝",
            "core"   : "📍",
            "lib"    : "📚",
            "revert" : "📦",
            "update" : "🔍",
            "clean"  : "🧹"
        },
        "commit" : {
            "default_message" : "Clean code",
            "default_type"    : "clean"
        },
        "break" : "|"
    }
}
```

- type
- default_message
- default_type
- break

## Examples:

```
nea -t feat -m "New feature"     :    ⭐️ feat | New feature
nea -t fix -m "New fix"          :    🔧 fix | New fix 
nea -t test                      :    📝 test | New Update
nea                              :    🔍 update | New Update
```
### OR 
```
git nea -t feat -m "New feature" :    ⭐️ feat | New feature
git nea -t fix -m "New fix"      :    🔧 fix | New fix 
git nea -t test                  :    📝 test | New Update
git nea                          :    🔍 update | New Update
```
