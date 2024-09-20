# Sign Language Detector

🛠️ This project identifies sign language symbols and translates them into words. It was trained using Teachable Machine and is deployed via Flask, allowing users to interact with it using hand symbols.<br>
<br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="33" alt="python logo"  />
<img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="30" alt="html5 logo"  />
<img width="12" />
<img src="https://upload.wikimedia.org/wikipedia/commons/3/32/OpenCV_Logo_with_text_svg_version.svg" height="35" alt="open cv" />
<img width="12" />
<img src="https://miro.medium.com/v2/resize:fit:600/0*2E9-J5WPFbVI_d32" height="35" width="45" alt="vscode logo"  />
<img width="12" />
## Video Demo
🎥 Here you can find a video of the working project


## Prerequisites

🚨 There is a pretrained model already available. <br>

 (**Optional**) But if you want to make custom dataset use 👉 [Teachable Machine](https://teachablemachine.withgoogle.com/train/image). Before downloading you custom model you have to grab pictures of all sign languages explained in **Deployment** process.  



## Deployment

To run this project first clone this repository using

```bash
  git clone https://github.com/aka-Harsh/Sign-Language-Detection.git
```
Locate this repository using terminal and then create a virtual enviroment and activate it using

```bash
  python -m venv venv
  venv\Scripts\activate
```
Perform this in your VScode editor to select python intepreter
```bash
  Select View > Command Palette > Python: Select Interpreter > Enter Interpreter path > venv > Script > python.exe
```

Install all the required packages 
```bash
  pip install -r requirements.txt
```

Run the **datacollection.py** file to take the pictures of different sign language symbols pictures 🚨 ***(use help.txt for more info)***
```bash
  python datacollection.py
```

Finally run the app.py file
```bash
  python app.py
```

## Project Outlook
<br>
