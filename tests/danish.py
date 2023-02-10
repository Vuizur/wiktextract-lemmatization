from wiktextract_lemmatization.utils import fix_inflections


forms_danish = [
    {
      "form": "aede",
      "tags": [
        "past"
      ]
    },
    {
      "form": "aet",
      "tags": [
        "participle",
        "past"
      ]
    },
    {
      "form": "",
      "source": "inflection",
      "tags": [
        "table-tags"
      ]
    },
    {
      "form": "da-conj",
      "source": "inflection",
      "tags": [
        "inflection-template"
      ]
    },
    {
      "form": "aer",
      "source": "inflection",
      "tags": [
        "present"
      ]
    },
    {
      "form": "aede",
      "source": "inflection",
      "tags": [
        "past"
      ]
    },
    {
      "form": "har aet",
      "source": "inflection",
      "tags": [
        "perfect",
        "present"
      ]
    },
    {
      "form": "havde aet",
      "source": "inflection",
      "tags": [
        "past",
        "perfect"
      ]
    },
    {
      "form": "aes",
      "source": "inflection",
      "tags": [
        "passive",
        "present"
      ]
    },
    {
      "form": "aedes",
      "source": "inflection",
      "tags": [
        "passive",
        "past"
      ]
    },
    {
      "form": "aende",
      "source": "inflection",
      "tags": [
        "participle",
        "present"
      ]
    },
    {
      "form": "aet",
      "source": "inflection",
      "tags": [
        "participle",
        "past"
      ]
    },
    {
      "form": "a",
      "source": "inflection",
      "tags": [
        "imperative",
        "present"
      ]
    },
    {
      "form": "-",
      "source": "inflection",
      "tags": [
        "imperative",
        "past"
      ]
    },
    {
      "form": "ae",
      "source": "inflection",
      "tags": [
        "infinitive",
        "present"
      ]
    },
    {
      "form": "-",
      "source": "inflection",
      "tags": [
        "infinitive",
        "past"
      ]
    },
    {
      "form": "have",
      "source": "inflection",
      "tags": [
        "auxiliary",
        "present"
      ]
    },
    {
      "form": "-",
      "source": "inflection",
      "tags": [
        "auxiliary",
        "past"
      ]
    },
    {
      "form": "aen",
      "source": "inflection",
      "tags": [
        "gerund",
        "present"
      ]
    },
    {
      "form": "-",
      "source": "inflection",
      "tags": [
        "gerund",
        "past"
      ]
    }
  ]
    
print(fix_inflections(forms_danish, "æble", "da"))