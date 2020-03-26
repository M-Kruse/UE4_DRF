# UE4-DRF

![image](https://user-images.githubusercontent.com/46699116/77597640-c10d4200-6ebc-11ea-8f23-81af5ad043fd.png)

![Preview Video](https://imgur.com/a/DQ440Cl)

This project is for playing around with some UE4 game concepts and learning more about REST API at the same time.

This is using

* Unreal Engine 4 (UE4)
* VARest
* Django REST Framework (DRF)

Currently there are demonstrations for CRUD logic with an example item. To progress into the demo room, the API will need to be online. The API heartbeat logic will unlock the door to proceed into the examples.

The UE4 project is being set up with authoritiative server logic. Anything critical to the gameplay should be stored/handled by the dedicated server which acts as the authority to clients.  Clients communicate with the server and the server communicates with the API.

Features

- [x] UE4 Item Class With API Support
- [x] CRUD Logic For Items
- [ ] Item Persistence
- [ ] Player Accounts
- [ ] Inventory Persistence

This is a WIP and is still wonky with running it on the built-in django development server. It crashes frequently if you tab out of the client, the request seem to buffer up and then happen at once when you focus on the client window again.


# Getting Started

For the project to work, you will need to install Unreal Engine 4.23.1 and docker-compose.

## Unreal Engine 4 Setup

You will need to download the [Epic Games Launcher](https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi) and go to the Library Tab. From there click on the + sign to add an engine version. Select version 4.23.1 from the list. The engine will download and install. There should also be an administrative prompt for prerequisite installation which will install required libraries and associate the project files to UE4. At this point, you should be able to go into the /UE4/ folder and launch the Django_REST.uproject by double clicking on it.

The project is configured to work with a dedicated server, so you need to click on the arrow of the "Play" button and check the box for dedicated server and set the players to at least 2.

![image](https://user-images.githubusercontent.com/46699116/77601255-80ff8c80-6ec7-11ea-8bd4-9f4a424aec99.png)

## DRF

From either your user or virtualenv, install the requirements with pip

`cd .\DRF\`

`python -m venv env`

`.\env\Scripts\activate`

`pip install -r .\requirements.txt`

`python manage.py migrate`

For the simple heartbeat example, the API just serves up data like {"healthy":"True"} so we need to add a record.

`python manage.py runshell`

```
>>> from api.models import Heartbeat
>>> hb = Heartbeat(healthy=True)
>>> hb.save()
```

Now you should be able to start the API.

`python manage.py runserver 127.0.0.1:8000`

You may now use the Play button in UE4 and the Blue example station will have a green electric arc indicating that the client and server are communicating.
