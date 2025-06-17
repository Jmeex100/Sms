from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid

class BaseModel(models.Model):
    """
    Abstract base model with common fields for all models
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        abstract = True
        ordering = ['-created_at']

class CustomUser(AbstractUser):
    """
    Custom user model extending AbstractUser for school hub
    """
    USER_TYPE_CHOICES = (
        ('student', _('Student')),
        ('teacher', _('Teacher')),
        ('admin', _('Admin')),
        ('parent', _('Parent')),
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='student',
        verbose_name=_("User Type")
    )
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        null=True,
        blank=True,
        verbose_name=_("Profile Picture")
    )
    phone_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name=_("Phone Number")
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("Date of Birth")
    )
    student_id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        verbose_name=_("Student ID"),
        help_text=_("Unique ID for students, automatically generated if not provided.")
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        indexes = [
            models.Index(fields=['student_id']),
        ]

    def __str__(self):
        return f"{self.get_full_name()} ({self.user_type})"

    def save(self, *args, **kwargs):
        # Generate student_id for students if not provided
        if self.user_type == 'student' and not self.student_id:
            self.student_id = f"STU-{uuid.uuid4().hex[:8].upper()}"
        # Ensure non-students have null student_id
        if self.user_type != 'student':
            self.student_id = None
        super().save(*args, **kwargs)

class School(BaseModel):
    """
    Model representing a school in the hub
    """
    name = models.CharField(max_length=200, verbose_name=_("School Name"))
    address = models.TextField(verbose_name=_("Address"))
    contact_email = models.EmailField(verbose_name=_("Contact Email"))
    contact_phone = models.CharField(max_length=15, verbose_name=_("Contact Phone"))

    class Meta:
        verbose_name = _("School")
        verbose_name_plural = _("Schools")

    def __str__(self):
        return self.name