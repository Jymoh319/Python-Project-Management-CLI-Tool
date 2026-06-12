import pytest
from models.user import User
from models.project import Project
from models.task import Task

def test_user_instantiation_mechanics():
    """Verifies that user data mapping logic works as expected."""
    u = User("Grace", "grace@dev.co.ke")
    assert u.name == "Grace"
    assert u.email == "grace@dev.co.ke"
    assert u.to_dict()["name"] == "Grace"

def test_project_date_normalization_guardrails():
    """Confirms that varying date text strings parse cleanly into ISO formatting."""
    p = Project("Core Engine", "Rebuild systems", "October 24, 2026", "Grace")
    assert p.due_date == "2026-10-24"

def test_task_mutation_lifecycle():
    """Validates that status changes modify tracking properties correctly."""
    t = Task(42, "Web Portal", "Write Documentation")
    assert t.status == "Pending"
    t.mark_complete()
    assert t.status == "Complete"
