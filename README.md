# Wiktextract lemmatization fixer

The wiktextract data is super great for many purposes. But if you want to use it directly to create a dictionary, for example, you might encounter some problems for cyrillic languages when the inflections are stressed, or there might be some data in the inflection table that actually is not an inflection, ....

This library aims to fix that.

WIP + not yet finished.

### Usage

```
from wiktextract_lemmatization.utils import fix_inflections
forms = [...]
fixed_ forms = fix_inflections(forms, "говорить", "ru")
```

Contributions welcome!