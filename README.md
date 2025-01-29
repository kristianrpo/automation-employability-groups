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

To use the system, a set of critical job vacancies needs to be prepared and sent to the endpoint generated by n8n. Each job vacancy must include the necessary attributes, which are specified in the project documentation (e.g., sector ID, platform ID, job title, location, etc.).

### Step-by-Step Workflow:
1. **Send Job Vacancies**: The process begins by sending a batch of job vacancies to the n8n workflow. Each job vacancy must contain the following attributes:
    - **Sector ID**: The ID associated with the productive sector to which the job belongs.
    - **Platform ID**: The ID associated with the platform (e.g., Telegram, WhatsApp, etc.) where the job should be sent.
    - **Job Details**: Includes the job title, description, location, salary, and other relevant information.
   
2. **Process in n8n**: Once the job vacancies are sent, the n8n workflow starts processing each vacancy. It checks the **sector ID** and **platform ID** associated with each vacancy:
    - **Classification**: Based on the sector and platform, n8n classifies the job vacancy accordingly.
    - **Data Formatting**: The necessary data for the job vacancy is formatted for the respective platform (e.g., Telegram message format, WhatsApp format).

3. **Send to FAST API Endpoint**: After processing, the n8n workflow sends the classified and formatted data to the **FASTAPI endpoint**.

4. **FASTAPI Processing**: The FASTAPI endpoint receives the formatted job vacancy data and processes it by using the appropriate APIs for each platform:
    - **Platform Integration**: The system integrates with the APIs of various platforms (e.g., Telegram) to send the job vacancy to the corresponding group or channel.
    - **Group Assignment**: Based on the classification and platform, the job vacancy is assigned to the correct group on the platform.

5. **Notification and Logging**: The system keeps the administrator informed of the status of each job vacancy submission, providing notifications about successful submissions and failed attempts for better tracking and debugging.

### Additional Features:
- **Scalability**: This system is scalable, meaning additional platforms can be added in the future (e.g., WhatsApp, Facebook Messenger) without major changes to the workflow.
- **Error Handling**: The workflow includes error handling mechanisms to ensure that if any job vacancy fails to be sent, the issue can be quickly identified and addressed.
- **Reporting**: The system can provide logs or reports on job vacancy submissions, detailing how many were successfully sent, to which platform, and any failures that occurred during the process.

This automation eliminates the need for manual intervention in sending job vacancies, allowing Magneto to efficiently reach a broader audience across multiple platforms while reducing human error.

---

### Why This Is Important
The primary goal of this automation is to enhance the reach and efficiency of job vacancy distribution to employability groups. By automating the process, Magneto can:
- Improve accuracy in categorizing and sending job vacancies.
- Increase the reach to a larger audience by leveraging multiple platforms.
- Save time and resources by eliminating manual efforts.

This system enables a more streamlined, efficient, and scalable process for managing job vacancy distribution across platforms.


## Authors
The project was created by:

- Sebastian Restrepo Ortiz : Lead Developer
- Kristian Restrepo Osorio : Automation Developer
- Luisa María Álvarez García : Backend Developer
- Miguel Ángel Martínez García : Automation Developer

