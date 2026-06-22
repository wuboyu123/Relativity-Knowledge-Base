---
title: "Supported languages matrix"
url: https://help.relativity.com/Server2025/Content/Solutions/Supported_languages_matrix.htm
collection: user
fetched_at: 2026-06-22T06:21:18+00:00
sha256: 9ae5a322abc6544c32ec0ccef0e287e271ea47595e1c8e95f2696cdb94ca04f8
---

Supported languages matrix Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Supported languages matrix

This table displays each language supported by a Relativity feature and its corresponding functionality status. The features include OCR , Assisted Review , Structured Analytics , Processing , and the Viewer . Stemming, date recognition, and querying on abbreviations (i.e., a single letter followed by a period) are only available in English text in a dtSearch index. The SQL Server settings determine the languages available for word-break characters used in the full text index.

Use the following resources for more information on SQL Server and dtSearch supported languages:

- See this site for a list of search features for languages supported by dtSearch.

- See this site for a list of Unicode supported languages also supported by dtSearch.

- See this site for a list of SQL Server supported languages.

See Command line import for a complete list of alternate language encoding values and Importing document metadata, files, and extracted text for instructions on importing documents with the Relativity Desktop Client and selecting the appropriate file encoding value.

- √ - indicates that the language is supported.

- √* - indicates that the language must be installed in the Microsoft operating system for the viewer to function. Specifically, you must install the language to the web server, conversion agent server, and local workstation.

- If the cell is empty, the feature is not supported.

## Special considerations

Note the following details about the supported languages:

-

dtSearch in Relativity is accent-insensitive by default. This means characters with accent marks and other diacritics are stored in the same fashion as those without those marks. If you need to perform a search that includes accents, change the Create Accent Sensitive setting on the dtSearch index to Yes.

- Indexing in SQL is based on the character set of the language you select. Western languages are similar grammatically, which means that you should experience no issues when searching for English words with SQL. In addition, SQL tokenization is only used for symbols that mean one thing when they are alone, but something else when they are put together with other symbols, such as with CJK languages.

-

Conceptual Analytics and Classification indexes are language-agnostic and therefore support all languages. Categorization does not display Unicode choices in the field tree properly.

## Supported languages

Language OCR Processing Native Imaging Structured Analytics Language Identification Viewer

English √ √ √ √ √

Abkhazian √

Afar √

Afrikaans √ √ √ √ √

Akan √

Albanian √ √ √ √ √

Amharic √

Arabic √ √ √ √ √ *

Armenian √ √ √ √ *

Assamese √

Aymara √ √ √ √ √

Azerbaijani √

Bashkir √

Basque √ √ √ √ √

Belarusian √ √ √

Bengali √

Bemba √ √ √ √

Bihari √

Bislama √

Blackfoot √ √ √ √

Bosnian √

Breton √ √ √ √ √

Bugotu √ √ √ √

Bulgarian (Cyrillic) √ √ √ √ √

Byelorussian (Cyrillic) √ √ √ √ √

Burmese √

Catalan √ √ √ √ √

Cebuano √

Chamorro √ √ √ √

Chechen √ √ √ √

Cherokee √

Chinese (Simplified) √ √ √ √ √ *

Chinese (Traditional) √ √ √ √ √ *

Chuana or Tswana √ √ √ √

Corsican √ √ √ √ √

Croatian √ √ √ √ √

Crow √ √ √ √

Czech √ √ √ √ √

Danish √ √ √ √ √

Dhivehi √

Dholuo √

Dutch √ √ √ √ √

Dzongkha √

Eskimo √ √ √ √

Esperanto √ √ √ √ √

Estonian √ √ √ √ √

Ewe √

Faroese √ √ √ √ √

Fijian √ √ √ √ √

Finnish √ √ √ √ √

French √ √ √ √ √

Frisian √ √ √ √ √

Friulian √ √ √ √

Ga √

Gaelic Irish √ √ √ √

Gaelic Scottish √ √ √ √

Galician √ √ √ √ √

Ganda or Luganda √ √ √ √ √

Georgian √ √ √ *

German √ √ √ √ √

Greek √ √ √ √ √

Greenlandic √

Guarani √ √ √ √ √

Gujarati √

Haitian Creole √

Hani √ √ √ √

Hausa √

Hawaiian √ √ √ √ √

Hebrew √ √ √ √ √ *

Hindi √

Hmong √

Hungarian √ √ √ √ √

Icelandic √ √ √ √ √

Ido √ √ √ √

Igbo √

Indic Languages √ *

Indonesian √ √ √ √ √

Interlingua √ √ √ √ √

Interlingue √

Inuktitut √

Inupiak √

Irish √

Italian √ √ √ √ √

Japanese √ √ √ √ √ *

Javanese √

Kabardian √ √ √ √

Kannada √

Kashmiri √

Kashubian √ √ √ √

Kawa √ √ √ √

Kazakh √

Khasi √

Khmer √

Kikuyu √ √ √ √

Kinyarwanda √

Kongo √ √ √ √

Korean √ √ √ √ √ *

Kpelle √ √ √ √

Krio √

Kurdish √ √ √ √ √

Kyrgyz √

Laothian √

Latin √ √ √ √ √

Latvian √ √ √ √ √

Limbu √

Lingala √

Lithuanian √ √ √ √ √

Lozi √

Luba √ √ √ √

Lule Sami √ √ √ √

Luxembourgian √ √ √ √ √

Macedonian (Cyrillic) √ √ √ √ √

Malagasy √ √ √ √ √

Malay √ √ √ √ √

Malayalam √

Malinke √ √ √ √

Maltese √ √ √ √ √

Manx √

Maori √ √ √ √ √

Marathi √

Mauritian Creole √

Mayan √ √ √ √

Miao √ √ √ √

Minankabaw √ √ √ √

Mohawk √ √ √ √

Moldavian (Cyrillic) √ √ √ √

Mongolian √

Montengrin √

Nahuatl √ √ √ √

Nauru √

Nepali √

Newari √

Northern Sami √ √ √ √

Norwegian √ √ √ √ √

Norwegian Nynorsk √

Nyanja √ √ √ √ √

Occidental √ √ √ √

Occitan √

Ojibway √ √ √ √

Oriya √

Oromo √

Ossetian √

Pampanga √

Papiamento √ √ √ √

Pashto √

Pedi √

Persian √

Pidgin English √ √ √ √

Polish √ √ √ √ √

Portuguese √ √ √ √ √

Portuguese (Brazilian) √ √ √ √ √

Provencal √ √ √ √

Punjabi √

Quechua √ √ √ √ √

Rajasthani √

Rhaetic √ √ √ √

Rhaeto - Romance √

Romanian √ √ √ √ √

Romany √ √ √ √

Ruanda √ √ √ √

Rundi √ √ √ √ √

Russian (Cyrillic) √ √ √ √ √

Sami √ √ √ √

Samoan √ √ √ √ √

Sango √

Sanskrit √

Sardinian √ √ √ √

Scots √

Scottish Gaelic √

Serbian (Cyrillic) √ √ √ √ √

Serbian (Latin) √ √ √ √ √

Seselwa √

Sesotho √

Shona √ √ √ √ √

Sindhi √

Sinhalese √

Sioux √ √ √ √

Siswant √

Slovak √ √ √ √ √

Slovenian √ √ √ √ √

Somali √ √ √ √ √

Sotho, Suto, or Sesuto √ √ √ √

Southern Sami √ √ √ √

Spanish √ √ √ √ √

Sundanese √

Swahili √ √ √ √ √

Swazi √ √ √ √

Swedish √ √ √ √ √

Syriac √

Tagalog √ √ √ √ √

Tahitian √ √ √ √

Tajik √

Tamil √

Tatar √

Telugu √

Thai √ √ √ √ √ *

Tibetan √

Tigrinya √

Tinpo √ √ √ √

Tonga √

Tongan √ √ √ √

Tshiluba √

Tsonga √

Tswana √

Tumbuka √

Tun √ √ √ √

Turkish √ √ √ √ √

Turkmen √

Twi √

Uighur √

Ukrainian (Cyrillic) √ √ √ √ √

Urdu √

Uzbek √

Venda √

Vietnamese √ √ √ √ *

Visayan √ √ √ √

Volapuk √

Waray-Waray √

Welsh √ √ √ √ √

Wend or Sorbian √ √ √ √

Wolof √ √ √ √ √

Xhosa √ √ √ √ √

Yiddish √

Yoruba √

Zapotec √ √ √ √

Zhuang √

Zulu √ √ √ √ √

See Command line import for a complete list of supported languages encoding values.

On this page

- Supported languages matrix

- Special considerations

- Supported languages


Why was this not helpful?

Check one that applies.

I could not find the information I was looking for.

The information was incorrect.

The instructions are confusing or unclear.

The instructions did not work.

Thank you for your feedback.

Want to tell us more?


Great!

Thanks for taking the time to provide feedback.


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use
