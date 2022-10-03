## 2.2.0 (2022-10-03)

### Feat

- **test**: added tests for views, forms and models
- **catalog/urls.py,catalog/views.py**: added routes for creating, updating and deleting books
- **catalog/urls.py,catalog/views.py**: learned about creating and handling forms
- **catalog/forms.py,catalog/views.py**: replaced the renewal form with the built-in `ModelForm` implementation
- **catalog/forms.py**: learned how to handle forms using a function view
- **catalog/forms.py**: learned how to handle forms using a function view
- **permissions**: allow users log in and view their own content
- **registration**: working on creating a listing of user's books
- **AuthorListView,AuthorDetailView**: created the author detail and list views and made them av
- used generic class-based list and detail views to create pages to view books
- **catalog/views.py,catalog/urls.py**: added views, urls and templates for the main catalog page display
- configured the admin site
- **catalog/models.py**: defined various models for handling a book
- **project-and-app-urls**: added the project urls for locallibrary and the app urls for catalog
- initial setup configurations

### Fix

- **catalog/views.py**: modified the permissions on the all loaned books view to get it working
- **catalog/views.py**: added code to detect user interaction
- **settings.py**: changed the fixture_dirs setting
- **catalog/apps.py**: code was formatted by black
- **catalog**: created the catalog app
