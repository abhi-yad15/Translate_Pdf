# Translate PDF from one language to another
This repository contains the code to translate any PDF document from one language to another.

## Getting Started
 At first you need to have "python3" installed on your system and you also need to have some python libraries.
 1. Selenium & chromedriver
 2. python-docx 
 3. googletrans
 
 As we are using "googletrans" library so our IP will get blocked after few requests, so we need to use VPN, for Windows i have included "psiphon3" in the repository, you may use VPN of your choice. Remember to change the country for tranlating the second pdf.
### Prerequisites

To install Selenium use 

```
pip install selenium
```
To install python-docx use 

```
pip install python-docx
```
To install googletrans use 

```
pip install googletrans
```

I have included a chromedriver.exe in the repository but you may need different version of chromedriver based on the version of you chrome browser. You can download the suitable version for you from [here](https://chromedriver.chromium.org/downloads).

### Using

To use the above code.
1. Download the repository.
2. Start the VPN.
3. Install all the requirements
4. Open Command Prompt(cmd) and type 

```
python translate.py "Name of the pdf" "Language to Change{Abbreviation (See below)}"
```

For Example

```
python translate_pdf.py Maths.pdf hi
```

## Abbreviation For Few Language

1. Hindi- hi
2. English -en
3. Nepali -ne
4. Punjabi -pa
5. Urdu -ur

For other languages's abbreviation check [here](https://cloud.google.com/translate/docs/languages).
### Steps involved

After doing the above steps, you will see a browser pop up, which will basically open chromedriver to convert pdf to docx. Then after that you will see your pdf is being tranlated (check cmd). After few minutes the pdf will get translated. 

### Error

1. In case you see some errors like "Error code(0) or char (0)" that means Google has blocked your IP, try changing the country (location) in your VPN and try again.
2. In case of some HTTPS error try doing the same.


## Built With

* [Python3](https://www.python.org/) - Python3
* [Selenium](https://www.seleniumhq.org/) -Selenium
* [Googletrans](https://pypi.org/project/googletrans/) - Googletrans
* [python-docx](https://pypi.org/project/python-docx/)- python-docx
