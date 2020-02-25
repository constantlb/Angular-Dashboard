# Dashboard

Dashboard is a useful tool to use on daily basis.



## Getting started

#### ❖ Prerequisites

This application runs under [**Docker**](https://www.docker.com/). In order to be able to run it, you must first have *Docker* installed on your machine. If you already have it, you can skip this part and directly go to the next section.

In the case you don't have *Docker* installed on your computer, be sure to install it properly before continuing. Here are the official installation guides:

| **OS**                                                       | **Official link**                                       |
| :----------------------------------------------------------- | :------------------------------------------------------ |
| <img src="https://img.icons8.com/metro/52/000000/mac-os.png" width="32px"> Mac | https://docs.docker.com/docker-for-mac/install/         |
| <img src="https://img.icons8.com/ios-glyphs/60/000000/windows-client.png" width="32px"> Windows | https://docs.docker.com/docker-for-windows/install/     |
| <img src="https://img.icons8.com/metro/52/000000/ubuntu.png" width="32px"> Ubuntu | https://docs.docker.com/install/linux/docker-ce/ubuntu/ |
| <img src="https://img.icons8.com/metro/52/000000/debian.png" width="32px"> Debian | https://docs.docker.com/install/linux/docker-ce/debian/ |
| <img src="https://img.icons8.com/ios-filled/50/000000/fedora.png" width="32px"> Fedora | https://docs.docker.com/install/linux/docker-ce/fedora/ |
| <img src="https://img.icons8.com/windows/32/000000/centos.png" width="32px"> CentOs | https://docs.docker.com/install/linux/docker-ce/centos/ |

Once *Docker* is installed, download and install [**`docker-compose`**](https://docs.docker.com/compose/install/).



#### ❖ Configuration

The domain name used for running the application can be changed in the **`.env`** file located at the root of the project.

```properties
# By default the application will run on localhost.
# If ever you wish to use a domain name, change the
# environment value here.
DOMAIN_NAME=localhost
```

> example: `DOMAIN_NAME=domain.com`



#### ❖ Run the application

To start the application, type the following command:

```
docker-compose up --build
```

> Yeah, that's right. Only one command!



## Features

Dashboard is fully customizable. You can add as many widgets as you want, and even organize it as you wish.



#### ❖ Services and widgets

​	⬥ **Weather**

​		⬦ **Temperature**

> **Type** `widget-weather-light`

| Description                  | Parameters           |
| ---------------------------- | -------------------- |
| `View a city's temperature.` | `City name (string)` |

​		⬦ **Forecast**

> **Type** `widget-weather-big`

| Description                                               | Parameters           |
| --------------------------------------------------------- | -------------------- |
| `View a city's forecast (pressure, humidity, wind, ...).` | `City name (string)` |

​		⬦ **Daytime**

> **Type** `widget-weather-day`

| Description                                         | Parameters           |
| --------------------------------------------------- | -------------------- |
| `View a city's daytime hours (sunrise and sunset).` | `City name (string)` |



​	⬥ **SoundCloud**

​		⬦ **Profile**

> **Type** `widget-soundcloud-profile`

| Description                 | Parameters                 |
| --------------------------- | -------------------------- |
| `View an artist's profile.` | `Artist username (string)` |

​		⬦ **Top 15**

> **Type** `widget-soundcloud-discover`

| Description                                                  | Parameters                                         |
| ------------------------------------------------------------ | -------------------------------------------------- |
| `View the top 15 songs of a music genre in a specific country.` | `Country name (string)`,<br>`Music genre (string)` |

​		⬦ **Artist popular tracks**

> **Type** `widget-soundcloud-top`

| Description                             | Parameters                 |
| --------------------------------------- | -------------------------- |
| `View an artist's most popular tracks.` | `Artist username (string)` |



​	⬥ **News**

​		⬦ **Topic**

> **Type** `widget-news-subject`

| Description                                               | Parameters              |
| --------------------------------------------------------- | ----------------------- |
| `View the latest articles written about a certain topic.` | `Search topic (string)` |

​		⬦ **Region**

> **Type** `widget-news-region`

| Description                                                  | Parameters                                           |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| `View the latest articles from a certain region and of a specific category.` | `Country name (string)`,<br>`Category name (string)` |

​		⬦ **Media source**

> **Type** `widget-news-media`

| Description                                            | Parameters                   |
| ------------------------------------------------------ | ---------------------------- |
| `View the latest articles of a specific media source.` | `Media source name (string)` |



## API

#### ❖ Routes

​	⬥ **Misc**

| Method | Route  | Description        |
| ------ | ------ | ------------------ |
| GET    | /about | get the about json |



​	⬥ **Services**

| Method | Route                 | Description           |
| ------ | --------------------- | --------------------- |
| GET    | /services             | get the services list |
| GET    | /services/:service_id | get a service         |



​	⬥ **Users**

| Method | Route                                   | Description                                      |
| ------ | --------------------------------------- | ------------------------------------------------ |
| GET    | /users                                  | get the users list                               |
| POST   | /users                                  | create a new user                                |
| POST   | /users/login                            | check credentials and get user data              |
| DELETE | /users/:user_id                         | delete a user                                    |
| GET    | /users/:user_id                         | get a user                                       |
| GET    | /users/:user_id/widgets                 | get a user's widgets list                        |
| POST   | /users/:user_id/widgets                 | add a new widget to a user's dashboard           |
| DELETE | /users/:user_id/widgets/:widget_id      | remove a widget from a user's dashboard          |
| GET    | /users/:user_id/widgets/:widget_id      | get a widget from a user's dashboard             |
| GET    | /users/:user_id/widgets/:widget_id/data | get the data of a widget from a user's dashboard |

> Here are examples of the required data for the **POST** routes:
>
> * **/users**
>
> ```json
> {
>       'username': 'username',
>       'password': 'p455w0rd',
>       'email': 'username@email.com'
> }
> ```
>
> * **/users/login**
>
> ```json
> {
>       'email': 'username@email.com',
>       'password': 'p455w0rd'
> }
> ```
>
> * **/users/:user_id/widgets**
>
> ```json
> {
>       'type': 'widget-soundcloud-profile',
>       'refresh_time': 15,
>       'params': [
>            'Haki'
>       ],
>       'position': {
>            'x': 0,
>            'y': 0
>       }
> }
> ```



​	⬥ **Widgets**

| Method | Route               | Description          |
| ------ | ------------------- | -------------------- |
| GET    | /widgets            | get the widgets list |
| GET    | /widgets/:widget_id | get a widget         |



#### ❖ Models

These are the different JSON that you can retrieve by using the API.

Also, note that all response is wrapped the following way:

```json
{
    'status': 200             // http status code
    'message': 'OK',          // http status message
    'success': true,          // was the request successful?
    'data': /* mixed */       // requested data
}
```

Each JSON from bellow will be found in the 'data' field.



​	⬥ **Misc**

 		⬦ **About**

``` json
{
    'client': {
        'host': /* string */,
    },
    'server': {
        'current_time': /* integer */,
        'services': [{
            'name': /* string */,
            'widgets': [{
                'name': /* string */,
                'description': /* string */,
                'params': [{
                    'name': /* string */,
                    'type': /* integer || string */
                }]
            }]
        }]
    }
}
```



​	⬥ **Services**

 		⬦ **Service**

```json
{
    'id': /* integer */,
    'name': /* string */,
    'connections': [{
        'name': /* string */
    }]
}
```



​	⬥ **Users**

 		⬦ **User**

```json
{
    'id': /* integer */,
    'username': /* string */,
    'email': /* string */,
    'creation_date': /* integer */
}
```

 		⬦ **User widget**

```json
{
    'id': /* integer */,
    'type': /* string */,
    'params': [
        /* integer || string */
    ],
    'position': {
        'x': /* integer */,
        'y': /* integer */
    }
}
```

 		⬦ **User widget data**

```json
{
    'id': /* integer */,
    'model': /* string */,
    'data': /* mixed */
}
```



​	⬥ **Widgets**

 		⬦ **Widget**

 ```json
{
    'id': /* integer */,
    'service_id': /* integer */
    'name': /* string */,
    'description': /* string */,
    'type': /* string */,
    'params': [{
        'name': /* string */,
        'type': /* integer || string */
    }]
}
 ```





## Technologies & Dependencies

Dashboard is split into 3 main services:

⬥ **Dashboard** made in [**Angular**](https://github.com/topics/angular) `v8`

​	⬦ [**angular-gridster2**](https://github.com/tiberiuzuld/angular-gridster2) `v8.2.0` 

​	⬦ [**bootstrap**](https://github.com/twbs/bootstrap) `v4.3.1` 

⬥ **API** made in [**Python**](https://github.com/topics/python) `v2.7`

​	⬦ [**flask**](https://github.com/pallets/flask) `v1.1.1` 

​	⬦ [**flask-cors**](https://github.com/corydolphin/flask-cors) `v3.0.8` 

​	⬦ [**rethinkdb**](https://github.com/rethinkdb/rethinkdb-python) `v2.4.4` 

​	⬦ [**requests**](https://github.com/psf/requests) `v2.22.0` 

⬥ **Database** using [**Rethinkdb**](https://github.com/rethinkdb/rethinkdb) `v2.3`