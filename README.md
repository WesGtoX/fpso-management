<h1 align="center">
  FPSO Management
</h1>

<p align="center">
  <a href="#about-the-project">About</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#technology">Technology</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#getting-started">Getting Started</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#usage">Usage</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#license">License</a>
</p>

<p align="center">
  <img alt="FPSO Management CI" src="https://github.com/WesGtoX/fpso-management/actions/workflows/docker-image.yml/badge.svg" />
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/wesgtox/fpso-management?style=plastic" />
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/wesgtox/fpso-management?style=plastic" />
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/wesgtox/fpso-management?style=plastic" />
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/wesgtox/fpso-management?style=plastic" />
  <img alt="License" src="https://img.shields.io/github/license/wesgtox/fpso-management?style=plastic" />
</p>


## About the Project

FPSO Management is a vessel and equipment management API, with registration, updating specific listings.


## Technology

This project was developed with the following technologies:

- [Python](https://www.python.org/)
- [Django Framework](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)


## Getting Started

### Prerequisites

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)


### Install and Run

1. Clone the repository:
```bash
git clone https://github.com/WesGtoX/fpso-management.git
```
2. Set a `SECRET_KEY` in `.env`:
```bash
cp .env.sample .env
```
3. Run:
```bash
make run
```
4. Run tests:
```bash
make test
```
5. To create a user with administrative access:
```bash
make user
```
6. To access the administrative area:
```bash
http://127.0.0.1:8000/admin
```


## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://github.com/WesGtoX/fpso-management/wiki)_


## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

Made with ♥ by [Wesley Mendes](https://wesleymendes.com.br/) :wave:
