class Task:
    def __init__(self, task_id, project_title, title, status="Pending", assigned_to=None):
        self.task_id = str(task_id)
        self.project_title = project_title
        self.title = title
        self.status = status
        self.assigned_to = assigned_to if assigned_to else "Unassigned"

    def mark_complete(self):
        """Updates the tracking status variable inline."""
        self.status = "Complete"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "project_title": self.project_title,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["task_id"], data["project_title"], data["title"], data["status"], data["assigned_to"])

    def __str__(self):
        return f"Task #{self.task_id}: [{self.status}] {self.title} (Assigned: {self.assigned_to})"
