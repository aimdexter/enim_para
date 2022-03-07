# enim_para
<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://cdn-05.9rayti.com/rsrc/cache/widen_292/uploads/2012/07/mines-rabat-logo.png" alt="Logo" >
  </a>

  <h3 align="center">ENSMR: Ecole Nationale Supérieure des Mines de Rabat</h3>

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>SOMMAIRE</summary>
  <ol>
    <li>
      <a href="#INTRODUCTION">INTRODUCTION</a>
      <ul>
        <li><a href="#Réaliser_Avec">Réaliser Avec</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## INTRODUCTION
<div align="center">
  
[![Product Name Screen Shot][product-screenshot]](https://example.com)
  
</div>
Mise en Contexte:
Le parascolaire représente l'échappatoire choisi par la quasi-totalité des Enimistes à tous
ces efforts acharnés exercés lors de leurs études .En effet s’adonner à des activités
ludiques parallèlement au parcours scolaire quelles qu'elles soient, est essentiel à
L'ENSMR du fait qu'elles sont le gage d'une meilleure adaptation à la vie scolaire et
sociale .
Néanmoins il arrive que les élèves ingénieurs confrontent des contraintes qui nuisent à
leur amusement et leur divertissement .
En effet la planification des réunions, l'avancement et le suivi des tâches se discutaient
auparavant bel et bien sur les deux réseaux sociaux : Facebook et WhatsApp. Et comme
le savons tous ces deux dernières plateformes ne sont ni efficaces ni professionnelles
pour la gestion de telles activités . Du coup l'intervention d'une nouvelle application
adaptée aux divers exigences mentionnées serai une solution efficace pour y remédier .

Motivation Et Objectifs:
* Pour les problèmes cités précédemment, la réalisation d'une application de gestion du
parascolaire est nécessaire . Notre application mobile a pour but de digitaliser et
centraliser le déroulement des activités parascolaires . En effet cette application va aider
le responsable des activités parascolaires, les présidents des clubs et comités ainsi que
les chefs de cellules à être plus efficaces dans la gestion du suivi des tâches . Aussi elle
permettra les membres des clubs et comités à être à jour et toujours au courant de
l'avancement des évènements.

<p align="right">(<a href="#top">back to top</a>)</p>



### 💼 Réaliser_Avec

![](https://img.shields.io/badge/Design-figma-informational?style=flat&logo=figma&logoColor=white&color=4AB197)
<br>

![](https://img.shields.io/badge/Code-HTML5-informational?style=flat&logo=html5&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Style-CSS-informational?style=flat&logo=css3&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Style-Tailwind-informational?style=flat&logo=Tailwind-CSS&logoColor=white&color=4AB197)
<br>

![](https://img.shields.io/badge/Code-python-informational?style=flat&logo=python&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Code-django-informational?style=flat&logo=django&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Code-JavaScript-informational?style=flat&logo=JavaScript&logoColor=white&color=4AB197)
<br>

![](https://img.shields.io/badge/Db-MySQL-informational?style=flat&logo=MySQL&logoColor=white&color=4AB197)
<br>

![](https://img.shields.io/badge/Hosting-herokul-informational?style=flat&logo=heroku&logoColor=white&color=4AB197)


![](https://img.shields.io/badge/Tools-Actions-informational?style=flat&logo=github-actions&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Tools-NPM-informational?style=flat&logo=npm&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Tools-GitHub-informational?style=flat&logo=GitHub&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Tools-Jira-informational?style=flat&logo=Jira-Software&logoColor=white&color=4AB197)
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps.

### Prerequisites

* Operating system : Centos 8
  
* Python 3.10
  
  ```sh
  https://tecadmin.net/how-to-install-python-3-10-on-centos-rhel-8-fedora/ 
  ```

* Mysql

  ```sh
  https://www.linuxcapable.com/how-to-install-mysql-8-0-on-centos-8-stream/
  https://dev.to/sm0ke/how-to-use-mysql-with-django-for-beginners-2ni0
  ```
  
* Pipenv : virual environment 

  ```sh
  https://pipenv.pypa.io/en/latest/
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/aimdexter/enim_para.git
   ```
2. Install packages
   ```sh
   pipenv shell
   pip install -r requirements.txt
   ```
3. Populate DB 
   ```sh
   cd core
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Run server 
   ```sh
   python manage.py runserver
   ```
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Python v 3.10 installation
- [x] Django v 4.0.1 installation
- [x] Core project initialized
- [x] Mysql database requirements installed
- [x] Paramin DB created
- [x] Core project DB switched from Sqllite to newly created Mysql DB
- [ ] Main configuration :
    - [x] Create main apps
    - [ ] Create all apps
    - [x] Set up basic models
    - [ ] Set up all models
    - [x] Set up superuser
- [x] Link Django Core and different apps to Tailwindcss style sheet
- [ ] final design
- [ ] Different pages
- [ ] Moroccan payment CMI
- [ ] International payment 💳 VISA 💳 MASTERCARD
- [ ] Migrate from monolithic architecture to microservices :
    - [ ] APIs
    - [ ] front-end ---> Nextjs
    - [ ] Hosting DB ---> AWS vs ENIM SERVERS
    - [ ] Hosting Back-end ---> AWS vs ENIM SERVERS
    - [ ] Hosting front-end ---> VERCEL


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the Apache License 2.0. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Django documentation](https://docs.djangoproject.com/en/4.0/)
* [How To Structure Your Django Project](https://python.plainenglish.io/how-to-structure-your-django-project-a5d50333a644)
* [How to Install MySQL 8.0 on CentOS 8 Stream](https://www.linuxcapable.com/how-to-install-mysql-8-0-on-centos-8-stream/)
* [How to use MySql with Django - For Beginners](https://dev.to/sm0ke/how-to-use-mysql-with-django-for-beginners-2ni0)
* [Django Tailwind’s documentation](https://django-tailwind.readthedocs.io/en/latest/)
* [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/connector-python-django-backend.html)
* [How to Manage your Python Projects with Pipenv & Pyenv](https://www.rootstrap.com/blog/how-to-manage-your-python-projects-with-pipenv-pyenv/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: paraenim.png
