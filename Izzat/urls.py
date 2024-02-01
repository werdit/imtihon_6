from django.urls import path
from Izzat.views import home_page,about_page,post_detail_page,post_form_page,post_confirm_delete_page,user_post_page

urlpatterns=[
    path('',home_page,name='home-page'),
    path('about_page',about_page,name='about-page'),
    path('post_detail_page',post_detail_page,name='post-detail-page'),
    path('post_form_page',post_form_page,name='post-form-page'),
    path('post_confirm_delete_page',post_confirm_delete_page,name='post-confirm-delete-page'),

]