<h1 align="center"> Cowin Notifier </h1>
<div align= "center">
  <img src="https://www.scnsoft.com/blog-pictures/testing/mobile-automated-testing-with-selenium-01.png" width="350" height="200"/>
  <h3>Cowin Notifier is Automation systeam built with Selenium using Chromedriver for a alert user to Vaccination center's are available in your area. PyQt5 use for convert script into a beautiful GUI.</h3>
</div><br>
<div align="center">

[![Python](https://img.shields.io/badge/python-3.8-brightgreen)](https://www.python.org)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15.4-orange)](https://www.qt.io)
[![selenium](https://img.shields.io/badge/SELENIUM-3.14-blue)](https://www.selenium.dev)
[![anaconda](https://img.shields.io/badge/Anaconda.org-1.3.1-blue)](https://www.anaconda.com/open-source)

![relase](https://img.shields.io/badge/release-v0.0.08-red)
![contib](https://img.shields.io/badge/contributions-welcome-brightgreen)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/dharmrajchauhan/)<br>
</div>


## :innocent: Motivation
In a current scenario Cowin/Covishield Vaccine is most important for safety purpose. And as we know, we are the second largest family in the world with 136.64 crore members. 
So it's quite impossible for the government to make the vaccine available to all the people. So as dev we trying to make a GUI which can notify you when slots are open in your area.

## :hourglass: Project Demo
:movie_camera: [YouTube Demo Link](https://youtu.be/)

:computer: [Software Link](https://drive.google.com/file/d/1rzxosnwBokQ6JddCnKN5v6L3Oqq5T69H/view?usp=sharing)

## :warning: TechStack/framework used

- [selenium](https://www.selenium.dev)
- [PyQt5](https://www.qt.io)
- [pyinstaller]()

## :sleeping: Working
<h4> How To use </h4>
<br><h4>1.  Provide a Pin of your area and choose your eligibility criteria</h4>
<img src="https://user-images.githubusercontent.com/84271454/128645300-ee60427b-61a7-438f-99b7-8c4a1b7036d7.jpg" width="1000" height="500">

---

<br><h4>2.  Provide a State & City Name of your location and choose your eligibility criteria.</h4>
<img src="https://user-images.githubusercontent.com/84271454/128645304-4fb56e1a-0aa5-47d7-aad7-fae6f4b71304.jpg" width="1000" height="500">

---

As you see in the the above both images, all the data which you require to know are displayed on the Table. So you can easily register for vaccination. And don't worry, you dont
need to seat whole day in front of the pc to check this results. Whenever script find the result it will alert you via the alert sound.

## :sweat: Problems
i know so many questions are come to your mind. okkk, so first start with the problems. 

When the first time goverment was release www.cowin.gov their api which work completely fine but after some time due to improper and heavy use, indian gov make some rules and regulation for api use. its also not big problem for devs, but then after, they stricaly put limit of featching data and now it create problem for small devs. 

So as a alternative solustion we deside to use selenium web-browser also selenium have their own 2 benefits.
1.  Selenium have ability to create fake_user_agent.
2.  Selenium is much faster for grabbing data and connect with the (Qt5)Software development and (Kavy)app development.

i am little worried about the timing of data featch and page refreshing time. But don't worry we would handle this thing with very carefully.
we try to reduce the complexity by not adding Exception conditions. so you can find some bugs somewhere, but dont worry it will not effect more.

First time it take 0.0.9 second to grab the result from web. but then after it take only 0.0.2 secs. And it's quite descent results but its good to going with it.




