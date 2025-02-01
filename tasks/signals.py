from tasks.models import Task
from django.db.models.signals import post_save, m2m_changed, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail

# Signals
@receiver(m2m_changed, sender=Task.assigned_to.through) # <- decorator
def notify_employee_on_task_creation(sender, instance, action, **kwargs):
    if action == 'post_add':
        assigned_email = [emp.email for emp in instance.assigned_to.all()]

        send_mail(
            "New Task Assigned",
            f"You have been assigned to the task:{instance.title}",
            "tohahpro@gmail.com",
            assigned_email,
        )

# @receiver(post_delete, sender= Task)
# def delete_associate_details(sender, instance, **kwargs):
#     if instance.details:
#         print(isinstance)
#         instance.details.delete()