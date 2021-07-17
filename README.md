<h1 align="center">Memo Project</h1>

<div align="center">

![Workflow](https://github.com/jiwonCha/memo-project/actions/workflows/docker-build-push.yaml/badge.svg)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/jiwonCha/memo-project.svg)](https://github.com/jiwonCha/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/jiwonCha/memo-project.svg)](https://github.com/jiwonCha/memo-project/issues)

</div>

---

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Github Action](#action)

## 🧐 About <a name = "about"></a>

It supports REST API to add / get memos

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

```bash
pip install -r requirements.txt
pip install flask_restx==0.4.0
```

### Running on python

```bash
python main.py -m local
```

### Docker Build

```bash
docker build .
```

## 🎈 Usage <a name="usage"></a>

### Swagger Open API

If you run this project in your local, can access this [Swagger API Page](http://127.0.0.1:5000/doc)

![image](https://user-images.githubusercontent.com/5278032/126025059-022823ac-efb2-4ddc-9259-33979e01c034.png)
![image](https://user-images.githubusercontent.com/5278032/126025068-5e17a523-99e9-4e5d-a016-9908d0ddc187.png)
![image](https://user-images.githubusercontent.com/5278032/126025060-08246e43-0a34-4449-9225-67cc7a5751af.png)
![image](https://user-images.githubusercontent.com/5278032/126025073-fef828c6-cf3a-4d64-8523-da707c7fcd37.png)

### Project Main Page

If you run this project in your local, can access this [Project Main Page](http://127.0.0.1:5000/memos)

![image](https://user-images.githubusercontent.com/5278032/126030036-87f7494c-3514-4e2e-9a7c-f32635b95c5c.png)



## 🚀 Deployment <a name = "deployment"></a>

Please refer below link.

[Memo Project Helm](https://github.com/jiwonCha/memo-project-helm) - Memo Project Helm Template

## ⛏️ Built Using <a name = "built_using"></a>

- [AWS RDS - PostgreSQL](https://aws.amazon.com/ko/rds/postgresql/) - Database
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Web Framework

## ✍️ Authors <a name = "authors"></a>

- [@jiwonCha](https://github.com/jiwonCha) - Develope Memo Project


## 🔧 GitHub Action <a name = "action">

This code manage with github action workflow.

If is invoked PR or Commits in main branch, build docker image and push theme to EC2 ECR
