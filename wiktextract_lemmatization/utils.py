import json
import unicodedata


def remove_accents(word):
    # print("Removing accent marks from query ", word)
    ACCENT_MAPPING = {
        "́": "",
        "̀": "",
        "а́": "а",
        "а̀": "а",
        "е́": "е",
        "ѐ": "е",
        "и́": "и",
        "ѝ": "и",
        "о́": "о",
        "о̀": "о",
        "у́": "у",
        "у̀": "у",
        "ы́": "ы",
        "ы̀": "ы",
        "э́": "э",
        "э̀": "э",
        "ю́": "ю",
        "̀ю": "ю",
        "я́́": "я",
        "я̀": "я",
    }
    word = unicodedata.normalize("NFKC", word)
    for old, new in ACCENT_MAPPING.items():
        word = word.replace(old, new)
    return word


CYRILLIC_LANGUAGES_WITH_HELPING_STRESS = [
    "ru",
    "uk",
    "be",
    "bg",
#    "sr", Really no idea
#    "sh",
]


def remove_macrons_etc_from_latin(word: str):
    return (
        word.replace("ā", "a")
        .replace("ē", "e")
        .replace("ī", "i")
        .replace("ō", "o")
        .replace("ū", "u")
        .replace("Ā", "A")
        .replace("Ē", "E")
        .replace("Ī", "I")
        .replace("Ō", "O")
        .replace("Ū", "U")
        .replace("ă", "a")
        .replace("ĕ", "e")
        .replace("ĭ", "i")
        .replace("ŏ", "o")
        .replace("ŭ", "u")
        .replace("Ă", "A")
        .replace("Ĕ", "E")
        .replace("Ĭ", "I")
        .replace("Ŏ", "O")
        .replace("Ŭ", "U")
    )


def form_is_canonical(form: dict):
    return "tags" in form and "canonical" in form["tags"]


FORM_TAGS_TO_IGNORE = ["table-tags", "auxiliary", "class", "inflection-template"]


def form_has_ignored_tags(form: dict):
    return "tags" in form and any(tag in FORM_TAGS_TO_IGNORE for tag in form["tags"])


def fix_inflections(forms: list, lemma: str, language_code: str):
    """It adds another """
    fixed_forms = []

    for form in forms:
        if form_has_ignored_tags(form): # auxiliary is relevant for German and Danish
            continue
        if language_code in CYRILLIC_LANGUAGES_WITH_HELPING_STRESS:
            if form_is_canonical(form):
                fixed_forms.append(form)
            else:
                fixed_forms.append(form)
                if remove_accents(form["form"]) != form["form"]:
                    fixed_forms.append(
                        {"form": remove_accents(form["form"]), "tags": form["tags"]}
                    )
        elif language_code == "la":
            if form_is_canonical(form):
                fixed_forms.append(form)
            else:
                if remove_macrons_etc_from_latin(form["form"]) != form["form"]:
                    fixed_forms.append(
                        {
                            "form": remove_macrons_etc_from_latin(form["form"]),
                            "tags": form["tags"],
                        }
                    )
        else:
            fixed_forms.append(form)

    return fixed_forms
    # TODO: Fix the cases where the inflection tables have something like "will eat", "has eaten"
