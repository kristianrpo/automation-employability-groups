<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Automation Employability Groups</h3>
  <p>Systems Information</p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About the Project</a></li>
    <li><a href="#tools-used-in-development">Tools Used in Development</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#authors">Authors</a></li>
  </ol>
</details>



## About the Project
### Problem

The issue identified in this process mainly lies in the significant amount of manual activities required by [Magneto](https://www.magneto365.com/es) to send job vacancies to employability groups on various platforms. Job vacancy classification must be done manually due to system errors, resulting in a percentage of vacancies being misclassified or incorrectly geographically assigned. Additionally, manual verification is needed to avoid duplicate posts in WhatsApp groups. Furthermore, there is a manual process for creating messages, graphics, and UTM links for the posts and sending all of this to the groups on different platforms.

The current process, which heavily relies on human intervention, does not allow for efficient management of employment groups. Therefore, we identified the need to automate the classification of job vacancies according to the productive sector and their assignment to the corresponding employability groups, ensuring content diversity and avoiding repetitions. Additionally, the exclusive use of WhatsApp as the dissemination platform limits reach to individuals who use other tools in their daily lives.

### Solution

In the employability group automation project, through the n8n platform, the automation of job vacancy sending and classification to employability groups on Telegram was achieved. This allowed Magneto, as an organization, to reach an additional 9,276 people in cities such as Barranquilla, Bogotá, Cartagena, Santa Marta, Medellín, and Ibagué, through attention-grabbing messages that capture people's interest in applying for job opportunities. Previously, this information did not reach this number of people because Magneto was not using Telegram to share job vacancies.

Furthermore, scalability was prioritized in the workflow, allowing it to be used in the future to send job vacancies to other platforms, such as WhatsApp, among others. In this way, Magneto can send a set of critical vacancies to the created flow, which will classify them and send them to the corresponding platform according to the specified sector and the associated groups. This eliminates the need for individuals to manually perform this action, saving time and resources.

The system also implemented notification management for the sending of job vacancies mentioned above, keeping the administrator informed of both successful and failed submissions, making it functional and scalable for different platforms that may be implemented in the future.

Finally, comprehensive documentation was provided on the flow's functionality, credentials, steps required to use the flow, and parameters on how to scale it for different platforms.


**Flow diagram created in n8n:**
<div align="center">
  <img src="https://i.imgur.com/bTF9TqI.png"/> 
</div>

**Image of Magneto's actual automated job vacancy submission to existing employability groups using the implemented system:**
<div align="center">
  <img src="https://i.imgur.com/Uzpdv8h.png"/> 
</div>

**Image of the database with the employability groups offered to the organization, with more than 9,276 people enrolled:**
<div align="center">
  <img src="https://i.imgur.com/0a7eOZE.png"/> 
</div>


## Tools Used in Development
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,fastapi,github,git" />
    <img src = "https://img.godotassetlibrary.com/K_2VqYVfAzYw-kw2ZOukZlCF6_GT9-8phSzRgYpY6QE/rs:fit:1920:1080:0/g:no/aHR0cHM6Ly91cGxvYWQud2lraW1lZGlhLm9yZy93aWtpcGVkaWEvY29tbW9ucy84LzgyL1RlbGVncmFtX2xvZ28uc3Zn.webp" width = 48px style = "border-radius:10px;margin-inline:3px" alt = "telegram"/>
    <img src = "https://avatars.githubusercontent.com/u/45487711?s=200&v=4" width = 48px style = "border-radius:10px;margin-inline:3px" alt = "n8n"/>
  </a>
</p>

## Installation
1. Add the n8n workflow to the workspace. To do this, download the JSON file from [automation-employability-groups](https://github.com/kristianrpo/automation-employability-groups/blob/main/n8n/automation_employability_groups_RPA.json) and import it into a flow in the platform.
2. Follow the [prerequisites](https://github.com/kristianrpo/automation-employability-groups/blob/main/docs/Documentation.md#pre-requisitos-para-funcionamiento) specified in the project documentation to ensure the n8n workflow is fully functional.
3. Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
4. Clone the project 
```bash
  git clone https://github.com/kristianrpo/automation-employability-groups.git
```
5. Set up the virtual environment by navigating to the directory and applying the corresponding command for its proper functioning.
 ```bash
   cd automation-employability-groups
   python -m venv venv 
```
6. Activate the created virtual environment with the corresponding command.
```bash
  ./venv/Scripts/activate
```
7. Install dependencies for the project to work properly.
```bash
  ./venv/Scripts/activate
```
8. Run the FastAPI application.
```bash
  uvicorn main:app --reload
```
9. Now, the n8n workflow can connect to the endpoint to allow the sending of job vacancies to the Telegram platform and future implementations.

## Usage
A set of critical job vacancies to be sent to certain platforms, along with the necessary attributes for each vacancy as specified in the documentation, is sent to the endpoint generated by n8n.

Subsequently, the n8n workflow will process the vacancy and, based on the associated sector ID and platform, it will classify the vacancy accordingly and send the necessary data to the FAST API endpoint.

The FASTAPI endpoint receives the data and utilizes the APIs of the various platforms to send the vacancy to the correct group.

Here’s the translation to English in Markdown format:

## Authors
The project was created by:

- Kristian Restrepo Osorio
- Sebastian Restrepo Ortiz
- Luisa María Álvarez García
- Miguel Ángel Martínez García

