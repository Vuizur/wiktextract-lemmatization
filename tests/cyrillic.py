from wiktextract_lemmatization.utils import fix_inflections


forms = [
    {
      "form": "тупо́й",
      "tags": [
        "canonical"
      ]
    },
    {
      "form": "tupój",
      "tags": [
        "romanization"
      ]
    },
    {
      "form": "(по)тупе́е",
      "tags": [
        "comparative"
      ]
    },
    {
      "form": "(по)тупе́й",
      "tags": [
        "comparative"
      ]
    },
    {
      "form": "ту́по",
      "tags": [
        "adverb"
      ]
    },
    {
      "form": "ту́пость",
      "tags": [
        "abstract-noun"
      ]
    },
    {
      "form": "ту́пенький",
      "tags": [
        "diminutive"
      ]
    },
    {
      "form": "",
      "source": "declension",
      "tags": [
        "table-tags"
      ]
    },
    {
      "form": "ru-decl-adj",
      "source": "declension",
      "tags": [
        "inflection-template"
      ]
    },
    {
      "form": "c'",
      "source": "declension",
      "tags": [
        "class"
      ]
    },
    {
      "form": "тупо́й",
      "roman": "tupój",
      "source": "declension",
      "tags": [
        "masculine",
        "nominative"
      ]
    },
    {
      "form": "тупо́е",
      "roman": "tupóje",
      "source": "declension",
      "tags": [
        "neuter",
        "nominative"
      ]
    },
    {
      "form": "тупа́я",
      "roman": "tupája",
      "source": "declension",
      "tags": [
        "feminine",
        "nominative"
      ]
    },
    {
      "form": "тупы́е",
      "roman": "tupýje",
      "source": "declension",
      "tags": [
        "nominative",
        "plural"
      ]
    },
    {
      "form": "тупо́го",
      "roman": "tupóvo",
      "source": "declension",
      "tags": [
        "genitive",
        "masculine",
        "neuter"
      ]
    },
    {
      "form": "тупо́й",
      "roman": "tupój",
      "source": "declension",
      "tags": [
        "feminine",
        "genitive"
      ]
    },
    {
      "form": "тупы́х",
      "roman": "tupýx",
      "source": "declension",
      "tags": [
        "genitive",
        "plural"
      ]
    },
    {
      "form": "тупо́му",
      "roman": "tupómu",
      "source": "declension",
      "tags": [
        "dative",
        "masculine",
        "neuter"
      ]
    },
    {
      "form": "тупо́й",
      "roman": "tupój",
      "source": "declension",
      "tags": [
        "dative",
        "feminine"
      ]
    },
    {
      "form": "тупы́м",
      "roman": "tupým",
      "source": "declension",
      "tags": [
        "dative",
        "plural"
      ]
    },
    {
      "form": "тупо́го",
      "roman": "tupóvo",
      "source": "declension",
      "tags": [
        "accusative",
        "animate",
        "masculine"
      ]
    },
    {
      "form": "тупо́е",
      "roman": "tupóje",
      "source": "declension",
      "tags": [
        "accusative",
        "neuter"
      ]
    },
    {
      "form": "тупу́ю",
      "roman": "tupúju",
      "source": "declension",
      "tags": [
        "accusative",
        "feminine"
      ]
    },
    {
      "form": "тупы́х",
      "roman": "tupýx",
      "source": "declension",
      "tags": [
        "accusative",
        "animate",
        "plural"
      ]
    },
    {
      "form": "тупо́й",
      "roman": "tupój",
      "source": "declension",
      "tags": [
        "accusative",
        "inanimate",
        "masculine"
      ]
    },
    {
      "form": "тупы́е",
      "roman": "tupýje",
      "source": "declension",
      "tags": [
        "accusative",
        "inanimate",
        "plural"
      ]
    },
    {
      "form": "тупы́м",
      "roman": "tupým",
      "source": "declension",
      "tags": [
        "instrumental",
        "masculine",
        "neuter"
      ]
    },
    {
      "form": "тупо́й",
      "roman": "tupój",
      "source": "declension",
      "tags": [
        "feminine",
        "instrumental"
      ]
    },
    {
      "form": "тупо́ю",
      "roman": "tupóju",
      "source": "declension",
      "tags": [
        "feminine",
        "instrumental"
      ]
    },
    {
      "form": "тупы́ми",
      "roman": "tupými",
      "source": "declension",
      "tags": [
        "instrumental",
        "plural"
      ]
    },
    {
      "form": "тупо́м",
      "roman": "tupóm",
      "source": "declension",
      "tags": [
        "masculine",
        "neuter",
        "prepositional"
      ]
    },
    {
      "form": "тупо́й",
      "roman": "tupój",
      "source": "declension",
      "tags": [
        "feminine",
        "prepositional"
      ]
    },
    {
      "form": "тупы́х",
      "roman": "tupýx",
      "source": "declension",
      "tags": [
        "plural",
        "prepositional"
      ]
    },
    {
      "form": "туп",
      "roman": "tup",
      "source": "declension",
      "tags": [
        "masculine",
        "short-form"
      ]
    },
    {
      "form": "ту́по",
      "roman": "túpo",
      "source": "declension",
      "tags": [
        "neuter",
        "short-form"
      ]
    },
    {
      "form": "тупа́",
      "roman": "tupá",
      "source": "declension",
      "tags": [
        "feminine",
        "short-form"
      ]
    },
    {
      "form": "тупы́",
      "roman": "tupý",
      "source": "declension",
      "tags": [
        "plural",
        "short-form"
      ]
    },
    {
      "form": "ту́пы",
      "roman": "túpy",
      "source": "declension",
      "tags": [
        "plural",
        "short-form"
      ]
    },
    {
      "form": "",
      "source": "declension",
      "tags": [
        "table-tags"
      ]
    },
    {
      "form": "ru-decl-adj",
      "source": "declension",
      "tags": [
        "inflection-template"
      ]
    },
    {
      "form": "c'",
      "source": "declension",
      "tags": [
        "class"
      ]
    },
    {
      "form": "тупо́й",
      "roman": "tupój",
      "source": "declension",
      "tags": [
        "dated",
        "masculine",
        "nominative"
      ]
    },
    {
      "form": "тупо́е",
      "roman": "tupóje",
      "source": "declension",
      "tags": [
        "dated",
        "neuter",
        "nominative"
      ]
    },
    {
      "form": "тупа́я",
      "roman": "tupája",
      "source": "declension",
      "tags": [
        "dated",
        "feminine",
        "nominative"
      ]
    },
    {
      "form": "тупы́е",
      "roman": "tupýje",
      "source": "declension",
      "tags": [
        "dated",
        "masculine",
        "nominative",
        "plural"
      ]
    },
    {
      "form": "тупы́я",
      "roman": "tupýja",
      "source": "declension",
      "tags": [
        "dated",
        "feminine",
        "neuter",
        "nominative",
        "plural"
      ]
    },
    {
      "form": "тупа́го",
      "roman": "tupávo",
      "source": "declension",
      "tags": [
        "dated",
        "genitive",
        "masculine",
        "neuter"
      ]
    },
    {
      "form": "тупо́го",
      "roman": "tupóvo",
      "source": "declension",
      "tags": [
        "dated",
        "genitive",
        "masculine",
        "neuter"
      ]
    },
    {
      "form": "тупо́й",
      "roman": "tupój",
      "source": "declension",
      "tags": [
        "dated",
        "feminine",
        "genitive"
      ]
    },
    {
      "form": "тупы́хъ",
      "roman": "tupýx",
      "source": "declension",
      "tags": [
        "dated",
        "feminine",
        "genitive",
        "masculine",
        "neuter"
      ]
    },
    {
      "form": "тупо́му",
      "roman": "tupómu",
      "source": "declension",
      "tags": [
        "dated",
        "dative",
        "masculine",
        "neuter"
      ]
    },
    {
      "form": "тупо́й",
      "roman": "tupój",
      "source": "declension",
      "tags": [
        "dated",
        "dative",
        "feminine"
      ]
    },
    {
      "form": "тупы́мъ",
      "roman": "tupým",
      "source": "declension",
      "tags": [
        "dated",
        "dative",
        "feminine",
        "masculine",
        "neuter"
      ]
    },
    {
      "form": "тупа́го",
      "roman": "tupávo",
      "source": "declension",
      "tags": [
        "accusative",
        "animate",
        "dated",
        "masculine"
      ]
    },
    {
      "form": "тупо́го",
      "roman": "tupóvo",
      "source": "declension",
      "tags": [
        "accusative",
        "animate",
        "dated",
        "masculine"
      ]
    },
    {
      "form": "тупо́е",
      "roman": "tupóje",
      "source": "declension",
      "tags": [
        "accusative",
        "dated",
        "neuter"
      ]
    },
    {
      "form": "тупу́ю",
      "roman": "tupúju",
      "source": "declension",
      "tags": [
        "accusative",
        "dated",
        "feminine"
      ]
    },
    {
      "form": "тупы́хъ",
      "roman": "tupýx",
      "source": "declension",
      "tags": [
        "accusative",
        "animate",
        "dated",
        "feminine",
        "masculine",
        "neuter"
      ]
    },
    {
      "form": "тупо́й",
      "roman": "tupój",
      "source": "declension",
      "tags": [
        "accusative",
        "dated",
        "inanimate",
        "masculine"
      ]
    },
    {
      "form": "тупы́е",
      "roman": "tupýje",
      "source": "declension",
      "tags": [
        "accusative",
        "dated",
        "inanimate",
        "masculine",
        "plural"
      ]
    },
    {
      "form": "тупы́я",
      "roman": "tupýja",
      "source": "declension",
      "tags": [
        "accusative",
        "dated",
        "feminine",
        "inanimate",
        "neuter",
        "plural"
      ]
    },
    {
      "form": "тупы́мъ",
      "roman": "tupým",
      "source": "declension",
      "tags": [
        "dated",
        "instrumental",
        "masculine",
        "neuter"
      ]
    },
    {
      "form": "тупо́й",
      "roman": "tupój",
      "source": "declension",
      "tags": [
        "dated",
        "feminine",
        "instrumental"
      ]
    },
    {
      "form": "тупо́ю",
      "roman": "tupóju",
      "source": "declension",
      "tags": [
        "dated",
        "feminine",
        "instrumental"
      ]
    },
    {
      "form": "тупы́ми",
      "roman": "tupými",
      "source": "declension",
      "tags": [
        "dated",
        "feminine",
        "instrumental",
        "masculine",
        "neuter"
      ]
    },
    {
      "form": "тупо́мъ",
      "roman": "tupóm",
      "source": "declension",
      "tags": [
        "dated",
        "masculine",
        "neuter",
        "prepositional"
      ]
    },
    {
      "form": "тупо́й",
      "roman": "tupój",
      "source": "declension",
      "tags": [
        "dated",
        "feminine",
        "prepositional"
      ]
    },
    {
      "form": "тупы́хъ",
      "roman": "tupýx",
      "source": "declension",
      "tags": [
        "dated",
        "feminine",
        "masculine",
        "neuter",
        "prepositional"
      ]
    },
    {
      "form": "тупъ",
      "roman": "tup",
      "source": "declension",
      "tags": [
        "dated",
        "masculine",
        "short-form"
      ]
    },
    {
      "form": "ту́по",
      "roman": "túpo",
      "source": "declension",
      "tags": [
        "dated",
        "neuter",
        "short-form"
      ]
    },
    {
      "form": "тупа́",
      "roman": "tupá",
      "source": "declension",
      "tags": [
        "dated",
        "feminine",
        "short-form"
      ]
    },
    {
      "form": "тупы́",
      "roman": "tupý",
      "source": "declension",
      "tags": [
        "dated",
        "feminine",
        "masculine",
        "neuter",
        "short-form"
      ]
    },
    {
      "form": "ту́пы",
      "roman": "túpy",
      "source": "declension",
      "tags": [
        "dated",
        "feminine",
        "masculine",
        "neuter",
        "short-form"
      ]
    }
  ]

print(fix_inflections(forms, "tup", "ru"))