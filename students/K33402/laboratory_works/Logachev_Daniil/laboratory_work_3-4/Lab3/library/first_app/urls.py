from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    path('auth/token', obtain_auth_token, name='token'),

    path('books/all', BookListView.as_view()),
    path('books/<int:pk>', BookRetrieveView.as_view()),
    path('books/update/<int:pk>', BookUpdateView.as_view()),
    path('books/new', BookCreateView.as_view()),

    path('halls/all', HallListView.as_view()),
    path('halls/<int:pk>', HallRetrieveView.as_view()),
    path('halls/update/<int:pk>', HallUpdateView.as_view()),
    path('halls/new', HallCreateView.as_view()),

    path('copys/all', CopyListView.as_view()),
    path('copys/<int:pk>', CopyRetrieveView.as_view()),
    path('copys/update/<int:pk>', CopyUpdateView.as_view()),
    path('copys/new', CopyCreateView.as_view()),

    path('readers/all', ReaderListView.as_view()),
    path('readers/<int:pk>', ReaderRetrieveView.as_view()),
    path('readers/update/<int:pk>', ReaderUpdateView.as_view()),
    path('readers/new', ReaderCreateView.as_view()),
    path('readers/assignments/<int:pk>', ReaderRetrieveAssignmentsView.as_view()),
    path('readers/debtors', ReadersRetrieveDebtorView.as_view()),
    path('readers/rareBooks', ReadersRetrieveRareBooksView.as_view()),
    path('readers/young', YoungReadersCountView.as_view()),
    path('readers/education', ReadersEducationCountView.as_view()),
    
    path('assignments/all', AssignmentListView.as_view()),
    path('assignments/<int:pk>', AssignmentRetrieveView.as_view()),
    path('assignments/update/<int:pk>', AssignmentUpdateView.as_view()),
    path('assignments/new', AssignmentCreateView.as_view()),
]
