from django.test import TestCase
from django.urls import reverse
from .models import Task

class CreateViewTest(TestCase):
    def test_create_post_request(self):
        response = self.client.post(reverse('taskmanager:create'), {
            'title': 'Test Task',
            'description': 'This is a test task',
            'completed': 'on'
        })
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.assertEqual(Task.objects.count(), 1)  # Check if a new task is created

    def test_create_get_request(self):
        response = self.client.get(reverse('taskmanager:create'))
        self.assertEqual(response.status_code, 200)  # Check if the response is successful

    def test_create_invalid_post_request(self):
        response = self.client.post(reverse('taskmanager:create'), {
            'title': 'Test Task',
            'description': 'This is a test task',
            'completed': 'invalid_value'
        })
        self.assertEqual(response.status_code, 200)  # Check if the response is successful
        self.assertEqual(Task.objects.count(), 0)  # Check if no task is createdfrom django.test import TestCase
from django.urls import reverse
from .models import Task

class CreateViewTest(TestCase):
    def test_create_post_request(self):
        response = self.client.post(reverse('taskmanager:create'), {
            'title': 'Test Task',
            'description': 'This is a test task',
            'completed': 'on'
        })
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.assertEqual(Task.objects.count(), 1)  # Check if a new task is created

    def test_create_get_request(self):
        response = self.client.get(reverse('taskmanager:create'))
        self.assertEqual(response.status_code, 200)  # Check if the response is successful

    def test_create_invalid_post_request(self):
        response = self.client.post(reverse('taskmanager:create'), {
            'title': 'Test Task',
            'description': 'This is a test task',
            'completed': 'invalid_value'
        })
        self.assertEqual(response.status_code, 200)  # Check if the response is successful
        self.assertEqual(Task.objects.count(), 0)  # Check if no task is created


class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('taskmanager:index'))
        self.assertEqual(response.status_code, 200)  # Check if the response is successful
        self.assertTemplateUsed(response, 'taskmanager/index.html')  # Check if the correct template is used
        self.assertQuerysetEqual(response.context['latest_task_list'], [])  # Check if the latest_task_list is empty

    def test_index_view_with_tasks(self):
        Task.objects.create(title='Task 1', description='Description 1', completed=True)
        Task.objects.create(title='Task 2', description='Description 2', completed=False)
        response = self.client.get(reverse('taskmanager:index'))
        self.assertEqual(response.status_code, 200)  # Check if the response is successful
        self.assertTemplateUsed(response, 'taskmanager/index.html')  # Check if the correct template is used
        self.assertQuerysetEqual(
            response.context['latest_task_list'],
            ['<Task: Task 2>', '<Task: Task 1>']
        )  # Check if the latest_task_list contains the correct tasksfrom django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Task

class CreateViewTest(TestCase):
    def test_create_post_request(self):
        response = self.client.post(reverse('taskmanager:create'), {
            'title': 'Test Task',
            'description': 'This is a test task',
            'completed': 'on'
        })
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.assertEqual(Task.objects.count(), 1)  # Check if a new task is created

    def test_create_get_request(self):
        response = self.client.get(reverse('taskmanager:create'))
        self.assertEqual(response.status_code, 200)  # Check if the response is successful

    def test_create_invalid_post_request(self):
        response = self.client.post(reverse('taskmanager:create'), {
            'title': 'Test Task',
            'description': 'This is a test task',
            'completed': 'invalid_value'
        })
        self.assertEqual(response.status_code, 200)  # Check if the response is successful
        self.assertEqual(Task.objects.count(), 0)  # Check if no task is created

class DetailViewTest(TestCase):
    def test_detail_view(self):
        task = Task.objects.create(title='Test Task', description='This is a test task', completed=True)
        response = self.client.get(reverse('taskmanager:detail', args=[task.id]))
        self.assertEqual(response.status_code, 200)  # Check if the response is successful
        self.assertContains(response, task.title)  # Check if the task title is present in the response
        self.assertContains(response, task.description)  # Check if the task description is present in the response