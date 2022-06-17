# Hammer of the Year

## Creator: Luke Back

### Objective

To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.  

### Project

Functioning web application where West Ham fans can vote for their Hammer of the year (player of the season) and register their name and reason as a voter.
The functionality of this application will include the following:  

#### Create
-	Add Players
-	Add Voters

#### Read
-	View Players
-	View Voters

#### Update
-	Edit Players
-	Edit Voters

#### Delete
-	Remove Players
-	Remove Voters

### The requirements to create the specified project will include the following:

* Kanban Board: Jira
* Database: GCP SQL Server
* Programming language: Python
* Unit Testing with Python (Pytest)
* Integration Testing with Python (Selenium)
* Front-end: Flask (HTML)
* Version Control: Git
* CI Server: Jenkins
* Cloud server: GCP Compute Engine
* IDE: VS Code

### Planning, Designing and Tracking

### Jira
For planning I used a Kanban board on Jira to help me keep on top of what tasks needed to be completed, what was currently in progress and what had been completed.   
I also added user stories to the board to plan what needed to be achieved.  
![Jira Tasks](https://user-images.githubusercontent.com/100779613/174315665-23e4b575-39b3-4325-8fce-9aa8bd9a8165.png)

### ERD
The Entity Relationship Diagram helped me visualise the data between tables and they relationship they share.  
This made structuring my database easier by following the ERD and to create this I used drawio.  
![ERD](https://user-images.githubusercontent.com/100779613/174315780-054822fd-3bcc-48dd-aeea-7118a06e1660.png)

### Risk Assessment
The risk assessment was created to evaluate any known threats to the project and what measures could be taken to prevent these from occurring.  
![Risk Assessment](https://user-images.githubusercontent.com/100779613/174315844-f69382d1-f3a5-4118-9dc1-ce4105fb6c5c.png)

### Front End
For the front end of my application I used html for the design and functionality.  
Once started you arrive at the home page and can navigate to different parts of the website.  
![Front End - Home](https://user-images.githubusercontent.com/100779613/174316121-2eebb110-3145-4341-a3e7-8940303426ba.png)
When navigating to the below page you can add a player.  
![Front End - Add Players](https://user-images.githubusercontent.com/100779613/174316187-246f6f9f-709b-4e64-b1a8-e1a363a0f85c.png)
Here you can add a voter.  
![Front End - Add Voters](https://user-images.githubusercontent.com/100779613/174316236-1dbee3fe-085f-4022-9bbc-80f5dcaafe36.png)
Here you can view the players added and either update or delete them.  
![Front End - View Players](https://user-images.githubusercontent.com/100779613/174316336-b88d9b4e-c752-4588-a84e-d8cf87f9230b.png)
Here you can view the voters added and either update or delete them.  
![Front End - View Voters](https://user-images.githubusercontent.com/100779613/174316415-aa160255-f1ce-4634-9ad9-d1f0927d6877.png)
Here you can update existing players.  
![Front End - Update Player](https://user-images.githubusercontent.com/100779613/174316466-de6e0e60-bf2d-4efc-ac33-f999f86e631c.png)
Here you can update existing voters.  
![Front End - Update Voter](https://user-images.githubusercontent.com/100779613/174316498-4779d129-847b-4949-be10-594472f0c845.png)

### Testing
I carried out several unit tests using pytest to assess the apps CRUD functionality. For the tests carried out I achieved 100% coverage.  
![testing](https://user-images.githubusercontent.com/100779613/174316660-dd289068-8f46-48bf-a67d-3cb6a0c8510a.png)

### Issues encountered
I originally started the project with a more complex idea in voting for a player, team & manager of the season.  
This became far too complicated for my current skillset and knowledge, so I decided to start again with a more simple idea.  
Time and knowledge contraints were a big obstacle as I was constantly referring to resources to ensure the work being completed was correct.  
Using GCP for virtual machines was a challenge in itself as I was regularly disconnecting from the server and also struggled to create new instances.  

### Future improvements
I will revisit the application to add greater functionality with more entities and improve the design.  
Due to the difficulties I experienced I didnt manage to use Jenkins. I have no experience even learning this so far, so I will need to catch up on it.  

### Contributors:
Luke Back  

### Acknowledgements:
QA, Earl-Leon-Adam, Resources  
