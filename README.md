
# [BudMan](https://budman.azurewebsites.net/)
Web App url https://budman.azurewebsites.net/

BudMan is a web app that helps you track and adjust your spending so that you are in control of money.



## Screenshots

![Screenshot 1](https://raw.githubusercontent.com/supsa-ak/BudMan/main/static/frontend/img/Screenshot1.png)
![Screenshot 2](https://raw.githubusercontent.com/supsa-ak/BudMan/main/static/frontend/img/Screenshot2.png)


# Built With
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Chart.js](https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Vim](https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=azure-devops&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white)

## Run Locally
Just follow this steps to run locally

Clone the Project

```bash
  git clone https://github.com/supsa-ak/BudMan.git
```

Go to the Project Directory

```bash
  cd BudMan
```

Create Virtual Environment
```bash
virtualenv env
```

Activate Virtual Environment
```bash
.\env\Scripts\activate
```

Install Dependencies

```bash
  pip install -r requirements.txt
```

Run Development Server
```bash
python manage.py runserver
```
## API Reference
User must be logged in for using apis
### Get All Spendings

```http
  GET /api/
```
SAMPLE JSON RESPONSE
```
{
    "data": [
        {
            "id": 26,
            "user": 1,
            "created": "2021-12-25T22:37:48.883377+05:30",
            "name": "asdf",
            "amount": 33,
            "category": "Fees",
            "note": "asdf"
        },
        {
            "id": 27,
            "user": 1,
            "created": "2021-12-25T22:38:02.467361+05:30",
            "name": "asdf",
            "amount": 33,
            "category": "Rent",
            "note": "adf"
        },
        {
            "id": 28,
            "user": 1,
            "created": "2021-12-25T22:41:32.641703+05:30",
            "name": "asdf",
            "amount": 23,
            "category": "Travel",
            "note": ""
        }
    ]
}
```
### Create Spending

```http
  POST  /api/create-transaction
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`    | `string` | **Required**. Name of Spending |
| `amount`    | `integer` | **Required**. Spending Amount |
| `category`    | `string` | **Required**. Category of Spending |
| `note`    | `string` | **Required**. About Spending |

SAMPLE JSON REQUEST 

```
{
    "name": "water bottle",
    "amount": 100,
    "category": "Shopping",
    "note": "Purchased from local store"
}
```

SAMPLE JSON RESPONSE
```
{
    "id": 36,
    "user": 1,
    "created": "2022-01-09T20:33:32.622050+05:30",
    "name": "water bottle",
    "amount": 100,
    "category": "Shopping",
    "note": "Purchased from local store"
}
```

### Update Spending
```http
  POST  /api/update-transaction
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`    | `integer` | **Required**. Id of Spending |
| `name`    | `string` | **Required**. Name of Spending |
| `amount`    | `integer` | **Required**. Spending Amount |
| `category`    | `string` | **Required**. Category of Spending |
| `note`    | `string` | **Required**. About Spending |

SAMPLE JSON REQUEST 

```
{
    "id": 36,
    "name": "water bottle",
    "amount": 100,
    "category": "Shopping",
    "note": "Purchased from local store"
}
```

SAMPLE JSON RESPONSE
```
{
    "id": 36,
    "user": 1,
    "created": "2022-01-09T20:33:32.622050+05:30",
    "name": "water bottle",
    "amount": 100,
    "category": "Shopping",
    "note": "Purchased from local store"
}
```

### Delete Transaction

```http
  POST  /api/delete-transaction
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`    | `integer` | **Required**. Id of Spending |

SAMPLE JSON REQUEST 

```
{
    "id": 36
}
```

SAMPLE JSON RESPONSE
```
{
    "message": "Deleted Successfully"
}
```
## License

```
MIT License

Copyright (c) 2021 Sarthak Kalpande

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
![Logo](https://raw.githubusercontent.com/supsa-ak/BudMan/main/static/frontend/img/logoreadme.png)