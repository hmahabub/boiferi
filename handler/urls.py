from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="homepage"),
    path("sign_up", views.sign_up, name="Sign up"),
    path("register", views.joinus, name="register"),
    path("login", views.login, name="Log in"),
    path("logout", views.logout, name="Log Out"),
    path("post", views.add_post, name="Add Post"),
    path("book_list", views.book, name="Book List"),
    path("blog", views.blog, name="Blog"),
    path("allwriters",views.all_writers, name=" all_writers"),
    path("profile",views.profile, name="profile"),
    path("edit/<str:pk>", views.edit, name ="blog_post_edit"),
    path("edit", views.editing, name ="blog_post_edit"),
    path("delete/<str:pk>", views.delete_post, name ="blog_post_delete"),
    path("contact", views.contact, name="Contact Page"),
    path("books/<str:pk>" ,views.author_book_list, name="author_book_list"),
    ]