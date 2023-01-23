Welcome to "My Task Manager"!

This web application allows users to have:

- An active task checklist
- Task organization through "Projects"

##################################################################

TECHNOLOGIES USED

This project was created to showcase the use of the Django framework, specifically Django's Model-View-Tenplate (MVT) architecture.

The project that was created is called "tracker", where three application were installed within it:
- accounts
- projects
- tasks

"accounts" application

    Models:
        - NA

    Views:
        - signup

    Templates:
        - login.html
        - signup.html


"projects" application

    Models:
        - Project

    Views:
        - ProjectListView
        - ProjectDetailView
        - ProjectCreateView

    Templates:
        - base.html
        - create.html
        - detail.html
        - list.html


"tasks" application

    Models:
        - Task


    Views:
        - TaskCreateView
        - TaskListView
        - TaskUpdateView

    Templates:
        - create.html
        - list.html


##################################################################

USING THIS APPLICATION | PAGE LAYOUT

On the top of every page, there will be three links to choose from. These links give you the option to:

- view tasks
- view projects (home page)
- logout


The first page after logging in is the "My Projects" page, which also is the home page. Here users can:

- create a new project
- view projects they are involved in


When navigating to the "Create a new project" link, the user will be brought to the "Create a new project" page. The user can then create a new project by entering the following information:

- project name
- project description
- user delegation (Who the project will be assigned to. A list of active users will be displayed where they can be chosen.)


When navigating to current projects on the home page, the user will be brought to a page that is specific to the project chosen. on this page they will see:

- description for the project
- the option to create a new task
- a list of tasks for the project
- each entry in the list will have the name of the project, whom it was assigned to, the start date, due date, and a status that indicates whether the task has been completed or not.


when navigating to "My tasks", the user will be brought to a page that lists out their tasks. The user will see:

- name of task
- start date of task
- end date of task
- is completed status (toggling the "complete" button will change the status to "true"). Toggling this will change the status on other applicable pages.

##################################################################
