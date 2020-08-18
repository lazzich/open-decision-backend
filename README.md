# Open Decision

Welcome to the Open Decision backend!

## Table of content
- [Important Links](#important-links)
- [Participate](#participate)
- [Deploy in the Cloud](#deploy-in-the-cloud)
- [Local Set-Up](#local-set-up)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Built with](#built-with)
- [Contributing](#contributing)
- [License](#license)
- [Links](#links)

## Important Links

See the working prototype on https://github.com/open-decision/open-decision

See the frontend on https://github.com/open-decision/open-decision-frontend

Further information about the project on www.open-decision.org

## Participate

Join our growing community and socialize in [our Slack-Workspace](https://join.slack.com/t/opendecision/shared_invite/enQtNjM2NDUxNTQyNzU4LWYwMzJlZjlhOWJkMmIxMTBmMjYwMDE0Y2Y2OGUyZDBiY2FmOWU4OTVmMDFhMjNhNTIxYWZkZTNkNDRmNjQ4MmM).

Feel free to pick an issue, open a bug report, feature request or fork the project. We are open to any input or suggestions on how to bring the project forward.

If you want to join our team, contact us at [contact@open-decision.org](mailto:contact@open-decision.org).

## Deploy in the Cloud
With one click, you can deploy your own instance of Open Decision for free on Heroku.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Make sure to replace the SECRET_KEY-variable as soon as possible to secure your instance. [Click here](https://djecrety.ir/) to generate a unique secret key and [replace it in the Heroku Dashboard.](https://devcenter.heroku.com/articles/config-vars#using-the-heroku-dashboard)

## Local Set-up

The instructions down below will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to install Python and the package manager PIP. When you install Python <= 3.4 from the [official website](https://www.python.org/downloads/), PIP is already installed.

```
# Install virtual enviroment
pip install virtualenv
```

### Installation

First set-up and start the virtual environment.

```
# Create virtualenv
virtualenv -p python3 od

# Start environment
source od/bin/activate

```

Now clone the repo to the "src"-folder or download the [repo](https://github.com/fbennets/open-decision) as zip, unpack the folder, move it into the folder of your environment and rename it to "src".

```
# Clone repository to current directory
cd od
git clone https://github.com/fbennets/open-decision.git src

```
Next install the requirements.

```
# Install dependencies
cd src
pip install -r requirements-dev.txt
```
Now start the Django development server and enjoy!

```
# Start the development server
python manage.py runserver
```
Access the server at [http://localhost:8000](http://localhost:8000) or [http://127.0.0.1:8000](http://127.0.0.1:8000).

Now you can create an account and start playing around or use the demo-account to get a first impression:

```
User: test@test.com
Password: Testuser1
```
If the demo-account doesn't work, simply create an own one, you don't need to use a valid email adress.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used


## Contributing

Please read [CONTRIBUTING.md](https://github.com/fbennets/open-decision/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/fbennets/open-decision/blob/master/LICENSE) file for details.

## Links

* [Project Website](http://open-decision.org)
* [Join our Slack-Workspace](https://join.slack.com/t/opendecision/shared_invite/enQtNjM2NDUxNTQyNzU4LWYwMzJlZjlhOWJkMmIxMTBmMjYwMDE0Y2Y2OGUyZDBiY2FmOWU4OTVmMDFhMjNhNTIxYWZkZTNkNDRmNjQ4MmM)
