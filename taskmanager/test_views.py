from django.test import TestCase
from django.urls import reverse
from .models import Task

class IndexViewTest(TestCase):
    def test_index_view_with_no_tasks(self):
        response = self.client.get(reverse('taskmanager:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Você não tem tarefas cadastradas")

    def test_index_view_with_tasks(self):
        t1 = Task.objects.create(title='Task 1', description='Task 1 description')
        t2 = Task.objects.create(title='Task 2')
        response = self.client.get(reverse('taskmanager:index'))
        print(f"tarefas {response.context['latest_task_list']}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'taskmanager/index.html')
        self.assertQuerysetEqual(
            response.context['latest_task_list'], [t2, t1]
            # ['<Task: Task 2>', '<Task: Task 1>']
        )