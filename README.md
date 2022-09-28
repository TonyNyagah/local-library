## MDN Local Library
This project is made while following the Mozilla tutorial on building a Django application.
Tutorial link: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

#### Why?
I wanna see how I can implement features and testing along with getting to understand Django better.

#### What features to implement?
Some of the features to try out include:
- [x] Fixture implementation.
  - [x] Link on how to add data to a new application - https://dev.to/mungaigikure/set-up-and-load-initial-data-in-django-2gg8
- [x] Use pre-commit and commitizen to manage commits.
- [ ] Containerizing the application with Docker.
- [ ] CI/CD integration.
- [ ] Implement recommendations from the `Two Scoops of Django` book after completing the tutorial.
- [ ] Add Django REST framework or Django Ninja to the project to create an API.
- [ ] Create a frontend in Vue.

### The model design
![](design%20notes/local_library_model_uml.svg)

### The basic django flow
![](design%20notes/basic-django.png)

### Django form handling
![](design%20notes/form_handling_-_standard.png)

#### Steps to take before committing
Run the following commands in sequence:
1. `pre-commit install --hook-type commit-msg --hook-type pre-push`
2. `pre-commit run --all-files`
3. `git add .`
4. `cz commit`
Push after the commitizen commit.
