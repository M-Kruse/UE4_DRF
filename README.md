# UE4-DRF

![image](https://user-images.githubusercontent.com/46699116/77034452-4fd30980-6967-11ea-8d47-607d8583c231.png)


This project is for playing around with some UE4 game concepts and learning more about REST API at the same time.

This is using

* Unreal Engine 4 (UE4)
* VARest
* Django REST Framework (DRF)

Right now there is just a big blaster that spawns small blasters if it can successfully POST the new item to DRF. It also displays a number of how many blasters have been spawned.

There is also another actor that just displays the status of the API by trying to run a get request, like a heartbeat function. 

The UE4 project is being set up with authoritiative server logic. Anything critical to the gameplay should be stored/handled by the dedicated server which acts as the authority to clients.  Clients communicate with the server and the server communicates with the API.

Features

- [x] UE4 Item Class With API Support
- [ ] CRUD Logic For Items
- [ ] Item Persistence
- [ ] Player Accounts
- [ ] Inventory Persistence

This is a WIP and is still wonky with running it on the built-in django development server. It crashes frequently if you tab out of the client, the request seem to buffer up and then happen at once when you focus on the client window again.
