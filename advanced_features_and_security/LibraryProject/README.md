# LibraryProject

This is the initial Django project for ALX Django Learn Lab.

## How to Run

Install dependencies:
pip install django

* **Model:** `users.CustomUser` extends `AbstractUser`, using `email` as the `USERNAME_FIELD`.
* **Fields:** Includes `date_of_birth` (DateField) and `profile_photo` (ImageField).
* **Manager:** `users.CustomUserManager` handles `create_user` and `create_superuser` correctly for email-based authentication and custom fields.
* **Admin Integration:** `users.admin.CustomUserAdmin` provides full management of `CustomUser` instances in the Django admin, exposing the new fields.
* **Configuration:** `AUTH_USER_MODEL = 'users.CustomUser'` is set in `LibraryProject/settings.py`.
* **Usage:** All `ForeignKey` or `OneToOneField` references to the default `User` model in other apps (e.g., `bookshelf`, `relationship_app`) have been updated to `settings.AUTH_USER_MODEL`.

* `can_view_book`: Allows viewing book details.
* `can_create_book`: Allows creating new books.
* `can_edit_book`: Allows modifying existing books.
* `can_delete_book`: Allows deleting books.
* **`Admins` Group:**
    * **Assigned Permissions:** `bookshelf | book | Can view book details`, `Can create new books`, `Can edit existing books`, `Can delete books`. (Full control over Books).
* **`Editors` Group:**
    * **Assigned Permissions:** `bookshelf | book | Can view book details`, `Can create new books`, `Can edit existing books`. (View, Create, Edit Books).
* **`Viewers` Group:**
    * **Assigned Permissions:** `bookshelf | book | Can view book details`. (View Books only).

 * **`book_list` view:** Protected by `@permission_required('bookshelf.can_view_book')`.
* **`book_create` view:** Protected by `@permission_required('bookshelf.can_create_book')`.
* **`book_edit` view:** Protected by `@permission_required('bookshelf.can_edit_book')`.
* **`book_delete` view:** Protected by `@permission_required('bookshelf.can_delete_book')`.

Testing is performed manually by:
1.  Creating test users in the admin.
2.  Assigning them to different groups (e.g., a 'viewer', an 'editor', an 'admin').
3.  Logging in as each user and attempting to perform actions (view, create, edit, delete books) to confirm that permissions are correctly enforced.

---
# Advanced Features and Security (Django Project)

This project demonstrates the implementation of a custom user model and a permissions and groups system in Django.

---

## 1. Custom User Model (`users` app)

**Location:** `advanced_features_and_security/users/`

* **Model (`users/models.py`):**
    * `CustomUser` extends `django.contrib.auth.models.AbstractUser`.
    * `USERNAME_FIELD` is set to `email` for email-based authentication.
    * **Custom fields added:** `date_of_birth` (DateField) and `profile_photo` (ImageField).
* **Manager (`users/models.py`):**
    * `CustomUserManager` inherits from `BaseUserManager` and provides custom `create_user` and `create_superuser` methods to handle the email field and other custom fields.
* **Admin Integration (`users/admin.py`):**
    * `CustomUserAdmin` (extending `django.contrib.auth.admin.UserAdmin`) is defined to properly display and manage `CustomUser` instances in the Django admin interface, including the new custom fields.
* **Project Settings (`LibraryProject/settings.py`):**
    * `AUTH_USER_MODEL = 'users.CustomUser'` is set to instruct Django to use this custom model throughout the project.
* **Application Updates:**
    * Any `ForeignKey` or `OneToOneField` relationships in other apps (e.g., `bookshelf/models.py`, `relationship_app/models.py`) that previously referred to Django's default `User` model have been updated to `settings.AUTH_USER_MODEL`. This ensures they correctly link to the `CustomUser`.

---

## 2. Permissions and Groups (`bookshelf` app example)

This section outlines the setup for controlling access to `Book` model operations within the `bookshelf` app using Django's permissions and groups system.

**Target App:** `bookshelf`
**Target Model:** `Book`

### 2.1. Custom Permissions Definition (`bookshelf/models.py`)

Custom permissions are defined directly within the `Book` model's `Meta` class:

```python
class Book(models.Model):
    # ... existing fields ...
    class Meta:
        permissions = [
            ("can_view", "Can view book details"),
            ("can_create", "Can create new books"),
            ("can_edit", "Can edit existing books"),
            ("can_delete", "Can delete books"),
        ]
        # ... other Meta options ...
