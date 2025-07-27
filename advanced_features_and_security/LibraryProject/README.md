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

