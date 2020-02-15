from django.urls import path

from .views import DashboardView, ProjectsListView, AddProjectView, UpdateProjectView, DeleteProjectView, \
    ProjectDetailView, IssueDetailView, AddIssueView, EditIssueView, DeleteAttachmentView, AddCommentView, \
    EditCommentView, DeleteCommentView

app_name = 'issues'

urlpatterns = [  # bardzo chaotyczna struktura
    path('', DashboardView.as_view(), name='dashboard'),
    path('projects/', ProjectsListView.as_view(), name='projects-list'),
    path('add-project', AddProjectView.as_view(), name="add-project"),
    path('update-project/<int:pk>', UpdateProjectView.as_view(), name='update-project'),
    path('delete-project/<int:pk>', DeleteProjectView.as_view(), name='delete-project'),
    path('project/<slug:slug>', ProjectDetailView.as_view(), name='project-detail'),  # wcześniej było `projects/` - to nie pasuje
    path('<slug:slug>/', IssueDetailView.as_view(), name='issue-detail'),   # co, jeśli ktoś jako slug da "projects" lub inny z użytych słów?
    path('project/<slug:slug>/add', AddIssueView.as_view(), name='add-issue'),
    path('<slug:slug>/edit', EditIssueView.as_view(), name='edit-issue'),
    path('delete-attachment/<int:pk>/', DeleteAttachmentView.as_view(), name='delete-attachment'),
    path('<slug:slug>/add-comment', AddCommentView.as_view(), name='add-comment'),
    path('edit-comment/<int:pk>', EditCommentView.as_view(), name='edit-comment'),
    path('delete-comment/<int:pk>', DeleteCommentView.as_view(), name='delete-comment')
]

# straszny chaos w URLach, spróbuj to uporządkować

# projects/ - lista projektów
# projects/~add - dodanie projektu
# projects/<slug> - detale projektu - lista issue w projekcie
# projects/<slug>/~edit - edycja projektu
# projects/<slug>/~delete - usunięcie projektu
# projects/<slug>/~add - dodanie issue
# projects/<slug>/<issue-slug> - detale issue
